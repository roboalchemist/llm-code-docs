# Source: https://node-llama-cpp.withcat.ai/api/classes/InputLookupTokenPredictor.md

---
url: /api/classes/InputLookupTokenPredictor.md
---
# Class: InputLookupTokenPredictor

Defined in: [evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts:22](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts#L22)

Attempts to find the last few generated tokens in the input (prompt) tokens to predict the next tokens.

This is useful in input-grounded tasks (when the model frequently repeats some of the input tokens in the output,
such as in text summarization or modifying code).

This works in all completion classes, including `LlamaChatSession`, `LlamaChat`, and `LlamaCompletion`.

Based on https://github.com/apoorvumang/prompt-lookup-decoding.

## See

[Using Token Predictors: Input Lookup Token Predictor](https://node-llama-cpp.withcat.ai/guide/token-prediction#input-lookup)

## Extends

* [`TokenPredictor`](TokenPredictor.md)

## Constructors

### Constructor

```ts
new InputLookupTokenPredictor(options?: {
  patternLength?: {
     min?: number;
     max?: number;
  };
  predictionLength?: {
     min?: number;
     max?: number;
  };
}): InputLookupTokenPredictor;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts:33](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts#L33)

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | { `patternLength?`: { `min?`: `number`; `max?`: `number`; }; `predictionLength?`: { `min?`: `number`; `max?`: `number`; }; } | - |
| `options.patternLength?` | { `min?`: `number`; `max?`: `number`; } | - |
| `options.patternLength.min?` | `number` | Min pattern length to look for in the input tokens. Defaults to `1`. |
| `options.patternLength.max?` | `number` | Max pattern length to look for in the input tokens. Set to `0` to disable the max pattern size. Defaults to `0`. |
| `options.predictionLength?` | { `min?`: `number`; `max?`: `number`; } | - |
| `options.predictionLength.min?` | `number` | Minimum number of tokens to predict. Defaults to `1`. |
| `options.predictionLength.max?` | `number` | Maximum number of tokens to predict. Defaults to `3`. |

#### Returns

`InputLookupTokenPredictor`

#### Overrides

[`TokenPredictor`](TokenPredictor.md).[`constructor`](TokenPredictor.md#constructor)

## Accessors

### patternMinLength

#### Get Signature

```ts
get patternMinLength(): number;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts:86](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts#L86)

##### Returns

`number`

***

### patternMaxLength

#### Get Signature

```ts
get patternMaxLength(): number;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts:90](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts#L90)

##### Returns

`number`

***

### predictionMinLength

#### Get Signature

```ts
get predictionMinLength(): number;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts:94](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts#L94)

##### Returns

`number`

***

### predictionMaxLength

#### Get Signature

```ts
get predictionMaxLength(): number;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts:98](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts#L98)

##### Returns

`number`

## Methods

### stop()

```ts
stop(untilPredictionsExhausted?: boolean): 
  | void
  | Promise<void>;
```

Defined in: [evaluator/LlamaContext/TokenPredictor.ts:52](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/TokenPredictor.ts#L52)

Stops the prediction process when it runs in the background.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `untilPredictionsExhausted?` | `boolean` | If true, the prediction process should not resume until the current predictions are exhausted. |

#### Returns

| `void`
| [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

#### Inherited from

[`TokenPredictor`](TokenPredictor.md).[`stop`](TokenPredictor.md#stop)

***

### reset()

```ts
reset(__namedParameters: {
  stateTokens: Token[];
}): void;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts:102](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts#L102)

Resets the state of the predictor.

Called before the generation starts.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | { `stateTokens`: [`Token`](../type-aliases/Token.md)\[]; } |
| `__namedParameters.stateTokens` | [`Token`](../type-aliases/Token.md)\[] |

#### Returns

`void`

#### Overrides

[`TokenPredictor`](TokenPredictor.md).[`reset`](TokenPredictor.md#reset)

***

### updateInputTokens()

```ts
updateInputTokens(tokens: Token[]): void;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts:110](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts#L110)

Called with the input tokens before the generation starts when using `LlamaChatSession`, `LlamaChat`, and `LlamaCompletion`.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `tokens` | [`Token`](../type-aliases/Token.md)\[] |

#### Returns

`void`

#### Overrides

[`TokenPredictor`](TokenPredictor.md).[`updateInputTokens`](TokenPredictor.md#updateinputtokens)

***

### pushTokens()

```ts
pushTokens(tokens: Token[]): void;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts:116](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts#L116)

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
predictTokens(): Token[];
```

Defined in: [evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts:124](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts#L124)

Predicts the next tokens based on the current state.

If the generation should wait until the minimum predications are ready,
this method should return a promise that resolves when the minimum predictions are ready.

A background prediction process can be started when this function is called,
so that the next predictions will be ready when this function is called again.

#### Returns

[`Token`](../type-aliases/Token.md)\[]

#### Overrides

[`TokenPredictor`](TokenPredictor.md).[`predictTokens`](TokenPredictor.md#predicttokens)

***

### dispose()

```ts
dispose(): void;
```

Defined in: [evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts:169](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/tokenPredictors/InputLookupTokenPredictor.ts#L169)

#### Returns

`void`

#### Overrides

[`TokenPredictor`](TokenPredictor.md).[`dispose`](TokenPredictor.md#dispose)
