# useCoAgentStateRender

The useCoAgentStateRender hook allows you to render the state of the agent in the chat.

The useCoAgentStateRender hook allows you to render UI or text based components on a Agentic Copilot's state in the chat.
This is particularly useful for showing intermediate state or progress during Agentic Copilot operations.

## [Usage](https://docs.copilotkit.ai/reference/hooks/useCoAgentStateRender\#usage)

### [Simple Usage](https://docs.copilotkit.ai/reference/hooks/useCoAgentStateRender\#simple-usage)

```
import { useCoAgentStateRender } from "@copilotkit/react-core";

type YourAgentState = {
  agent_state_property: string;
}

useCoAgentStateRender<YourAgentState>({
  name: "basic_agent",
  nodeName: "optionally_specify_a_specific_node",
  render: ({ status, state, nodeName }) => {
    return (
      <YourComponent
        agentStateProperty={state.agent_state_property}
        status={status}
        nodeName={nodeName}
      />
    );
  },
});
```

This allows for you to render UI components or text based on what is happening within the agent.

### [Example](https://docs.copilotkit.ai/reference/hooks/useCoAgentStateRender\#example)

A great example of this is in our Perplexity Clone where we render the progress of an agent's internet search as it is happening.
You can play around with it below or learn how to build it with its [demo](https://docs.copilotkit.ai/coagents/videos/perplexity-clone).

This example is hosted on Vercel and may take a few seconds to load.

AI Researcher