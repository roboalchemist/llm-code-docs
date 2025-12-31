# Source: https://humanloop.com/docs/sdk/decorators/flow.md

# Flow Decorator

> Technical reference for the Flow decorator in the Humanloop SDK


## Overview

The Flow decorator creates and manages traces for your AI feature. When applied to a function, it:

- Creates a new trace on function invocation.
- Adds all Humanloop logging calls made inside the function to the trace.
- Completes the trace when the function exits.

<Info>
On Humanloop, a trace is the collection of Logs associated with a Flow Log.
</Info>

## Usage

The `flow` decorator will trace all downstream Humanloop logs, whether they are created by other decorators or SDK calls.


### Tracing Decorators

<CodeBlocks>

```python maxLines=50 wrapLines title="Python"

@hl_client.prompt(path="MyFeature/Call LLM"):
def call_llm(messages: List[ChatMessage]):
    return openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    ).choices[0].message.content

@hl_client.flow(path="MyFeature/Process")
def process_input(inputs: list[str]) -> list[str]:
    # Logs created by the Prompt decorator are added to the trace
    return [
        call_llm([{"role": "user", "content": text}])
        for text in inputs
    ]
```

```typescript maxLines=50 wrapLines title="TypeScript"
const callLLM = hlClient.prompt({
    path: "MyFeature/Call LLM",
    callable: async (messages: ChatMessage[]): Promise<string> => {
        const response = await openai.chat.completions.create({
            model: "gpt-4o-mini",
            messages
        });
        return response.choices[0].message.content;
    }
});

const processInput = hlClient.flow({
    path: "MyFeature/Process",
    callable: async (inputs: string[]): Promise<string[]> => {
        // Logs created by the Prompt decorator are added to the trace
        return inputs.map(async (text) => await callLLM([
            {"role": "user", "content": text}
        ]));
});
```

</CodeBlocks>

### Tracing SDK Calls

Logs created through the Humanloop SDK are added to the trace.

<CodeBlocks>

```python maxLines=50 title="Python" wrapLines
@hl_client.flow(path="MyFeature/Process")
def process_input(text: str) -> str:
    # Created Log is added to the trace
    llm_output = hl_client.prompts.call(
        path="MyFeature/Transform",
        messages=[{"role": "user", "content": text}]
    ).logs[0].output_message.content

    transformed_output = transform(llm_output)
    # Created Log is added to the trace
    hl_client.tools.log(
        path="MyFeature/Transform",
        tool={function: TRANSFORM_JSON_SCHEMA},
        inputs={"text": text},
        output=transformed_output
    )

    return transformed_output
```

```typescript maxLines=50
const processInput = hlClient.flow({
  path: "MyFeature/Process",
  callable: async (text: string): Promise<string> => {
    // Created Log is added to the trace
    const llmOutput = (
      await hlClient.prompts.call({
        path: "MyFeature/Transform",
        messages: [{ role: "user", content: text }],
      })
    ).logs[0].outputMessage.content;

    const transformedOutput = transform(llmOutput);
    // Created Log is added to the trace
    await hlClient.tools.log({
      path: "MyFeature/Transform",
      tool: { function: TRANSFORM_JSON_SCHEMA },
      inputs: { text },
      output: transformedOutput,
    });

    return transformedOutput;
  },
});
```

</CodeBlocks>

## Behavior

<Tabs>
<Tab title="Python" language="python">

The decorated function creates a Flow Log when called. All Logs created inside the decorated function are added to its trace.

The Flow Log's fields are populated as follows:

| Field            | Type        | Description                                                          |
| ---------------- | ----------- | -------------------------------------------------------------------- |
| `inputs`         | object      | Function arguments that aren't ChatMessage arrays                    |
| `messages`       | array       | ChatMessage arrays passed as arguments                               |
| `output_message` | ChatMessage | Return value if it's a ChatMessage-like object                       |
| `output`         | string      | Stringified return value if not a ChatMessage-like object            |
| `error`          | string      | Error message if function throws or return value can't be serialized |

