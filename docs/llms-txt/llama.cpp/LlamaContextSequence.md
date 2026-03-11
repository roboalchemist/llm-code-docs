# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaContextSequence.md

---
url: /api/classes/LlamaContextSequence.md
---
# Class: LlamaContextSequence

Defined in: [evaluator/LlamaContext/LlamaContext.ts:934](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L934)

## Properties

### onDispose

```ts
readonly onDispose: EventRelay<void>;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:957](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L957)

## Accessors

### disposed

#### Get Signature

```ts
get disposed(): boolean;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1009](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1009)

##### Returns

`boolean`

***

### context

#### Get Signature

```ts
get context(): LlamaContext;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1013](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1013)

##### Returns

[`LlamaContext`](LlamaContext.md)

***

### model

#### Get Signature

```ts
get model(): LlamaModel;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1017](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1017)

##### Returns

[`LlamaModel`](LlamaModel.md)

***

### contextSize

#### Get Signature

```ts
get contextSize(): number;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1022](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1022)

The maximum number of tokens that the sequence state can hold

##### Returns

`number`

***

### nextTokenIndex

#### Get Signature

```ts
get nextTokenIndex(): number;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1027](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1027)

The index where the next evaluated token will be placed in the context

##### Returns

`number`

***

### contextTokens

#### Get Signature

```ts
get contextTokens(): Token[];
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1032](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1032)

The current context state tokens

##### Returns

[`Token`](../type-aliases/Token.md)\[]

***

### tokenMeter

#### Get Signature

```ts
get tokenMeter(): TokenMeter;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1039](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1039)

##### Returns

[`TokenMeter`](TokenMeter.md)

***

### tokenPredictor

#### Get Signature

```ts
get tokenPredictor(): TokenPredictor | undefined;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1046](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1046)

The token predictor used when creating this sequence.

##### Returns

[`TokenPredictor`](TokenPredictor.md) | `undefined`

***

### stateCellsStartIndex

#### Get Signature

```ts
get stateCellsStartIndex(): number;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1069](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1069)

Get the index of the first token in the KV cache.

If you remove any tokens from the state that come before this index,
no cached prefix tokens evaluation state will be used for the next evaluation.

For example, if `stateCellsStartIndex` is `10` and you remove the range `{start: 11, end: 16}`
then the cached state for range `0-10` will be used in the next evaluation,
but if you remove the range `{start: 10, end: 16}` (or `{start: 9, end: 16}`) then the cached state will not be used at all
and will be re-evaluated in the next evaluation.

This index can be greater than `0` only when SWA (Sliding Window Attention) is used (only on supported models).

When SWA is used, this index will usually be `Math.max(-1, .nextTokenIndex - .model.fileInsights.swaSize)` or larger.

When the KV cache is empty, this index will be `-1`.

You can disable SWA by setting the `swaFullCache` option to `true` when creating a context.

##### Returns

`number`

***

### tokenPredictions

#### Get Signature

```ts
get tokenPredictions(): {
  used: number;
  unused: number;
  validated: number;
  refuted: number;
};
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1084](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1084)

Statistics of token predictions using the sequence's `tokenPredictor`.

The statistics change only when token prediction is used in this sequence.

`validated` + `refuted` = total number of evaluated predictions.

Prefer using `validated` and `refuted` to evaluate the effectiveness of token prediction.

##### Returns

###### used

```ts
used: number;
```

Number of token predictions that were actually used (tokens that were validated and then consumed)

###### unused

```ts
unused: number;
```

Number of token predictions that were not used (tokens that were validated and were not consumed)

###### validated

```ts
validated: number;
```

Number of token predictions that were validated successfully

###### refuted

```ts
refuted: number;
```

Number of token predictions that were refuted

***

### isLoadedToMemory

#### Get Signature

```ts
get isLoadedToMemory(): boolean;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1105](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1105)

##### Returns

`boolean`

## Methods

### dispose()

```ts
dispose(): void;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:993](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L993)

#### Returns

`void`

***

### compareContextTokens()

```ts
compareContextTokens(tokens: Token[]): {
  firstDifferentIndex: number;
};
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1109](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1109)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `tokens` | [`Token`](../type-aliases/Token.md)\[] |

#### Returns

```ts
{
  firstDifferentIndex: number;
}
```

##### firstDifferentIndex

