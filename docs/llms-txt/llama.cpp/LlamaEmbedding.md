# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaEmbedding.md

---
url: /api/classes/LlamaEmbedding.md
---
# Class: LlamaEmbedding

Defined in: [evaluator/LlamaEmbedding.ts:10](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbedding.ts#L10)

## Constructors

### Constructor

```ts
new LlamaEmbedding(options: LlamaEmbeddingOptions): LlamaEmbedding;
```

Defined in: [evaluator/LlamaEmbedding.ts:13](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbedding.ts#L13)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`LlamaEmbeddingOptions`](../type-aliases/LlamaEmbeddingOptions.md) |

#### Returns

`LlamaEmbedding`

## Properties

### vector

```ts
readonly vector: readonly number[];
```

Defined in: [evaluator/LlamaEmbedding.ts:11](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbedding.ts#L11)

## Methods

### toJSON()

```ts
toJSON(): LlamaEmbeddingJSON;
```

Defined in: [evaluator/LlamaEmbedding.ts:17](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbedding.ts#L17)

#### Returns

[`LlamaEmbeddingJSON`](../type-aliases/LlamaEmbeddingJSON.md)

***

### calculateCosineSimilarity()

```ts
calculateCosineSimilarity(other: 
  | readonly number[]
  | LlamaEmbeddingJSON
  | LlamaEmbedding): number;
```

Defined in: [evaluator/LlamaEmbedding.ts:31](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbedding.ts#L31)

Calculates the cosine similarity between this embedding and another embedding.

Note that you should only compare embeddings created by the exact same model file.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `other` | | readonly `number`\[] | [`LlamaEmbeddingJSON`](../type-aliases/LlamaEmbeddingJSON.md) | `LlamaEmbedding` |

#### Returns

`number`

A value between 0 and 1 representing the similarity between the embedding vectors,
where 1 means the embeddings are identical.

***

### fromJSON()

```ts
static fromJSON(json: LlamaEmbeddingJSON): LlamaEmbedding;
```

Defined in: [evaluator/LlamaEmbedding.ts:65](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaEmbedding.ts#L65)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `json` | [`LlamaEmbeddingJSON`](../type-aliases/LlamaEmbeddingJSON.md) |

#### Returns

`LlamaEmbedding`
