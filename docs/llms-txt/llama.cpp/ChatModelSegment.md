# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ChatModelSegment.md

---
url: /api/type-aliases/ChatModelSegment.md
---
# Type Alias: ChatModelSegment

```ts
type ChatModelSegment = {
  type: "segment";
  segmentType: ChatModelSegmentType;
  text: string;
  ended: boolean;
  raw?: LlamaTextJSON;
  startTime?: string;
  endTime?: string;
};
```

Defined in: [types.ts:352](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L352)

## Properties

### type

```ts
type: "segment";
```

Defined in: [types.ts:353](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L353)

***

### segmentType

```ts
segmentType: ChatModelSegmentType;
```

Defined in: [types.ts:354](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L354)

***

### text

```ts
text: string;
```

Defined in: [types.ts:355](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L355)

***

### ended

```ts
ended: boolean;
```

Defined in: [types.ts:356](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L356)

***

### raw?

```ts
optional raw: LlamaTextJSON;
```

Defined in: [types.ts:357](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L357)

***

### startTime?

```ts
optional startTime: string;
```

Defined in: [types.ts:358](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L358)

***

### endTime?

```ts
optional endTime: string;
```

Defined in: [types.ts:359](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L359)
