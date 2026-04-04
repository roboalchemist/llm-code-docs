# useCoAgent

The useCoAgent hook allows you to share state bidirectionally between your application and the agent.

Usage of this hook assumes some additional setup in your application, for more information
on that see the CoAgents [getting started guide](https://docs.copilotkit.ai/coagents/quickstart/langgraph).

![CoAgents demonstration](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/coagents/SharedStateCoAgents.gif)

This hook is used to integrate an agent into your application. With its use, you can
render and update the state of an agent, allowing for a dynamic and interactive experience.
We call these shared state experiences agentic copilots, or CoAgents for short.

## [Usage](https://docs.copilotkit.ai/reference/hooks/useCoAgent\#usage)

### [Simple Usage](https://docs.copilotkit.ai/reference/hooks/useCoAgent\#simple-usage)

```
import { useCoAgent } from "@copilotkit/react-core";

type AgentState = {
  count: number;
}

const agent = useCoAgent<AgentState>({
  name: "my-agent",
  initialState: {
    count: 0,
  },
});

```

`useCoAgent` returns an object with the following properties:

```
const {
  name,     // The name of the agent currently being used.
  nodeName, // The name of the current LangGraph node.
  state,    // The current state of the agent.
  setState, // A function to update the state of the agent.
  running,  // A boolean indicating if the agent is currently running.
  start,    // A function to start the agent.
  stop,     // A function to stop the agent.
  run,      // A function to re-run the agent. Takes a HintFunction to inform the agent why it is being re-run.
} = agent;
```

Finally we can leverage these properties to create reactive experiences with the agent!

```
const { state, setState } = useCoAgent<AgentState>({
  name: "my-agent",
  initialState: {
    count: 0,
  },
});

return (
  <div>
    <p>Count: {state.count}</p>
    <button onClick={() => setState({ count: state.count + 1 })}>Increment</button>
  </div>
);
```

This reactivity is bidirectional, meaning that changes to the state from the agent will be reflected in the UI and vice versa.

## [Parameters](https://docs.copilotkit.ai/reference/hooks/useCoAgent\#parameters)

optionsUseCoagentOptions<T>required

The options to use when creating the coagent.

namestringrequired

The name of the agent to use.

initialStateT \| any

The initial state of the agent.

stateT \| any

State to manage externally if you are using this hook with external state management.

setState(newState: T \| ((prevState: T \| undefined) => T)) => void

A function to update the state of the agent if you are using this hook with external state management.

[Previous\\
\\
useCopilotChatSuggestions](https://docs.copilotkit.ai/reference/hooks/useCopilotChatSuggestions) [Next\\
\\
useCoAgentStateRender](https://docs.copilotkit.ai/reference/hooks/useCoAgentStateRender)

### On this page

[Usage](https://docs.copilotkit.ai/reference/hooks/useCoAgent#usage) [Simple Usage](https://docs.copilotkit.ai/reference/hooks/useCoAgent#simple-usage) [Parameters](https://docs.copilotkit.ai/reference/hooks/useCoAgent#parameters)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/hooks/useCoAgent.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## CopilotKit Component Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageExample