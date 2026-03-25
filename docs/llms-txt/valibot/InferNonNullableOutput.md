# Source: https://valibot.dev/api/InferNonNullableOutput.md

# InferNonNullableOutput

Infer non nullable output type.

```ts
// Create nullable string schema
const NullableStringSchema = v.nullable(
  v.pipe(
    v.string(),
    v.transform((input) => input.length)
  )
);

// Infer non nullable string output type
type NonNullableStringOutput = v.InferNonNullableOutput<
  typeof NullableStringSchema
>; // number
```
