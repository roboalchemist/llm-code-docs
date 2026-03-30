# Multi-Agent Flows

Use multiple agents to orchestrate complex flows.

![Multi-Agent Flows](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/coagents/multi-agent-flows.png)

## [What are Multi-Agent Flows?](https://docs.copilotkit.ai/coagents/multi-agent-flows\#what-are-multi-agent-flows)

When building agentic applications, you often want to orchestrate complex flows together that require the coordination of multiple
agents. This is traditionally called multi-agent orchestration.

## [When should I use this?](https://docs.copilotkit.ai/coagents/multi-agent-flows\#when-should-i-use-this)

Multi-agent flows are useful when you want to orchestrate complex flows together that require the coordination of multiple agents. As
your agentic application grows, delegation of sub-tasks to other agents can help you scale key pieces of your application.

- Divide context into smaller chunks
- Delegate sub-tasks to other agents
- Use a single agent to orchestrate the flow

## [How does CopilotKit support this?](https://docs.copilotkit.ai/coagents/multi-agent-flows\#how-does-copilotkit-support-this)

CopilotKit can be used in either of two distinct modes: **Router Mode**, or **Agent Lock**. By default, CopilotKit
will use Router Mode, leveraging your defined LLM to route requests between agents.

### [Router Mode (default)](https://docs.copilotkit.ai/coagents/multi-agent-flows\#router-mode-default)

Router Mode is enabled by default when using CoAgents. To use it, specify a runtime URL prop in the `CopilotKit` provider component and omit the `agent` prop, like so:

```
<CopilotKit runtimeUrl="<copilot-runtime-url>">
  {/* Your application components */}
</CopilotKit>
```

In router mode, CopilotKit acts as a central hub, dynamically selecting and _routing_ requests between different agents or actions based on the user's input. This mode can be good for chat-first experiences where an LLM chatbot is the entry point for a range of interactions, which can stay in the chat UI or expand to include native React UI widgets.

In this mode, CopilotKit will intelligently route requests to the most appropriate agent or action based on the context and user input.

Be advised that when using this mode, you'll have to "exit the workflow" explicitly in your agent code.
You can find more information about it in the ["Exiting the agent loop" section](https://docs.copilotkit.ai/coagents/advanced/exit-agent).

Router mode requires that you set up an LLM adapter. See how in ["Set up a copilot runtime"](https://docs.copilotkit.ai/direct-to-llm/guides/quickstart?copilot-hosting=self-hosted#set-up-a-copilot-runtime-endpoint) section of the docs.

### [Agent Lock Mode](https://docs.copilotkit.ai/coagents/multi-agent-flows\#agent-lock-mode)

To use Agent Lock Mode, specify the agent name in the `CopilotKit` component with the `agent` prop:

```
<CopilotKit runtimeUrl="<copilot-runtime-url>" agent="<the-name-of-the-agent>">
  {/* Your application components */}
</CopilotKit>
```

In this mode, CopilotKit is configured to work exclusively with a specific agent. This mode is useful when you want to focus on a particular task or domain. Whereas in Router Mode the LLM and CopilotKit's router are free to switch between agents to handle user requests, in Agent Lock Mode all requests will stay within a single workflow graph, ensuring precise control over the workflow.

Use whichever mode works best for your app experience! Also, note that while you cannot nest `CopilotKit` providers, you can use different agents or modes in different areas of your app — for example, you may want a chatbot in router mode that can call on any agent or tool, but may also want to integrate one specific agent elsewhere for a more focused workflow.

[Previous\\
\\
Frontend Actions](https://docs.copilotkit.ai/coagents/frontend-actions) [Next\\
\\
Loading Agent State](https://docs.copilotkit.ai/coagents/persistence/loading-agent-state)

### On this page

[What are Multi-Agent Flows?](https://docs.copilotkit.ai/coagents/multi-agent-flows#what-are-multi-agent-flows) [When should I use this?](https://docs.copilotkit.ai/coagents/multi-agent-flows#when-should-i-use-this) [How does CopilotKit support this?](https://docs.copilotkit.ai/coagents/multi-agent-flows#how-does-copilotkit-support-this) [Router Mode (default)](https://docs.copilotkit.ai/coagents/multi-agent-flows#router-mode-default) [Agent Lock Mode](https://docs.copilotkit.ai/coagents/multi-agent-flows#agent-lock-mode)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/multi-agent-flows.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Copilot Sidebar Component
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageInstall Dependencies

[Chat Components](https://docs.copilotkit.ai/reference/components/chat)