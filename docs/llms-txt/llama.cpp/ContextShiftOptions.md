# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ContextShiftOptions.md

---
url: /api/type-aliases/ContextShiftOptions.md
---
# Type Alias: ContextShiftOptions

```ts
type ContextShiftOptions = {
  size?:   | number
     | (sequence: LlamaContextSequence) => 
     | number
     | Promise<number>;
  strategy?:   | "eraseBeginning"
     | (options: {
     sequence: LlamaContextSequence;
     size: number;
   }) => 
     | ContextTokensDeleteRange[]
     | Promise<ContextTokensDeleteRange[]>;
};
```

Defined in: [evaluator/LlamaContext/types.ts:336](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L336)

## Properties

### size?

```ts
optional size: 
  | number
  | (sequence: LlamaContextSequence) => 
  | number
  | Promise<number>;
```

Defined in: [evaluator/LlamaContext/types.ts:337](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L337)

***

### strategy?

```ts
optional strategy: 
  | "eraseBeginning"
  | (options: {
  sequence: LlamaContextSequence;
  size: number;
}) => 
  | ContextTokensDeleteRange[]
  | Promise<ContextTokensDeleteRange[]>;
```

Defined in: [evaluator/LlamaContext/types.ts:338](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L338)
