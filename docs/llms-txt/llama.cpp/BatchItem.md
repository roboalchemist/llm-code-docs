# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/BatchItem.md

---
url: /api/type-aliases/BatchItem.md
---
# Type Alias: BatchItem

```ts
type BatchItem = {
  tokens: readonly Token[];
  logits: readonly (true | undefined)[];
  evaluationPriority: EvaluationPriority;
};
```

Defined in: [evaluator/LlamaContext/types.ts:630](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L630)

## Properties

### tokens

```ts
readonly tokens: readonly Token[];
```

Defined in: [evaluator/LlamaContext/types.ts:631](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L631)

***

### logits

```ts
readonly logits: readonly (true | undefined)[];
```

Defined in: [evaluator/LlamaContext/types.ts:632](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L632)

***

### evaluationPriority

```ts
readonly evaluationPriority: EvaluationPriority;
```

Defined in: [evaluator/LlamaContext/types.ts:633](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L633)
