# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaCompletionOptions.md

---
url: /api/type-aliases/LlamaCompletionOptions.md
---
# Type Alias: LlamaCompletionOptions

```ts
type LlamaCompletionOptions = {
  contextSequence: LlamaContextSequence;
  autoDisposeSequence?: boolean;
};
```

Defined in: [evaluator/LlamaCompletion.ts:22](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L22)

## Properties

### contextSequence

```ts
contextSequence: LlamaContextSequence;
```

Defined in: [evaluator/LlamaCompletion.ts:23](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L23)

***

### autoDisposeSequence?

```ts
optional autoDisposeSequence: boolean;
```

Defined in: [evaluator/LlamaCompletion.ts:30](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L30)

Automatically dispose the sequence when the object is disposed.

Defaults to `false`.
