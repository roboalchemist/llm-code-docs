# Chat with an Agent

Chat with an agent using CopilotKit's UI components.

This video shows the [coagents starter](https://github.com/CopilotKit/CopilotKit/tree/main/examples/coagents-starter) repo with various Copilot UI components applied to it!

## [What is this?](https://docs.copilotkit.ai/coagents/agentic-chat-ui\#what-is-this)

Agentic chat UIs are ways for your users to interact with your agent. CopilotKit provides a variety of different components to choose from, each
with their own unique use cases.

If you've gone through the [getting started guide](https://docs.copilotkit.ai/coagents/quickstart/langgraph) **you already have a agentic chat UI setup**! Nothing else is needed
to get started.

## [When should I use this?](https://docs.copilotkit.ai/coagents/agentic-chat-ui\#when-should-i-use-this)

CopilotKit provides a variety of different batteries-included components to choose from to create agent native applications. They scale
from simple chat UIs to completely custom applications.

CopilotPopupCopilotSidebarCopilotChatHeadless UI

`CopilotPopup` is a convenience wrapper for `CopilotChat` that lives at the same level as your main content in the view hierarchy. It provides **a floating chat interface** that can be toggled on and off.

![Popup Example](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/popup-example.gif)

```
import { CopilotPopup } from "@copilotkit/react-ui";

export function YourApp() {
  return (
    <>
      <YourMainContent />
      <CopilotPopup
        instructions={"You are assisting the user as best as you can. Answer in the best way possible given the data you have."}
        labels={{
          title: "Popup Assistant",
          initial: "Need any help?",
        }}
      />
    </>
  );
}
```

[Previous\\
\\
Quickstart (LangGraph)](https://docs.copilotkit.ai/coagents/quickstart/langgraph) [Next\\
\\
Generative UI](https://docs.copilotkit.ai/coagents/generative-ui)

### On this page

[What is this?](https://docs.copilotkit.ai/coagents/agentic-chat-ui#what-is-this) [When should I use this?](https://docs.copilotkit.ai/coagents/agentic-chat-ui#when-should-i-use-this)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/agentic-chat-ui.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## CrewAIAgent Overview
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageCrewAIAgent

Python