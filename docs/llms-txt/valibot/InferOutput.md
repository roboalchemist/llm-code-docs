# Source: https://valibot.dev/api/InferOutput.md

# InferOutput

Infer output type.

## Generics

- `TItem` <Property {...properties.TItem} />

## Definition

- `InferIssue` <Property {...properties.InferIssue} />

## Example

```ts
// Create object schema
const ObjectSchema = v.object({
  key: v.pipe(
    v.string(),
    v.transform((input) => input.length)
  ),
});

// Infer object output type
type ObjectOutput = v.InferOutput<typeof ObjectSchema>; // { key: number }
```
