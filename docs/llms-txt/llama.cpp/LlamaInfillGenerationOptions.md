# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaInfillGenerationOptions.md

---
url: /api/type-aliases/LlamaInfillGenerationOptions.md
---
# Type Alias: LlamaInfillGenerationOptions

```ts
type LlamaInfillGenerationOptions = LlamaCompletionGenerationOptions & {
  minPrefixKeepTokens?:   | number
     | (sequence: LlamaContextSequence) => 
     | number
     | Promise<number>;
};
```

Defined in: [evaluator/LlamaCompletion.ts:204](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L204)

## Type Declaration

### minPrefixKeepTokens?

```ts
optional minPrefixKeepTokens: 
  | number
  | (sequence: LlamaContextSequence) => 
  | number
  | Promise<number>;
```

The minimum number of tokens to keep from the prefix input when making a context shift.
Defaults to 10% of the context size.
