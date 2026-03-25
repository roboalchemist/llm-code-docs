# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaRankingContextOptions.md

---
url: /api/type-aliases/LlamaRankingContextOptions.md
---
# Type Alias: LlamaRankingContextOptions

```ts
type LlamaRankingContextOptions = {
  contextSize?:   | "auto"
     | number
     | {
     min?: number;
     max?: number;
   };
  batchSize?: number;
  threads?: number;
  createSignal?: AbortSignal;
  template?:   | `${string}{{query}}${string}{{document}}${string}`
     | `${string}{{document}}${string}{{query}}${string}`;
  ignoreMemorySafetyChecks?: boolean;
};
```

Defined in: [evaluator/LlamaRankingContext.ts:10](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L10)

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

Defined in: [evaluator/LlamaRankingContext.ts:23](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L23)

The number of tokens the model can see at once.

* **`"auto"`** - adapt to the current VRAM state and attempt to set the context size as high as possible up to the size
  the model was trained on.
* **`number`** - set the context size to a specific number of tokens.
  If there's not enough VRAM, an error will be thrown.
  Use with caution.
* **`{min?: number, max?: number}`** - adapt to the current VRAM state and attempt to set the context size as high as possible
  up to the size the model was trained on, but at least `min` and at most `max`.

Defaults to `"auto"`.

***

### batchSize?

```ts
optional batchSize: number;
```

Defined in: [evaluator/LlamaRankingContext.ts:29](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L29)

prompt processing batch size

***

### threads?

```ts
optional threads: number;
```

Defined in: [evaluator/LlamaRankingContext.ts:35](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L35)

number of threads to use to evaluate tokens.
set to 0 to use the maximum threads supported by the current machine hardware

***

### createSignal?

```ts
optional createSignal: AbortSignal;
```

Defined in: [evaluator/LlamaRankingContext.ts:38](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L38)

An abort signal to abort the context creation

***

### template?

```ts
optional template: 
  | `${string}{{query}}${string}{{document}}${string}`
  | `${string}{{document}}${string}{{query}}${string}`;
```

Defined in: [evaluator/LlamaRankingContext.ts:54](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L54)

The template to use for the ranking evaluation.
If not provided, the model's template will be used by default.

The template is tokenized with special tokens enabled, but the provided query and document are not.

**`{{query}}`** is replaced with the query content.

**`{{document}}`** is replaced with the document content.

It's recommended to not set this option unless you know what you're doing.

Defaults to the model's template.

***

### ignoreMemorySafetyChecks?

```ts
optional ignoreMemorySafetyChecks: boolean;
```

Defined in: [evaluator/LlamaRankingContext.ts:62](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L62)

Ignore insufficient memory errors and continue with the context creation.
Can cause the process to crash if there's not enough VRAM for the new context.

Defaults to `false`.
