# Source: https://humanloop.com/docs/sdk/decorators/tool.md

# Tool Decorator

> Technical reference for the Tool decorator in the Humanloop SDK


## Overview

The Tool decorator helps you define [Tools](/docs/v5/explanation/tools) for use in function calling. It automatically instruments function calls and creates Tool Logs on Humanloop.

<Tabs>
<Tab title="Python" language="python">

Calling a decorated function will create a Tool Log with the following fields:

- `inputs`: The function arguments.
- `output`: The function return value.
- `error`: The error message if the function call fails.

</Tab>

<Tab title="TypeScript" language="typescript">

Calling a decorated function will create a Tool Log with the following fields:

- `inputs`: The function arguments.
- `output`: The function return value.
- `error`: The error message if the function call fails.    

</Tab>
</Tabs>

### Definition

<Tabs>
<Tab title="Python" language="python">
```python
@hl_client.tool(
    # Required: path on Humanloop workspace for the Tool
    path: str,
    # Optional: additional metadata for the Tool
    attributes: Optional[dict[str, Any]] = None,
    # Optional: values needed to setup the Tool
    setup_values: Optional[dict[str, Any]] = None
)
def function(*args, **kwargs): ...
```

The decorated function will have the same signature as the original function and will have a `json_schema` attribute containing the inferred JSON Schema.
</Tab>

<Tab title="TypeScript" language="typescript">
```typescript
hlClient.tool<I, O>({
    // Required: path on Humanloop workspace for the Tool
    path: string,
    // Required: decorated function
    callable: I extends Record<string, unknown> ?
        (args: I) => O :
        () => O,
    // Required: JSON Schema for the Tool
    version: ToolKernelRequest
}) => Promise<O | undefined>
```

The decorated function is always async and has the same signature as the `callable` argument. It will have a `jsonSchema` attribute containing the provided JSON Schema.

</Tab>
</Tabs>

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `path` | string | Yes | Path on Humanloop workspace for the Tool |
| `attributes` | object | No | Additional metadata for the Tool (Python only) |
| `setup_values` | object | No | Values needed to setup the Tool (Python only) |
| `version` | ToolKernelRequest | Yes | JSON Schema for the Tool (TypeScript only) |

### Usage

<Tabs>
    <Tab title="Python" language="python">
        ```python
        @hl_client.tool(path="MyFeature/Calculator")
        def calculator(a: int, b: Optional[int] = None) -> int:
            """Add two numbers together."""
            return a + (b or 0)
        ```

        Decorating a function will set a `json_schema` attribute that can be used for function calling.

        ```python {5, 12-14}
        # Use with prompts.call
        response = hl_client.prompts.call(
            path="MyFeature/Assistant",
            messages=[{"role": "user", "content": "What is 5 + 3?"}],
            tools=[calculator.json_schema]
        )

        # Or with OpenAI directly!
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "What is 5 + 3?"}],
            tools=[{
                "type": "function",
                "function": calculator.json_schema
            }]
        )
        ```
    </Tab>

    <Tab title="TypeScript" language="typescript">
        ```typescript maxLines=50
        const calculator = hlClient.tool({
            path: "MyFeature/Calculator",
            callable: (inputs: { a: number; b?: number }) => {
                return inputs.a + (inputs.b || 0);
            },
            version: {
                function: {
                    name: "calculator",
                    description: "Add two numbers together.",
                    parameters: {
                        type: "object",
                        properties: {
                            a: { type: "number" },
                            b: { type: "number" }
                        },
                        required: ["a"]
                    }
                }
            }
        });
        ```

        Decorating a function will set a `jsonSchema` attribute that can be used for function calling.

        ```typescript {5, 12-14}
        // Use with prompts.call
        const response = await hlClient.prompts.call({
            path: "MyFeature/Assistant",
            messages: [{ role: "user", content: "What is 5 + 3?" }],
            tools: [calculator.jsonSchema]
        });

        // Or with OpenAI directly!
        const response = await openai.chat.completions.create({
            model: "gpt-4o-mini",
            messages: [{ role: "user", content: "What is 5 + 3?" }],
            tools: [{
                type: "function",
                function: calculator.jsonSchema
            }]
        });
        ```
    </Tab>
