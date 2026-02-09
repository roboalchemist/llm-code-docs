# Source: https://docs.baseten.co/development/model-apis/reasoning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Reasoning

> Control extended thinking for reasoning-capable models

Some Model APIs support *extended thinking*, where the model reasons through a problem before producing a final answer. The reasoning process generates additional tokens that appear in a separate `reasoning_content` field, distinct from the final response.

## Supported models

| Model            | Slug                           | Reasoning          |
| ---------------- | ------------------------------ | ------------------ |
| DeepSeek V3.2    | `deepseek-ai/DeepSeek-V3.2`    | Enabled by default |
| DeepSeek V3.1    | `deepseek-ai/DeepSeek-V3.1`    | Enabled by default |
| DeepSeek V3 0324 | `deepseek-ai/DeepSeek-V3-0324` | Enabled by default |
| Kimi K2 Thinking | `moonshotai/Kimi-K2-Thinking`  | Always enabled     |
| GLM 4.7          | `zai-org/GLM-4.7`              | Enabled by default |
| GLM 4.6          | `zai-org/GLM-4.6`              | Enabled by default |

Models not listed here do not support reasoning.

## Control reasoning depth

The `reasoning_effort` parameter controls how thoroughly the model reasons through a problem.

| Value    | Behavior                                  |
| -------- | ----------------------------------------- |
| `low`    | Faster responses, less thorough reasoning |
| `medium` | Balanced (default)                        |
| `high`   | Slower responses, more thorough reasoning |

<Tabs>
  <Tab title="Python">
    Pass `reasoning_effort` through `extra_body` since it extends the standard OpenAI API:

    ```python  theme={"system"}
    from openai import OpenAI
    import os

    client = OpenAI(
        base_url="https://inference.baseten.co/v1",
        api_key=os.environ.get("BASETEN_API_KEY")
    )

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3.2",
        messages=[
            {"role": "user", "content": "What is the sum of the first 100 prime numbers?"}
        ],
        extra_body={"reasoning_effort": "high"}  # [!code ++]
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    Include `reasoning_effort` directly in the request options:

    ```jsx  theme={"system"}
    import OpenAI from "openai";

    const client = new OpenAI({
        baseURL: "https://inference.baseten.co/v1",
        apiKey: process.env.BASETEN_API_KEY,
    });

    const response = await client.chat.completions.create({
        model: "deepseek-ai/DeepSeek-V3.2",
        messages: [
            { role: "user", content: "What is the sum of the first 100 prime numbers?" }
        ],
        reasoning_effort: "high"  // [!code ++]
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="cURL">
    Include `reasoning_effort` in the JSON request body:

    ```bash  theme={"system"}
    curl https://inference.baseten.co/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Api-Key $BASETEN_API_KEY" \
      -d '{
        "model": "deepseek-ai/DeepSeek-V3.2",
        "messages": [{"role": "user", "content": "What is the sum of the first 100 prime numbers?"}],
        "reasoning_effort": "high"
      }'
    ```
  </Tab>
</Tabs>

## Parse the response

The model's thinking process appears in `reasoning_content`, separate from the final answer in `content`.

```json  theme={"system"}
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "The sum of the first 100 prime numbers is 24,133.",
        "reasoning_content": "Let me work through this step by step. The first prime number is 2..."
      }
    }
  ],
  "usage": {
    "prompt_tokens": 18,
    "completion_tokens": 245,
    "total_tokens": 263,
    "completion_tokens_details": {
      "reasoning_tokens": 198
    }
  }
}
```

The `reasoning_tokens` field in `completion_tokens_details` shows how many tokens the model used for reasoning. These tokens count toward your total usage and billing.

## Decide when to reason

Reasoning improves quality for tasks that benefit from step-by-step thinking: mathematical calculations, multi-step logic problems, code generation with complex requirements, and analysis requiring multiple considerations.

For straightforward tasks like simple Q\&A or text generation, reasoning adds latency and token cost without improving quality. In these cases, use a model without reasoning support or set `reasoning_effort` to `low`.
