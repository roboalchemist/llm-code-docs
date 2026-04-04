# Source: https://trigger.dev/docs/guides/examples/vercel-ai-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Vercel AI SDK

> This example demonstrates how to use the Vercel AI SDK with Trigger.dev.

## Overview

The [Vercel AI SDK](https://www.npmjs.com/package/ai) is a simple way to use AI models from many different providers, including OpenAI, Microsoft Azure, Google Generative AI, Anthropic, Amazon Bedrock, Groq, Perplexity and [more](https://sdk.vercel.ai/providers/ai-sdk-providers).

It provides a consistent interface to interact with the different AI models, so you can easily switch between them without needing to change your code.

## Generate text using OpenAI

This task shows how to use the Vercel AI SDK to generate text from a prompt with OpenAI.

### Task code

```ts trigger/vercel-ai-sdk-openai.ts theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";
import { generateText } from "ai";
// Install the package of the AI model you want to use, in this case OpenAI
import { openai } from "@ai-sdk/openai"; // Ensure OPENAI_API_KEY environment variable is set

export const openaiTask = task({
  id: "openai-text-generate",

  run: async (payload: { prompt: string }) => {
    const chatCompletion = await generateText({
      model: openai("gpt-4-turbo"),
      // Add a system message which will be included with the prompt
      system: "You are a friendly assistant!",
      // The prompt passed in from the payload
      prompt: payload.prompt,
    });

    // Log the generated text
    logger.log("chatCompletion text:" + chatCompletion.text);

    return chatCompletion;
  },
});
```

## Testing your task

To test this task in the dashboard, you can use the following payload:

```json  theme={"theme":"css-variables"}
{
  "prompt": "What is the meaning of life?"
}
```

## Learn more about Next.js and Trigger.dev

### Walk-through guides from development to deployment

<CardGroup cols={2}>
  <Card title="Next.js - setup guide" icon="N" href="/guides/frameworks/nextjs">
    Learn how to setup Trigger.dev with Next.js, using either the pages or app router.
  </Card>

  <Card title="Next.js - triggering tasks using webhooks" icon="N" href="/guides/frameworks/nextjs-webhooks">
    Learn how to create a webhook handler for incoming webhooks in a Next.js app, and trigger a task from it.
  </Card>
</CardGroup>

### Task examples

<CardGroup cols={2}>
  <Card title="Fal.ai with Realtime in Next.js" img="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-realtime-thumbnail.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=9ac31bb57678b222a82b04055184eea0" href="/guides/examples/fal-ai-realtime" data-og-width="1442" width="1442" data-og-height="812" height="812" data-path="images/fal-realtime-thumbnail.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-realtime-thumbnail.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=086231461af2b9520f9200889fc04724 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-realtime-thumbnail.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=c5ab58baba8000266aac79117dc8944d 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-realtime-thumbnail.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=988fe253a646e5af2188f81297d01897 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-realtime-thumbnail.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=db65bbdf0995fc1ac72bda2512c31800 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-realtime-thumbnail.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=6e7890d597065f8bc9edd0ac90257185 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-realtime-thumbnail.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=60bc05bc63c0c1d1ad59eaafb0808aa6 2500w">
    Generate an image from a prompt using Fal.ai and Trigger.dev Realtime.
  </Card>

  <Card title="Generate a cartoon using Fal.ai in Next.js" img="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-generate-cartoon-thumbnail.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=003d7870f36310d14ca9a71a952667d3" href="/guides/examples/fal-ai-image-to-cartoon" data-og-width="1442" width="1442" data-og-height="816" height="816" data-path="images/fal-generate-cartoon-thumbnail.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-generate-cartoon-thumbnail.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=ec0e05813f874082257e2d32bad407a8 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-generate-cartoon-thumbnail.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=f3f70889ad11953d44f72224712722aa 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-generate-cartoon-thumbnail.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=b8df38a222a7431d55a1af1af61dffd1 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-generate-cartoon-thumbnail.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=268ac6b0faf34bb46a8a8d676658b0b8 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-generate-cartoon-thumbnail.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=4be96f4df2d49b7a71d0e960df9cc93b 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/fal-generate-cartoon-thumbnail.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=bc15e1a3df4484cfdcd200d49fd1ac4b 2500w">
    Convert an image to a cartoon using Fal.ai.
  </Card>

  <Card title="Vercel sync environment variables" icon="code" href="/guides/examples/vercel-sync-env-vars">
    Learn how to automatically sync environment variables from your Vercel projects to Trigger.dev.
  </Card>

  <Card title="Vercel AI SDK" icon="code" href="/guides/examples/vercel-ai-sdk">
    Learn how to use the Vercel AI SDK, which is a simple way to use AI models from different
    providers, including OpenAI, Anthropic, Amazon Bedrock, Groq, Perplexity etc.
  </Card>
</CardGroup>
