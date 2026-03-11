# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaModel.md

---
url: /api/classes/LlamaModel.md
---
# Class: LlamaModel

Defined in: [evaluator/LlamaModel/LlamaModel.ts:173](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L173)

## Properties

### tokenizer

```ts
readonly tokenizer: Tokenizer;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:197](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L197)

***

### onDispose

```ts
readonly onDispose: EventRelay<void>;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:198](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L198)

## Accessors

### disposed

#### Get Signature

```ts
get disposed(): boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:305](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L305)

##### Returns

`boolean`

***

### llama

#### Get Signature

```ts
get llama(): Llama;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:309](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L309)

##### Returns

[`Llama`](Llama.md)

***

### tokens

#### Get Signature

```ts
get tokens(): LlamaModelTokens;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:313](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L313)

##### Returns

[`LlamaModelTokens`](LlamaModelTokens.md)

***

### filename

#### Get Signature

```ts
get filename(): string | undefined;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:317](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L317)

##### Returns

`string` | `undefined`

***

### fileInfo

#### Get Signature

```ts
get fileInfo(): GgufFileInfo;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:321](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L321)

##### Returns

[`GgufFileInfo`](../type-aliases/GgufFileInfo.md)

***

### fileInsights

#### Get Signature

```ts
get fileInsights(): GgufInsights;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:325](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L325)

##### Returns

[`GgufInsights`](GgufInsights.md)

***

### gpuLayers

#### Get Signature

```ts
get gpuLayers(): number;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:333](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L333)

Number of layers offloaded to the GPU.
If GPU support is disabled, this will always be `0`.

##### Returns

`number`

***

### size

#### Get Signature

```ts
get size(): number;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:342](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L342)

Total model size in memory in bytes.

When using mmap, actual memory usage may be higher than this value due to `llama.cpp`'s performance optimizations.

##### Returns

`number`

***

### flashAttentionSupported

#### Get Signature

```ts
get flashAttentionSupported(): boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:348](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L348)

##### Returns

`boolean`

***

### defaultContextFlashAttention

#### Get Signature

```ts
get defaultContextFlashAttention(): boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:352](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L352)

##### Returns

`boolean`

***

### defaultContextSwaFullCache

#### Get Signature

```ts
get defaultContextSwaFullCache(): boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:356](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L356)

##### Returns

`boolean`

***

### trainContextSize

#### Get Signature

```ts
get trainContextSize(): number;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:645](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L645)

The context size the model was trained on

##### Returns

`number`

***

### embeddingVectorSize

#### Get Signature

```ts
get embeddingVectorSize(): number;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:655](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L655)

The size of an embedding vector the model can produce

##### Returns

`number`

***

### vocabularyType

#### Get Signature

```ts
get vocabularyType(): LlamaVocabularyType;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:664](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L664)

##### Returns

[`LlamaVocabularyType`](../enumerations/LlamaVocabularyType.md)

## Methods

### dispose()

```ts
dispose(): Promise<void>;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:291](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L291)

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

***

### tokenize()

#### Call Signature

```ts
tokenize(
   text: string, 
   specialTokens?: boolean, 
   options?: "trimLeadingSpace"): Token[];
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:370](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L370)

Transform text into tokens that can be fed to the model

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `text` | `string` | the text to tokenize |
| `specialTokens?` | `boolean` | if set to true, text that correspond to special tokens will be tokenized to those tokens. For example, `<s>` will be tokenized to the BOS token if `specialTokens` is set to `true`, otherwise it will be tokenized to tokens that corresponds to the plaintext `<s>` string. |
| `options?` | `"trimLeadingSpace"` | additional options for tokenization. If set to `"trimLeadingSpace"`, a leading space will be trimmed from the tokenized output if the output has an additional space at the beginning. |

##### Returns

[`Token`](../type-aliases/Token.md)\[]

#### Call Signature

