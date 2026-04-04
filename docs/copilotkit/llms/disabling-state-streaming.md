# Disabling state streaming

Granularly control what is streamed to the frontend.

## [What is this?](https://docs.copilotkit.ai/coagents/advanced/disabling-state-streaming\#what-is-this)

By default, CopilotKit will stream both your state and tool calls to the frontend.
You can disable this by using CopilotKit's custom `RunnableConfig`.

## [When should I use this?](https://docs.copilotkit.ai/coagents/advanced/disabling-state-streaming\#when-should-i-use-this)

Occasionally, you'll want to disable streaming temporarily — for example, the LLM may be
doing something the current user should not see, like emitting tool calls or questions
pertaining to other employees in an HR system.

## [Implementation](https://docs.copilotkit.ai/coagents/advanced/disabling-state-streaming\#implementation)

### [Disable all streaming](https://docs.copilotkit.ai/coagents/advanced/disabling-state-streaming\#disable-all-streaming)

You can disable all message streaming and tool call streaming by passing `emit_messages=False` and `emit_tool_calls=False` to the CopilotKit config.

PythonTypeScript

```
from copilotkit.langgraph import copilotkit_customize_config

async def frontend_actions_node(state: AgentState, config: RunnableConfig):

    # 1) Configure CopilotKit not to emit messages
    modifiedConfig = copilotkit_customize_config(
        config,
        emit_messages=False, # if you want to disable message streaming
        emit_tool_calls=False # if you want to disable tool call streaming
    )

    # 2) Provide the actions to the LLM
    model = ChatOpenAI(model="gpt-4o").bind_tools([\
      *state["copilotkit"]["actions"],\
      # ... any tools you want to make available to the model\
    ])

    # 3) Call the model with CopilotKit's modified config
    response = await model.ainvoke(state["messages"], modifiedConfig)

    # don't return the new response to hide it from the user
    return state
```

BEWARE!

In LangGraph Python, the `config` variable in the surrounding namespace is **implicitly** passed into LangChain LLM calls, even when not explicitly provided.

This is why we create a new variable `modifiedConfig` rather than modifying `config` directly. If we modified `config` itself, it would change the default configuration for all subsequent LLM calls in that namespace.

```