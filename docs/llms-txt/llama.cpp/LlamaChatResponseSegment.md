# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/LlamaChatResponseSegment.md

---
url: /api/type-aliases/LlamaChatResponseSegment.md
---
# Type Alias: LlamaChatResponseSegment

```ts
type LlamaChatResponseSegment = {
  type: "segment";
  segmentType: ChatModelSegmentType;
  text: string;
  ended: boolean;
  raw: LlamaTextJSON;
  startTime?: string;
  endTime?: string;
};
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1086](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1086)

## Properties

### type

```ts
type: "segment";
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1087](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1087)

***

### segmentType

```ts
segmentType: ChatModelSegmentType;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1088](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1088)

***

### text

```ts
text: string;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1089](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1089)

***

### ended

```ts
ended: boolean;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1090](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1090)

***

### raw

```ts
raw: LlamaTextJSON;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1091](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1091)

***

### startTime?

```ts
optional startTime: string;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1092](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1092)

***

### endTime?

```ts
optional endTime: string;
```

Defined in: [evaluator/LlamaChat/LlamaChat.ts:1093](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChat/LlamaChat.ts#L1093)
