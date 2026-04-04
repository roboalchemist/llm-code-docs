# Source: https://valibot.dev/api/InferInput.md

# InferInput

Infer input type.

## Generics

- `TItem` <Property {...properties.TItem} />

## Definition

- `InferInput` <Property {...properties.InferInput} />

## Example

```ts
// Create object schema
const ObjectSchema = v.object({
  key: v.pipe(
    v.string(),
    v.transform((input) => input.length)
  ),
});

// Infer object input type
type ObjectInput = v.InferInput<typeof ObjectSchema>; // { key: string }
```
