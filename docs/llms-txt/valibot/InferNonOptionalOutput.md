# Source: https://valibot.dev/api/InferNonOptionalOutput.md

# InferNonOptionalOutput

Infer non optional output type.

```ts
// Create optional string schema
const OptionalStringSchema = v.optional(
  v.pipe(
    v.string(),
    v.transform((input) => input.length)
  )
);

// Infer non optional string output type
type NonOptionalStringOutput = v.InferNonOptionalOutput<
  typeof OptionalStringSchema
>; // number
```
