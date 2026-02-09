# Source: https://trigger.dev/docs/guides/ai-agents/route-question.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Route a question to a different AI model

> Create an AI agent workflow that routes a question to a different AI model depending on its complexity

## Overview

**Routing** is a workflow pattern that classifies an input and directs it to a specialized followup task. This pattern allows for separation of concerns and building more specialized prompts, which is particularly effective when there are distinct categories that are better handled separately. Without routing, optimizing for one kind of input can hurt performance on other inputs.

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/routing.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=2f586095b267c7d969afdc0a1e167071" alt="Routing" data-og-width="1293" width="1293" data-og-height="428" height="428" data-path="guides/ai-agents/routing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/routing.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=40f3589d2b62e618a7b1d792be296330 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/routing.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=d0cd9a0c53b7ee3fb0d7ef0e84e97936 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/routing.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=b0e6a9e0aef55f30078825981a3f5445 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/routing.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=97fc784cc9a90f4c542f7ce4423d4ea5 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/routing.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=2ccca06d7bf06a3fd3d07bde7fc982ef 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/guides/ai-agents/routing.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=371e95357260a464adb4fe5408fe6a30 2500w" />

## Example task

In this example, we'll create a workflow that routes a question to a different AI model depending on its complexity. This approach is particularly effective when tasks require different models or approaches for different inputs.

**This task:**

* Uses `generateText` from [Vercel's AI SDK](https://sdk.vercel.ai/docs/introduction) to interact with OpenAI models
* Uses `experimental_telemetry` in the source verification and historical analysis tasks to provide LLM logs
* Routes questions using a lightweight model (`o1-mini`) to classify complexity
* Directs simple questions to `gpt-4o` and complex ones to `gpt-o3-mini`
* Returns both the answer and metadata about the routing decision

````typescript  theme={"theme":"css-variables"}
import { openai } from "@ai-sdk/openai";
import { task } from "@trigger.dev/sdk";
import { generateText } from "ai";
import { z } from "zod";

// Schema for router response
const routingSchema = z.object({
  model: z.enum(["gpt-4o", "gpt-o3-mini"]),
  reason: z.string(),
});

// Router prompt template
const ROUTER_PROMPT = `You are a routing assistant that determines the complexity of questions.
Analyze the following question and route it to the appropriate model:

- Use "gpt-4o" for simple, common, or straightforward questions
- Use "gpt-o3-mini" for complex, unusual, or questions requiring deep reasoning

Respond with a JSON object in this exact format:
{"model": "gpt-4o" or "gpt-o3-mini", "reason": "your reasoning here"}

Question: `;

export const routeAndAnswerQuestion = task({
  id: "route-and-answer-question",
  run: async (payload: { question: string }) => {
    // Step 1: Route the question
    const routingResponse = await generateText({
      model: openai("o1-mini"),
      messages: [
        {
          role: "system",
          content:
            "You must respond with a valid JSON object containing only 'model' and 'reason' fields. No markdown, no backticks, no explanation.",
        },
        {
          role: "user",
          content: ROUTER_PROMPT + payload.question,
        },
      ],
      temperature: 0.1,
      experimental_telemetry: {
        isEnabled: true,
        functionId: "route-and-answer-question",
      },
    });

    // Add error handling and cleanup
    let jsonText = routingResponse.text.trim();
    if (jsonText.startsWith("```")) {
      jsonText = jsonText.replace(/```json\n|\n```/g, "");
    }

    const routingResult = routingSchema.parse(JSON.parse(jsonText));

    // Step 2: Get the answer using the selected model
    const answerResult = await generateText({
      model: openai(routingResult.model),
      messages: [{ role: "user", content: payload.question }],
    });

    return {
      answer: answerResult.text,
      selectedModel: routingResult.model,
      routingReason: routingResult.reason,
    };
  },
});
````

## Run a test

Triggering our task with a simple question shows it routing to the gpt-4o model and returning the answer with reasoning:

```json  theme={"theme":"css-variables"}
{
  "question": "How many planets are there in the solar system?"
}
```

<video src="https://content.trigger.dev/agent-routing.mp4" controls muted autoPlay loop />
