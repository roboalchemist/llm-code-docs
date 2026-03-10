# useLangGraphInterrupt

The useLangGraphInterrupt hook allows setting the generative UI to be displayed on LangGraph's Interrupt event.

`useLangGraphInterrupt` is a React hook that you can use in your application to provide
custom UI to be rendered when using `interrupt` by LangGraph.
Once an Interrupt event is emitted, that hook would execute, allowing to receive user input with a user experience to your choice.

## [Usage](https://docs.copilotkit.ai/reference/hooks/useLangGraphInterrupt\#usage)

### [Simple Usage](https://docs.copilotkit.ai/reference/hooks/useLangGraphInterrupt\#simple-usage)

app/page.tsx

```
import { useLangGraphInterrupt } from "@copilotkit/react-core";
// ...

const YourMainContent = () => {
  // ...

  // styles omitted for brevity
  useLangGraphInterrupt<string>({
    render: ({ event, resolve }) => (
      <div>
        <p>{event.value}</p>
        <form onSubmit={(e) => {
          e.preventDefault();
          resolve((e.target as HTMLFormElement).response.value);
        }}>
          <input type="text" name="response" placeholder="Enter your response" />
          <button type="submit">Submit</button>
        </form>
      </div>
    )
  });
  // ...

  return <div>{/* ... */}</div>
}
```

## [Parameters](https://docs.copilotkit.ai/reference/hooks/useLangGraphInterrupt\#parameters)

actionActionrequired

The action to perform when an Interrupt event is emitted. Either `handler` or `render` must be defined as arguments

namestringrequired

The name of the action.

handler(args: LangGraphInterruptRenderProps<T>) => any \| Promise<any>

A handler to programmatically resolve the Interrupt, or perform operations which result will be passed to the `render` method

render(props: LangGraphInterruptRenderProps<T>) => string \| React.ReactElement

Render lets you define a custom component or string to render when an Interrupt event is emitted.

enabled(args: { eventValue: TEventValue; agentMetadata: AgentSession }) => boolean

Method that returns a boolean, indicating if the interrupt action should run. Useful when using multiple interrupts

dependenciesany\[\]

An optional array of dependencies.

[Previous\\
\\
useCoAgentStateRender](https://docs.copilotkit.ai/reference/hooks/useCoAgentStateRender) [Next\\
\\
CopilotRuntime](https://docs.copilotkit.ai/reference/classes/CopilotRuntime)

### On this page

[Usage](https://docs.copilotkit.ai/reference/hooks/useLangGraphInterrupt#usage) [Simple Usage](https://docs.copilotkit.ai/reference/hooks/useLangGraphInterrupt#simple-usage) [Parameters](https://docs.copilotkit.ai/reference/hooks/useLangGraphInterrupt#parameters)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/hooks/useLangGraphInterrupt.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## CopilotTextarea Component
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageExample