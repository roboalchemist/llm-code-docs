# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ChatModelResponse.md

---
url: /api/type-aliases/ChatModelResponse.md
---
# Type Alias: ChatModelResponse

```ts
type ChatModelResponse = {
  type: "model";
  response: (
     | string
     | ChatModelFunctionCall
    | ChatModelSegment)[];
};
```

Defined in: [types.ts:328](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L328)

## Properties

### type

```ts
type: "model";
```

Defined in: [types.ts:329](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L329)

***

### response

```ts
response: (
  | string
  | ChatModelFunctionCall
  | ChatModelSegment)[];
```

Defined in: [types.ts:330](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L330)
