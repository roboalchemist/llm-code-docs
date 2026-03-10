# Node-based

Learn how to implement Human-in-the-Loop (HITL) using a node-based flow.

The usage of node based interrupt is [now discouraged](https://langchain-ai.github.io/langgraph/concepts/v0-human-in-the-loop/) by both LangGraph and CopilotKit.
As of LangGraph 0.2.57, the recommended way to set breakpoints is using [the interrupt function](https://https//docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow) as it simplifies human-in-the-loop patterns.

Pictured above is the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) with
the implementation below applied!

## [What is this?](https://docs.copilotkit.ai/coagents/human-in-the-loop/node-flow\#what-is-this)

[Node based flows](https://langchain-ai.github.io/langgraph/concepts/v0-human-in-the-loop/#dynamic-breakpoints) are predicated on LangGraph concept
of `breakpoints` which will interrupt a node before or after its execution to allow for user input.

CopilotKit allows you to add custom UI to take user input and then pass it back to the agent upon completion.

## [Why should I use this?](https://docs.copilotkit.ai/coagents/human-in-the-loop/node-flow\#why-should-i-use-this)

Human-in-the-loop is a powerful way to implement complex workflows that are production ready. By having a human in the loop,
you can ensure that the agent is always making the right decisions and ultimately is being steered in the right direction.

Node-based flows are a great way to implement HITL for more complex workflows where you want to ensure the agent is aware
of everything that has happened during a HITL interaction. This is contrasted with interrupt-based flows, where the agent
is interrupted and then resumes execution from where it left off, unaware of the context of the interaction by default.

## [Implementation](https://docs.copilotkit.ai/coagents/human-in-the-loop/node-flow\#implementation)

### [Run and connect your agent](https://docs.copilotkit.ai/coagents/human-in-the-loop/node-flow\#run-and-connect-your-agent)

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already,
you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/coagents/quickstart/langgraph) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point
as this guide uses it as a starting point.

### [Install the CopilotKit SDK](https://docs.copilotkit.ai/coagents/human-in-the-loop/node-flow\#install-the-copilotkit-sdk)

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic
experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

Poetrypipconda

```
poetry add copilotkit