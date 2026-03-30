# Source: https://docs.together.ai/docs/glm-5-quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GLM-5 Quickstart

> How to get the most out of GLM-5 for reasoning and agentic tasks.

GLM-5 is a state-of-the-art mixture-of-experts (MoE) language model from Zhipu AI, purpose-built for complex systems engineering and long-horizon agentic tasks. It's a 744B total parameter model (40B activated), pre-trained on 28.5T tokens, with a 200K context window and up to 128K output tokens. It achieves best-in-class performance among open-source models on reasoning, coding, and agentic benchmarks.

What makes GLM-5 special is the combination of scale and efficiency: it integrates DeepSeek Sparse Attention (DSA), significantly reducing deployment cost while preserving long-context capacity. Paired with a novel asynchronous RL infrastructure called *slime*, GLM-5 closes the gap with frontier models across a wide range of tasks.

## How to use GLM-5

Get started with this model in just a few lines of code. The model ID is `zai-org/GLM-5` and it supports a 200K context window with up to 128K output tokens. Thinking is enabled by default, so you'll receive both reasoning tokens and content tokens.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  stream = client.chat.completions.create(
      model="zai-org/GLM-5",
      messages=[
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          }
      ],
      temperature=1.0,
      top_p=0.95,
      stream=True,
  )

  for chunk in stream:
      if chunk.choices:
          delta = chunk.choices[0].delta

          # Show reasoning tokens if present
          if hasattr(delta, "reasoning") and delta.reasoning:
              print(delta.reasoning, end="", flush=True)

          # Show content tokens if present
          if hasattr(delta, "content") and delta.content:
              print(delta.content, end="", flush=True)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const stream = await together.chat.completions.create({
    model: "zai-org/GLM-5",
    messages: [
      {
        role: "user",
        content: "What are some fun things to do in New York?",
      },
    ],
    temperature: 1.0,
    top_p: 0.95,
    stream: true,
  });

  for await (const chunk of stream) {
    const delta = chunk.choices[0]?.delta;

    // Show reasoning tokens if present
    if (delta?.reasoning) process.stdout.write(delta.reasoning);

    // Show content tokens if present
    if (delta?.content) process.stdout.write(delta.content);
  }
  ```
</CodeGroup>

## Thinking Modes

GLM-5 has thinking enabled by default and supports multiple thinking modes for different scenarios:

* **Interleaved Thinking** (default): The model thinks between tool calls and after receiving tool results, enabling complex step-by-step reasoning — interpreting each tool output before deciding what to do next.
* **Preserved Thinking**: The model retains reasoning content from previous assistant turns in the context, improving reasoning continuity and cache hit rates. Ideal for coding agents and agentic workflows.
* **Turn-level Thinking**: Control reasoning on a per-turn basis within the same session — enable thinking for hard turns, disable it for simple ones.

<Warning>
  **Thinking is on by default.** To disable thinking for simple tasks where reasoning overhead isn't needed, pass `reasoning={"enabled": False}` in the request.
</Warning>

### Recommended Thinking Mode by Use Case

| Scenario                                    | Mode                             | Rationale                                     |
| ------------------------------------------- | -------------------------------- | --------------------------------------------- |
| General chat                                | Interleaved Thinking (default)   | Step-by-step reasoning between tool calls     |
| Coding agents (e.g., Claude Code, Roo Code) | Interleaved + Preserved Thinking | Retains reasoning across turns for continuity |
| Simple factual queries                      | Thinking disabled                | Faster responses, lower cost                  |

### Disabling Thinking

For lightweight tasks where you don't need the model to reason:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="zai-org/GLM-5",
      messages=[
          {
              "role": "user",
              "content": "What is the capital of France?",
          }
      ],
      reasoning={"enabled": False},
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "zai-org/GLM-5",
    messages: [
      {
        role: "user",
        content: "What is the capital of France?",
      },
    ],
    reasoning: { enabled: false }
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

## Tool Calling with Interleaved and Preserved Thinking

GLM-5 excels at multi-turn tool calling with reasoning interleaved between each step. The model thinks about each tool result before deciding what to do next, enabling sophisticated agentic workflows.

GLM-5 also supports **streaming tool calls** — set `stream=True` to receive tool call parameters in real-time as they're generated, rather than waiting for the complete function call.

For agentic workflows, we recommend enabling **Preserved Thinking** so the model retains reasoning from previous turns. Set `"clear_thinking": false` in `chat_template_kwargs` to keep reasoning content in context.

The example below demonstrates a multi-turn conversation where the model:

1. Reasons about the user's request and calls a weather tool
2. Receives the tool result, reasons about it, and responds naturally

```python Python theme={null}
import json
from together import Together

client = Together()

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather information for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city name, e.g. SF",
                    }
                },
                "required": ["city"],
            },
        },
    }
]

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What's the weather like in San Francisco?"},
]

# Round 1: Model reasons and calls the tool
response = client.chat.completions.create(
    model="zai-org/GLM-5",
    messages=messages,
    tools=tools,
    stream=True,
    chat_template_kwargs={
        "clear_thinking": False,  # Preserved Thinking
    },
)

reasoning, content, tool_calls = "", "", []
for chunk in response:
    if not getattr(chunk, "choices", None) or len(chunk.choices) == 0:
        continue

    delta = chunk.choices[0].delta
    if hasattr(delta, "reasoning") and delta.reasoning:
        reasoning += delta.reasoning
    if hasattr(delta, "content") and delta.content:
        content += delta.content
    if hasattr(delta, "tool_calls") and delta.tool_calls:
        for tc in delta.tool_calls:
            idx = int(tc.index)
            if idx >= len(tool_calls):
                tool_calls.append(
                    {
                        "id": tc.id,
                        "function": {"name": "", "arguments": ""},
                    }
                )
            if tc.function.name:
                tool_calls[idx]["function"]["name"] = tc.function.name
            if tc.function.arguments:
                tool_calls[idx]["function"][
                    "arguments"
                ] += tc.function.arguments

