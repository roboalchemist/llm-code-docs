# Source: https://node-llama-cpp.withcat.ai/api/classes/TokenPredictor.md

---
url: /api/classes/TokenPredictor.md
---
# Abstract Class: TokenPredictor

Defined in: [evaluator/LlamaContext/TokenPredictor.ts:8](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/TokenPredictor.ts#L8)

## See

[Using Token Predictors](https://node-llama-cpp.withcat.ai/guide/token-prediction#custom)

## Extended by

* [`DraftSequenceTokenPredictor`](DraftSequenceTokenPredictor.md)
* [`InputLookupTokenPredictor`](InputLookupTokenPredictor.md)

## Constructors

### Constructor

```ts
new TokenPredictor(): TokenPredictor;
```

#### Returns

`TokenPredictor`

## Methods

### reset()

```ts
abstract reset(params: {
  targetSequence: LlamaContextSequence;
  stateTokens: Token[];
  evaluateOptions: Readonly<SequenceEvaluateOptions>;
}): 
  | void
  | Promise<void>;
```

Defined in: [evaluator/LlamaContext/TokenPredictor.ts:14](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/TokenPredictor.ts#L14)

Resets the state of the predictor.

Called before the generation starts.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `params` | { `targetSequence`: [`LlamaContextSequence`](LlamaContextSequence.md); `stateTokens`: [`Token`](../type-aliases/Token.md)\[]; `evaluateOptions`: [`Readonly`](https://www.typescriptlang.org/docs/handbook/utility-types.html#readonlytype)<[`SequenceEvaluateOptions`](../type-aliases/SequenceEvaluateOptions.md)>; } | - |
| `params.targetSequence` | [`LlamaContextSequence`](LlamaContextSequence.md) | The target sequence that this token predictor is generating tokens for |
| `params.stateTokens` | [`Token`](../type-aliases/Token.md)\[] | The tokens that are or will be loaded into the state. The initial predictions should be based on these tokens. When additional tokens are pushed into the state, the `pushTokens` method will be called with those tokens. |
| `params.evaluateOptions` | [`Readonly`](https://www.typescriptlang.org/docs/handbook/utility-types.html#readonlytype)<[`SequenceEvaluateOptions`](../type-aliases/SequenceEvaluateOptions.md)> | Options used for the evaluation on the target sequence. The `grammarEvaluationState` is cloned before being passed to the token predictor, so it can be modified without affecting the original state. |

#### Returns

| `void`
| [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

***

### pushTokens()

```ts
abstract pushTokens(tokens: Token[]): void;
```

Defined in: [evaluator/LlamaContext/TokenPredictor.ts:35](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/TokenPredictor.ts#L35)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `tokens` | [`Token`](../type-aliases/Token.md)\[] |

#### Returns

`void`

***

### predictTokens()

```ts
abstract predictTokens(): 
  | Token[]
  | Promise<Token[]>;
```

Defined in: [evaluator/LlamaContext/TokenPredictor.ts:46](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/TokenPredictor.ts#L46)

Predicts the next tokens based on the current state.

If the generation should wait until the minimum predications are ready,
this method should return a promise that resolves when the minimum predictions are ready.

A background prediction process can be started when this function is called,
so that the next predictions will be ready when this function is called again.

#### Returns

| [`Token`](../type-aliases/Token.md)\[]
| [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`Token`](../type-aliases/Token.md)\[]>

***

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

***

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

***

### dispose()

```ts
dispose(): 
  | void
  | Promise<void>;
```

Defined in: [evaluator/LlamaContext/TokenPredictor.ts:59](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/TokenPredictor.ts#L59)

#### Returns

| `void`
| [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>
