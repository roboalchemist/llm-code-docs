# Source: https://node-llama-cpp.withcat.ai/api/classes/GgufInsightsConfigurationResolver.md

---
url: /api/classes/GgufInsightsConfigurationResolver.md
---
# Class: GgufInsightsConfigurationResolver

Defined in: [gguf/insights/GgufInsightsConfigurationResolver.ts:16](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/insights/GgufInsightsConfigurationResolver.ts#L16)

## Accessors

### ggufInsights

#### Get Signature

```ts
get ggufInsights(): GgufInsights;
```

Defined in: [gguf/insights/GgufInsightsConfigurationResolver.ts:23](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/insights/GgufInsightsConfigurationResolver.ts#L23)

##### Returns

[`GgufInsights`](GgufInsights.md)

## Methods

### resolveAndScoreConfig()

```ts
resolveAndScoreConfig(options?: {
  targetGpuLayers?: number | "max";
  targetContextSize?: number;
  embeddingContext?: boolean;
  flashAttention?: boolean;
  swaFullCache?: boolean;
  useMmap?: boolean;
}, hardwareOverrides?: {
  getVramState?: Promise<{
     total: number;
     free: number;
     unifiedSize: number;
  }>;
  getRamState?: Promise<{
     total: number;
     free: number;
  }>;
  getSwapState?: Promise<{
     total: number;
     free: number;
  }>;
  llamaVramPaddingSize?: number;
  llamaGpu?: false | "metal" | "cuda" | "vulkan";
  llamaSupportsGpuOffloading?: boolean;
}): Promise<{
  compatibilityScore: number;
  bonusScore: number;
  totalScore: number;
  resolvedValues: {
     gpuLayers: number;
     contextSize: number;
     modelRamUsage: number;
     contextRamUsage: number;
     totalRamUsage: number;
     modelVramUsage: number;
     contextVramUsage: number;
     totalVramUsage: number;
  };
}>;
```

Defined in: [gguf/insights/GgufInsightsConfigurationResolver.ts:37](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/insights/GgufInsightsConfigurationResolver.ts#L37)

Resolve the best configuration for loading a model and creating a context using the current hardware.

Specifying a `targetGpuLayers` and/or `targetContextSize` will ensure the resolved configuration matches those values,
but note it can lower the compatibility score if the hardware doesn't support it.

Overriding hardware values it possible by configuring `hardwareOverrides`.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | { `targetGpuLayers?`: `number` | `"max"`; `targetContextSize?`: `number`; `embeddingContext?`: `boolean`; `flashAttention?`: `boolean`; `swaFullCache?`: `boolean`; `useMmap?`: `boolean`; } | - |
| `options.targetGpuLayers?` | `number` | `"max"` | - |
| `options.targetContextSize?` | `number` | - |
| `options.embeddingContext?` | `boolean` | - |
| `options.flashAttention?` | `boolean` | - |
| `options.swaFullCache?` | `boolean` | - |
| `options.useMmap?` | `boolean` | - |
| `hardwareOverrides` | { `getVramState?`: [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{ `total`: `number`; `free`: `number`; `unifiedSize`: `number`; }>; `getRamState?`: [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{ `total`: `number`; `free`: `number`; }>; `getSwapState?`: [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{ `total`: `number`; `free`: `number`; }>; `llamaVramPaddingSize?`: `number`; `llamaGpu?`: `false` | `"metal"` | `"cuda"` | `"vulkan"`; `llamaSupportsGpuOffloading?`: `boolean`; } | - |
| `hardwareOverrides.getVramState?` | - |
| `hardwareOverrides.getRamState?` | - |
| `hardwareOverrides.getSwapState?` | - |
| `hardwareOverrides.llamaVramPaddingSize?` | `number` | - |
| `hardwareOverrides.llamaGpu?` | `false` | `"metal"` | `"cuda"` | `"vulkan"` | - |
| `hardwareOverrides.llamaSupportsGpuOffloading?` | `boolean` | - |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{
`compatibilityScore`: `number`;
`bonusScore`: `number`;
`totalScore`: `number`;
`resolvedValues`: {
`gpuLayers`: `number`;
`contextSize`: `number`;
`modelRamUsage`: `number`;
`contextRamUsage`: `number`;
`totalRamUsage`: `number`;
`modelVramUsage`: `number`;
`contextVramUsage`: `number`;
`totalVramUsage`: `number`;
};
}>

***

### scoreModelConfigurationCompatibility()

```ts
scoreModelConfigurationCompatibility(__namedParameters?: {
  contextSize?: number;
  embeddingContext?: boolean;
  flashAttention?: boolean;
  swaFullCache?: boolean;
  maximumFittedContextSizeMultiplier?: number;
  maximumUnfitConfigurationResourceMultiplier?: number;
  forceStrictContextSize?: boolean;
  forceGpuLayers?: number | "max";
  useMmap?: boolean;
}, __namedParameters?: {
  getVramState?: Promise<{
     total: number;
     free: number;
     unifiedSize: number;
  }>;
  getRamState?: Promise<{
     total: number;
     free: number;
  }>;
  getSwapState?: Promise<{
     total: number;
     free: number;
  }>;
  llamaVramPaddingSize?: number;
  llamaGpu?: false | "metal" | "cuda" | "vulkan";
  llamaSupportsGpuOffloading?: boolean;
}): Promise<{
  compatibilityScore: number;
  bonusScore: number;
  totalScore: number;
  resolvedValues: {
     gpuLayers: number;
     contextSize: number;
     modelRamUsage: number;
     contextRamUsage: number;
     totalRamUsage: number;
     modelVramUsage: number;
     contextVramUsage: number;
     totalVramUsage: number;
  };
}>;
```

Defined in: [gguf/insights/GgufInsightsConfigurationResolver.ts:107](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/insights/GgufInsightsConfigurationResolver.ts#L107)

Score the compatibility of the model configuration with the current GPU and VRAM state.
Assumes a model is loaded with the default `"auto"` configurations.
Scored based on the following criteria:

* The number of GPU layers that can be offloaded to the GPU (only if there's a GPU. If there's no GPU then by how small the model is)
* Whether all layers can be offloaded to the GPU (gives additional points)
* Whether the resolved context size is at least as large as the specified `contextSize`

If the resolved context size is larger than the specified context size, for each multiplier of the specified `contextSize`
that the resolved context size is larger by, 1 bonus point is given in the `bonusScore`.

`maximumFittedContextSizeMultiplier` is used to improve the proportionality of the bonus score between models.
Set this to any value higher than `<max compared model context size> / contextSize`.
Defaults to `100`.

`maximumUnfitConfigurationResourceMultiplier` is used to improve the proportionality of the bonus score between unfit models.
Set this to any value higher than `<max compared model resource usage> / <total available resources>`.
Defaults to `100`.

`contextSize` defaults to `4096` (if the model train context size is lower than this, the model train context size is used instead).

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `__namedParameters` | { `contextSize?`: `number`; `embeddingContext?`: `boolean`; `flashAttention?`: `boolean`; `swaFullCache?`: `boolean`; `maximumFittedContextSizeMultiplier?`: `number`; `maximumUnfitConfigurationResourceMultiplier?`: `number`; `forceStrictContextSize?`: `boolean`; `forceGpuLayers?`: `number` | `"max"`; `useMmap?`: `boolean`; } | - |
| `__namedParameters.contextSize?` | `number` | - |
| `__namedParameters.embeddingContext?` | `boolean` | - |
| `__namedParameters.flashAttention?` | `boolean` | - |
| `__namedParameters.swaFullCache?` | `boolean` | - |
| `__namedParameters.maximumFittedContextSizeMultiplier?` | `number` | - |
| `__namedParameters.maximumUnfitConfigurationResourceMultiplier?` | `number` | - |
| `__namedParameters.forceStrictContextSize?` | `boolean` | Do not resolve a context size larger than the specified `contextSize`. Defaults to `false`. |
| `__namedParameters.forceGpuLayers?` | `number` | `"max"` | - |
| `__namedParameters.useMmap?` | `boolean` | - |
| `__namedParameters` | { `getVramState?`: [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{ `total`: `number`; `free`: `number`; `unifiedSize`: `number`; }>; `getRamState?`: [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{ `total`: `number`; `free`: `number`; }>; `getSwapState?`: [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{ `total`: `number`; `free`: `number`; }>; `llamaVramPaddingSize?`: `number`; `llamaGpu?`: `false` | `"metal"` | `"cuda"` | `"vulkan"`; `llamaSupportsGpuOffloading?`: `boolean`; } | - |
| `__namedParameters.getVramState?` | - |
| `__namedParameters.getRamState?` | - |
| `__namedParameters.getSwapState?` | - |
| `__namedParameters.llamaVramPaddingSize?` | `number` | - |
| `__namedParameters.llamaGpu?` | `false` | `"metal"` | `"cuda"` | `"vulkan"` | - |
| `__namedParameters.llamaSupportsGpuOffloading?` | `boolean` | - |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{
`compatibilityScore`: `number`;
`bonusScore`: `number`;
`totalScore`: `number`;
`resolvedValues`: {
`gpuLayers`: `number`;
`contextSize`: `number`;
`modelRamUsage`: `number`;
`contextRamUsage`: `number`;
`totalRamUsage`: `number`;
`modelVramUsage`: `number`;
`contextVramUsage`: `number`;
`totalVramUsage`: `number`;
};
}>

***

### resolveModelGpuLayers()

```ts
resolveModelGpuLayers(gpuLayers?: 
  | number
  | "auto"
  | "max"
  | {
  min?: number;
  max?: number;
  fitContext?: {
     contextSize?: number;
     embeddingContext?: boolean;
  };
}, __namedParameters?: {
  ignoreMemorySafetyChecks?: boolean;
  getVramState?: Promise<{
     total: number;
     free: number;
  }>;
  llamaVramPaddingSize?: number;
  llamaGpu?: false | "metal" | "cuda" | "vulkan";
  llamaSupportsGpuOffloading?: boolean;
  defaultContextFlashAttention?: boolean;
  defaultContextSwaFullCache?: boolean;
  useMmap?: boolean;
}): Promise<number>;
```

Defined in: [gguf/insights/GgufInsightsConfigurationResolver.ts:385](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/insights/GgufInsightsConfigurationResolver.ts#L385)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `gpuLayers?` | | `number` | `"auto"` | `"max"` | { `min?`: `number`; `max?`: `number`; `fitContext?`: { `contextSize?`: `number`; `embeddingContext?`: `boolean`; }; } |
| `__namedParameters?` | { `ignoreMemorySafetyChecks?`: `boolean`; `getVramState?`: [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{ `total`: `number`; `free`: `number`; }>; `llamaVramPaddingSize?`: `number`; `llamaGpu?`: `false` | `"metal"` | `"cuda"` | `"vulkan"`; `llamaSupportsGpuOffloading?`: `boolean`; `defaultContextFlashAttention?`: `boolean`; `defaultContextSwaFullCache?`: `boolean`; `useMmap?`: `boolean`; } |
| `__namedParameters.ignoreMemorySafetyChecks?` | `boolean` |
| `__namedParameters.getVramState?` |
| `__namedParameters.llamaVramPaddingSize?` | `number` |
| `__namedParameters.llamaGpu?` | `false` | `"metal"` | `"cuda"` | `"vulkan"` |
| `__namedParameters.llamaSupportsGpuOffloading?` | `boolean` |
| `__namedParameters.defaultContextFlashAttention?` | `boolean` |
| `__namedParameters.defaultContextSwaFullCache?` | `boolean` |
| `__namedParameters.useMmap?` | `boolean` |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`number`>

***

### resolveContextContextSize()

```ts
resolveContextContextSize(contextSize: 
  | number
  | "auto"
  | {
  min?: number;
  max?: number;
}
  | undefined, __namedParameters: {
  modelGpuLayers: number;
  modelTrainContextSize: number;
  flashAttention?: boolean;
  swaFullCache?: boolean;
  batchSize?: number;
  sequences?: number;
  getVramState?: Promise<{
     total: number;
     free: number;
     unifiedSize: number;
  }>;
  getRamState?: Promise<{
     total: number;
     free: number;
  }>;
  getSwapState?: Promise<{
     total: number;
     free: number;
  }>;
  llamaGpu?: false | "metal" | "cuda" | "vulkan";
  ignoreMemorySafetyChecks?: boolean;
  isEmbeddingContext?: boolean;
}): Promise<number>;
```

Defined in: [gguf/insights/GgufInsightsConfigurationResolver.ts:416](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/gguf/insights/GgufInsightsConfigurationResolver.ts#L416)

Resolve a context size option for the given options and constraints.

If there's no context size that can fit the available resources, an `InsufficientMemoryError` is thrown.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `contextSize` | | `number` | `"auto"` | { `min?`: `number`; `max?`: `number`; } | `undefined` |
| `__namedParameters` | { `modelGpuLayers`: `number`; `modelTrainContextSize`: `number`; `flashAttention?`: `boolean`; `swaFullCache?`: `boolean`; `batchSize?`: `number`; `sequences?`: `number`; `getVramState?`: [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{ `total`: `number`; `free`: `number`; `unifiedSize`: `number`; }>; `getRamState?`: [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{ `total`: `number`; `free`: `number`; }>; `getSwapState?`: [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{ `total`: `number`; `free`: `number`; }>; `llamaGpu?`: `false` | `"metal"` | `"cuda"` | `"vulkan"`; `ignoreMemorySafetyChecks?`: `boolean`; `isEmbeddingContext?`: `boolean`; } |
| `__namedParameters.modelGpuLayers` | `number` |
| `__namedParameters.modelTrainContextSize` | `number` |
| `__namedParameters.flashAttention?` | `boolean` |
| `__namedParameters.swaFullCache?` | `boolean` |
| `__namedParameters.batchSize?` | `number` |
| `__namedParameters.sequences?` | `number` |
| `__namedParameters.getVramState?` |
| `__namedParameters.getRamState?` |
| `__namedParameters.getSwapState?` |
| `__namedParameters.llamaGpu?` | `false` | `"metal"` | `"cuda"` | `"vulkan"` |
| `__namedParameters.ignoreMemorySafetyChecks?` | `boolean` |
| `__namedParameters.isEmbeddingContext?` | `boolean` |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`number`>
