# Source: https://trigger.dev/docs/guides/ai-agents/generate-translate-copy.md

# Generate and translate copy

> Create an AI agent workflow that generates and translates copy

## Overview

**Prompt chaining** is an AI workflow pattern that decomposes a complex task into a sequence of steps, where each LLM call processes the output of the previous one. This approach trades off latency for higher accuracy by making each LLM call an easier, more focused task, with the ability to add programmatic checks between steps to ensure the process remains on track.

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/prompt-chaining.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=8bc4a5c5ff644c6b7c675672d5cab313" alt="Generating and translating copy" data-og-width="1293" width="1293" data-og-height="428" height="428" data-path="guides/ai-agents/prompt-chaining.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/prompt-chaining.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=b3122be12a3e08d344331200b5beff33 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/prompt-chaining.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=b505be00532b2e8c583a7a83d7d1ad67 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/prompt-chaining.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=5e63269a727185873ea0d35392d8a568 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/prompt-chaining.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=16ad5688eac01d05220a8b20fc75af1a 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/prompt-chaining.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=40c58aedf4cccde7e3654e25aedc274a 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/prompt-chaining.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=fcf4372192360767b8e1de9a50ff6340 2500w" />

## Example task

In this example, we'll create a workflow that generates and translates copy. This approach is particularly effective when tasks require different models or approaches for different inputs.

**This task:**

* Uses `generateText` from [Vercel's AI SDK](https://sdk.vercel.ai/docs/introduction) to interact with OpenAI models
* Uses `experimental_telemetry` to provide LLM logs
* Generates marketing copy based on subject and target word count
* Validates the generated copy meets word count requirements (±10 words)
* Translates the validated copy to the target language while preserving tone

```typescript  theme={null}
import { openai } from "@ai-sdk/openai";
import { task } from "@trigger.dev/sdk";
import { generateText } from "ai";

export interface TranslatePayload {
  marketingSubject: string;
  targetLanguage: string;
  targetWordCount: number;
}

export const generateAndTranslateTask = task({
  id: "generate-and-translate-copy",
  maxDuration: 300, // Stop executing after 5 mins of compute
  run: async (payload: TranslatePayload) => {
    // Step 1: Generate marketing copy
    const generatedCopy = await generateText({
      model: openai("o1-mini"),
      messages: [
        {
          role: "system",
          content: "You are an expert copywriter.",
        },
        {
          role: "user",
          content: `Generate as close as possible to ${payload.targetWordCount} words of compelling marketing copy for ${payload.marketingSubject}`,
        },
      ],
      experimental_telemetry: {
        isEnabled: true,
        functionId: "generate-and-translate-copy",
      },
    });

    // Gate: Validate the generated copy meets the word count target
    const wordCount = generatedCopy.text.split(/\s+/).length;

    if (
      wordCount < payload.targetWordCount - 10 ||
      wordCount > payload.targetWordCount + 10
    ) {
      throw new Error(
        `Generated copy length (${wordCount} words) is outside acceptable range of ${
          payload.targetWordCount - 10
        }-${payload.targetWordCount + 10} words`
      );
    }

    // Step 2: Translate to target language
    const translatedCopy = await generateText({
      model: openai("o1-mini"),
      messages: [
        {
          role: "system",
          content: `You are an expert translator specializing in marketing content translation into ${payload.targetLanguage}.`,
        },
        {
          role: "user",
          content: `Translate the following marketing copy to ${payload.targetLanguage}, maintaining the same tone and marketing impact:\n\n${generatedCopy.text}`,
        },
      ],
      experimental_telemetry: {
        isEnabled: true,
        functionId: "generate-and-translate-copy",
      },
    });

    return {
      englishCopy: generatedCopy,
      translatedCopy,
    };
  },
});
```

## Run a test

On the Test page in the dashboard, select the `generate-and-translate-copy` task and include a payload like the following:

```json  theme={null}
{
  marketingSubject: "The controversial new Jaguar electric concept car",
  targetLanguage: "Spanish",
  targetWordCount: 100,
}
```

This example payload generates copy and then translates it using sequential LLM calls. The translation only begins after the generated copy has been validated against the word count requirements.

<video src="https://content.trigger.dev/agent-prompt-chaining-3.mp4" controls muted autoPlay loop />