```ts
tokenize(text: BuiltinSpecialTokenValue, specialTokens: "builtin"): Token[];
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:371](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L371)

Transform text into tokens that can be fed to the model

##### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `text` | [`BuiltinSpecialTokenValue`](../type-aliases/BuiltinSpecialTokenValue.md) | the text to tokenize |
| `specialTokens` | `"builtin"` | if set to true, text that correspond to special tokens will be tokenized to those tokens. For example, `<s>` will be tokenized to the BOS token if `specialTokens` is set to `true`, otherwise it will be tokenized to tokens that corresponds to the plaintext `<s>` string. |

##### Returns

[`Token`](../type-aliases/Token.md)\[]

***

### detokenize()

```ts
detokenize(
   tokens: readonly Token[], 
   specialTokens?: boolean, 
   lastTokens?: readonly Token[]): string;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:485](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L485)

Transform tokens into text

#### Parameters

| Parameter | Type | Default value | Description |
| ------ | ------ | ------ | ------ |
| `tokens` | readonly [`Token`](../type-aliases/Token.md)\[] | `undefined` | the tokens to detokenize. |
| `specialTokens?` | `boolean` | `false` | if set to `true`, special tokens will be detokenized to their corresponding token text representation. Recommended for debugging purposes only. > **Note:** there may be additional spaces around special tokens that were not present in the original text - this is not a bug, this is [how the tokenizer is supposed to work](https://github.com/ggml-org/llama.cpp/pull/7697#issuecomment-2144003246). Defaults to `false`. |
| `lastTokens?` | readonly [`Token`](../type-aliases/Token.md)\[] | `undefined` | the last few tokens that preceded the tokens to detokenize. If provided, the last few tokens will be used to determine whether a space has to be added before the current tokens or not, and apply other detokenizer-specific heuristics to provide the correct text continuation to the existing tokens. Using it may have no effect with some models, but it is still recommended. |

#### Returns

`string`

***

### getTokenAttributes()

```ts
getTokenAttributes(token: Token): TokenAttributes;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:506](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L506)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `token` | [`Token`](../type-aliases/Token.md) |

#### Returns

[`TokenAttributes`](TokenAttributes.md)

***

### isSpecialToken()

```ts
isSpecialToken(token: Token | undefined): boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:517](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L517)

Check whether the given token is a special token (a control-type token or a token with no normal text representation)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `token` | [`Token`](../type-aliases/Token.md) | `undefined` |

#### Returns

`boolean`

***

### iterateAllTokens()

```ts
iterateAllTokens(): Generator<Token, void, unknown>;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:532](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L532)

#### Returns

[`Generator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Generator)<[`Token`](../type-aliases/Token.md), `void`, `unknown`>

***

### isEogToken()

```ts
isEogToken(token: Token | undefined): boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:545](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L545)

Check whether the given token is an EOG (End Of Generation) token, like EOS or EOT.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `token` | [`Token`](../type-aliases/Token.md) | `undefined` |

#### Returns

`boolean`

***

### createContext()

```ts
createContext(options?: LlamaContextOptions): Promise<LlamaContext>;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:552](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L552)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`LlamaContextOptions`](../type-aliases/LlamaContextOptions.md) |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`LlamaContext`](LlamaContext.md)>

***

### createEmbeddingContext()

```ts
createEmbeddingContext(options?: LlamaEmbeddingContextOptions): Promise<LlamaEmbeddingContext>;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:569](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L569)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`LlamaEmbeddingContextOptions`](../type-aliases/LlamaEmbeddingContextOptions.md) |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`LlamaEmbeddingContext`](LlamaEmbeddingContext.md)>

#### See

[Using Embedding](https://node-llama-cpp.withcat.ai/guide/embedding) tutorial

***

### createRankingContext()

```ts
createRankingContext(options?: LlamaRankingContextOptions): Promise<LlamaRankingContext>;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:579](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L579)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`LlamaRankingContextOptions`](../type-aliases/LlamaRankingContextOptions.md) |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`LlamaRankingContext`](LlamaRankingContext.md)>

#### See

[Reranking Documents](https://node-llama-cpp.withcat.ai/guide/embedding#reranking) tutorial

***

### getWarnings()

```ts
getWarnings(): string[];
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:591](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L591)

Get warnings about the model file that would affect its usage.

These warnings include all the warnings generated by `GgufInsights`, but are more comprehensive.

#### Returns

`string`\[]
