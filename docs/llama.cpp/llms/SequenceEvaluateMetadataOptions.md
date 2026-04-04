# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/SequenceEvaluateMetadataOptions.md

---
url: /api/type-aliases/SequenceEvaluateMetadataOptions.md
---
# Type Alias: SequenceEvaluateMetadataOptions

```ts
type SequenceEvaluateMetadataOptions = {
  confidence?: boolean;
  probabilities?: boolean;
};
```

Defined in: [evaluator/LlamaContext/types.ts:438](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L438)

## Properties

### confidence?

```ts
readonly optional confidence: boolean;
```

Defined in: [evaluator/LlamaContext/types.ts:448](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L448)

Get the confidence (probability) of the selected token.

Same as `probabilities.get(token)` from the output.

If you need only this value, you can skip getting the full probabilities list to improve performance.

This value might be slightly different when evaluated on different GPUs and configurations.

***

### probabilities?

```ts
readonly optional probabilities: boolean;
```

Defined in: [evaluator/LlamaContext/types.ts:457](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L457)

Get the full probabilities list of tokens from the vocabulary to be the next token, after applying the given options.

Only enable when needed, as it impacts the performance.

Defaults to `false`.
