# LangSmith

To trace your LLM runs with LangSmith, make sure to set up your environment variables:

.env

```
LANGCHAIN_API_KEY="<your-api-key>"
LANGCHAIN_PROJECT="<your-project-name>"
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com""
```

Next, use the `LangChainAdapter` to trace your CopilotKit runs:

```
const { LangChainAdapter } = await import("@copilotkit/runtime");
const { ChatOpenAI } = await import("@langchain/openai");

async function getLangChainOpenAIAdapter() {
  return new LangChainAdapter({
    chainFn: async ({ messages, tools, threadId }) => {
      const model = new ChatOpenAI({
        modelName: "gpt-4-1106-preview",
      }).bindTools(tools, {
        strict: true,
      });
      return model.stream(messages, {
        tools,
        metadata: { conversation_id: threadId },
      });
    },
  });
}
```

Note that `threadId` is passed to the model as `conversation_id` in the metadata.

[Previous\\
\\
Anonymous Telemetry](https://docs.copilotkit.ai/telemetry)

### On this page

No Headings

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/(root)/(other)/observability/langsmith.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Disabling State Streaming
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is this?

Advanced