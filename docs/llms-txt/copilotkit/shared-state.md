# Shared State

Create a two-way connection between your UI and agent state.

![Shared State Demo](https://docs.copilotkit.ai/_next/image?url=%2Fimages%2Fcoagents%2FSharedStateCoAgents.gif&w=3840&q=75)

This video demonstrates the [Research Canvas](https://docs.copilotkit.ai/coagents/examples/research-canvas) utilizing shared state.

## [What is shared state?](https://docs.copilotkit.ai/coagents/shared-state\#what-is-shared-state)

CoAgents maintain a shared state that seamlessly connects your UI with the agent's execution. This shared state system allows you to:

- Display the agent's current progress and intermediate results
- Update the agent's state through UI interactions
- React to state changes in real-time across your application

![Agentic Copilot State Diagram](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/coagents/coagents-state-diagram.png)

The foundation of this system is built on LangGraph's stateful architecture. Unlike traditional LangChains, LangGraphs maintain their
internal state throughout execution, which you can access via the `useCoAgentState` hook.

## [When should I use this?](https://docs.copilotkit.ai/coagents/shared-state\#when-should-i-use-this)

State streaming is perfect when you want to faciliate collaboration between your agent and the user. Any state that your LangGraph agent
persists will be automatically shared by the UI. Similarly, any state that the user updates in the UI will be automatically reflected

This allows for a consistent experience where both the agent and the user are on the same page.

[Previous\\
\\
Node-based](https://docs.copilotkit.ai/coagents/human-in-the-loop/node-flow) [Next\\
\\
Reading agent state](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read)

### On this page

[What is shared state?](https://docs.copilotkit.ai/coagents/shared-state#what-is-shared-state) [When should I use this?](https://docs.copilotkit.ai/coagents/shared-state#when-should-i-use-this)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/shared-state/index.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

![Shared State Demo](https://docs.copilotkit.ai/_next/image?url=%2Fimages%2Fcoagents%2FSharedStateCoAgents.gif&w=3840&q=75)

## Frontend Actions Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageLet the Copilot Take Action