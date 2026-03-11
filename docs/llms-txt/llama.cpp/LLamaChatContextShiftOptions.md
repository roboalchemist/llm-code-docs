# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LLamaChatContextShiftOptions.md

---
url: /api/type-aliases/LLamaChatContextShiftOptions.md
---
# Type Alias: LLamaChatContextShiftOptions

```ts
type LLamaChatContextShiftOptions = {
  size?:   | number
     | (sequence: LlamaContextSequence) => 
     | number
     | Promise<number>;
  strategy?:   | "eraseFirstResponseAndKeepFirstSystem"
     | (options: {
     chatHistory: readonly ChatHistoryItem[];
     maxTokensCount: number;
     tokenizer: Tokenizer;
     chatWrapper: ChatWrapper;
     lastShiftMetadata?: object | null;
   }) => 
     | {
     chatHistory: ChatHistoryItem[];
     metadata?: object | null;
   }
     | Promise<{
     chatHistory: ChatHistoryItem[];
     metadata?: object | null;
   }>;
  lastEvaluationMetadata?: object | null;
};
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:463](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L463)

## Properties

### size?

```ts
optional size: 
  | number
  | (sequence: LlamaContextSequence) => 
  | number
  | Promise<number>;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:468](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L468)

The number of tokens to delete from the context window to make space for new ones.
Defaults to 10% of the context size.

***

### strategy?

```ts
optional strategy: 
  | "eraseFirstResponseAndKeepFirstSystem"
  | (options: {
  chatHistory: readonly ChatHistoryItem[];
  maxTokensCount: number;
  tokenizer: Tokenizer;
  chatWrapper: ChatWrapper;
  lastShiftMetadata?: object | null;
}) => 
  | {
  chatHistory: ChatHistoryItem[];
  metadata?: object | null;
}
  | Promise<{
  chatHistory: ChatHistoryItem[];
  metadata?: object | null;
}>;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:475](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L475)

The strategy to use when deleting tokens from the context window.

Defaults to `"eraseFirstResponseAndKeepFirstSystem"`.

***

### lastEvaluationMetadata?

```ts
optional lastEvaluationMetadata: object | null;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:502](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L502)

The `contextShiftMetadata` returned from the last evaluation.
This is an optimization to utilize the existing context state better when possible.
