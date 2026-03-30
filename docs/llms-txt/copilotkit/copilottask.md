# CopilotTask

CopilotTask is used to execute one-off tasks, for example on button click.

This class is used to execute one-off tasks, for example on button press. It can use the context available via [useCopilotReadable](https://docs.copilotkit.ai/reference/hooks/useCopilotReadable) and the actions provided by [useCopilotAction](https://docs.copilotkit.ai/reference/hooks/useCopilotAction), or you can provide your own context and actions.

## [Example](https://docs.copilotkit.ai/reference/classes/CopilotTask\#example)

In the simplest case, use CopilotTask in the context of your app by giving it instructions on what to do.

```
import { CopilotTask, useCopilotContext } from "@copilotkit/react-core";

export function MyComponent() {
  const context = useCopilotContext();

  const task = new CopilotTask({
    instructions: "Set a random message",
    actions: [\
      {\
        name: "setMessage",\
      description: "Set the message.",\
      argumentAnnotations: [\
        {\
          name: "message",\
          type: "string",\
          description:\
            "A message to display.",\
          required: true,\
        },\
      ],\
     }\
    ]
  });

  const executeTask = async () => {
    await task.run(context, action);
  }

  return (
    <>
      <button onClick={executeTask}>
        Execute task
      </button>
    </>
  )
}
```

Have a look at the [Presentation Example App](https://github.com/CopilotKit/CopilotKit/blob/main/CopilotKit/examples/next-openai/src/app/presentation/page.tsx) for a more complete example.

## [Constructor Parameters](https://docs.copilotkit.ai/reference/classes/CopilotTask\#constructor-parameters)

instructionsstringrequired

The instructions to be given to the assistant.

actionsFrontendAction<any>\[\]

An array of action definitions that can be called.

includeCopilotReadableboolean

Whether to include the copilot readable context in the task.

includeCopilotActionsboolean

Whether to include actions defined via useCopilotAction in the task.

forwardedParametersForwardedParametersInput

The forwarded parameters to use for the task.

runcontext: CopilotContextParams, data?: T

Run the task.

contextCopilotContextParamsrequired

The CopilotContext to use for the task. Use `useCopilotContext` to obtain the current context.

dataT

The data to use for the task.

[Previous\\
\\
GoogleGenerativeAIAdapter](https://docs.copilotkit.ai/reference/classes/llm-adapters/GoogleGenerativeAIAdapter) [Next\\
\\
Remote Endpoints](https://docs.copilotkit.ai/reference/sdk/python/RemoteEndpoints)

### On this page

[Example](https://docs.copilotkit.ai/reference/classes/CopilotTask#example) [Constructor Parameters](https://docs.copilotkit.ai/reference/classes/CopilotTask#constructor-parameters)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/classes/CopilotTask.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Copilot Textarea Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageInstall @copilotkit/react-textarea