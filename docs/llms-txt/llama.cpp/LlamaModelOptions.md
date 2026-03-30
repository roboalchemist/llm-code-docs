# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaModelOptions.md

---
url: /api/type-aliases/LlamaModelOptions.md
---
# Type Alias: LlamaModelOptions

```ts
type LlamaModelOptions = {
  modelPath: string;
  gpuLayers?:   | "auto"
     | "max"
     | number
     | {
     min?: number;
     max?: number;
     fitContext?: {
        contextSize?: number;
        embeddingContext?: boolean;
     };
   };
  vocabOnly?: boolean;
  useMmap?: boolean;
  useDirectIo?: boolean;
  useMlock?: boolean;
  checkTensors?: boolean;
  defaultContextFlashAttention?: boolean;
  defaultContextSwaFullCache?: boolean;
  onLoadProgress?: void;
  loadSignal?: AbortSignal;
  ignoreMemorySafetyChecks?: boolean;
  metadataOverrides?: OverridesObject<GgufMetadata, number | bigint | boolean | string>;
};
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:26](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L26)

## Properties

### modelPath

```ts
modelPath: string;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:28](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L28)

path to the model on the filesystem

***

### gpuLayers?

```ts
optional gpuLayers: 
  | "auto"
  | "max"
  | number
  | {
  min?: number;
  max?: number;
  fitContext?: {
     contextSize?: number;
     embeddingContext?: boolean;
  };
};
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:44](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L44)

Number of layers to store in VRAM.

* **`"auto"`** - adapt to the current VRAM state and try to fit as many layers as possible in it.
  Takes into account the VRAM required to create a context with a `contextSize` set to `"auto"`.
* **`"max"`** - store all layers in VRAM. If there's not enough VRAM, an error will be thrown. Use with caution.
* **`number`** - store the specified number of layers in VRAM. If there's not enough VRAM, an error will be thrown. Use with caution.
* **`{min?: number, max?: number, fitContext?: {contextSize: number}}`** - adapt to the current VRAM state and try to fit as
  many layers as possible in it, but at least `min` and at most `max` layers. Set `fitContext` to the parameters of a context you
  intend to create with the model, so it'll take it into account in the calculations and leave enough memory for such a context.

If GPU support is disabled, will be set to `0` automatically.

Defaults to `"auto"`.

***

### vocabOnly?

```ts
optional vocabOnly: boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:64](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L64)

Only load the vocabulary, not weight tensors.

Useful when you only want to use the model to use its tokenizer but not for evaluation.

Defaults to `false`.

***

### useMmap?

```ts
optional useMmap: boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:77](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L77)

Use mmap (memory-mapped file) to load the model.

Using mmap allows the OS to load the model tensors directly from the file on the filesystem,
and makes it easier for the system to manage memory.

When using mmap, you might notice a delay the first time you actually use the model,
which is caused by the OS itself loading the model into memory.

Defaults to `true` if the current system supports it.

***

### useDirectIo?

```ts
optional useDirectIo: boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:93](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L93)

Direct I/O is a method of reading and writing data to and from the storage device directly to the application memory,
bypassing OS in-memory caches.

It can lead to improved model loading times and reduced RAM usage,
on the expense of higher loading times when the model unloaded and loaded again repeatedly in a short period of time.

When this option is enabled, if Direct I/O is supported by the system (and for the given file)
it will be used and mmap will be disabled.

Unsupported on macOS.

Defaults to `false`.

***

### useMlock?

```ts
optional useMlock: boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:99](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L99)

Force the system to keep the model in the RAM/VRAM.
Use with caution as this can crash your system if the available resources are insufficient.

***

### checkTensors?

```ts
optional checkTensors: boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:107](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L107)

Check for tensor validity before actually loading the model.
Using it increases the time it takes to load the model.

Defaults to `false`.

***

### defaultContextFlashAttention?

```ts
optional defaultContextFlashAttention: boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:128](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L128)

Enable flash attention by default for contexts created with this model.
Only works with models that support flash attention.

Flash attention is an optimization in the attention mechanism that makes inference faster, more efficient and uses less memory.

The support for flash attention is currently experimental and may not always work as expected.
Use with caution.

This option will be ignored if flash attention is not supported by the model.

Enabling this affects the calculations of default values for the model and contexts created with it
as flash attention reduces the amount of memory required,
which allows for more layers to be offloaded to the GPU and for context sizes to be bigger.

Defaults to `false`.

Upon flash attention exiting the experimental status, the default value will become `true`.

***

### defaultContextSwaFullCache?

```ts
optional defaultContextSwaFullCache: boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:139](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L139)

When using SWA (Sliding Window Attention) on a supported model,
extend the sliding window size to the current context size (meaning practically disabling SWA)
by default for contexts created with this model.

See the `swaFullCache` option of the `.createContext()` method for more information.

Defaults to `false`.

***

### loadSignal?

```ts
optional loadSignal: AbortSignal;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:148](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L148)

An abort signal to abort the model load

***

### ignoreMemorySafetyChecks?

```ts
optional ignoreMemorySafetyChecks: boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:156](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L156)

Ignore insufficient memory errors and continue with the model load.
Can cause the process to crash if there's not enough VRAM to fit the model.

Defaults to `false`.

***

### metadataOverrides?

```ts
optional metadataOverrides: OverridesObject<GgufMetadata, number | bigint | boolean | string>;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:165](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L165)

Metadata overrides to load the model with.

> **Note:** Most metadata value overrides aren't supported and overriding them will have no effect on `llama.cpp`.
> Only use this for metadata values that are explicitly documented to be supported by `llama.cpp` to be overridden,
> and only in cases when this is crucial, as this is not guaranteed to always work as expected.

## Methods

### onLoadProgress()?

```ts
optional onLoadProgress(loadProgress: number): void;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:145](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L145)

Called with the load percentage when the model is being loaded.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `loadProgress` | `number` | a number between 0 (exclusive) and 1 (inclusive). |

#### Returns

`void`
