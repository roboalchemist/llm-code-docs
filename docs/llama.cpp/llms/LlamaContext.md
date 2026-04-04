# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaContext.md

---
url: /api/classes/LlamaContext.md
---
# Class: LlamaContext

Defined in: [evaluator/LlamaContext/LlamaContext.ts:42](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L42)

## Properties

### onDispose

```ts
readonly onDispose: EventRelay<void>;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:73](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L73)

## Accessors

### disposed

#### Get Signature

```ts
get disposed(): boolean;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:182](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L182)

##### Returns

`boolean`

***

### model

#### Get Signature

```ts
get model(): LlamaModel;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:186](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L186)

##### Returns

[`LlamaModel`](LlamaModel.md)

***

### contextSize

#### Get Signature

```ts
get contextSize(): number;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:190](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L190)

##### Returns

`number`

***

### batchSize

#### Get Signature

```ts
get batchSize(): number;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:194](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L194)

##### Returns

`number`

***

### flashAttention

#### Get Signature

```ts
get flashAttention(): boolean;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:198](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L198)

##### Returns

`boolean`

***

### stateSize

#### Get Signature

```ts
get stateSize(): number;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:206](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L206)

The actual size of the state in the memory in bytes.
This value is provided by `llama.cpp` and doesn't include all the memory overhead of the context.

##### Returns

`number`

***

### currentThreads

#### Get Signature

```ts
get currentThreads(): number;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:213](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L213)

The number of threads currently used to evaluate tokens

##### Returns

`number`

***

### idealThreads

#### Get Signature

```ts
get idealThreads(): number;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:224](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L224)

The number of threads that are preferred to be used to evaluate tokens.

The actual number of threads used may be lower when other evaluations are running in parallel.

##### Returns

`number`

***

### totalSequences

#### Get Signature

```ts
get totalSequences(): number;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:237](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L237)

##### Returns

`number`

***

### sequencesLeft

#### Get Signature

```ts
get sequencesLeft(): number;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:241](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L241)

##### Returns

`number`

## Methods

### dispose()

```ts
dispose(): Promise<void>;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:168](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L168)

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

***

### getAllocatedContextSize()

```ts
getAllocatedContextSize(): number;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:228](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L228)

#### Returns

`number`

***

### getSequence()

```ts
getSequence(options?: {
  contextShift?: ContextShiftOptions;
  tokenPredictor?: TokenPredictor;
}): LlamaContextSequence;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:249](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L249)

Before calling this method, make sure to call `sequencesLeft` to check if there are any sequences left.
When there are no sequences left, this method will throw an error.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | { `contextShift?`: [`ContextShiftOptions`](../type-aliases/ContextShiftOptions.md); `tokenPredictor?`: [`TokenPredictor`](TokenPredictor.md); } | - |
| `options.contextShift?` | [`ContextShiftOptions`](../type-aliases/ContextShiftOptions.md) | - |
| `options.tokenPredictor?` | [`TokenPredictor`](TokenPredictor.md) | Token predictor to use for the sequence. Don't share the same token predictor between multiple sequences. Using a token predictor doesn't affect the generation output itself - it only allows for greater parallelization of the token evaluation to speed up the generation. > **Note:** that if a token predictor is too resource intensive, > it can slow down the generation process due to the overhead of running the predictor. > > Testing the effectiveness of a token predictor on the target machine is recommended before using it in production. Automatically disposed when disposing the sequence. **See** [Using Token Predictors](https://node-llama-cpp.withcat.ai/guide/token-prediction) |

#### Returns

[`LlamaContextSequence`](LlamaContextSequence.md)

***

### dispatchPendingBatch()

```ts
dispatchPendingBatch(): void;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:300](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L300)

#### Returns

`void`

***

### printTimings()

```ts
printTimings(): Promise<void>;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:608](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L608)

Print the timings of token evaluation since that last print for this context.

Requires the `performanceTracking` option to be enabled.

> **Note:** it prints on the `LlamaLogLevel.info` level, so if you set the level of your `Llama` instance higher than that,
> it won't print anything.

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>
