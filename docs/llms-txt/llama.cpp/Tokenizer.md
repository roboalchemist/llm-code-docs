# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/Tokenizer.md

---
url: /api/type-aliases/Tokenizer.md
---
# Type Alias: Tokenizer

```ts
type Tokenizer = {
  tokenize: Token[];
}["tokenize"] & {
  detokenize: Detokenizer;
  isSpecialToken: boolean;
  isEogToken: boolean;
};
```

Defined in: [types.ts:12](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L12)

## Type Declaration

### detokenize

```ts
readonly detokenize: Detokenizer;
```

### isSpecialToken()

```ts
isSpecialToken(token: Token): boolean;
```

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `token` | [`Token`](Token.md) |

#### Returns

`boolean`

### isEogToken()

```ts
isEogToken(token: Token): boolean;
```

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `token` | [`Token`](Token.md) |

#### Returns

`boolean`