print(f"Reasoning: {reasoning}")
print(f"Tool calls: {tool_calls}")

# Key: return reasoning content to keep the reasoning coherent
messages.append(
    {
        "role": "assistant",
        "content": content,
        "reasoning": reasoning,
        "tool_calls": [
            {
                "id": tc["id"],
                "type": "function",
                "function": tc["function"],
            }
            for tc in tool_calls
        ],
    }
)

# Simulate tool response
messages.append(
    {
        "role": "tool",
        "tool_call_id": tool_calls[0]["id"],
        "content": json.dumps({"weather": "Sunny", "temp": "70°F"}),
    }
)

# Round 2: Model reasons about the tool result and responds
response = client.chat.completions.create(
    model="zai-org/GLM-5",
    messages=messages,
    tools=tools,
    stream=True,
    chat_template_kwargs={
        "clear_thinking": False,  # Preserved Thinking
    },
)

reasoning, content = "", ""
for chunk in response:
    if not getattr(chunk, "choices", None) or len(chunk.choices) == 0:
        continue
    delta = chunk.choices[0].delta
    if hasattr(delta, "reasoning") and delta.reasoning:
        reasoning += delta.reasoning
    if hasattr(delta, "content") and delta.content:
        content += delta.content

print(f"Reasoning: {reasoning}")
print(f"Reply: {content}")
```

This outputs:

```text Output theme={null}
Reasoning: The user is asking about the weather in San Francisco. I have access to a get_weather function that takes a city parameter. The user mentioned "San Francisco" which I should use as the city name. I should call the get_weather function with "San Francisco" as the city parameter.
Tool calls: [{'id': 'call_ea4154ccc2f14874ad2c9d92', 'function': {'name': 'get_weather', 'arguments': '{"city": "San Francisco"}'}}]
Reasoning: The function returned weather information for San Francisco. The weather is sunny with a temperature of 70°F. This is straightforward information to share with the user.
Reply: The weather in San Francisco is sunny with a temperature of 70°F. It's looking like a beautiful day there!
```

<Info>
  When using Preserved Thinking, all consecutive `reasoning` blocks must **exactly match the original sequence** generated by the model. Do not reorder or edit these blocks — otherwise, performance may degrade and cache hit rates will be affected.
</Info>

## Use Cases

GLM-5 excels in scenarios requiring deep reasoning and autonomous, multi-step execution:

* **Complex Systems Engineering**: Tackle multi-component system design, architecture decisions, and integration challenges that require reasoning through dependencies and trade-offs
* **Long-Horizon Agentic Workflows**: Build autonomous agents that maintain coherent goal-directed behavior across extended sequences of tool calls — stable across 200+ sequential invocations
* **Coding & Debugging**: Solve complex software engineering tasks (SWE-bench, Terminal Bench), generate patches, debug intricate issues, and reason through large codebases
* **Multi-Step Research & Analysis**: Automate research workflows using tools and APIs with interleaved reasoning between each step
* **STEM Problem-Solving**: Advanced math, logic puzzles, and scientific reasoning with transparent chain-of-thought processing
* **Tool Orchestration**: Build agents that chain multiple tool calls with reasoning steps, making finer-grained decisions based on intermediate results

## Prompting Tips

| Tip                                      | Rationale                                                                                                                                                      |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Temperature = 1.0, top\_p = 0.95**     | Recommended defaults for most tasks. Avoid tuning both simultaneously — pick one to adjust.                                                                    |
| **Temperature = 0.7 for SWE tasks**      | Use lower temperature with `top_p=1.0` for SWE-bench and Terminal Bench tasks.                                                                                 |
| **Temperature = 0 for Tau2-Bench**       | Use `temperature=0` with `max_tokens=16384` for multi-turn agentic benchmarks.                                                                                 |
| **Think in goals, not steps**            | GLM-5 is agentic — give high-level objectives and let it orchestrate sub-tasks and tool calls.                                                                 |
| **Use Preserved Thinking for agents**    | Set `"clear_thinking": false` in `chat_template_kwargs` for coding agents and multi-turn agentic workflows to maintain reasoning continuity.                   |
| **Return reasoning content faithfully**  | When using Preserved Thinking, always return the unmodified `reasoning` from previous turns back to the API.                                                   |
| **Use Turn-level Thinking to save cost** | Disable thinking on simple turns (facts, rewording) and enable it on complex turns (planning, debugging) within the same session.                              |
| **Set generous max tokens**              | GLM-5 supports up to 128K output tokens. Default `max_tokens` of 131072 accommodates deep reasoning. For SWE and agentic benchmark tasks, 16384 is sufficient. |

## General Limitations

GLM-5 is optimized for deep reasoning and agentic tasks, but there are scenarios where other models may be a better fit:

* **Latency-sensitive applications**: The reasoning process generates additional tokens, making GLM-5 slower than non-reasoning models. For real-time voice agents or instant-response scenarios, consider a non-reasoning model.
* **Simple, direct tasks**: For straightforward classification, basic text generation, or quick factual lookups, the reasoning overhead adds unnecessary cost and latency — disable thinking or use a faster model.
* **Cost-sensitive high-volume pipelines**: Reasoning tokens increase output volume. If you're processing many simple queries at scale, consider using Turn-level Thinking to selectively enable reasoning only where it adds value.


Built with [Mintlify](https://mintlify.com).