```ts
firstDifferentIndex: number;
```

***

### adaptStateToTokens()

```ts
adaptStateToTokens(tokens: Token[], allowShift?: boolean): Promise<void>;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1136](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1136)

Erase parts of the context state to align it with the given tokens.

If the given tokens do not align with the current context state, the context state will be erased to align with the given tokens.

To find the first different token index between the context state and the given tokens, access the `nextTokenIndex` property.

If `allowShift` is `true` (the default), shifting tokens may happen to align the context state with the given tokens,
which incurs token evaluation of the shifted tokens.

#### Parameters

| Parameter | Type | Default value |
| ------ | ------ | ------ |
| `tokens` | [`Token`](../type-aliases/Token.md)\[] | `undefined` |
| `allowShift` | `boolean` | `true` |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

***

### clearHistory()

```ts
clearHistory(): Promise<void>;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1187](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1187)

Clear the history of the sequence.

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

***

### eraseContextTokenRanges()

```ts
eraseContextTokenRanges(ranges: ContextTokensDeleteRange[]): Promise<void>;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1198](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1198)

Erase context tokens in the provided ranges to free up space for new tokens to be generated.
The start of each range is inclusive, and the end of each range is exclusive.
For example, the range `{start: 0, end: 1}` will remove the token at the `0` index only.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `ranges` | [`ContextTokensDeleteRange`](../type-aliases/ContextTokensDeleteRange.md)\[] |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

***

### evaluate()

```ts
evaluate(tokens: Token[], options?: SequenceEvaluateOptions): AsyncGenerator<Token, void, 
  | void
  | Token
  | Token[]>;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1335](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1335)

Evaluate the provided tokens into the context sequence, and continue generating new tokens on iterator iterations.

This method uses the token predictor (when provided) to generate new tokens faster.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `tokens` | [`Token`](../type-aliases/Token.md)\[] |
| `options` | [`SequenceEvaluateOptions`](../type-aliases/SequenceEvaluateOptions.md) |

#### Returns

[`AsyncGenerator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator)<[`Token`](../type-aliases/Token.md), `void`,
| `void`
| [`Token`](../type-aliases/Token.md)
| [`Token`](../type-aliases/Token.md)\[]>

***

### evaluateWithMetadata()

```ts
evaluateWithMetadata<Metadata>(
   tokens: Token[], 
   metadata: Metadata, 
   options?: SequenceEvaluateOptions): AsyncGenerator<SequenceEvaluateOutput<Metadata>, void, 
  | void
  | Token
  | Token[]>;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1357](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1357)

Like [\`.evaluate(...)\`](#evaluate), but with additional metadata for each generated token.

Configure the additional metadata options to choose which metadata to include.

#### Type Parameters

| Type Parameter |
| ------ |
| `Metadata` *extends* [`SequenceEvaluateMetadataOptions`](../type-aliases/SequenceEvaluateMetadataOptions.md) |

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `tokens` | [`Token`](../type-aliases/Token.md)\[] |
| `metadata` | `Metadata` |
| `options` | [`SequenceEvaluateOptions`](../type-aliases/SequenceEvaluateOptions.md) |

#### Returns

[`AsyncGenerator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator)<[`SequenceEvaluateOutput`](../type-aliases/SequenceEvaluateOutput.md)<`Metadata`>, `void`,
| `void`
| [`Token`](../type-aliases/Token.md)
| [`Token`](../type-aliases/Token.md)\[]>

***

### evaluateWithoutGeneratingNewTokens()

