# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaContextOptions.md

---
url: /api/type-aliases/LlamaContextOptions.md
---
# Type Alias: LlamaContextOptions

```ts
type LlamaContextOptions = {
  sequences?: number;
  contextSize?:   | "auto"
     | number
     | {
     min?: number;
     max?: number;
   };
  batchSize?: number;
  flashAttention?: boolean;
  threads?:   | number
     | {
     ideal?: number;
     min?: number;
   };
  batching?: BatchingOptions;
  swaFullCache?: boolean;
  lora?:   | string
     | {
     adapters: {
        filePath: string;
        scale?: number;
     }[];
     onLoadProgress?: void;
   };
  createSignal?: AbortSignal;
  ignoreMemorySafetyChecks?: boolean;
  failedCreationRemedy?:   | false
     | {
     retries?: number;
     autoContextSizeShrink?: number | (contextSize: number) => number;
   };
  performanceTracking?: boolean;
};
```

Defined in: [evaluator/LlamaContext/types.ts:8](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L8)

## Properties

### sequences?

```ts
optional sequences: number;
```

Defined in: [evaluator/LlamaContext/types.ts:19](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L19)

number of sequences for the context.
Each sequence is a different "text generation process" that can run in parallel to other sequences in the same context.
Although a single context has multiple sequences, the sequences are separate from each other and do not share data with each other.
This is beneficial for performance, as multiple sequences can be evaluated in parallel (on the same batch).

Each sequence increases the memory usage of the context.

Defaults to `1`.

***

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

Defined in: [evaluator/LlamaContext/types.ts:38](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L38)

The number of tokens the model can see at once.

* **`"auto"`** - adapt to the current VRAM state and attemp to set the context size as high as possible up to the size
  the model was trained on.
* **`number`** - set the context size to a specific number of tokens.
  If there's not enough VRAM, an error will be thrown.
  Use with caution.
* **`{min?: number, max?: number}`** - adapt to the current VRAM state and attemp to set the context size as high as possible
  up to the size the model was trained on, but at least `min` and at most `max`.

The actual context size may be slightly larger than your request (by up to 256) due to the implementation in `llama.cpp` that
aligns the context size to multiples of 256 for performance reasons.
To check the actual context size that gets created, use the `.contextSize` property
of the created context instance or any of its sequences.

Defaults to `"auto"`.

***

### batchSize?

```ts
optional batchSize: number;
```

Defined in: [evaluator/LlamaContext/types.ts:48](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L48)

The number of tokens that can be processed at once by the GPU.

Defaults to `512` or `contextSize` if `contextSize` is less than `512`.

***

### flashAttention?

```ts
optional flashAttention: boolean;
```

Defined in: [evaluator/LlamaContext/types.ts:63](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L63)

Flash attention is an optimization in the attention mechanism that makes inference faster, more efficient and uses less memory.

The support for flash attention is currently experimental and may not always work as expected.
Use with caution.

This option will be ignored if flash attention is not supported by the model.

Defaults to `false` (inherited from the model option `defaultContextFlashAttention`).

Upon flash attention exiting the experimental status, the default value will become `true`
(the inherited value from the model option `defaultContextFlashAttention` will become `true`).

***

### threads?

```ts
optional threads: 
  | number
  | {
  ideal?: number;
  min?: number;
};
```

Defined in: [evaluator/LlamaContext/types.ts:78](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L78)

number of threads to use to evaluate tokens.
set to 0 to use the maximum threads supported by the current machine hardware.

This value is considered as a hint, and the actual number of threads used may be lower when other evaluations are running.
To ensure the minimum number of threads you want to use are always used,
set this to an object with a `min` property (see the `min` property description for more details).

If `maxThreads` from the Llama instance is set to `0`, this value will always be the actual number of threads used.

If `maxThreads` from the Llama instance is set to `0`, defaults to the `.cpuMathCores` value from the Llama instance,
otherwise defaults to `maxThreads` from the Llama instance (see the `maxThreads` option of `getLlama` method for more details).

#### Type Declaration

`number`

```ts
{
  ideal?: number;
  min?: number;
}
```

#### ideal?

```ts
optional ideal: number;
```

The ideal number of threads to use for evaluations.

If other evaluations are running, the actual number of threads may be lower than this value.

If `maxThreads` from the Llama instance is set to `0`, this value will always be the actual number of threads used.

