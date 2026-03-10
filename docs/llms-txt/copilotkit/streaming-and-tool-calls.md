# Streaming and Tool Calls

CoAgents support streaming your messages and tool calls to the frontend.

If you'd like to change how LangGraph agents behave as CoAgents you can utilize our CopilotKit SDK which provides a collection
of functions and utilities for interacting with the agent's state or behavior. One example of this is the CopilotKit config
which is a wrapper of the LangGraph `config` object. This allows you to extend the configuration of your LangGraph nodes to
change how LangGraph and CopilotKit interact with each other. This allows you to change how messages and tool calls are emitted and
streamed to the frontend.

## [Message Streaming](https://docs.copilotkit.ai/coagents/concepts/copilotkit-config\#message-streaming)

If you did not change anything in your LangGraph node, message streaming will be on by default. This allows for a message to be
streamed to CopilotKit as it is being generated, allowing for a more responsive experience. However, you can disable this if you
want to have the message only be sent after the agent has finished generating it.

```
config = copilotkit_customize_config(
    config,
    # True or False
    emit_messages=False,
)
```

## [Emitting Tool Calls](https://docs.copilotkit.ai/coagents/concepts/copilotkit-config\#emitting-tool-calls)

Emission of tool calls are off by default. This means that tool calls will not be sent to CopilotKit for processing and rendering.
However, within a node you can extend the LangGraph `config` object to emit tool calls to CopilotKit. This is useful in situations
where you may to emit what a potential tool call will look like prior to being executed.

```
config = copilotkit_customize_config(
    config,
    # Can set to True, False, or a list of tool call names to emit.
    emit_tool_calls=["tool_name"],
)
```

For more information on how tool calls are utilized check out our [frontend actions](https://docs.copilotkit.ai/coagents/frontend-actions)
documentation.

[Next\\
\\
Introduction](https://docs.copilotkit.ai/)

### On this page

[Message Streaming](https://docs.copilotkit.ai/coagents/concepts/copilotkit-config#message-streaming) [Emitting Tool Calls](https://docs.copilotkit.ai/coagents/concepts/copilotkit-config#emitting-tool-calls)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/concepts/copilotkit-config.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Agentic Chat UI
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is this?