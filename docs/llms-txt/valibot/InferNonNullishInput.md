# Source: https://valibot.dev/api/InferNonNullishInput.md

# InferNonNullishInput

Infer non nullable input type.

```ts
// Create nullish string schema
const NullishStringSchema = v.nullish(
  v.pipe(
    v.string(),
    v.transform((input) => input.length)
  )
);

// Infer non nullish string input type
type NonNullishStringInput = v.InferNonNullishInput<typeof NullishStringSchema>; // string
```
