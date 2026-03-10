# useCopilotAction

The useCopilotAction hook allows your copilot to take action in the app.

![](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/use-copilot-action/useCopilotAction.gif)

`useCopilotAction` is a React hook that you can use in your application to provide
custom actions that can be called by the AI. Essentially, it allows the Copilot to
execute these actions contextually during a chat, based on the user’s interactions
and needs.

Here's how it works:

Use `useCopilotAction` to set up actions that the Copilot can call. To provide
more context to the Copilot, you can provide it with a `description` (for example to explain
what the action does, under which conditions it can be called, etc.).

Then you define the parameters of the action, which can be simple, e.g. primitives like strings or numbers,
or complex, e.g. objects or arrays.

Finally, you provide a `handler` function that receives the parameters and returns a result.
CopilotKit takes care of automatically inferring the parameter types, so you get type safety
and autocompletion for free.

To render a custom UI for the action, you can provide a `render()` function. This function
lets you render a custom component or return a string to display.

## [Usage](https://docs.copilotkit.ai/reference/hooks/useCopilotAction\#usage)

### [Simple Usage](https://docs.copilotkit.ai/reference/hooks/useCopilotAction\#simple-usage)

```
useCopilotAction({
  name: "sayHello",
  description: "Say hello to someone.",
  parameters: [\
    {\
      name: "name",\
      type: "string",\
      description: "name of the person to say greet",\
    },\
  ],
  handler: async ({ name }) => {
    alert(`Hello, ${name}!`);
  },
});
```

## [Generative UI](https://docs.copilotkit.ai/reference/hooks/useCopilotAction\#generative-ui)

This hooks enables you to dynamically generate UI elements and render them in the copilot chat. For more information, check out the [Generative UI](https://docs.copilotkit.ai/guides/generative-ui) page.

## [Parameters](https://docs.copilotkit.ai/reference/hooks/useCopilotAction\#parameters)

actionActionrequired

The function made available to the Copilot. See [Action](https://docs.copilotkit.ai/reference/hooks/useCopilotAction#action).

namestringrequired

The name of the action.

handler(args) => Promise<any>required

The handler of the action.

descriptionstring

A description of the action. This is used to instruct the Copilot on how to
use the action.

available'enabled' \| 'disabled' \| 'remote'

Use this property to control when the action is available to the Copilot. When set to `"remote"`, the action is
available only for remote agents.

followUpboolean

Default:"true"

Whether to report the result of a function call to the LLM which will then provide a follow-up response. Pass `false` to disable

parametersParameter\[\]

The parameters of the action. See [Parameter](https://docs.copilotkit.ai/reference/hooks/useCopilotAction#parameter).

namestringrequired

The name of the parameter.

typestringrequired

The type of the argument. One of:

- `"string"`
- `"number"`
- `"boolean"`
- `"object"`
- `"object[]"`
- `"string[]"`
- `"number[]"`
- `"boolean[]"`

descriptionstring

A description of the argument. This is used to instruct the Copilot on what
this argument is used for.

enumstring\[\]

For string arguments, you can provide an array of possible values.

requiredboolean

Whether or not the argument is required. Defaults to true.

attributes

If the argument is of a complex type, i.e. `object` or `object[]`, this field
lets you define the attributes of the object. For example:

```
{
  name: "addresses",
  description: "The addresses extracted from the text.",
  type: "object[]",
  attributes: [\
    {\
      name: "street",\
      type: "string",\
      description: "The street of the address.",\
    },\
    {\
      name: "city",\
      type: "string",\
      description: "The city of the address.",\
    },\
    // ...\
  ],
}
```

renderstring \| (props: ActionRenderProps<T>) => string

Render lets you define a custom component or string to render instead of the
default. You can either pass in a string or a function that takes the following props:

status'inProgress' \| 'executing' \| 'complete'

- `"inProgress"`: arguments are dynamically streamed to the function, allowing you to adjust your UI in real-time.
- `"executing"`: The action handler is executing.
- `"complete"`: The action handler has completed execution.

argsT

The arguments passed to the action in real time. When the status is `"inProgress"`, they are
possibly incomplete.

resultany

The result returned by the action. It is only available when the status is `"complete"`.

renderAndWaitForResponse(props: ActionRenderPropsWait<T>) => React.ReactElement

This is similar to `render`, but provides a `respond` function in the props that you must call with the user's response. The component will remain rendered until `respond` is called. The response will be passed as the result to the action handler.

status'inProgress' \| 'executing' \| 'complete'

- `"inProgress"`: arguments are dynamically streamed to the function, allowing you to adjust your UI in real-time.
- `"executing"`: The action handler is executing.
- `"complete"`: The action handler has completed execution.

argsT

The arguments passed to the action in real time. When the status is `"inProgress"`, they are
possibly incomplete.

respond(result: any) => void

A function that must be called with the user's response. The response will be passed as the result to the action handler.
Only available when status is `"executing"`.

resultany

The result returned by the action. It is only available when the status is `"complete"`.

dependenciesany\[\]

An optional array of dependencies.

[Previous\\
\\
useCopilotReadable](https://docs.copilotkit.ai/reference/hooks/useCopilotReadable) [Next\\
\\
useCopilotAdditionalInstructions](https://docs.copilotkit.ai/reference/hooks/useCopilotAdditionalInstructions)

### On this page

[Usage](https://docs.copilotkit.ai/reference/hooks/useCopilotAction#usage) [Simple Usage](https://docs.copilotkit.ai/reference/hooks/useCopilotAction#simple-usage) [Generative UI](https://docs.copilotkit.ai/reference/hooks/useCopilotAction#generative-ui) [Parameters](https://docs.copilotkit.ai/reference/hooks/useCopilotAction#parameters)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/hooks/useCopilotAction.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## State Machine Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageOverview