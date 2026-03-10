# LangGraph SDK

The CopilotKit LangGraph SDK for JavaScript allows you to build and run LangGraph workflows with CopilotKit.

## [copilotkitCustomizeConfig](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#copilotkitcustomizeconfig)

Customize the LangGraph configuration for use in CopilotKit.

To the CopilotKit SDK, run:

```
npm install @copilotkit/sdk-js
```

### [Examples](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#examples)

Disable emitting messages and tool calls:

```
import { copilotkitCustomizeConfig } from "@copilotkit/sdk-js";

config = copilotkitCustomizeConfig(
  config,
  emitMessages=false,
  emitToolCalls=false
)
```

To emit a tool call as streaming LangGraph state, pass the destination key in state,
the tool name and optionally the tool argument. (If you don't pass the argument name,
all arguments are emitted under the state key.)

```
import { copilotkitCustomizeConfig } from "@copilotkit/sdk-js";

config = copilotkitCustomizeConfig(
  config,
  emitIntermediateState=[\
    {\
      "stateKey": "steps",\
      "tool": "SearchTool",\
      "toolArgument": "steps",\
    },\
  ],
)
```

### [Parameters](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#parameters)

baseConfigRunnableConfigrequired

The LangChain/LangGraph configuration to customize.

optionsOptionsConfig

Configuration options:

- `emitMessages: boolean?`
Configure how messages are emitted. By default, all messages are emitted. Pass false to
disable emitting messages.
- `emitToolCalls: boolean | string | string[]?`
Configure how tool calls are emitted. By default, all tool calls are emitted. Pass false to
disable emitting tool calls. Pass a string or list of strings to emit only specific tool calls.
- `emitIntermediateState: IntermediateStateConfig[]?`
Lets you emit tool calls as streaming LangGraph state.

## [copilotkitExit](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#copilotkitexit)

Exits the current agent after the run completes. Calling copilotkit\_exit() will
not immediately stop the agent. Instead, it signals to CopilotKit to stop the agent after
the run completes.

### [Examples](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#examples-1)

```
import { copilotkitExit } from "@copilotkit/sdk-js";

async function myNode(state: Any):
  await copilotkitExit(config)
  return state
```

### [Parameters](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#parameters-1)

configRunnableConfigrequired

The LangChain/LangGraph configuration.

## [copilotkitEmitState](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#copilotkitemitstate)

Emits intermediate state to CopilotKit. Useful if you have a longer running node and you want to
update the user with the current state of the node.

### [Examples](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#examples-2)

```
import { copilotkitEmitState } from "@copilotkit/sdk-js";

for (let i = 0; i < 10; i++) {
  await someLongRunningOperation(i);
  await copilotkitEmitState(config, { progress: i });
}
```

### [Parameters](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#parameters-2)

configRunnableConfigrequired

The LangChain/LangGraph configuration.

stateanyrequired

The state to emit.

## [copilotkitEmitMessage](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#copilotkitemitmessage)

Manually emits a message to CopilotKit. Useful in longer running nodes to update the user.
Important: You still need to return the messages from the node.

### [Examples](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#examples-3)

```
import { copilotkitEmitMessage } from "@copilotkit/sdk-js";

const message = "Step 1 of 10 complete";
await copilotkitEmitMessage(config, message);

// Return the message from the node
return {
  "messages": [AIMessage(content=message)]
}
```

### [Parameters](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#parameters-3)

configRunnableConfigrequired

The LangChain/LangGraph configuration.

messagestringrequired

The message to emit.

## [copilotkitEmitToolCall](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#copilotkitemittoolcall)

Manually emits a tool call to CopilotKit.

### [Examples](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#examples-4)

```
import { copilotkitEmitToolCall } from "@copilotkit/sdk-js";

await copilotkitEmitToolCall(config, name="SearchTool", args={"steps": 10})
```

### [Parameters](https://docs.copilotkit.ai/reference/sdk/js/LangGraph\#parameters-4)

configRunnableConfigrequired

The LangChain/LangGraph configuration.

namestringrequired

The name of the tool to emit.

argsanyrequired

The arguments to emit.

[Previous\\
\\
CrewAI SDK](https://docs.copilotkit.ai/reference/sdk/python/CrewAI)

### On this page

[copilotkitCustomizeConfig](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#copilotkitcustomizeconfig) [Examples](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#examples) [Parameters](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#parameters) [copilotkitExit](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#copilotkitexit) [Examples](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#examples-1) [Parameters](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#parameters-1) [copilotkitEmitState](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#copilotkitemitstate) [Examples](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#examples-2) [Parameters](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#parameters-2) [copilotkitEmitMessage](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#copilotkitemitmessage) [Examples](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#examples-3) [Parameters](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#parameters-3) [copilotkitEmitToolCall](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#copilotkitemittoolcall) [Examples](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#examples-4) [Parameters](https://docs.copilotkit.ai/reference/sdk/js/LangGraph#parameters-4)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/sdk/js/LangGraph.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Multi-Agent Flows
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat are Multi-Agent Flows?