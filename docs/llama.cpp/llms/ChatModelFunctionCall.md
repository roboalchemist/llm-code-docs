# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ChatModelFunctionCall.md

---
url: /api/type-aliases/ChatModelFunctionCall.md
---
# Type Alias: ChatModelFunctionCall

```ts
type ChatModelFunctionCall = {
  type: "functionCall";
  name: string;
  description?: string;
  params: any;
  result: any;
  rawCall?: LlamaTextJSON;
  startsNewChunk?: boolean;
};
```

Defined in: [types.ts:332](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L332)

## Properties

### type

```ts
type: "functionCall";
```

Defined in: [types.ts:333](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L333)

***

### name

```ts
name: string;
```

Defined in: [types.ts:334](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L334)

***

### description?

```ts
optional description: string;
```

Defined in: [types.ts:335](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L335)

***

### params

```ts
params: any;
```

Defined in: [types.ts:336](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L336)

***

### result

```ts
result: any;
```

Defined in: [types.ts:337](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L337)

***

### rawCall?

```ts
optional rawCall: LlamaTextJSON;
```

Defined in: [types.ts:338](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L338)

***

### startsNewChunk?

```ts
optional startsNewChunk: boolean;
```

Defined in: [types.ts:345](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L345)

Whether this function call starts a new function calling chunk.

Relevant only when parallel function calling is supported.