</Tabs>

## Behavior 

### Schema Definition

<Tabs>
<Tab title="Python" language="python">

In Python, the decorator automatically infers a JSON Schema from the source code, argument signature, and docstrings:

- Function name becomes the tool name
- Function docstring becomes the tool description
- Parameter type hints are converted to JSON Schema types
- Optional parameters (using `Optional[T]` or `T | None`) are marked as not required
- Return type is not included in the schema

Supported type hints:

| Python Type | JSON Schema Type |
|-------------|------------------|
| `str` | `"string"` |
| `int` | `"integer"` |
| `float` | `"number"` |
| `bool` | `"boolean"` |
| `list[T]` | `"array"` with items of type T |
| `dict[K, V]` | `"object"` with properties of types K and V |
| `tuple[T1, T2, ...]` | `"array"` with items of specific types |
| `Optional[T]` or `T \| None` | Type T with `"null"` added |
| `Union[T1, T2, ...]` | `"anyOf"` with types T1, T2, etc. |
| No type hint | `any` |

</Tab>

<Tab title="TypeScript" language="typescript">

In TypeScript, you must provide a JSON Schema in the `version` parameter:

```typescript
version: {
    function: {
        name: string;
        description: string;
        parameters: {
            type: "object";
            properties: Record<string, any>;
            required?: string[];
        };
    };
    attributes?: Record<string, any>;
    setup_values?: Record<string, any>;
}
```

</Tab>
</Tabs>

### Log Creation

Each function call creates a Tool Log with the following fields:

<Tabs>
<Tab title="Python" language="python">

| Field | Type | Description |
|-------|------|-------------|
| `inputs` | dict[str, Any] | Function arguments |
| `output` | string | JSON-serialized return value |
| `error` | string | Error message if the function call fails |

</Tab>

<Tab title="TypeScript" language="typescript">

| Field | Type | Description |
|-------|------|-------------|
| `inputs` | object | Function arguments |
| `output` | string | JSON-serialized return value |
| `error`  | string | Error message if the function call fails |

</Tab>
</Tabs>

## Error Handling

<Tabs>
<Tab title="Python" language="python">
- Function errors are caught and logged in the Log's `error` field.
- The decorated function returns `None` when an error occurs.
- `HumanloopRuntimeError` is not caught and will be re-raised, as it indicates incorrect SDK or decorator usage.
</Tab>

<Tab title="TypeScript" language="typescript">
- Function errors are caught and logged in the Log's `error` field.
- The decorated function returns `undefined` when an error occurs.
- Schema validation errors are thrown if the inputs don't match the schema.
- `HumanloopRuntimeError` is not caught and will be re-thrown, as it indicates incorrect SDK or decorator usage.
</Tab>
</Tabs>

## Best Practices

<Tabs>
<Tab title="Python" language="python">

1. Use clear and descriptive docstrings in Python to provide good tool descriptions
2. Ensure all function parameters have appropriate type hints in Python
3. Make return values JSON-serializable
4. Use the `json_schema` attribute when passing the tool to `prompts.call()`

</Tab>

<Tab title="TypeScript" language="typescript">

1. Use clear and descriptive docstrings in TypeScript to provide good tool descriptions
2. Ensure all function parameters have appropriate type hints in TypeScript
3. Make return values JSON-serializable
4. Use the `jsonSchema` attribute when passing the tool to `prompts.call()`

</Tab>
</Tabs>

## Related Documentation

For a deeper understanding of Tools and their role in the Humanloop platform, refer to our [Tools](/docs/v5/explanation/tools) documentation.

For attaching a Tool to a Prompt, see [Tool calling in Editor](/docs/v5/guides/prompts/tool-calling-editor) and [linking a Tool to a Prompt](/docs/v5/guides/prompts/link-tool).

