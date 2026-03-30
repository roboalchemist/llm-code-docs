# Reading agent state

Read the realtime agent state in your native application.

![read agent state](https://docs.copilotkit.ai/_next/image?url=%2Fimages%2Fcoagents%2Fread-agent-state.png&w=3840&q=75)

Pictured above is the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) with
the [implementation](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read#implementation) section applied!

## [What is this?](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read\#what-is-this)

You can easily use the realtime agent state not only in the chat UI, but also in the native application UX.

## [When should I use this?](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read\#when-should-i-use-this)

You can use this when you want to provide the user with feedback about your agent's state. As your agent's
state updates, you can reflect these updates natively in your application.

## [Implementation](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read\#implementation)

### [Run and Connect Your Agent to CopilotKit](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read\#run-and-connect-your-agent-to-copilotkit)

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already,
you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/getting-started) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point
as this guide uses it as a starting point.

### [Define the Agent State](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read\#define-the-agent-state)

LangGraph is stateful. As you transition between nodes, that state is updated and passed to the next node. For this example,
let's assume that our agent state looks something like this.

PythonTypeScript

agent-py/sample\_agent/agent.py

```
from copilotkit import CopilotKitState
from typing import Literal

class AgentState(CopilotKitState):
    language: Literal["english", "spanish"] = "spanish"

def chat_node(state: AgentState, config: RunnableConfig):
  # If language is not defined, set a value.
  # this is because a default value in a state class is not read on runtime
  language = state.get("language", "spanish")

  # ... add the rest of the node implementation and use the language variable

  return {
    # ... add the rest of state to return
    # return the language to make it available for the next nodes & frontend to read
    "language": language
  }
```

### [Use the `useCoAgent` Hook](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read\#use-the-usecoagent-hook)

With your agent connected and running all that is left is to call the [useCoAgent](https://docs.copilotkit.ai/reference/hooks/useCoAgent) hook, pass the agent's name, and
optionally provide an initial state.

ui/app/page.tsx

```
import { useCoAgent } from "@copilotkit/react-core";

// Define the agent state type, should match the actual state of your agent
type AgentState = {
  language: "english" | "spanish";
}

function YourMainContent() {
  const { state } = useCoAgent<AgentState>({
    name: "sample_agent",
    initialState: { language: "spanish" }  // optionally provide an initial state
  });

  // ...

  return (
    // style excluded for brevity
    <div>
      <h1>Your main content</h1>
      <p>Language: {state.language}</p>
    </div>
  );
}
```

The `state` in `useCoAgent` is reactive and will automatically update when the agent's state changes.

### [Give it a try!](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read\#give-it-a-try)

As the agent state updates, your `state` variable will automatically update with it! In this case, you'll see the
language set to "spanish" as that's the initial state we set.

## [Rendering agent state in the chat](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read\#rendering-agent-state-in-the-chat)

You can also render the agent's state in the chat UI. This is useful for informing the user about the agent's state in a
more in-context way. To do this, you can use the [useCoAgentStateRender](https://docs.copilotkit.ai/reference/hooks/useCoAgentStateRender) hook.

ui/app/page.tsx

```
import { useCoAgentStateRender } from "@copilotkit/react-core";

// Define the agent state type, should match the actual state of your agent
type AgentState = {
  language: "english" | "spanish";
}

function YourMainContent() {
  // ...

  useCoAgentStateRender({
    name: "sample_agent",
    render: ({ state }) => {
      if (!state.language) return null;
      return <div>Language: {state.language}</div>;
    },
  });
  // ...
}
```

The `state` in `useCoAgentStateRender` is reactive and will automatically update when the agent's state changes.

## [Intermediately Stream and Render Agent State](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read\#intermediately-stream-and-render-agent-state)

By default, the LangGraph agent state will only update _between_ LangGraph node transitions --
which means state updates will be discontinuous and delayed.

You likely want to render the agent state as it updates **continuously.**

See **[predictive state updates](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates).**

[Previous\\
\\
Shared State](https://docs.copilotkit.ai/coagents/shared-state) [Next\\
\\
Writing agent state](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write)

### On this page

[What is this?](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read#what-is-this) [When should I use this?](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read#when-should-i-use-this) [Implementation](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read#implementation) [Run and Connect Your Agent to CopilotKit](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read#run-and-connect-your-agent-to-copilotkit) [Define the Agent State](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read#define-the-agent-state) [Use the useCoAgent Hook](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read#use-the-usecoagent-hook) [Give it a try!](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read#give-it-a-try) [Rendering agent state in the chat](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read#rendering-agent-state-in-the-chat) [Intermediately Stream and Render Agent State](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read#intermediately-stream-and-render-agent-state)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/shared-state/in-app-agent-read.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

![read agent state](https://docs.copilotkit.ai/_next/image?url=%2Fimages%2Fcoagents%2Fread-agent-state.png&w=3840&q=75)

## Human-in-the-Loop Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is this?

[Human in the Loop (HITL)](https://docs.copilotkit.ai/coagents/human-in-the-loop)