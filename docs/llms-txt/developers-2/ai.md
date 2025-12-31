# Source: https://developers.raycast.com/api-reference/ai.md

# AI

The AI API provides developers with seamless access to AI functionality without requiring API keys, configuration, or extra dependencies.

{% hint style="info" %}
Some users might not have access to this API. If a user doesn't have access to Raycast Pro, they will be asked if they want to get access when your extension calls the AI API. If the user doesn't wish to get access, the API call will throw an error.

You can check if a user has access to the API using [`environment.canAccess(AI)`](https://developers.raycast.com/api-reference/environment).
{% endhint %}

## API Reference

### AI.ask

Ask AI anything you want. Use this in “no-view” Commands, effects, or callbacks. In a React component, you might want to use the [useAI util hook](https://developers.raycast.com/utilities/react-hooks/useai) instead.

#### Signature

```typescript
async function ask(prompt: string, options?: AskOptions): Promise<string> & EventEmitter;
```

#### Example

{% tabs %}
{% tab title="Basic Usage" %}

```typescript
import { AI, Clipboard } from "@raycast/api";

export default async function command() {
  const answer = await AI.ask("Suggest 5 jazz songs");

  await Clipboard.copy(answer);
}
```

{% endtab %}

{% tab title="Error handling" %}

```typescript
import { AI, showToast, Toast } from "@raycast/api";

export default async function command() {
  try {
    await AI.ask("Suggest 5 jazz songs");
  } catch (error) {
    // Handle error here, eg: by showing a Toast
    await showToast({
      style: Toast.Style.Failure,
      title: "Failed to generate answer",
    });
  }
}
```

{% endtab %}

{% tab title="Stream answer" %}

```typescript
import { AI, getSelectedFinderItems, showHUD } from "@raycast/api";
import fs from "fs";

export default async function main() {
  let allData = "";
  const [file] = await getSelectedFinderItems();

  const answer = AI.ask("Suggest 5 jazz songs");

  // Listen to "data" event to stream the answer
  answer.on("data", async (data) => {
    allData += data;
    await fs.promises.writeFile(`${file.path}`, allData.trim(), "utf-8");
  });

  await answer;

  await showHUD("Done!");
}
```

{% endtab %}

{% tab title="User Feedback" %}

```typescript
import { AI, getSelectedFinderItems, showHUD } from "@raycast/api";
import fs from "fs";

export default async function main() {
  let allData = "";
  const [file] = await getSelectedFinderItems();

  // If you're doing something that happens in the background
  // Consider showing a HUD or a Toast as the first step
  // To give users feedback about what's happening
  await showHUD("Generating answer...");

  const answer = await AI.ask("Suggest 5 jazz songs");

  await fs.promises.writeFile(`${file.path}`, allData.trim(), "utf-8");

  // Then, when everythig is done, notify the user again
  await showHUD("Done!");
}
```

{% endtab %}

{% tab title="Check for access" %}

```typescript
import { AI, getSelectedFinderItems, showHUD, environment } from "@raycast/api";
import fs from "fs";

export default async function main() {
  if (environment.canAccess(AI)) {
    const answer = await AI.ask("Suggest 5 jazz songs");
    await Clipboard.copy(answer);
  } else {
    await showHUD("You don't have access :(");
  }
}
```

{% endtab %}
{% endtabs %}

#### Parameters

| Name                                     | Description                                                  | Type                              |
| ---------------------------------------- | ------------------------------------------------------------ | --------------------------------- |
| prompt<mark style="color:red;">\*</mark> | The prompt to ask the AI.                                    | `string`                          |
| options                                  | Options to control which and how the AI model should behave. | [`AI.AskOptions`](#ai.askoptions) |

#### Return

A Promise that resolves with a prompt completion.

## Types

### AI.Creativity

Concrete tasks, such as fixing grammar, require less creativity while open-ended questions, such as generating ideas, require more.

```typescript
type Creativity = "none" | "low" | "medium" | "high" | "maximum" | number;
```

If a number is passed, it needs to be in the range 0-2. For larger values, 2 will be used. For lower values, 0 will be used.

### AI.Model

The AI model to use to answer to the prompt. Defaults to `AI.Model["OpenAI_GPT3.5-turbo"]`.

#### Enumeration members

| Model                                         | Description                                                                            |
| --------------------------------------------- | -------------------------------------------------------------------------------------- |
| OpenAI\_GPT5-mini                             | OpenAI's latest model, great for well-defined tasks and precise prompts.               |
| OpenAI\_GPT5-nano                             | OpenAI's latest model, great for summarization and classification tasks.               |
| OpenAI\_GPT4.1                                | OpenAI's flagship model optimized for complex problem solving.                         |
| OpenAI\_GPT4.1-mini                           | Balanced GPT-4.1 variant optimized for speed and cost efficiency.                      |
| OpenAI\_GPT4.1-nano                           | Fastest and most cost-effective GPT-4.1 variant.                                       |
| OpenAI\_GPT4                                  | Previous generation GPT-4 model with broad knowledge and complex instruction handling. |
| OpenAI\_GPT4-turbo                            | Previous generation GPT-4 with expanded context window.                                |
| OpenAI\_GPT4o                                 | Advanced OpenAI model optimized for speed and complex problem solving.                 |
| OpenAI\_GPT4o-mini                            | Fast and intelligent model for everyday tasks.                                         |
| OpenAI\_GPT5                                  | OpenAI's latest model, great for coding and agentic tasks across domains.              |
| OpenAI\_o3                                    | Advanced model excelling in math, science, coding, and visual tasks.                   |
| OpenAI\_o4-mini                               | Fast, efficient model optimized for coding and visual tasks.                           |
| OpenAI\_o1                                    | Advanced reasoning model for complex STEM problems.                                    |
| OpenAI\_o3-mini                               | Fast reasoning model optimized for STEM tasks.                                         |
| OpenAI\_GPT\_OSS\_20b                         | OpenAI's first open-source model, 20b variant.                                         |
| OpenAI\_GPT\_OSS\_120b                        | OpenAI's first open-source model, 120b variant.                                        |
| Anthropic\_Claude\_Haiku                      | Anthropic's fastest model with large context window for code and text analysis.        |
| Anthropic\_Claude\_Sonnet                     | Enhanced Claude model for complex tasks and visual reasoning.                          |
| Anthropic\_Claude\_Sonnet\_3.7                | Anthropic's most intelligent model.                                                    |
| Anthropic\_Claude\_4\_Sonnet                  | Anthropic's most intelligent model.                                                    |
| Anthropic\_Claude\_4\_Opus                    | Anthropic's model for complex tasks with exceptional fluency.                          |
| Anthropic\_Claude\_4.1\_Opus                  | Anthropic's model for complex tasks with exceptional fluency.                          |
| Perplexity\_Sonar                             | Fast Perplexity model with integrated search capabilities.                             |
| Perplexity\_Sonar\_Pro                        | Advanced Perplexity model for complex queries with search integration.                 |
| Perplexity\_Sonar\_Reasoning                  | Fast reasoning model powered by DeepSeek R1.                                           |
| Perplexity\_Sonar\_Reasoning\_Pro             | Premium reasoning model with DeepSeek R1 capabilities.                                 |
| Llama4\_Scout                                 | Advanced 17B parameter multimodal model with 16 experts.                               |
| Llama3.3\_70B                                 | Meta's state-of-the-art model for reasoning and general knowledge.                     |
| Llama3.1\_8B                                  | Fast, instruction-optimized open-source model.                                         |
| Llama3.1\_405B                                | Meta's flagship model with advanced capabilities across multiple domains.              |
| Mistral\_Nemo                                 | Small, Apache-licensed model built with NVIDIA.                                        |
| Mistral\_Large                                | Top-tier reasoning model with strong multilingual support.                             |
| Mistral\_Medium                               | A powerful, cost-effective, frontier-class multimodal model.                           |
| Mistral\_Small                                | Latest enterprise-grade small model with improved reasoning.                           |
| Mistral\_Codestral                            | Specialized model for code-related tasks and testing.                                  |
| Groq\_Kimi\_K2\_Instruct                      | Kimi K2 is a powerful and versatile AI model designed for a wide range of tasks.       |
| Groq\_Qwen3\_32B                              | The latest generation of large language models in the Qwen series.                     |
| DeepSeek\_R1\_Distill\_Llama\_3.3\_70B        | Fine-tuned Llama model with enhanced reasoning capabilities.                           |
| Google\_Gemini\_2.5\_Pro                      | Advanced thinking model for complex problem solving.                                   |
| Google\_Gemini\_2.5\_Flash                    | Fast, well-rounded thinking model.                                                     |
| Google\_Gemini\_2.5\_Flash\_Lite              | Fast model optimized for large-scale text output.                                      |
| Google\_Gemini\_2.0\_Flash                    | Low-latency model optimized for agentic experiences.                                   |
| Groq\_Qwen3\_235B\_A22B\_Instruct\_2507\_tput | A varied model with enhanced reasoning.                                                |
| DeepSeek\_R1                                  | Open-source model matching OpenAI-o1 performance.                                      |
| DeepSeek\_V3                                  | Advanced Mixture-of-Experts model.                                                     |
| xAI\_Grok\_4                                  | Advanced language model with enhanced reasoning and tool capabilities.                 |
| xAI\_Grok\_3                                  | Enterprise-focused model for data, coding, and summarization tasks.                    |
| xAI\_Grok\_3\_Mini                            | Fast, lightweight model for logic-based tasks.                                         |
| xAI\_Grok\_2                                  | Advanced language model with strong reasoning capabilities.                            |

If a model isn't available to the user (or has been disabled by the user), Raycast will fallback to a similar one.

### AI.AskOptions

#### Properties

| Property   | Description                                                                                                                                                                                                                                                      | Type                                                                   |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| creativity | Concrete tasks, such as fixing grammar, require less creativity while open-ended questions, such as generating ideas, require more. If a number is passed, it needs to be in the range 0-2. For larger values, 2 will be used. For lower values, 0 will be used. | [`AI.Creativity`](#ai.creativity)                                      |
| model      | The AI model to use to answer to the prompt.                                                                                                                                                                                                                     | [`AI.Model`](#ai.model)                                                |
| signal     | Abort signal to cancel the request.                                                                                                                                                                                                                              | [`Date`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) |
