"""Microsoft Agent Framework runtime: Agents wired together with WorkflowBuilder.

* every role is an `agent_framework.Agent` backed by a chat client
* sequential apps use `add_chain`; fan-out apps use `add_fan_out_edges`,
  a small `Join` executor (fan-in) and then the merger agent
An offline `BaseChatClient` replaces Azure OpenAI / OpenAI / Foundry.
"""
from __future__ import annotations

import asyncio
import logging

from agent_framework import (Agent, AgentExecutorResponse, BaseChatClient, ChatResponse, Executor,
                             Message, WorkflowBuilder, WorkflowContext, handler)

from common.flow import FANOUT, compose_input, dependencies, system_prompt
from common.offline_llm import offline_complete

logging.getLogger("agent_framework").setLevel(logging.ERROR)


class OfflineChatClient(BaseChatClient):
    """Chat client with no network access. Records each agent's answer in `outputs`."""

    def __init__(self, index, agents, task, pattern, outputs):
        super().__init__()
        self.index, self.agents, self.task, self.pattern, self.outputs = index, agents, task, pattern, outputs

    def _inner_get_response(self, *, messages, stream, options, **kwargs):
        if stream:
            raise NotImplementedError("streaming is not supported by the offline client")
        key, role, instr = self.agents[self.index]
        deps = dependencies(self.pattern, len(self.agents))[self.index]
        ups = [(self.agents[j][1], self.outputs[self.agents[j][0]]) for j in deps if self.agents[j][0] in self.outputs]
        text = offline_complete(system_prompt(role, instr), compose_input(self.task, ups))
        self.outputs[key] = text

        async def respond() -> ChatResponse:
            return ChatResponse(messages=[Message("assistant", [text])])

        return respond()


class Join(Executor):
    """Fan-in: collects the specialists' replies into one message for the merger."""

    def __init__(self) -> None:
        super().__init__(id="join")

    @handler
    async def join(self, results: list[AgentExecutorResponse], ctx: WorkflowContext[Message]) -> None:
        await ctx.send_message(Message("user", ["\n".join(r.agent_response.text for r in results)]))


def build_workflow(agents, task, pattern, outputs, client_factory=None):
    client_factory = client_factory or (lambda i: OfflineChatClient(i, agents, task, pattern, outputs))
    team = [Agent(client_factory(i), instructions=system_prompt(role, instr), name=key)
            for i, (key, role, instr) in enumerate(agents)]
    builder = WorkflowBuilder(start_executor=team[0])
    if pattern == FANOUT and len(team) >= 4:
        middle, join = team[1:-1], Join()
        builder.add_fan_out_edges(team[0], middle).add_fan_in_edges(middle, join).add_edge(join, team[-1])
    else:
        builder.add_chain(team)
    return builder.build()


async def _run(agents, task, pattern):
    outputs: dict[str, str] = {}
    await build_workflow(agents, task, pattern, outputs).run(task)
    return {key: outputs[key] for key, _, _ in agents}


def run_app(title, agents, task, pattern="sequential", provider=None) -> dict:
    return asyncio.run(_run(agents, task, pattern))
