# GoogleGenerativeAIAdapter

Copilot Runtime adapter for Google Generative AI (e.g. Gemini).

Copilot Runtime adapter for Google Generative AI (e.g. Gemini).

## [Example](https://docs.copilotkit.ai/reference/classes/llm-adapters/GoogleGenerativeAIAdapter\#example)

```
import { CopilotRuntime, GoogleGenerativeAIAdapter } from "@copilotkit/runtime";
const { GoogleGenerativeAI } = require("@google/generative-ai");

const genAI = new GoogleGenerativeAI(process.env["GOOGLE_API_KEY"]);

const copilotKit = new CopilotRuntime();

return new GoogleGenerativeAIAdapter({ model: "gemini-1.5-pro" });
```

## [Constructor Parameters](https://docs.copilotkit.ai/reference/classes/llm-adapters/GoogleGenerativeAIAdapter\#constructor-parameters)

modelstring

A custom Google Generative AI model to use.

[Previous\\
\\
GroqAdapter](https://docs.copilotkit.ai/reference/classes/llm-adapters/GroqAdapter) [Next\\
\\
CopilotTask](https://docs.copilotkit.ai/reference/classes/CopilotTask)

### On this page

[Example](https://docs.copilotkit.ai/reference/classes/llm-adapters/GoogleGenerativeAIAdapter#example) [Constructor Parameters](https://docs.copilotkit.ai/reference/classes/llm-adapters/GoogleGenerativeAIAdapter#constructor-parameters)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/classes/llm-adapters/GoogleGenerativeAIAdapter.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## CrewAI Documentation
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageCopilot Infrastructure for CrewAI Crews