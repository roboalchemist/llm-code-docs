# Return the message from the node
return {
    "messages": [AIMessage(content=message)]
}
```

### [Parameters](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#parameters-3)

configRunnableConfigrequired

The LangGraph configuration.

messagestrrequired

The message to emit.

### [Returns](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#returns-3)

returnsAwaitable\[bool\]

Always return True.

## [copilotkit\_emit\_tool\_call](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#copilotkit_emit_tool_call)

Manually emits a tool call to CopilotKit.

```
from copilotkit.langgraph import copilotkit_emit_tool_call

await copilotkit_emit_tool_call(config, name="SearchTool", args={"steps": 10})
```

### [Parameters](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#parameters-4)

configRunnableConfigrequired

The LangGraph configuration.

namestrrequired

The name of the tool to emit.

argsDict\[str, Any\]required

The arguments to emit.

### [Returns](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#returns-4)

returnsAwaitable\[bool\]

Always return True.

[Previous\\
\\
LangGraphAgent](https://docs.copilotkit.ai/reference/sdk/python/LangGraphAgent) [Next\\
\\
CrewAIAgent](https://docs.copilotkit.ai/reference/sdk/python/CrewAIAgent)

### On this page

[copilotkit\_customize\_config](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#copilotkit_customize_config) [Examples](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#examples) [Parameters](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#parameters) [Returns](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#returns) [copilotkit\_exit](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#copilotkit_exit) [Examples](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#examples-1) [Parameters](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#parameters-1) [Returns](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#returns-1) [copilotkit\_emit\_state](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#copilotkit_emit_state) [Examples](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#examples-2) [Parameters](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#parameters-2) [Returns](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#returns-2) [copilotkit\_emit\_message](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#copilotkit_emit_message) [Examples](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#examples-3) [Parameters](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#parameters-3) [Returns](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#returns-3) [copilotkit\_emit\_tool\_call](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#copilotkit_emit_tool_call) [Parameters](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#parameters-4) [Returns](https://docs.copilotkit.ai/reference/sdk/python/LangGraph#returns-4)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/sdk/python/LangGraph.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## CopilotKit Remote Endpoints
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageCopilotKitRemoteEndpoint

Python