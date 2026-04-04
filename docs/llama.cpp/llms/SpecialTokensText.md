# Source: https://node-llama-cpp.withcat.ai/api/classes/SpecialTokensText.md

---
url: /api/classes/SpecialTokensText.md
---
# Class: SpecialTokensText

Defined in: [utils/LlamaText.ts:433](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L433)

## Constructors

### Constructor

```ts
new SpecialTokensText(value: string): SpecialTokensText;
```

Defined in: [utils/LlamaText.ts:436](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L436)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `value` | `string` |

#### Returns

`SpecialTokensText`

## Properties

### value

```ts
readonly value: string;
```

Defined in: [utils/LlamaText.ts:434](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L434)

## Methods

### toString()

```ts
toString(): string;
```

Defined in: [utils/LlamaText.ts:440](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L440)

#### Returns

`string`

***

### tokenize()

```ts
tokenize(tokenizer: Tokenizer, trimLeadingSpace?: boolean): Token[];
```

Defined in: [utils/LlamaText.ts:444](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L444)

#### Parameters

| Parameter | Type | Default value |
| ------ | ------ | ------ |
| `tokenizer` | [`Tokenizer`](../type-aliases/Tokenizer.md) | `undefined` |
| `trimLeadingSpace` | `boolean` | `false` |

#### Returns

[`Token`](../type-aliases/Token.md)\[]

***

### tokenizeSpecialTokensOnly()

```ts
tokenizeSpecialTokensOnly(tokenizer: Tokenizer): (string | Token)[];
```

Defined in: [utils/LlamaText.ts:448](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L448)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `tokenizer` | [`Tokenizer`](../type-aliases/Tokenizer.md) |

#### Returns

(`string` | [`Token`](../type-aliases/Token.md))\[]

***

### toJSON()

```ts
toJSON(): LlamaTextSpecialTokensTextJSON;
```

Defined in: [utils/LlamaText.ts:471](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L471)

#### Returns

[`LlamaTextSpecialTokensTextJSON`](../type-aliases/LlamaTextSpecialTokensTextJSON.md)

***

### fromJSON()

```ts
static fromJSON(json: LlamaTextSpecialTokensTextJSON): SpecialTokensText;
```

Defined in: [utils/LlamaText.ts:495](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L495)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `json` | [`LlamaTextSpecialTokensTextJSON`](../type-aliases/LlamaTextSpecialTokensTextJSON.md) |

#### Returns

`SpecialTokensText`

***

### isSpecialTokensTextJSON()

```ts
static isSpecialTokensTextJSON(value: LlamaTextJSONValue): value is LlamaTextSpecialTokensTextJSON;
```

Defined in: [utils/LlamaText.ts:502](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L502)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `value` | [`LlamaTextJSONValue`](../type-aliases/LlamaTextJSONValue.md) |

#### Returns

`value is LlamaTextSpecialTokensTextJSON`

***

### wrapIf()

```ts
static wrapIf(shouldWrap: boolean, value: string): string | SpecialTokensText;
```

Defined in: [utils/LlamaText.ts:509](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L509)

Wraps the value with a `SpecialTokensText` only if `shouldWrap` is true

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `shouldWrap` | `boolean` |
| `value` | `string` |

#### Returns

`string` | `SpecialTokensText`
