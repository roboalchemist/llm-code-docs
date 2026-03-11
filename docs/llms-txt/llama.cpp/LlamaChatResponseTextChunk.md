# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaChatResponseTextChunk.md

---
url: /api/type-aliases/LlamaChatResponseTextChunk.md
---
# Type Alias: LlamaChatResponseTextChunk

```ts
type LlamaChatResponseTextChunk = {
  type: undefined;
  segmentType: undefined;
  text: string;
  tokens: Token[];
};
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:51](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L51)

## Properties

### type

```ts
type: undefined;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:53](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L53)

When `type` is `undefined`, the chunk is part of the main response and is not a segment

***

### segmentType

```ts
segmentType: undefined;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:58](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L58)

`segmentType` has no purpose when `type` is `undefined` (meaning that this chunk is part of the main response and is not a segment).

***

### text

```ts
text: string;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:68](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L68)

The generated text chunk.

Detokenized from the `tokens` property,
but with the context of the previous generation (for better spacing of the text with some models).

Prefer using this property over `tokens` when streaming the generated response as text.

***

### tokens

```ts
tokens: Token[];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:71](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L71)

The generated tokens
