# Loading Agent State

Learn how threadId is used to load previous agent states.

### [Setting the threadId](https://docs.copilotkit.ai/coagents/persistence/loading-agent-state\#setting-the-threadid)

When setting the `threadId` property in CopilotKit, i.e:

When using LangGraph platform, the `threadId` must be a UUID.

```
<CopilotKit threadId="2140b272-7180-410d-9526-f66210918b13">
  <YourApp />
</CopilotKit>
```

CopilotKit will restore the complete state of the thread, including the messages, from the database. (See [Message Persistence](https://docs.copilotkit.ai/coagents/persistence/message-persistence) for more details.)

### [Loading Agent State](https://docs.copilotkit.ai/coagents/persistence/loading-agent-state\#loading-agent-state)

This means that the state of any agent will also be restored. For example:

```
const { state } = useCoAgent({name: "research_agent"});

// state will now be the state of research_agent in the thread id given above
```

### [Learn More](https://docs.copilotkit.ai/coagents/persistence/loading-agent-state\#learn-more)

To learn more about persistence and state in CopilotKit, see:

- [Reading agent state](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-read)
- [Writing agent state](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write)
- [Loading Message History](https://docs.copilotkit.ai/coagents/persistence/loading-message-history)

[Previous\\
\\
Multi-Agent Flows](https://docs.copilotkit.ai/coagents/multi-agent-flows) [Next\\
\\
Threads](https://docs.copilotkit.ai/coagents/persistence/loading-message-history)

### On this page

[Setting the threadId](https://docs.copilotkit.ai/coagents/persistence/loading-agent-state#setting-the-threadid) [Loading Agent State](https://docs.copilotkit.ai/coagents/persistence/loading-agent-state#loading-agent-state) [Learn More](https://docs.copilotkit.ai/coagents/persistence/loading-agent-state#learn-more)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/persistence/loading-agent-state.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## OpenAIAdapter Overview
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageExample

LLM Adapters