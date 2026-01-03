# Source: https://braintrust.dev/docs/reference/reasoning.md

# Reasoning

<Note>
  If you are on a hybrid deployment, reasoning support is available starting with `v0.0.74`.
</Note>

Reasoning models like OpenAI’s o4, Anthropic’s Claude 3.5 Sonnet, and Google’s Gemini 2.5 Flash generate intermediate reasoning steps before producing a final response. Braintrust provides unified support for these models, so you can work with reasoning outputs no matter which provider you choose.

You can use reasoning models in both [playgrounds](/core/playground#reasoning) and [programmatically through the SDK](/guides/proxy#reasoning-models).

## Parameters

Three parameters control reasoning behavior:

* **`reasoning_effort`**: Controls the intensity of reasoning (compatible with OpenAI's parameter). The value can be set to **low**, **medium**, or **high**.
* **`reasoning_enabled`**: A boolean flag to explicitly enable or disable reasoning output. Note: This parameter has no effect when using OpenAI models, which default to "medium" reasoning effort unless specified by you.
* **`reasoning_budget`**: Specifies a token budget for the reasoning process. You must provide either `reasoning_effort` or `reasoning_budget`, not both.

To facilitate working with reasoning models in your codebase, Braintrust offers type augmentation packages for the OpenAI SDK:

* **`@braintrust/proxy/types`** (TypeScript/JavaScript): Extends OpenAI's TypeScript definitions to include Braintrust-specific reasoning parameters and response fields. ([npm](https://www.npmjs.com/package/@braintrust/proxy), [GitHub](https://github.com/braintrustdata/braintrust-proxy))
* **`braintrust-proxy`** (Python): Provides casting utilities and type-safe helpers for using reasoning parameters and accessing reasoning responses. ([PyPi](https://pypi.org/project/braintrust-proxy/), [GitHub](https://github.com/braintrustdata/braintrust-proxy))

Since reasoning features extend the standard OpenAI API interface, these packages are necessary. They ensure type safety and autocomplete support in your IDE for reasoning-specific parameters (like `reasoning_effort`) and response fields (`reasoning`), while maintaining compatibility with your existing OpenAI SDK integration.

You can add reasoning parameters to any chat completion request when using Braintrust's proxy with your OpenAI SDK:

<CodeGroup dropdown>
  ```ts  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";
  import "@braintrust/proxy/types"; // importing this module augments the OpenAI SDK's types with the new reasoning params and response

  const openai = new OpenAI({
    baseURL: `${process.env.BRAINTRUST_API_URL || "https://api.braintrust.dev"}/v1/proxy`,
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const main = async () => {
    const response = await openai.chat.completions.create({
      model: "claude-3-7-sonnet-latest",
      reasoning_effort: "medium",
      messages: [
        {
          role: "user",
          content: "What's 15% of 240?",
        },
      ],
    });

    // Access the final response
    console.log(response.choices[0].message.content);
    // Output: "15% of 240 is 36."

    // Access the reasoning steps
    console.log(response.choices[0].reasoning);
    // Output: Array of reasoning objects with step-by-step calculation

    // Example reasoning structure:
    // [
    //   {
    //     "id": "reasoning_step_1",
    //     "content": "I need to calculate 15% of 240. To find a percentage, I multiply the number by the percentage divided by 100.\n\n15% = 15/100 = 0.15\n\nSo I need to calculate: 240 × 0.15"
    //   },
    //   {
    //     "id": "reasoning_step_2",
    //     "content": "240 × 0.15 = 36\n\nTherefore, 15% of 240 is 36."
    //   }
    // ]
  };

  main().catch(console.error);
  ```

  ```py  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from openai import OpenAI

  client = OpenAI(
      base_url=f"{os.getenv('BRAINTRUST_API_URL') or 'https://api.braintrust.dev'}/v1/proxy",
      api_key=os.getenv("BRAINTRUST_API_KEY"),
  )

  response = client.chat.completions.create(
      model="claude-3-7-sonnet-latest",
      reasoning_effort="medium",
      messages=[{"role": "user", "content": "What's 15% of 240?"}],
  )

  # Access the final response
  print(response.choices[0].message.content)
  # Output: "15% of 240 is 36."

  # Access the reasoning steps
  print(getattr(response.choices[0], "reasoning", None))
  ```
</CodeGroup>

<Note>
  The `id` field contains a unique identifier for each reasoning step. For providers like Anthropic, these IDs are signatures that must be preserved when including reasoning in multi-turn conversations. Always use the exact ID returned by the provider. Learn more in the [multi-turn conversations](#multi-turn-conversations) section.
</Note>

## Streaming

For streaming responses, reasoning is delivered through `deltas` objects as a new `reasoning` property:

<CodeGroup dropdown>
  ```ts  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";
  import "@braintrust/proxy/types"; // importing this module augments the OpenAI SDK's types with the new reasoning params and response

  const openai = new OpenAI({
    baseURL: `${process.env.BRAINTRUST_API_URL || "https://api.braintrust.dev"}/v1/proxy`,
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const main = async () => {
    const stream = await openai.chat.completions.create({
      model: "claude-3-7-sonnet-latest",
      reasoning_effort: "high",
      stream: true,
      messages: [
        {
          role: "user",
          content: "Explain quantum entanglement in simple terms.",
        },
      ],
    });

    for await (const chunk of stream) {
      const delta = chunk.choices[0]?.delta;

      // Handle regular content
      if (delta?.content) {
        process.stdout.write(delta.content);
      }

      // Handle reasoning deltas
      if (delta?.reasoning) {
        console.log("\nReasoning step:", delta.reasoning);
      }
    }
  };

  main().catch(console.error);
  ```

  ```py  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  from braintrust_proxy import from_openai_chat_completion_choice_delta
  from openai import OpenAI

  client = OpenAI(
      base_url=f"{os.getenv('BRAINTRUST_API_URL') or 'https://api.braintrust.dev'}/v1/proxy",
      api_key=os.getenv("BRAINTRUST_API_KEY"),
  )

  stream = client.chat.completions.create(
      model="claude-3-7-sonnet-latest",
      reasoning_effort="high",
      stream=True,
      messages=[{"role": "user", "content": "Explain quantum entanglement in simple terms."}],
  )

  for chunk in stream:
      delta = from_openai_chat_completion_choice_delta(chunk.choices[0].delta)

      # Handle regular content
      if delta.content:
          print(delta.content, end="")

      # Handle reasoning deltas
      if delta.reasoning:
          print(f"\nReasoning step: {delta.reasoning.dict()}")
  ```
</CodeGroup>

## Multi-turn conversations

You can include reasoning from previous turns in multi-turn conversations, allowing the model to build upon its previous thinking:

<CodeGroup dropdown>
  ```ts  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { OpenAI } from "openai";
  import "@braintrust/proxy/types"; // importing this module augments the OpenAI SDK's types with the new reasoning params and response

  const openai = new OpenAI({
    baseURL: `${process.env.BRAINTRUST_API_URL || "https://api.braintrust.dev"}/v1/proxy`,
    apiKey: process.env.BRAINTRUST_API_KEY,
  });

  const main = async () => {
    const firstResponse = await openai.chat.completions.create({
      model: "claude-3-7-sonnet-latest",
      reasoning_effort: "medium",
      messages: [
        {
          role: "user",
          content: "What's the best approach to solve a complex math problem?",
        },
      ],
    });

    // Include the previous reasoning in the next turn
    const secondResponse = await openai.chat.completions.create({
      model: "claude-3-7-sonnet-latest",
      reasoning_effort: "medium",
      messages: [
        {
          role: "user",
          content: "What's the best approach to solve a complex math problem?",
        },
        {
          role: "assistant",
          content: firstResponse.choices[0].message.content,
          reasoning: firstResponse.choices[0].reasoning,
        },
        {
          role: "user",
          content: "Now apply that approach to solve: 2x² + 5x - 3 = 0",
        },
      ],
    });
  };

  main().catch(console.error);
  ```

  ```py  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import os

  # For proper type handling, use the braintrust-proxy utilities
  from braintrust_proxy import as_openai_chat_message_param
  from openai import OpenAI

  client = OpenAI(
      base_url=f"{os.getenv('BRAINTRUST_API_URL') or 'https://api.braintrust.dev'}/v1/proxy",
      api_key=os.getenv("BRAINTRUST_API_KEY"),
  )

  first_response = client.chat.completions.create(
      model="claude-3-7-sonnet-latest",
      reasoning_effort="medium",
      messages=[{"role": "user", "content": "What's the best approach to solve a complex math problem?"}],
  )

  # Include the previous reasoning in the next turn
  second_response = client.chat.completions.create(
      model="claude-3-7-sonnet-latest",
      reasoning_effort="medium",
      messages=[
          {"role": "user", "content": "What's the best approach to solve a complex math problem?"},
          as_openai_chat_message_param(
              {
                  "role": "assistant",
                  "content": first_response.choices[0].message.content,
                  "reasoning": getattr(first_response.choices[0].message, "reasoning", None),
              }
          ),
          {"role": "user", "content": "Now apply that approach to solve: 2x² + 5x - 3 = 0"},
      ],
  )
  ```
</CodeGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt