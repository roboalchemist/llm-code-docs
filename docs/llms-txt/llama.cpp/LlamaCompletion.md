# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaCompletion.md

---
url: /api/classes/LlamaCompletion.md
---
# Class: LlamaCompletion

Defined in: [evaluator/LlamaCompletion.ts:234](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L234)

## See

[Text Completion](https://node-llama-cpp.withcat.ai/guide/text-completion) tutorial

## Constructors

### Constructor

```ts
new LlamaCompletion(__namedParameters: LlamaCompletionOptions): LlamaCompletion;
```

Defined in: [evaluator/LlamaCompletion.ts:240](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L240)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | [`LlamaCompletionOptions`](../type-aliases/LlamaCompletionOptions.md) |

#### Returns

`LlamaCompletion`

## Properties

### onDispose

```ts
readonly onDispose: EventRelay<void>;
```

Defined in: [evaluator/LlamaCompletion.ts:238](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L238)

## Accessors

### disposed

#### Get Signature

```ts
get disposed(): boolean;
```

Defined in: [evaluator/LlamaCompletion.ts:272](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L272)

##### Returns

`boolean`

***

### infillSupported

#### Get Signature

```ts
get infillSupported(): boolean;
```

Defined in: [evaluator/LlamaCompletion.ts:276](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L276)

##### Returns

`boolean`

## Methods

### dispose()

```ts
dispose(__namedParameters?: {
  disposeSequence?: boolean;
}): void;
```

Defined in: [evaluator/LlamaCompletion.ts:255](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L255)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | { `disposeSequence?`: `boolean`; } |
| `__namedParameters.disposeSequence?` | `boolean` |

#### Returns

`void`

***

### generateCompletion()

```ts
generateCompletion(input: 
  | string
  | LlamaText
  | Token[], options?: LlamaCompletionGenerationOptions): Promise<string>;
```

Defined in: [evaluator/LlamaCompletion.ts:287](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L287)

Generate a completion for an input.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `input` | | `string` | [`LlamaText`](LlamaText.md) | [`Token`](../type-aliases/Token.md)\[] |
| `options` | [`LlamaCompletionGenerationOptions`](../type-aliases/LlamaCompletionGenerationOptions.md) |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`string`>

***

### generateCompletionWithMeta()

```ts
generateCompletionWithMeta(input: 
  | string
  | LlamaText
  | Token[], __namedParameters?: LlamaCompletionGenerationOptions): Promise<LlamaCompletionResponse>;
```

Defined in: [evaluator/LlamaCompletion.ts:297](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L297)

Same as `generateCompletion`, but returns additional metadata about the generation.
See `generateCompletion` for more information.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `input` | | `string` | [`LlamaText`](LlamaText.md) | [`Token`](../type-aliases/Token.md)\[] |
| `__namedParameters` | [`LlamaCompletionGenerationOptions`](../type-aliases/LlamaCompletionGenerationOptions.md) |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`LlamaCompletionResponse`](../type-aliases/LlamaCompletionResponse.md)>

***

### generateInfillCompletion()

```ts
generateInfillCompletion(
   prefixInput: 
  | string
  | LlamaText
  | Token[], 
   suffixInput: 
  | string
  | LlamaText
  | Token[], 
   options?: LlamaInfillGenerationOptions): Promise<string>;
```

Defined in: [evaluator/LlamaCompletion.ts:429](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L429)

Infill (also known as Fill-In-Middle), generates a completion for an input (`prefixInput`) that
should connect to a given continuation (`suffixInput`).
For example, for `prefixInput: "123"` and `suffixInput: "789"`, the model is expected to generate `456`
to make the final text be `123456789`.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `prefixInput` | | `string` | [`LlamaText`](LlamaText.md) | [`Token`](../type-aliases/Token.md)\[] |
| `suffixInput` | | `string` | [`LlamaText`](LlamaText.md) | [`Token`](../type-aliases/Token.md)\[] |
| `options` | [`LlamaInfillGenerationOptions`](../type-aliases/LlamaInfillGenerationOptions.md) |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`string`>

***

### generateInfillCompletionWithMeta()

```ts
generateInfillCompletionWithMeta(
   prefixInput: 
  | string
  | LlamaText
  | Token[], 
   suffixInput: 
  | string
  | LlamaText
  | Token[], 
   __namedParameters?: LlamaInfillGenerationOptions): Promise<LlamaCompletionResponse>;
```

Defined in: [evaluator/LlamaCompletion.ts:443](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaCompletion.ts#L443)

Same as `generateInfillCompletion`, but returns additional metadata about the generation.
See `generateInfillCompletion` for more information.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `prefixInput` | | `string` | [`LlamaText`](LlamaText.md) | [`Token`](../type-aliases/Token.md)\[] |
| `suffixInput` | | `string` | [`LlamaText`](LlamaText.md) | [`Token`](../type-aliases/Token.md)\[] |
| `__namedParameters` | [`LlamaInfillGenerationOptions`](../type-aliases/LlamaInfillGenerationOptions.md) |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`LlamaCompletionResponse`](../type-aliases/LlamaCompletionResponse.md)>
