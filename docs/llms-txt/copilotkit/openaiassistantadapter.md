# OpenAIAssistantAdapter

Copilot Runtime adapter for OpenAI Assistant API.

Copilot Runtime adapter for the OpenAI Assistant API.

## [Example](https://docs.copilotkit.ai/reference/classes/llm-adapters/OpenAIAssistantAdapter\#example)

```
import { CopilotRuntime, OpenAIAssistantAdapter } from "@copilotkit/runtime";
import OpenAI from "openai";

const copilotKit = new CopilotRuntime();

const openai = new OpenAI({
  organization: "<your-organization-id>",
  apiKey: "<your-api-key>",
});

return new OpenAIAssistantAdapter({
  openai,
  assistantId: "<your-assistant-id>",
  codeInterpreterEnabled: true,
  fileSearchEnabled: true,
});
```

## [Constructor Parameters](https://docs.copilotkit.ai/reference/classes/llm-adapters/OpenAIAssistantAdapter\#constructor-parameters)

assistantIdstringrequired

The ID of the assistant to use.

openaiOpenAI

An optional OpenAI instance to use. If not provided, a new instance will be created.

codeInterpreterEnabledboolean

Default:"true"

Whether to enable code interpretation.

fileSearchEnabledboolean

Default:"true"

Whether to enable file search.

disableParallelToolCallsboolean

Default:"false"

Whether to disable parallel tool calls.
You can disable parallel tool calls to force the model to execute tool calls sequentially.
This is useful if you want to execute tool calls in a specific order so that the state changes
introduced by one tool call are visible to the next tool call. (i.e. new actions or readables)

[Previous\\
\\
OpenAIAdapter](https://docs.copilotkit.ai/reference/classes/llm-adapters/OpenAIAdapter) [Next\\
\\
AnthropicAdapter](https://docs.copilotkit.ai/reference/classes/llm-adapters/AnthropicAdapter)

### On this page

[Example](https://docs.copilotkit.ai/reference/classes/llm-adapters/OpenAIAssistantAdapter#example) [Constructor Parameters](https://docs.copilotkit.ai/reference/classes/llm-adapters/OpenAIAssistantAdapter#constructor-parameters)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/classes/llm-adapters/OpenAIAssistantAdapter.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## LangChainAdapter Overview
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageExample

LLM Adapters