# Common Issues

Common issues you may encounter when using CoAgents.

Welcome to the CoAgents Troubleshooting Guide! If you're having trouble getting tool calls to work, you've come to the right place.

Have an issue not listed here? Open a ticket on [GitHub](https://github.com/CopilotKit/CopilotKit/issues) or reach out on [Discord](https://discord.com/invite/6dffbvGU3D)
and we'll be happy to help.

We also highly encourage any open source contributors that want to add their own troubleshooting issues to [Github as a pull request](https://github.com/CopilotKit/CopilotKit/blob/main/CONTRIBUTING.md).

## [My tool calls are not being streamed](https://docs.copilotkit.ai/coagents/troubleshooting/common-issues\#my-tool-calls-are-not-being-streamed)

This could be due to a few different reasons.

First, we strongly recommend checking out our [Human In the Loop](https://docs.copilotkit.ai/coagents/human-in-the-loop) guide to follow a more in depth example of how to stream tool calls
in your LangGraph agents. You can also check out our [travel tutorial](https://docs.copilotkit.ai/coagents/tutorials/ai-travel-app/step-6-human-in-the-loop) which talks about how to stream
tool calls in a more complex example.

If you have already done that, you can check the following:

### You have not specified the tool call in the \`copilotkit\_customize\_config\`

### You're using llm.invoke() instead of llm.ainvoke()

## [Error: `'AzureOpenAI' object has no attribute 'bind_tools'`](https://docs.copilotkit.ai/coagents/troubleshooting/common-issues\#error-azureopenai-object-has-no-attribute-bind_tools)

This error is typically due to the use of an incorrect import from LangGraph. Instead of importing `AzureOpenAI` import `AzureChatOpenAI` and your
issue will be resolved.

```
from langchain_openai import AzureOpenAI
from langchain_openai import AzureChatOpenAI
```

## [I am getting "agent not found" error](https://docs.copilotkit.ai/coagents/troubleshooting/common-issues\#i-am-getting-agent-not-found-error)

If you're seeing this error, it means CopilotKit couldn't find the LangGraph agent you're trying to use. Here's how to fix it:

### Verify your agent lock mode configuration

### Check your agent registration on a LangGraph Platform endpoint

### Check your agent name in useCoAgent

### Check your agent name in useCoAgentStateRender

## [Connection issues with tunnel creation](https://docs.copilotkit.ai/coagents/troubleshooting/common-issues\#connection-issues-with-tunnel-creation)

If you notice the tunnel creation process spinning indefinitely, your router or ISP might be blocking the connection to CopilotKit's tunnel service.

### Router or ISP blocking tunnel connections

## [I am getting "Failed to find or contact remote endpoint at url, Make sure the API is running and that it's indeed a LangGraph platform url" error](https://docs.copilotkit.ai/coagents/troubleshooting/common-issues\#i-am-getting-failed-to-find-or-contact-remote-endpoint-at-url-make-sure-the-api-is-running-and-that-its-indeed-a-langgraph-platform-url-error)

If you're seeing this error, it means the LangGraph platform client cannot connect to your endpoint.

### Verify the endpoint is reachable

### Verify running a LangGraph platform endpoint using LangGraph deployment tools

### Verify the remote endpoint matches the endpoint definition type

## [I see messages being streamed and disappear](https://docs.copilotkit.ai/coagents/troubleshooting/common-issues\#i-see-messages-being-streamed-and-disappear)

LangGraph agents are stateful. As a graph is traversed, the state is saved at the end of each node. CopilotKit uses the agent's state as
the source of truth for what to display in the frontend chat. However, since state is only emitted at the end of a node, CopilotKit allows
you to stream predictive state updates _in the middle of a node_. By default, CopilotKit will stream messages and tool calls being actively
generated to the frontend chat that initiated the interaction. **If this predictive state is not persisted at the end of the node, it will**
**disappear in the frontend chat**.

In this situation, the most likely scenario is that the `messages` property in the state is being updated in the middle of a node but those edits are not being
persisted at the end of a node.

![](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/coagents/message-state-diagram.png)

### I want these messages to be persisted

### I don't want these messages to streamed at all

[Previous\\
\\
Message flow](https://docs.copilotkit.ai/coagents/concepts/message-management) [Next\\
\\
Migrate from v0.2 to v0.3](https://docs.copilotkit.ai/coagents/troubleshooting/migrate-from-v0.2-to-v0.3)

### On this page

[My tool calls are not being streamed](https://docs.copilotkit.ai/coagents/troubleshooting/common-issues#my-tool-calls-are-not-being-streamed) [Error: 'AzureOpenAI' object has no attribute 'bind\_tools'](https://docs.copilotkit.ai/coagents/troubleshooting/common-issues#error-azureopenai-object-has-no-attribute-bind_tools) [I am getting "agent not found" error](https://docs.copilotkit.ai/coagents/troubleshooting/common-issues#i-am-getting-agent-not-found-error) [Connection issues with tunnel creation](https://docs.copilotkit.ai/coagents/troubleshooting/common-issues#connection-issues-with-tunnel-creation) [I am getting "Failed to find or contact remote endpoint at url, Make sure the API is running and that it's indeed a LangGraph platform url" error](https://docs.copilotkit.ai/coagents/troubleshooting/common-issues#i-am-getting-failed-to-find-or-contact-remote-endpoint-at-url-make-sure-the-api-is-running-and-that-its-indeed-a-langgraph-platform-url-error) [I see messages being streamed and disappear](https://docs.copilotkit.ai/coagents/troubleshooting/common-issues#i-see-messages-being-streamed-and-disappear)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/troubleshooting/common-issues.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Agentic Generative UI
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is this?

[Generative UI](https://docs.copilotkit.ai/coagents/generative-ui)