# Source: https://node-llama-cpp.withcat.ai/api/classes/SpecialToken.md

---
url: /api/classes/SpecialToken.md
---
# Class: SpecialToken

Defined in: [utils/LlamaText.ts:518](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L518)

## Constructors

### Constructor

```ts
new SpecialToken(value: BuiltinSpecialTokenValue): SpecialToken;
```

Defined in: [utils/LlamaText.ts:521](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L521)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `value` | [`BuiltinSpecialTokenValue`](../type-aliases/BuiltinSpecialTokenValue.md) |

#### Returns

`SpecialToken`

## Properties

### value

```ts
readonly value: BuiltinSpecialTokenValue;
```

Defined in: [utils/LlamaText.ts:519](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L519)

## Methods

### toString()

```ts
toString(): BuiltinSpecialTokenValue;
```

Defined in: [utils/LlamaText.ts:525](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L525)

#### Returns

[`BuiltinSpecialTokenValue`](../type-aliases/BuiltinSpecialTokenValue.md)

***

### tokenize()

```ts
tokenize(tokenizer: Tokenizer): Token[];
```

Defined in: [utils/LlamaText.ts:529](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L529)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `tokenizer` | [`Tokenizer`](../type-aliases/Tokenizer.md) |

#### Returns

[`Token`](../type-aliases/Token.md)\[]

***

### toJSON()

```ts
toJSON(): LlamaTextSpecialTokenJSON;
```

Defined in: [utils/LlamaText.ts:533](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L533)

#### Returns

[`LlamaTextSpecialTokenJSON`](../type-aliases/LlamaTextSpecialTokenJSON.md)

***

### fromJSON()

```ts
static fromJSON(json: LlamaTextSpecialTokenJSON): SpecialToken;
```

Defined in: [utils/LlamaText.ts:557](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L557)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `json` | [`LlamaTextSpecialTokenJSON`](../type-aliases/LlamaTextSpecialTokenJSON.md) |

#### Returns

`SpecialToken`

***

### isSpecialTokenJSON()

```ts
static isSpecialTokenJSON(value: LlamaTextJSONValue): value is LlamaTextSpecialTokenJSON;
```

Defined in: [utils/LlamaText.ts:564](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L564)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `value` | [`LlamaTextJSONValue`](../type-aliases/LlamaTextJSONValue.md) |

#### Returns

`value is LlamaTextSpecialTokenJSON`

***

### getTokenToValueMap()

```ts
static getTokenToValueMap(tokenizer: Tokenizer): ReadonlyMap<Token | undefined, BuiltinSpecialTokenValue>;
```

Defined in: [utils/LlamaText.ts:568](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L568)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `tokenizer` | [`Tokenizer`](../type-aliases/Tokenizer.md) |

#### Returns

`ReadonlyMap`<[`Token`](../type-aliases/Token.md) | `undefined`, [`BuiltinSpecialTokenValue`](../type-aliases/BuiltinSpecialTokenValue.md)>
