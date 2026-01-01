# Source: https://docs.together.ai/docs/deepseek-3-1-quickstart.md

> How to get started with DeepSeek V3.1

# DeepSeek V3.1 QuickStart

DeepSeek V3.1 is the latest, state-of-the-art hybrid-inference AI model from DeepSeek, blending "Think" and "Non-Think" modes within a single architecture. It's the newer version of the DeepSeek V3 model with efficient hybrid reasoning.

## How to use DeepSeek V3.1

Get started with this model in 10 lines of code! The model ID is `deepseek-ai/DeepSeek-V3.1` and the pricing is \$0.60 for input tokens and \$1.70 for output tokens.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()
  resp = client.chat.completions.create(
  model="deepseek-ai/DeepSeek-V3.1",
  messages=[{"role":"user","content":"What are some fun things to do in New York?"}],
  stream=True,
  )
  for tok in resp:
  print(tok.choices[0].delta.content, end="", flush=True)

  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: 'deepseek-ai/DeepSeek-V3.1',
    messages: [{ role: 'user', content: 'What are some fun things to do in New York?' }],
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
  ```
</CodeGroup>

<Warning>
  **Current Limitations**. The following features are not yet supported, but
  will be added soon: Function calling and JSON mode.
</Warning>

## Hybrid Thinking

Here's how to enable thinking in DeepSeek V3.1.

<CodeGroup>
  ```python Python theme={null}
  from together import Together
  client = Together()

  stream = client.chat.completions.create(
  model="deepseek-ai/DeepSeek-V3.1",
  messages=[
  {"role": "user", "content": "What are some fun things to do in New York?"}
  ],
  reasoning={"enabled": True},
  stream=True,
  )

  for chunk in stream:
  delta = chunk.choices[0].delta

    # Show reasoning tokens if present
    if hasattr(delta, "reasoning") and delta.reasoning:
        print(delta.reasoning, end="", flush=True)

    # Show content tokens if present
    if hasattr(delta, "content") and delta.content:
        print(delta.content, end="", flush=True)

  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  import type { ChatCompletionChunk } from "together-ai/resources/chat/completions";

  const together = new Together();

  async function main() {
    const stream = await together.chat.completions.stream({
      model: "deepseek-ai/DeepSeek-V3.1",
      messages: [
        { role: "user", content: "What are some fun things to do in New York?" },
      ],
      reasoning: {
        enabled: true,
      },
    } as any);

    for await (const chunk of stream) {
      const delta = chunk.choices[0]
            ?.delta as ChatCompletionChunk.Choice.Delta & { reasoning?: string };

      // Show reasoning tokens if present
      if (delta?.reasoning) process.stdout.write(delta.reasoning);

      // Show content tokens if present
      if (delta?.content) process.stdout.write(delta.content);
    }
  }

  main();

  ```
</CodeGroup>

<Warning>
  For TypeScript users, you need to cast the parameters as `any` because `reasoning.enabled: true` is not yet recognized by the SDK. Additionally, the delta object requires a custom type to include the `reasoning` property.
</Warning>

## How is it different from DeepSeek V3?

DeepSeek V3.1 – the newer better version of DeepSeek V3 – has a few key differences:

* Hybrid model w/ two main modes: Non-thinking and Thinking mode
* Function calling only works in non-thinking mode
* Agent capabilities: Built-in support for code agents and search agents
* More efficient reasoning than DeepSeek-R1
* Continued long-context pre-training


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt