# Manually emitting messages

While most agent interactions happen automatically through shared state updates as the agent runs, you can also **manually send messages from within your agent code** to provide immediate feedback to users.

This video shows the [coagents starter](https://github.com/CopilotKit/CopilotKit/tree/main/examples/coagents-starter) repo with the [implementation](https://docs.copilotkit.ai/coagents/advanced/emit-messages#implementation) section applied to it!

## [What is this?](https://docs.copilotkit.ai/coagents/advanced/emit-messages\#what-is-this)

In LangGraph, messages are only emitted when a node is completed. CopilotKit allows you to manually emit messages
in the middle of a node's execution to provide immediate feedback to the user.

## [When should I use this?](https://docs.copilotkit.ai/coagents/advanced/emit-messages\#when-should-i-use-this)

Manually emitted messages are great for **when you don't want to wait for the node** to complete **and you**:

- Have a long running task that you want to provide feedback on
- Want to provide a status update to the user
- Want to provide a warning or error message

## [Implementation](https://docs.copilotkit.ai/coagents/advanced/emit-messages\#implementation)

### [Run and Connect Your Agent to CopilotKit](https://docs.copilotkit.ai/coagents/advanced/emit-messages\#run-and-connect-your-agent-to-copilotkit)

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already,
you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/coagents/quickstart/langgraph) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point
as this guide uses it as a starting point.

### [Install the CopilotKit SDK](https://docs.copilotkit.ai/coagents/advanced/emit-messages\#install-the-copilotkit-sdk)

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic
experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

Poetrypipconda

```
poetry add copilotkit