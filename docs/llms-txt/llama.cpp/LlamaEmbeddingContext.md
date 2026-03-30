# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaEmbeddingContext.md

---
url: /api/classes/LlamaEmbeddingContext.md
---
# Class: LlamaEmbeddingContext

Defined in: [evaluator/LlamaEmbeddingContext.ts:52](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbeddingContext.ts#L52)

## See

[Using Embedding](https://node-llama-cpp.withcat.ai/guide/embedding) tutorial

## Properties

### onDispose

```ts
readonly onDispose: EventRelay<void>;
```

Defined in: [evaluator/LlamaEmbeddingContext.ts:57](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbeddingContext.ts#L57)

## Accessors

### disposed

#### Get Signature

```ts
get disposed(): boolean;
```

Defined in: [evaluator/LlamaEmbeddingContext.ts:129](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbeddingContext.ts#L129)

##### Returns

`boolean`

***

### model

#### Get Signature

```ts
get model(): LlamaModel;
```

Defined in: [evaluator/LlamaEmbeddingContext.ts:133](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbeddingContext.ts#L133)

##### Returns

[`LlamaModel`](LlamaModel.md)

## Methods

### getEmbeddingFor()

```ts
getEmbeddingFor(input: 
  | string
  | LlamaText
  | Token[]): Promise<LlamaEmbedding>;
```

Defined in: [evaluator/LlamaEmbeddingContext.ts:78](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbeddingContext.ts#L78)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `input` | | `string` | [`LlamaText`](LlamaText.md) | [`Token`](../type-aliases/Token.md)\[] |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`LlamaEmbedding`](LlamaEmbedding.md)>

***

### dispose()

```ts
dispose(): Promise<void>;
```

Defined in: [evaluator/LlamaEmbeddingContext.ts:120](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbeddingContext.ts#L120)

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>
