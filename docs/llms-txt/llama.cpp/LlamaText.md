# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaText.md

---
url: /api/classes/LlamaText.md
---
# Class: LlamaText

Defined in: [utils/LlamaText.ts:16](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L16)

## See

[Using `LlamaText`](https://node-llama-cpp.withcat.ai/guide/llama-text) tutorial

## Constructors

### Constructor

```ts
new LlamaText(...values: readonly LlamaTextInputValue[]): LlamaText;
```

Defined in: [utils/LlamaText.ts:22](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L22)

Can also be called without `new`

#### Parameters

| Parameter | Type |
| ------ | ------ |
| ...`values` | readonly [`LlamaTextInputValue`](../type-aliases/LlamaTextInputValue.md)\[] |

#### Returns

`LlamaText`

## Properties

### values

```ts
readonly values: readonly LlamaTextValue[];
```

Defined in: [utils/LlamaText.ts:17](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L17)

## Methods

### concat()

```ts
concat(value: LlamaTextInputValue): LlamaText;
```

Defined in: [utils/LlamaText.ts:27](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L27)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `value` | [`LlamaTextInputValue`](../type-aliases/LlamaTextInputValue.md) |

#### Returns

`LlamaText`

***

### mapValues()

```ts
mapValues(mapper: (this: readonly LlamaTextValue[], value: LlamaTextValue, index: number, values: readonly LlamaTextValue[]) => LlamaTextInputValue): LlamaText;
```

Defined in: [utils/LlamaText.ts:31](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L31)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `mapper` | (`this`: readonly [`LlamaTextValue`](../type-aliases/LlamaTextValue.md)\[], `value`: [`LlamaTextValue`](../type-aliases/LlamaTextValue.md), `index`: `number`, `values`: readonly [`LlamaTextValue`](../type-aliases/LlamaTextValue.md)\[]) => [`LlamaTextInputValue`](../type-aliases/LlamaTextInputValue.md) |

#### Returns

`LlamaText`

***

### joinValues()

```ts
joinValues(separator: LlamaTextValue | LlamaText): LlamaText;
```

Defined in: [utils/LlamaText.ts:51](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L51)

Joins the values with the given separator.

Note that the values are squashed when they are loaded into the `LlamaText`, so the separator is not added between adjacent strings.

To add the separator on values before squashing them, use `LlamaText.joinValues` instead.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `separator` | [`LlamaTextValue`](../type-aliases/LlamaTextValue.md) | `LlamaText` |

#### Returns

`LlamaText`

***

### toString()

```ts
toString(): string;
```

Defined in: [utils/LlamaText.ts:68](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L68)

#### Returns

`string`

***

### toJSON()

```ts
toJSON(): LlamaTextJSON;
```

Defined in: [utils/LlamaText.ts:81](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L81)

#### Returns

[`LlamaTextJSON`](../type-aliases/LlamaTextJSON.md)

***

### tokenize()

```ts
tokenize(tokenizer: Tokenizer, options?: "trimLeadingSpace"): Token[];
```

Defined in: [utils/LlamaText.ts:97](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L97)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `tokenizer` | [`Tokenizer`](../type-aliases/Tokenizer.md) |
| `options?` | `"trimLeadingSpace"` |

#### Returns

[`Token`](../type-aliases/Token.md)\[]

***

### compare()

```ts
compare(other: LlamaText): boolean;
```

Defined in: [utils/LlamaText.ts:121](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L121)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `other` | `LlamaText` |

#### Returns

`boolean`

***

### trimStart()

```ts
trimStart(): LlamaText;
```

Defined in: [utils/LlamaText.ts:125](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L125)

#### Returns

`LlamaText`

***

### trimEnd()

```ts
trimEnd(): LlamaText;
```

Defined in: [utils/LlamaText.ts:163](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L163)

#### Returns

`LlamaText`

***

### includes()

```ts
includes(value: LlamaText): boolean;
```

Defined in: [utils/LlamaText.ts:201](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L201)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `value` | `LlamaText` |

#### Returns

`boolean`

***

### fromJSON()

```ts
static fromJSON(json: LlamaTextJSON): LlamaText;
```

Defined in: [utils/LlamaText.ts:268](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L268)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `json` | [`LlamaTextJSON`](../type-aliases/LlamaTextJSON.md) |

#### Returns

`LlamaText`

***

### compare()

```ts
static compare(a: LlamaText, b: LlamaText): boolean;
```

Defined in: [utils/LlamaText.ts:290](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L290)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `a` | `LlamaText` |
| `b` | `LlamaText` |

#### Returns

`boolean`

***

### fromTokens()

```ts
static fromTokens(tokenizer: Tokenizer, tokens: Token[]): LlamaText;
```

Defined in: [utils/LlamaText.ts:312](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L312)

Attempt to convert tokens to a `LlamaText` while preserving special tokens.

Non-standard special tokens that don't have a text representation are ignored.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `tokenizer` | [`Tokenizer`](../type-aliases/Tokenizer.md) |
| `tokens` | [`Token`](../type-aliases/Token.md)\[] |

#### Returns

`LlamaText`

***

### joinValues()

```ts
static joinValues(separator: string | LlamaText, values: readonly LlamaTextInputValue[]): LlamaText;
```

Defined in: [utils/LlamaText.ts:365](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L365)

Join values with the given separator before squashing adjacent strings inside the values

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `separator` | `string` | `LlamaText` |
| `values` | readonly [`LlamaTextInputValue`](../type-aliases/LlamaTextInputValue.md)\[] |

#### Returns

`LlamaText`

***

### isLlamaText()

```ts
static isLlamaText(value: unknown): value is LlamaText;
```

Defined in: [utils/LlamaText.ts:382](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L382)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `value` | `unknown` |

#### Returns

`value is LlamaText`
