# GroqAdapter

Copilot Runtime adapter for Groq.

Copilot Runtime adapter for Groq.

## [Example](https://docs.copilotkit.ai/reference/classes/llm-adapters/GroqAdapter\#example)

```
import { CopilotRuntime, GroqAdapter } from "@copilotkit/runtime";
import { Groq } from "groq-sdk";

const groq = new Groq({ apiKey: process.env["GROQ_API_KEY"] });

const copilotKit = new CopilotRuntime();

return new GroqAdapter({ groq, model: "<model-name>" });
```

## [Constructor Parameters](https://docs.copilotkit.ai/reference/classes/llm-adapters/GroqAdapter\#constructor-parameters)

groqGroq

An optional Groq instance to use.

modelstring

The model to use.

disableParallelToolCallsboolean

Default:"false"

Whether to disable parallel tool calls.
You can disable parallel tool calls to force the model to execute tool calls sequentially.
This is useful if you want to execute tool calls in a specific order so that the state changes
introduced by one tool call are visible to the next tool call. (i.e. new actions or readables)

[Previous\\
\\
LangChainAdapter](https://docs.copilotkit.ai/reference/classes/llm-adapters/LangChainAdapter) [Next\\
\\
GoogleGenerativeAIAdapter](https://docs.copilotkit.ai/reference/classes/llm-adapters/GoogleGenerativeAIAdapter)

### On this page

[Example](https://docs.copilotkit.ai/reference/classes/llm-adapters/GroqAdapter#example) [Constructor Parameters](https://docs.copilotkit.ai/reference/classes/llm-adapters/GroqAdapter#constructor-parameters)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/classes/llm-adapters/GroqAdapter.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## OpenAI Assistant Adapter
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageExample

LLM Adapters