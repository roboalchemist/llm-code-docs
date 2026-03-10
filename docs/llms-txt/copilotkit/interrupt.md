# Interrupt

Learn how to implement Human-in-the-Loop (HITL) using a interrupt-based flow.

Pictured above is the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) with
the implementation below applied!

## [What is this?](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow\#what-is-this)

[LangGraph's interrupt flow](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) provides an intuitive way to implement Human-in-the-loop workflows.

This guide will show you how to both use `interrupt` and how to integrate it with CopilotKit.

## [When should I use this?](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow\#when-should-i-use-this)

Human-in-the-loop is a powerful way to implement complex workflows that are production ready. By having a human in the loop,
you can ensure that the agent is always making the right decisions and ultimately is being steered in the right direction.

Interrupt-based flows are a very intuitive way to implement HITL. Instead of having a node await user input before or after its execution,
nodes can be interrupted in the middle of their execution to allow for user input. The trade-off is that the agent is not aware of the
interaction, however [CopilotKit's SDKs provide helpers to alleviate this](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#make-your-agent-aware-of-interruptions).

## [Implementation](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow\#implementation)

### [Run and connect your agent](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow\#run-and-connect-your-agent)

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already,
you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/coagents/quickstart/langgraph) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point
as this guide uses it as a starting point.

### [Install the CopilotKit SDK](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow\#install-the-copilotkit-sdk)

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic
experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

Poetrypipconda

```
poetry add copilotkit