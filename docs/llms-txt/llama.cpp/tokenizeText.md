# Source: https://node-llama-cpp.withcat.ai/api/functions/tokenizeText.md

---
url: /api/functions/tokenizeText.md
---
# Function: tokenizeText()

```ts
function tokenizeText(text: string | LlamaText, tokenizer: Tokenizer): Token[];
```

Defined in: [utils/LlamaText.ts:593](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/LlamaText.ts#L593)

Tokenize the given input using the given tokenizer, whether it's a `string` or a `LlamaText`

## Parameters

| Parameter | Type |
| ------ | ------ |
| `text` | `string` | [`LlamaText`](../classes/LlamaText.md) |
| `tokenizer` | [`Tokenizer`](../type-aliases/Tokenizer.md) |

## Returns

[`Token`](../type-aliases/Token.md)\[]
