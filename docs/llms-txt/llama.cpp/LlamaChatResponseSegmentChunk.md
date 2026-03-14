# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaChatResponseSegmentChunk.md

---
url: /api/type-aliases/LlamaChatResponseSegmentChunk.md
---
# Type Alias: LlamaChatResponseSegmentChunk

```ts
type LlamaChatResponseSegmentChunk = {
  type: "segment";
  segmentType: ChatModelSegmentType;
  text: string;
  tokens: Token[];
  segmentStartTime?: Date;
  segmentEndTime?: Date;
};
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:74](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L74)

## Properties

### type

```ts
type: "segment";
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:75](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L75)

***

### segmentType

```ts
segmentType: ChatModelSegmentType;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:78](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L78)

Segment type

***

### text

```ts
text: string;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:88](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L88)

The generated text chunk.

Detokenized from the `tokens` property,
but with the context of the previous generation (for better spacing of the text with some models).

Prefer using this property over `tokens` when streaming the generated response as text.

***

### tokens

```ts
tokens: Token[];
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:91](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L91)

The generated tokens

***

### segmentStartTime?

```ts
optional segmentStartTime: Date;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:99](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L99)

When the current chunk is the start of a segment, this field will be set.

It's possible that a chunk with no tokens and empty text will be emitted just to set this field
to signify that the segment has started.

***

### segmentEndTime?

```ts
optional segmentEndTime: Date;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:107](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L107)

When the current chunk is the last one of a segment (meaning the current segment has ended), this field will be set.

It's possible that a chunk with no tokens and empty text will be emitted just to set this field
to signify that the segment has ended.
