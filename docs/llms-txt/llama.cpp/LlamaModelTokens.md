# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaModelTokens.md

---
url: /api/classes/LlamaModelTokens.md
---
# Class: LlamaModelTokens

Defined in: [evaluator/LlamaModel/LlamaModel.ts:801](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L801)

## Accessors

### infill

#### Get Signature

```ts
get infill(): LlamaModelInfillTokens;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:826](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L826)

##### Returns

[`LlamaModelInfillTokens`](LlamaModelInfillTokens.md)

infill tokens

***

### bos

#### Get Signature

```ts
get bos(): Token | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:838](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L838)

##### Returns

[`Token`](../type-aliases/Token.md) | `null`

The BOS (Beginning Of Sequence) token.

***

### eos

#### Get Signature

```ts
get eos(): Token | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:853](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L853)

##### Returns

[`Token`](../type-aliases/Token.md) | `null`

The EOS (End Of Sequence) token.

***

### eot

#### Get Signature

```ts
get eot(): Token | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:868](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L868)

##### Returns

[`Token`](../type-aliases/Token.md) | `null`

The EOT (End Of Turn) token.

***

### sep

#### Get Signature

```ts
get sep(): Token | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:883](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L883)

##### Returns

[`Token`](../type-aliases/Token.md) | `null`

The SEP (Sentence Separator) token.

***

### nl

#### Get Signature

```ts
get nl(): Token | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:898](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L898)

##### Returns

[`Token`](../type-aliases/Token.md) | `null`

The NL (New Line) token.

***

### bosString

#### Get Signature

```ts
get bosString(): string | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:913](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L913)

##### Returns

`string` | `null`

The BOS (Beginning Of Sequence) token text representation.

***

### eosString

#### Get Signature

```ts
get eosString(): string | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:930](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L930)

##### Returns

`string` | `null`

The EOS (End Of Sequence) token text representation.

***

### eotString

#### Get Signature

```ts
get eotString(): string | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:947](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L947)

##### Returns

`string` | `null`

The EOT (End Of Turn) token text representation.

***

### sepString

#### Get Signature

```ts
get sepString(): string | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:964](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L964)

##### Returns

`string` | `null`

The SEP (Sentence Separator) token text representation.

***

### nlString

#### Get Signature

```ts
get nlString(): string | null;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:981](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L981)

##### Returns

`string` | `null`

The NL (New Line) token text representation.

***

### shouldPrependBosToken

#### Get Signature

```ts
get shouldPrependBosToken(): boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:998](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L998)

##### Returns

`boolean`

Whether we should prepend a BOS (Beginning Of Sequence) token for evaluations with this model.

***

### shouldAppendEosToken

#### Get Signature

```ts
get shouldAppendEosToken(): boolean;
```

Defined in: [evaluator/LlamaModel/LlamaModel.ts:1010](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaModel/LlamaModel.ts#L1010)

##### Returns

`boolean`

Whether we should append an EOS (End Of Sequence) token for evaluations with this model.
