# OpenAIAdapter

Copilot Runtime adapter for OpenAI.

Copilot Runtime adapter for OpenAI.

## [Example](https://docs.copilotkit.ai/reference/classes/llm-adapters/OpenAIAdapter\#example)

```
import { CopilotRuntime, OpenAIAdapter } from "@copilotkit/runtime";
import OpenAI from "openai";

const copilotKit = new CopilotRuntime();

const openai = new OpenAI({
  organization: "<your-organization-id>", // optional
  apiKey: "<your-api-key>",
});

return new OpenAIAdapter({ openai });
```

## [Example with Azure OpenAI](https://docs.copilotkit.ai/reference/classes/llm-adapters/OpenAIAdapter\#example-with-azure-openai)

```
import { CopilotRuntime, OpenAIAdapter } from "@copilotkit/runtime";
import OpenAI from "openai";

// The name of your Azure OpenAI Instance.
// https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
const instance = "<your instance name>";

// Corresponds to your Model deployment within your OpenAI resource, e.g. my-gpt35-16k-deployment
// Navigate to the Azure OpenAI Studio to deploy a model.
const model = "<your model>";

const apiKey = process.env["AZURE_OPENAI_API_KEY"];
if (!apiKey) {
  throw new Error("The AZURE_OPENAI_API_KEY environment variable is missing or empty.");
}

const copilotKit = new CopilotRuntime();

const openai = new OpenAI({
  apiKey,
  baseURL: `https://${instance}.openai.azure.com/openai/deployments/${model}`,
  defaultQuery: { "api-version": "2024-04-01-preview" },
  defaultHeaders: { "api-key": apiKey },
});

return new OpenAIAdapter({ openai });
```

## [Constructor Parameters](https://docs.copilotkit.ai/reference/classes/llm-adapters/OpenAIAdapter\#constructor-parameters)

openaiOpenAI

An optional OpenAI instance to use. If not provided, a new instance will be
created.

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
CopilotRuntime](https://docs.copilotkit.ai/reference/classes/CopilotRuntime) [Next\\
\\
OpenAIAssistantAdapter](https://docs.copilotkit.ai/reference/classes/llm-adapters/OpenAIAssistantAdapter)

### On this page

[Example](https://docs.copilotkit.ai/reference/classes/llm-adapters/OpenAIAdapter#example) [Example with Azure OpenAI](https://docs.copilotkit.ai/reference/classes/llm-adapters/OpenAIAdapter#example-with-azure-openai) [Constructor Parameters](https://docs.copilotkit.ai/reference/classes/llm-adapters/OpenAIAdapter#constructor-parameters)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/classes/llm-adapters/OpenAIAdapter.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## GroqAdapter Overview
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageExample

LLM Adapters