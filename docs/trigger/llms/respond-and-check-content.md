# Source: https://trigger.dev/docs/guides/ai-agents/respond-and-check-content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Respond to customer inquiry and check for inappropriate content

> Create an AI agent workflow that responds to customer inquiries while checking if their text is inappropriate

## Overview

**Parallelization** is a workflow pattern where multiple tasks or processes run simultaneously instead of sequentially, allowing for more efficient use of resources and faster overall execution. It's particularly valuable when different parts of a task can be handled independently, such as running content analysis and response generation at the same time.
<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/parallelization.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=385b3c71db00c3995cb3de787ef462b4" alt="Parallelization" data-og-width="1293" width="1293" data-og-height="428" height="428" data-path="guides/ai-agents/parallelization.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/parallelization.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=560093586ba22fa29ef9b31f99e9b773 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/parallelization.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=2fe3d6a2b9d9dc31804cf5ba89910849 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/parallelization.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=84ccb0dd6586fdd84ffbed4705f8e05a 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/parallelization.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=8c036426d21172e60147fa5cb5907f6d 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/parallelization.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=03cf5a5f250bac272f7a068e7283abc4 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/parallelization.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=7d50bd85587ffbe8a020ad63b797e414 2500w" />

## Example task

In this example, we'll create a workflow that simultaneously checks content for issues while responding to customer inquiries. This approach is particularly effective when tasks require multiple perspectives or parallel processing streams, with the orchestrator synthesizing the results into a cohesive output.

**This task:**

* Uses `generateText` from [Vercel's AI SDK](https://sdk.vercel.ai/docs/introduction) to interact with OpenAI models
* Uses `experimental_telemetry` to provide LLM logs
* Uses [`batch.triggerByTaskAndWait`](/triggering#batch-triggerbytaskandwait) to run customer response and content moderation tasks in parallel
* Generates customer service responses using an AI model
* Simultaneously checks for inappropriate content while generating responses

```typescript  theme={"theme":"css-variables"}
import { openai } from "@ai-sdk/openai";
import { batch, task } from "@trigger.dev/sdk";
import { generateText } from "ai";

// Task to generate customer response
export const generateCustomerResponse = task({
  id: "generate-customer-response",
  run: async (payload: { question: string }) => {
    const response = await generateText({
      model: openai("o1-mini"),
      messages: [
        {
          role: "system",
          content: "You are a helpful customer service representative.",
        },
        { role: "user", content: payload.question },
      ],
      experimental_telemetry: {
        isEnabled: true,
        functionId: "generate-customer-response",
      },
    });

    return response.text;
  },
});

// Task to check for inappropriate content
export const checkInappropriateContent = task({
  id: "check-inappropriate-content",
  run: async (payload: { text: string }) => {
    const response = await generateText({
      model: openai("o1-mini"),
      messages: [
        {
          role: "system",
          content:
            "You are a content moderator. Respond with 'true' if the content is inappropriate or contains harmful, threatening, offensive, or explicit content, 'false' otherwise.",
        },
        { role: "user", content: payload.text },
      ],
      experimental_telemetry: {
        isEnabled: true,
        functionId: "check-inappropriate-content",
      },
    });

    return response.text.toLowerCase().includes("true");
  },
});

// Main task that coordinates the parallel execution
export const handleCustomerQuestion = task({
  id: "handle-customer-question",
  run: async (payload: { question: string }) => {
    const {
      runs: [responseRun, moderationRun],
    } = await batch.triggerByTaskAndWait([
      {
        task: generateCustomerResponse,
        payload: { question: payload.question },
      },
      {
        task: checkInappropriateContent,
        payload: { text: payload.question },
      },
    ]);

    // Check moderation result first
    if (moderationRun.ok && moderationRun.output === true) {
      return {
        response:
          "I apologize, but I cannot process this request as it contains inappropriate content.",
        wasInappropriate: true,
      };
    }

    // Return the generated response if everything is ok
    if (responseRun.ok) {
      return {
        response: responseRun.output,
        wasInappropriate: false,
      };
    }

    // Handle any errors
    throw new Error("Failed to process customer question");
  },
});
```

## Run a test

On the Test page in the dashboard, select the `handle-customer-question` task and include a payload like the following:

```json  theme={"theme":"css-variables"}
{
  "question": "Can you explain 2FA?"
}
```

When triggered with a question, the task simultaneously generates a response while checking for inappropriate content using two parallel LLM calls. The main task waits for both operations to complete before delivering the final response.

<video src="https://content.trigger.dev/agent-parallelization.mp4" controls muted autoPlay loop />