If the decorated function returns a ChatMessage object, the `output_message` field is populated. Otherwise, the `output` field is populated with the stringified return value.

</Tab>

<Tab title="TypeScript" language="typescript">

The decorated function creates a Flow Log when called. All Logs created inside the decorated function are added to its trace.

The Flow Log's fields are populated as follows:

| Field           | Type        | Description                                                          |
| --------------- | ----------- | -------------------------------------------------------------------- |
| `inputs`        | object      | Function arguments that aren't ChatMessage arrays                    |
| `messages`      | array       | ChatMessage arrays passed as arguments                               |
| `outputMessage` | ChatMessage | Return value if it's a ChatMessage-like object                       |
| `output`        | string      | Stringified return value if not a ChatMessage-like object            |
| `error`         | string      | Error message if function throws or return value can't be serialized |

If the decorated function returns a ChatMessage object, the `outputMessage` field is populated. Otherwise, the `output` field is populated with the stringified return value.

</Tab>
</Tabs>

## Definition

<Tabs>
<Tab title="Python" language="python">
```python
@hl_client.flow(
    # Required: path on Humanloop workspace for the Flow
    path: str,
    # Optional: metadata for versioning the Flow
    attributes: dict[str, Any] = None
)
def function(*args, **kwargs): ...
```

The decorator will preserve the function's signature.
</Tab>

<Tab title="TypeScript" language="typescript">
```typescript
hlClient.flow<I, O>({
    // Required: path on Humanloop workspace for the Flow
    path: string,
    // Required: decorated function
    callable: I extends Record<string, unknown> & 
        { messages: ChatMessage[] } ?
        (inputs: I) => O :
        () => O;
    // Optional: metadata for versioning the Flow
    attributes?: Record<string, any>;
}) => Promise<O | undefined>
```

The function returned by the decorator is async and preserves the signature of `callable`.

Callable's `inputs` must extend `Record<string, unknown>`. If a `messages` field is present in the `inputs`, it must have the `ChatMessage[]` type.

The decorated function will not wrap the return value in a second Promise if the `callable` is also asynchronous.
</Tab>
</Tabs>

The decorator accepts the following parameters:

| Parameter    | Type   | Required | Description                              |
| ------------ | ------ | -------- | ---------------------------------------- |
| `path`       | string | Yes      | Path on Humanloop workspace for the Flow |
| `attributes` | object | No       | Key-value object for versioning the Flow |

## SDK Interactions

<Tabs>
<Tab title="Python" language="python">
- It's not possible to call `flows.log()` inside a decorated function. This will raise a [`HumanloopRuntimeError`](#error-handling)
- To create nested traces, call another flow-decorated function.
- Passing `trace_parent_id` argument to an SDK logging call inside the decorated function is ignored and emits a warning; the Log is added to the trace of the decorated function.
</Tab>

<Tab title="TypeScript" language="typescript">
- It's not possible to call `flows.log()` inside a decorated function. This will raise a [`HumanloopRuntimeError`](#error-handling)
- To create nested traces, call another flow-decorated function.
- Passing `traceParentId` argument to an SDK logging call inside the decorated function is ignored and emits a warning; the Log is added to the trace of the decorated function.
</Tab>
</Tabs>

## Error Handling

<Tabs>
<Tab title="Python" language="python">
- If user-written code (e.g. in code Evaluators) raises an exception, the relevant Log's `error` field is populated with the exception message and the decorated function returns `None`.
- `HumanloopRuntimeError` exceptions indicate incorrect decorator or SDK usage and are re-raised instead of being logged under `error`.
</Tab>

<Tab title="TypeScript" language="typescript">
- If user-written code (e.g. in code Evaluators) throws an exception, the relevant Log's `error` field is populated with the exception message and the decorated function returns `undefined`.
- `HumanloopRuntimeError` exceptions indicate incorrect decorator or SDK usage and are re-thrown instead of being logged under `error`.
</Tab>
</Tabs>

## Related Documentation

A explanation of Flows and their role in the Humanloop platform is found in our [Flows](/docs/v5/explanation/flows) documentation.
