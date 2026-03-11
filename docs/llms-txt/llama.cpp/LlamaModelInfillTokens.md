# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaModelInfillTokens.md

---
url: /api/classes/LlamaModelInfillTokens.md
---
# Class: LlamaModelInfillTokens

Defined in: [evaluator/LlamaModel/LlamaModel.ts:1031](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L1031)

## Accessors

### prefix

#### Get Signature

```ts
get prefix(): Token | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:1049](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L1049)

##### Returns

[`Token`](../type-aliases/Token.md) | `null`

The beginning of infill prefix token.

***

### middle

#### Get Signature

```ts
get middle(): Token | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:1064](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L1064)

##### Returns

[`Token`](../type-aliases/Token.md) | `null`

The beginning of infill middle token.

***

### suffix

#### Get Signature

```ts
get suffix(): Token | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:1079](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L1079)

##### Returns

[`Token`](../type-aliases/Token.md) | `null`

The beginning of infill suffix token.

***

### prefixString

#### Get Signature

```ts
get prefixString(): string | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:1094](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L1094)

##### Returns

`string` | `null`

The beginning of infill prefix token as a string.

***

### middleString

#### Get Signature

```ts
get middleString(): string | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:1111](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L1111)

##### Returns

`string` | `null`

The beginning of infill middle token as a string.

***

### suffixString

#### Get Signature

```ts
get suffixString(): string | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:1128](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L1128)

##### Returns

`string` | `null`

The beginning of infill suffix token as a string.
