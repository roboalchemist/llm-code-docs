# Source: https://node-llama-cpp.withcat.ai/api/classes/DraftSequenceTokenPredictor.md

---
url: /api/classes/DraftSequenceTokenPredictor.md
---
# Class: DraftSequenceTokenPredictor

Defined in: [evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts:20](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts#L20)

Predicts the next tokens by evaluating the current state of the target sequence
on a draft sequence from a smaller and faster draft model.

## See

[Using Token Predictors: Draft Model Token Predictor](https://node-llama-cpp.withcat.ai/guide/token-prediction#draft-model)

## Extends

* [`TokenPredictor`](TokenPredictor.md)

## Constructors

### Constructor

```ts
new DraftSequenceTokenPredictor(draftSequence: LlamaContextSequence, options?: {
  minTokens?: number;
  maxTokens?: number;
  evaluateOptions?: Pick<SequenceEvaluateOptions, 
     | "contextShift"
     | "evaluationPriority"
     | "temperature"
     | "minP"
     | "topK"
     | "topP"
     | "seed"
     | "xtc"
     | "repeatPenalty"
     | "dryRepeatPenalty"
    | "tokenBias">;
  minConfidence?: number;
}): DraftSequenceTokenPredictor;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts:41](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts#L41)

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `draftSequence` | [`LlamaContextSequence`](LlamaContextSequence.md) | - |
| `options` | { `minTokens?`: `number`; `maxTokens?`: `number`; `evaluateOptions?`: [`Pick`](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[`SequenceEvaluateOptions`](../type-aliases/SequenceEvaluateOptions.md), | `"contextShift"` | `"evaluationPriority"` | `"temperature"` | `"minP"` | `"topK"` | `"topP"` | `"seed"` | `"xtc"` | `"repeatPenalty"` | `"dryRepeatPenalty"` | `"tokenBias"`>; `minConfidence?`: `number`; } | - |
| `options.minTokens?` | `number` | The minimum number of tokens to draft. Defaults to `0`. |
| `options.maxTokens?` | `number` | Maximum number of tokens to draft. Defaults to `16`. |
| `options.evaluateOptions?` | [`Pick`](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[`SequenceEvaluateOptions`](../type-aliases/SequenceEvaluateOptions.md), | `"contextShift"` | `"evaluationPriority"` | `"temperature"` | `"minP"` | `"topK"` | `"topP"` | `"seed"` | `"xtc"` | `"repeatPenalty"` | `"dryRepeatPenalty"` | `"tokenBias"`> | Evaluate options default to the values of the target sequence. You can override any of the options for the prediction here. |
| `options.minConfidence?` | `number` | Minimum token confidence (probability of the token to be generated, assigned by the model) to consider the token as a prediction. When the generated token confidence is lower than this value, the prediction process will stop until all the predicted tokens are exhausted (either by a token that was not predicted being pushed, or all the generated predictions are consumed). A number between `0` and `1` representing the minimum probability of the token to be generated. Set to `0` to disable. Defaults to `0.6`. |

#### Returns

`DraftSequenceTokenPredictor`

#### Overrides

[`TokenPredictor`](TokenPredictor.md).[`constructor`](TokenPredictor.md#constructor)

## Accessors

### draftSequence

#### Get Signature

```ts
get draftSequence(): LlamaContextSequence;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts:88](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts#L88)

##### Returns

[`LlamaContextSequence`](LlamaContextSequence.md)

***

### minTokens

#### Get Signature

```ts
get minTokens(): number;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts:92](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts#L92)

##### Returns

`number`

***

### maxTokens

#### Get Signature

```ts
get maxTokens(): number;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts:96](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts#L96)

##### Returns

`number`

***

### minConfidence

#### Get Signature

```ts
get minConfidence(): number | undefined;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts:100](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts#L100)

##### Returns

`number` | `undefined`

## Methods

### updateInputTokens()

```ts
updateInputTokens(tokens: Token[]): void;
```

Defined in: [evaluator/LlamaContext/TokenPredictor.ts:57](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/TokenPredictor.ts#L57)

Called with the input tokens before the generation starts when using `LlamaChatSession`, `LlamaChat`, and `LlamaCompletion`.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `tokens` | [`Token`](../type-aliases/Token.md)\[] |

#### Returns

`void`

#### Inherited from

[`TokenPredictor`](TokenPredictor.md).[`updateInputTokens`](TokenPredictor.md#updateinputtokens)

***

### reset()

```ts
reset(__namedParameters: {
  targetSequence: LlamaContextSequence;
  stateTokens: Token[];
  evaluateOptions: Readonly<SequenceEvaluateOptions>;
}): Promise<void>;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts:104](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts#L104)

Resets the state of the predictor.

Called before the generation starts.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | { `targetSequence`: [`LlamaContextSequence`](LlamaContextSequence.md); `stateTokens`: [`Token`](../type-aliases/Token.md)\[]; `evaluateOptions`: [`Readonly`](https://www.typescriptlang.org/docs/handbook/utility-types.html#readonlytype)<[`SequenceEvaluateOptions`](../type-aliases/SequenceEvaluateOptions.md)>; } |
| `__namedParameters.targetSequence` | [`LlamaContextSequence`](LlamaContextSequence.md) |
| `__namedParameters.stateTokens` | [`Token`](../type-aliases/Token.md)\[] |
| `__namedParameters.evaluateOptions` | [`Readonly`](https://www.typescriptlang.org/docs/handbook/utility-types.html#readonlytype)<[`SequenceEvaluateOptions`](../type-aliases/SequenceEvaluateOptions.md)> |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

#### Overrides

[`TokenPredictor`](TokenPredictor.md).[`reset`](TokenPredictor.md#reset)

***

### pushTokens()

```ts
pushTokens(tokens: Token[]): void;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts:156](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts#L156)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `tokens` | [`Token`](../type-aliases/Token.md)\[] |

#### Returns

`void`

#### Overrides

[`TokenPredictor`](TokenPredictor.md).[`pushTokens`](TokenPredictor.md#pushtokens)

***

### predictTokens()

```ts
predictTokens(): 
  | Token[]
  | Promise<Token[]>;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts:192](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts#L192)

Predicts the next tokens based on the current state.

If the generation should wait until the minimum predications are ready,
this method should return a promise that resolves when the minimum predictions are ready.

A background prediction process can be started when this function is called,
so that the next predictions will be ready when this function is called again.

#### Returns

| [`Token`](../type-aliases/Token.md)\[]
| [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`Token`](../type-aliases/Token.md)\[]>

#### Overrides

[`TokenPredictor`](TokenPredictor.md).[`predictTokens`](TokenPredictor.md#predicttokens)

***

### stop()

```ts
stop(untilPredictionsExhausted?: boolean): void;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts:221](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts#L221)

Stops the prediction process when it runs in the background.

#### Parameters

| Parameter | Type | Default value | Description |
| ------ | ------ | ------ | ------ |
| `untilPredictionsExhausted` | `boolean` | `false` | If true, the prediction process should not resume until the current predictions are exhausted. |

#### Returns

`void`

#### Overrides

[`TokenPredictor`](TokenPredictor.md).[`stop`](TokenPredictor.md#stop)

***

### dispose()

```ts
dispose(): void;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts:235](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/DraftSequenceTokenPredictor.ts#L235)

#### Returns

`void`

#### Overrides

[`TokenPredictor`](TokenPredictor.md).[`dispose`](TokenPredictor.md#dispose)