If `maxThreads` from the Llama instance is set to `0`, defaults to the `.cpuMathCores` value from the Llama instance,
otherwise defaults to `maxThreads` from the Llama instance (see the `maxThreads` option of `getLlama` method for more details).

#### min?

```ts
optional min: number;
```

Ensure evaluations always use at least this number of threads.

Use with caution, since setting this value too high can lead to the context waiting too much time
to reserve this number of threads before the evaluation can start.

***

### batching?

```ts
optional batching: BatchingOptions;
```

Defined in: [evaluator/LlamaContext/types.ts:105](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L105)

Control the parallel sequences processing behavior.

See [BatchingOptions](BatchingOptions.md) for more information.

***

### swaFullCache?

```ts
optional swaFullCache: boolean;
```

Defined in: [evaluator/LlamaContext/types.ts:121](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L121)

When using SWA (Sliding Window Attention) on a supported model,
extend the sliding window size to the current context size (meaning practically disabling SWA).

Enabling this option will consume more memory on models that support SWA (Sliding Window Attention),
but will allow reusing the evaluation cache of any prefix length of the context sequence state
(instead of just the size of the sliding window when SWA is used).

This option has no effect on models that do not support SWA (Sliding Window Attention).

> **Note:** you can check the SWA size using `model.fileInsights.swaSize`.

Defaults to `false` (inherited from the model option `defaultContextSwaFullCache`);

***

### lora?

```ts
optional lora: 
  | string
  | {
  adapters: {
     filePath: string;
     scale?: number;
  }[];
  onLoadProgress?: void;
};
```

Defined in: [evaluator/LlamaContext/types.ts:132](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L132)

Load the provided LoRA adapters onto the context.
LoRA adapters are used to modify the weights of a pretrained model to adapt to new tasks or domains
without the need for extensive retraining from scratch.

If a string is provided, it will be treated as a path to a single LoRA adapter file.

The adapters will be released from memory once the model (not just the context) is disposed.

#### Type Declaration

`string`

```ts
{
  adapters: {
     filePath: string;
     scale?: number;
  }[];
  onLoadProgress?: void;
}
```

#### adapters

```ts
adapters: {
  filePath: string;
  scale?: number;
}[];
```

#### onLoadProgress()?

```ts
optional onLoadProgress(loadProgress: number): void;
```

Called with the LoRA adapters load percentage when the LoRA adapters are being loaded.

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `loadProgress` | `number` | a number between 0 (exclusive) and 1 (inclusive). |

##### Returns

`void`

***

### createSignal?

```ts
optional createSignal: AbortSignal;
```

Defined in: [evaluator/LlamaContext/types.ts:150](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L150)

An abort signal to abort the context creation

***

### ignoreMemorySafetyChecks?

```ts
optional ignoreMemorySafetyChecks: boolean;
```

Defined in: [evaluator/LlamaContext/types.ts:158](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L158)

Ignore insufficient memory errors and continue with the context creation.
Can cause the process to crash if there's not enough VRAM for the new context.

Defaults to `false`.

***

### failedCreationRemedy?

```ts
optional failedCreationRemedy: 
  | false
  | {
  retries?: number;
  autoContextSizeShrink?: number | (contextSize: number) => number;
};
```

Defined in: [evaluator/LlamaContext/types.ts:167](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L167)

On failed context creation, retry the creation with a smaller context size.

Only works if `contextSize` is set to `"auto"`, left as default or set to an object with `min` and/or `max` properties.

Set `retries` to `false` to disable.

#### Type Declaration

`false`

```ts
{
  retries?: number;
  autoContextSizeShrink?: number | (contextSize: number) => number;
}
```

#### retries?

```ts
optional retries: number;
```

Retries to attempt to create the context.

Defaults to `6`.

#### autoContextSizeShrink?

```ts
optional autoContextSizeShrink: number | (contextSize: number) => number;
```

The percentage to decrease the context size by on each retry.
Should be a number between `0` and `1`.

If a function is provided, it will be called with the current context size and should return the new context size.

Defaults to `0.16`.

***

### performanceTracking?

```ts
optional performanceTracking: boolean;
```

Defined in: [evaluator/LlamaContext/types.ts:191](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/types.ts#L191)

Track the inference performance of the context, so using `.printTimings()` will work.

Defaults to `false`.
