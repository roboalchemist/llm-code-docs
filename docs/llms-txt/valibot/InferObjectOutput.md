# Source: https://valibot.dev/api/InferObjectOutput.md

# InferObjectOutput

Infer object output type.

```ts
// Create object entries
const entries = {
  key: v.pipe(
    v.string(),
    v.transform((input) => input.length)
  ),
};

// Infer entries output type
type EntriesOutput = v.InferObjectOutput<typeof entries>; // { key: number }
```
