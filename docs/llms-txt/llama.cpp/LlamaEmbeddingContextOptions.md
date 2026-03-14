# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaEmbeddingContextOptions.md

---
url: /api/type-aliases/LlamaEmbeddingContextOptions.md
---
# Type Alias: LlamaEmbeddingContextOptions

```ts
type LlamaEmbeddingContextOptions = {
  contextSize?:   | "auto"
     | number
     | {
     min?: number;
     max?: number;
   };
  batchSize?: number;
  threads?: number;
  createSignal?: AbortSignal;
  ignoreMemorySafetyChecks?: boolean;
};
```

Defined in: [evaluator/LlamaEmbeddingContext.ts:10](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbeddingContext.ts#L10)

## Properties

### contextSize?

```ts
optional contextSize: 
  | "auto"
  | number
  | {
  min?: number;
  max?: number;
};
```

Defined in: [evaluator/LlamaEmbeddingContext.ts:23](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbeddingContext.ts#L23)

The number of tokens the model can see at once.

* **`"auto"`** - adapt to the current VRAM state and attemp to set the context size as high as possible up to the size
  the model was trained on.
* **`number`** - set the context size to a specific number of tokens.
  If there's not enough VRAM, an error will be thrown.
  Use with caution.
* **`{min?: number, max?: number}`** - adapt to the current VRAM state and attemp to set the context size as high as possible
  up to the size the model was trained on, but at least `min` and at most `max`.

Defaults to `"auto"`.

***

### batchSize?

```ts
optional batchSize: number;
```

Defined in: [evaluator/LlamaEmbeddingContext.ts:29](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbeddingContext.ts#L29)

prompt processing batch size

***

### threads?

```ts
optional threads: number;
```

Defined in: [evaluator/LlamaEmbeddingContext.ts:35](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbeddingContext.ts#L35)

number of threads to use to evaluate tokens.
set to 0 to use the maximum threads supported by the current machine hardware

***

### createSignal?

```ts
optional createSignal: AbortSignal;
```

Defined in: [evaluator/LlamaEmbeddingContext.ts:38](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbeddingContext.ts#L38)

An abort signal to abort the context creation

***

### ignoreMemorySafetyChecks?

```ts
optional ignoreMemorySafetyChecks: boolean;
```

Defined in: [evaluator/LlamaEmbeddingContext.ts:46](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbeddingContext.ts#L46)

Ignore insufficient memory errors and continue with the context creation.
Can cause the process to crash if there's not enough VRAM for the new context.

Defaults to `false`.
