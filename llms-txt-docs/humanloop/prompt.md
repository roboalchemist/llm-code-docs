# Source: https://humanloop.com/docs/sdk/decorators/prompt.md

# Prompt Decorator

> Technical reference for the Prompt decorator in the Humanloop SDK


## Overview

The Prompt decorator automatically instruments LLM provider calls and creates Prompt Logs on Humanloop. When applied to a function, it:
- Creates a new Log for each LLM provider call made within the decorated function.
- Versions the Prompt using hyperparameters of the provider call.

### Decorator Definition

<Tabs>
<Tab title="Python" language="python">
```python
@hl_client.prompt(
    # Required: path on Humanloop workspace for the Prompt
    path: str
)
def function(*args, **kwargs): ...
```

The decorated function will have the same signature as the original function.
</Tab>

<Tab title="TypeScript" language="typescript">
```typescript
hlClient.prompt<I, O>({
    // Required: path on Humanloop workspace for the Prompt
    path: string,
    // Required: decorated function
    callable: I extends Record<string, unknown> & 
        { messages?: ChatMessage[] } ?
        (args: I) => O :
        () => O;
}) => Promise<O | undefined>
```

The decorated function is always async and has the same signature as the `callable` argument.

Callable's `args` must extend `Record<string, unknown>`. If a `messages` field is present in the `args`, it must have type `ChatMessage[]`.

The decorated function will not wrap the return value in a second Promise if the `callable` is also asynchronous.

<Warning>
You must pass the providers you want to auto-instrument to the HumanloopClient constructor. Otherwise, the decorated function will work, but no Logs will be created.

```typescript {6-7}
import { HumanloopClient } from "humanloop";
import { OpenAI } from "openai";

const hlClient = new HumanloopClient({
    apiKey: process.env.HL_API_KEY,
    // Pass the provider module here
    instrumentProviders: { OpenAI }
})

// You can now use the prompt decorator
```
</Warning>
</Tab>
</Tabs>

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `path` | string | Yes | Path on Humanloop workspace for the Prompt |

### Usage

<CodeBlock>
```python
@hl_client.prompt(path="MyFeature/Process")
def process_input(text: str) -> str:
    return openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text}]
    ).choices[0].message.content
```

```typescript
const processInput = hlClient.prompt({
    path: "MyFeature/Process",
    callable: async (text: string): Promise<string> => {
        return openai.chat.completions.create({
            model: "gpt-4o-mini",
            messages: [{ role: "user", content: text }]
        }).choices[0].message.content;
    }
});
```
</CodeBlock>

## Behavior 

### Versioning

The hyperparameters of the LLM provider call are used to version the Prompt.

If the configuration changes, new Logs will be created under the new version of the the same Prompt.

The following parameters are considered for versioning the Prompt:

| Parameter | Description |
|-----------|-------------|
| `model` | The LLM model identifier |
| `endpoint` | The API endpoint type |
| `provider` | The LLM provider (e.g., "openai", "anthropic") |
| `max_tokens` | Maximum tokens in completion |
| `temperature` | Sampling temperature |
| `top_p` | Nucleus sampling parameter |
| `presence_penalty` | Presence penalty for token selection |
| `frequency_penalty` | Frequency penalty for token selection |

### Log Creation

Each LLM provider call within the decorated function creates a Log with the following fields set:

<Tabs>
<Tab title="Python" language="python">

| Field | Type | Description |
|-------|------|-------------|
| `inputs` | dict[str, Any] | Function arguments that aren't ChatMessage arrays |
| `messages` | ChatMessage[] | ChatMessage arrays passed to the LLM |
| `output_message` | ChatMessage | LLM response with role and content |
| `error` | string | Error message if the LLM call fails |
| `prompt_tokens` | int | Number of tokens in the prompt |
| `reasoning_tokens` | int | Number of tokens used in reasoning |
| `output_tokens` | int | Number of tokens in the completion |
| `finish_reason` | string | Reason the LLM stopped generating |
| `start_time` | datetime | When the LLM call started |
| `end_time` | datetime | When the LLM call completed |

</Tab>

<Tab title="TypeScript" language="typescript">

| Field | Type | Description |
|-------|------|-------------|
| `inputs` | object | Function arguments that aren't ChatMessage arrays |
| `messages` | ChatMessage[] | ChatMessage arrays passed to the LLM |
| `output_message` | ChatMessage | LLM response with role and content |
| `error` | string | Error message if the LLM call fails |
| `prompt_tokens` | number | Number of tokens in the prompt |
| `reasoning_tokens` | number | Number of tokens used in reasoning |
| `output_tokens` | number | Number of tokens in the completion |
| `finish_reason` | string | Reason the LLM stopped generating |
| `start_time` | Date | When the LLM call started |
| `end_time` | Date | When the LLM call completed |

</Tab>

</Tabs>

## Error Handling

<Tabs>
<Tab title="Python" language="python">
- LLM provider errors are caught and logged in the Log's `error` field. However, `HumanloopRuntimeError` is not caught and will be re-raised: they indicate wrong SDK or decorator usage.
- The decorated function propagates exceptions from the LLM provider.
</Tab>

<Tab title="TypeScript" language="typescript">
- LLM provider errors are caught and logged in the Log's `error` field. However, `HumanloopRuntimeError` is not caught and will be re-thrown: they indicate wrong SDK or decorator usage.
- The decorated function propagates exceptions from the LLM provider.
</Tab>
</Tabs>

## Best Practices

1. Multiple Logs will be created if you make multiple calls inside the decorated function. To avoid confusion, avoid calls with different providers or hyperparameters, as this will create multiple versions of the Prompt.
2. Calling `prompts.log()` or `prompts.call()` inside the decorated function works normally, with no interaction with the decorator. However, it indicates a misuse of the decorator, as they are alternatives for achieving the same result.
3. If you want to switch between providers with ease, use [`prompts.call()`](/docs/v5/api/prompts/call) with a `provider` parameter instead of the decorator.

## Related Documentation

Humanloop Prompts are more than the string passed to the LLM provider. They encapsulate LLM hyperparameters, associations to available tools, and can be templated. For more details, refer to our [Prompts explanation](/docs/v5/explanation/prompts).

