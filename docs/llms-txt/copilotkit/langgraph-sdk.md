# LangGraph SDK

The CopilotKit LangGraph SDK for Python allows you to build and run LangGraph workflows with CopilotKit.

## [copilotkit\_customize\_config](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#copilotkit_customize_config)

Customize the LangGraph configuration for use in CopilotKit.

To install the CopilotKit SDK, run:

```
pip install copilotkit
```

### [Examples](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#examples)

Disable emitting messages and tool calls:

```
from copilotkit.langgraph import copilotkit_customize_config

config = copilotkit_customize_config(
    config,
    emit_messages=False,
    emit_tool_calls=False
)
```

To emit a tool call as streaming LangGraph state, pass the destination key in state,
the tool name and optionally the tool argument. (If you don't pass the argument name,
all arguments are emitted under the state key.)

```
from copilotkit.langgraph import copilotkit_customize_config

config = copilotkit_customize_config(
    config,
    emit_intermediate_state=[\
       {\
            "state_key": "steps",\
            "tool": "SearchTool",\
            "tool_argument": "steps"\
        },\
    ]
)
```

### [Parameters](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#parameters)

base\_configOptional\[RunnableConfig\]

The LangChain/LangGraph configuration to customize. Pass None to make a new configuration.

emit\_messagesOptional\[bool\]

Configure how messages are emitted. By default, all messages are emitted. Pass False to disable emitting messages.

emit\_tool\_callsOptional\[Union\[bool, str, List\[str\]\]\]

Configure how tool calls are emitted. By default, all tool calls are emitted. Pass False to disable emitting tool calls. Pass a string or list of strings to emit only specific tool calls.

emit\_intermediate\_stateOptional\[List\[IntermediateStateConfig\]\]

Lets you emit tool calls as streaming LangGraph state.

### [Returns](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#returns)

returnsRunnableConfig

The customized LangGraph configuration.

## [copilotkit\_exit](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#copilotkit_exit)

Exits the current agent after the run completes. Calling copilotkit\_exit() will
not immediately stop the agent. Instead, it signals to CopilotKit to stop the agent after
the run completes.

### [Examples](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#examples-1)

```
from copilotkit.langgraph import copilotkit_exit

def my_node(state: Any):
    await copilotkit_exit(config)
    return state
```

### [Parameters](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#parameters-1)

configRunnableConfigrequired

The LangGraph configuration.

### [Returns](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#returns-1)

returnsAwaitable\[bool\]

Always return True.

## [copilotkit\_emit\_state](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#copilotkit_emit_state)

Emits intermediate state to CopilotKit. Useful if you have a longer running node and you want to
update the user with the current state of the node.

### [Examples](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#examples-2)

```
from copilotkit.langgraph import copilotkit_emit_state

for i in range(10):
    await some_long_running_operation(i)
    await copilotkit_emit_state(config, {"progress": i})
```

### [Parameters](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#parameters-2)

configRunnableConfigrequired

The LangGraph configuration.

stateAnyrequired

The state to emit (Must be JSON serializable).

### [Returns](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#returns-2)

returnsAwaitable\[bool\]

Always return True.

## [copilotkit\_emit\_message](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#copilotkit_emit_message)

Manually emits a message to CopilotKit. Useful in longer running nodes to update the user.
Important: You still need to return the messages from the node.

### [Examples](https://docs.copilotkit.ai/reference/sdk/python/LangGraph\#examples-3)

```
from copilotkit.langgraph import copilotkit_emit_message

message = "Step 1 of 10 complete"
await copilotkit_emit_message(config, message)