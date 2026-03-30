# LangChainAdapter

Copilot Runtime adapter for LangChain.

Copilot Runtime adapter for LangChain.

## [Example](https://docs.copilotkit.ai/reference/classes/llm-adapters/LangChainAdapter\#example)

```
import { CopilotRuntime, LangChainAdapter } from "@copilotkit/runtime";
import { ChatOpenAI } from "@langchain/openai";

const copilotKit = new CopilotRuntime();

const model = new ChatOpenAI({
  model: "gpt-4o",
  apiKey: "<your-api-key>",
});

return new LangChainAdapter({
  chainFn: async ({ messages, tools }) => {
    return model.bindTools(tools).stream(messages);
    // or optionally enable strict mode
    // return model.bindTools(tools, { strict: true }).stream(messages);
  }
});
```

The asynchronous handler function ( `chainFn`) can return any of the following:

- A simple `string` response
- A LangChain stream ( `IterableReadableStream`)
- A LangChain `BaseMessageChunk` object
- A LangChain `AIMessage` object

## [Constructor Parameters](https://docs.copilotkit.ai/reference/classes/llm-adapters/LangChainAdapter\#constructor-parameters)

chainFn(parameters: ChainFnParameters) => Promise<LangChainReturnType>required

A function that uses the LangChain API to generate a response.

[Previous\\
\\
AnthropicAdapter](https://docs.copilotkit.ai/reference/classes/llm-adapters/AnthropicAdapter) [Next\\
\\
GroqAdapter](https://docs.copilotkit.ai/reference/classes/llm-adapters/GroqAdapter)

### On this page

[Example](https://docs.copilotkit.ai/reference/classes/llm-adapters/LangChainAdapter#example) [Constructor Parameters](https://docs.copilotkit.ai/reference/classes/llm-adapters/LangChainAdapter#constructor-parameters)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/classes/llm-adapters/LangChainAdapter.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Loading Agent State
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageSetting the threadId

Persistence