# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaRankingContext.md

---
url: /api/classes/LlamaRankingContext.md
---
# Class: LlamaRankingContext

Defined in: [evaluator/LlamaRankingContext.ts:68](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L68)

## See

[Reranking Documents](https://node-llama-cpp.withcat.ai/guide/embedding#reranking) tutorial

## Properties

### onDispose

```ts
readonly onDispose: EventRelay<void>;
```

Defined in: [evaluator/LlamaRankingContext.ts:74](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L74)

## Accessors

### disposed

#### Get Signature

```ts
get disposed(): boolean;
```

Defined in: [evaluator/LlamaRankingContext.ts:170](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L170)

##### Returns

`boolean`

***

### model

#### Get Signature

```ts
get model(): LlamaModel;
```

Defined in: [evaluator/LlamaRankingContext.ts:174](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L174)

##### Returns

[`LlamaModel`](LlamaModel.md)

## Methods

### rank()

```ts
rank(query: 
  | string
  | LlamaText
  | Token[], document: 
  | string
  | LlamaText
  | Token[]): Promise<number>;
```

Defined in: [evaluator/LlamaRankingContext.ts:104](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L104)

Get the ranking score for a document for a query.

A ranking score is a number between 0 and 1 representing the probability that the document is relevant to the query.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `query` | | `string` | [`LlamaText`](LlamaText.md) | [`Token`](../type-aliases/Token.md)\[] |
| `document` | | `string` | [`LlamaText`](LlamaText.md) | [`Token`](../type-aliases/Token.md)\[] |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`number`>

a ranking score between 0 and 1 representing the probability that the document is relevant to the query.

***

### rankAll()

```ts
rankAll(query: 
  | string
  | LlamaText
  | Token[], documents: (
  | string
  | LlamaText
  | Token[])[]): Promise<number[]>;
```

Defined in: [evaluator/LlamaRankingContext.ts:123](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L123)

Get the ranking scores for all the given documents for a query.

A ranking score is a number between 0 and 1 representing the probability that the document is relevant to the query.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `query` | | `string` | [`LlamaText`](LlamaText.md) | [`Token`](../type-aliases/Token.md)\[] |
| `documents` | ( | `string` | [`LlamaText`](LlamaText.md) | [`Token`](../type-aliases/Token.md)\[])\[] |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`number`\[]>

an array of ranking scores between 0 and 1 representing the probability that the document is relevant to the query.

***

### rankAndSort()

```ts
rankAndSort<T>(query: 
  | string
  | LlamaText
  | Token[], documents: T[]): Promise<{
  document: T;
  score: number;
}[]>;
```

Defined in: [evaluator/LlamaRankingContext.ts:146](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L146)

Get the ranking scores for all the given documents for a query and sort them by score from highest to lowest.

A ranking score is a number between 0 and 1 representing the probability that the document is relevant to the query.

#### Type Parameters

| Type Parameter |
| ------ |
| `T` *extends* `string` |

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `query` | | `string` | [`LlamaText`](LlamaText.md) | [`Token`](../type-aliases/Token.md)\[] |
| `documents` | `T`\[] |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{
`document`: `T`;
`score`: `number`;
}\[]>

***

### dispose()

```ts
dispose(): Promise<void>;
```

Defined in: [evaluator/LlamaRankingContext.ts:161](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaRankingContext.ts#L161)

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>
