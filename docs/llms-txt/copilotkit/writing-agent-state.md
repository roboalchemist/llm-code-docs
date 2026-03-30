# Writing agent state

Write to agent's state from your application.

This video shows the [coagents starter](https://github.com/CopilotKit/CopilotKit/tree/main/examples/coagents-starter) repo with the previous steps applied to it!

## [What is this?](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write\#what-is-this)

This guide shows you how to write to your agent's state from your application.

## [When should I use this?](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write\#when-should-i-use-this)

You can use this when you want to provide the user with feedback about what your agent is doing, specifically
when your agent is calling tools. CopilotKit allows you to fully customize how these tools are rendered in the chat.

## [Implementation](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write\#implementation)

### [Run and Connect Your Agent to CopilotKit](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write\#run-and-connect-your-agent-to-copilotkit)

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already,
you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/getting-started) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point
as this guide uses it as a starting point.

### [Define the Agent State](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write\#define-the-agent-state)

LangGraph is stateful. As you transition between nodes, that state is updated and passed to the next node. For this example,
let's assume that our agent state looks something like this.

PythonTypeScript

agent-py/sample\_agent/agent.py

```
from copilotkit import CopilotKitState
from typing import Literal

class AgentState(CopilotKitState):
    language: Literal["english", "spanish"] = "english"
```

### [Call `setState` function from the `useCoAgent` hook](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write\#call-setstate-function-from-the-usecoagent-hook)

`useCoAgent` returns a `setState` function that you can use to update the agent state. Calling this
will update the agent state and trigger a rerender of anything that depends on the agent state.

ui/app/page.tsx

```
import { useCoAgent } from "@copilotkit/react-core";

// Define the agent state type, should match the actual state of your agent
type AgentState = {
  language: "english" | "spanish";
}

// Example usage in a pseudo React component
function YourMainContent() {
  const { state, setState } = useCoAgent<AgentState>({
    name: "sample_agent",
    initialState: { language: "spanish" }  // optionally provide an initial state
  });

  // ...

  const toggleLanguage = () => {
    setState({ language: state.language === "english" ? "spanish" : "english" });
  };

  // ...

  return (
    // style excluded for brevity
    <div>
      <h1>Your main content</h1>
      <p>Language: {state.language}</p>
      <button onClick={toggleLanguage}>Toggle Language</button>
    </div>
  );
}
```

### [Give it a try!](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write\#give-it-a-try)

You can now use the `setState` function to update the agent state and `state` to read it. Try toggling the language button
and talking to your agent. You'll see the language change to match the agent's state.

## [Advanced Usage](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write\#advanced-usage)

### [Re-run the agent with a hint about what's changed](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write\#re-run-the-agent-with-a-hint-about-whats-changed)

The new agent state will be used next time the agent runs.
If you want to re-run it manually, use the `run` argument on the `useCoAgent` hook.

The agent will be re-run, and it will get not only the latest updated state, but also a **hint** that can depend on the data delta between the previous and the current state.

ui/app/page.tsx

```
import { useCoAgent } from "@copilotkit/react-core";
import { TextMessage, MessageRole } from "@copilotkit/runtime-client-gql";

// ...

function YourMainContent() {
  const { state, setState, run } = useCoAgent<AgentState>({
    name: "sample_agent",
    initialState: { language: "spanish" }  // optionally provide an initial state
  });

  // setup to be called when some event in the app occurs
  const toggleLanguage = () => {
    const newLanguage = state.language === "english" ? "spanish" : "english";
    setState({ language: newLanguage });

    // re-run the agent and provide a hint about what's changed
    run(({ previousState, currentState }) => {
      return new TextMessage({
        role: MessageRole.User,
        content: `the language has been updated to ${currentState.language}`,
      });
    });
  };

  return (
    // ...
  );
}
```

### [Intermediately Stream and Render Agent State](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write\#intermediately-stream-and-render-agent-state)

By default, the LangGraph agent state will only update _between_ LangGraph node transitions --
which means state updates will be discontinuous and delayed.

You likely want to render the agent state as it updates **continuously.**

See **[predictive state updates](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates).**

[Previous\\
\\
Reading agent state](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read) [Next\\
\\
Agent state inputs and outputs](https://docs.copilotkit.ai/coagents/shared-state/workflow-execution)

### On this page

[What is this?](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write#what-is-this) [When should I use this?](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write#when-should-i-use-this) [Implementation](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write#implementation) [Run and Connect Your Agent to CopilotKit](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write#run-and-connect-your-agent-to-copilotkit) [Define the Agent State](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write#define-the-agent-state) [Call setState function from the useCoAgent hook](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write#call-setstate-function-from-the-usecoagent-hook) [Give it a try!](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write#give-it-a-try) [Advanced Usage](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write#advanced-usage) [Re-run the agent with a hint about what's changed](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write#re-run-the-agent-with-a-hint-about-whats-changed) [Intermediately Stream and Render Agent State](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write#intermediately-stream-and-render-agent-state)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/shared-state/in-app-agent-write.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Chat Components Overview
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this page