```ts
evaluateWithoutGeneratingNewTokens(tokens: Token[], options?: {
  evaluationPriority?: EvaluationPriority;
  contextShift?: ContextShiftOptions;
}): Promise<void>;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1429](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1429)

Evaluate the provided tokens into the context sequence without generating new tokens.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `tokens` | [`Token`](../type-aliases/Token.md)\[] | - |
| `options` | { `evaluationPriority?`: [`EvaluationPriority`](../type-aliases/EvaluationPriority.md); `contextShift?`: [`ContextShiftOptions`](../type-aliases/ContextShiftOptions.md); } | - |
| `options.evaluationPriority?` | [`EvaluationPriority`](../type-aliases/EvaluationPriority.md) | When a lot of tokens are queued for the next batch, more than the configured `batchSize`, the tokens for each sequence will be evaluated based on the strategy chosen for the context. By default, the `"maximumParallelism"` strategy is used, which will try to evaluate as many sequences in parallel as possible, but at some point, it'll have to choose which sequences to evaluate more tokens of, so it'll prioritize the sequences with the highest evaluation priority. Also, a custom strategy can be used to prioritize the sequences differently, but generally, the higher the evaluation priority is, the more likely and more tokens will be evaluated for that sequence in the next queued batch. |
| `options.contextShift?` | [`ContextShiftOptions`](../type-aliases/ContextShiftOptions.md) | Override the sequence context shift options for this evaluation |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

***

### controlledEvaluate()

```ts
controlledEvaluate(input: ControlledEvaluateInputItem[], options?: {
  evaluationPriority?: EvaluationPriority;
  contextShift?: ContextShiftOptions;
  onTokenResult?: void;
}): Promise<(
  | ControlledEvaluateIndexOutput
  | undefined)[]>;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1511](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1511)

Evaluate the provided tokens into the context sequence with custom options for each token.

This method allows for more precise control of the generation process.

A next token will be generated for a given token only if any of the `generateNext` options for it are used.

To generate more tokens after this method finishes,
use it again with token(s) you selected to add to the context from the previous evaluation.

This method doesn't use the token predictor (when provided) since it cannot predict which tokens are actually needed.
Use the `evaluate` method when you need to use token prediction.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `input` | [`ControlledEvaluateInputItem`](../type-aliases/ControlledEvaluateInputItem.md)\[] | - |
| `options?` | { `evaluationPriority?`: [`EvaluationPriority`](../type-aliases/EvaluationPriority.md); `contextShift?`: [`ContextShiftOptions`](../type-aliases/ContextShiftOptions.md); `onTokenResult?`: `void`; } | - |
| `options.evaluationPriority?` | [`EvaluationPriority`](../type-aliases/EvaluationPriority.md) | When a lot of tokens are queued for the next batch, more than the configured `batchSize`, the tokens for each sequence will be evaluated based on the strategy chosen for the context. By default, the `"maximumParallelism"` strategy is used, which will try to evaluate as many sequences in parallel as possible, but at some point, it'll have to choose which sequences to evaluate more tokens of, so it'll prioritize the sequences with the highest evaluation priority. Also, a custom strategy can be used to prioritize the sequences differently, but generally, the higher the evaluation priority is, the more likely and more tokens will be evaluated for that sequence in the next queued batch. |
| `options.contextShift?` | [`ContextShiftOptions`](../type-aliases/ContextShiftOptions.md) | Override the sequence context shift options for this evaluation |
| `options.onTokenResult?` | - |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<(
| [`ControlledEvaluateIndexOutput`](../type-aliases/ControlledEvaluateIndexOutput.md)
| `undefined`)\[]>

An array where for each token in the input array, there can be an output item at the same index in the output array.
For indexes that have no output, there won't be any value at the corresponding index in the output array.

It's recommended to iterate from `0` up to the length of the input array to check the results in the output array.

***

### saveStateToFile()

```ts
saveStateToFile(filePath: string): Promise<{
  fileSize: number;
}>;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1644](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1644)

Save the current context sequence evaluation state to a file.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `filePath` | `string` |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{
`fileSize`: `number`;
}>

#### See

[Saving and restoring a context sequence evaluation state](https://node-llama-cpp.withcat.ai/guide/chat-session#save-and-restore-with-context-sequence-state)

***

### loadStateFromFile()

```ts
loadStateFromFile(filePath: string, acceptRisk: {
  acceptRisk: true;
}): Promise<void>;
```

Defined in: [evaluator/LlamaContext/LlamaContext.ts:1677](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaContext/LlamaContext.ts#L1677)

Load a context sequence evaluation state from a file.

Trying to load a state file with a longer context size than the current sequence's context size will fail and throw an error.

You must ensure that the file was created from the exact same model, otherwise, using this function may crash the process.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `filePath` | `string` | - |
| `acceptRisk` | { `acceptRisk`: `true`; } | - |
| `acceptRisk.acceptRisk` | `true` | Loading a state file created using a different model may crash the process. You must accept this risk to use this feature. |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

#### See

[Saving and restoring a context sequence evaluation state](https://node-llama-cpp.withcat.ai/guide/chat-session#save-and-restore-with-context-sequence-state)
