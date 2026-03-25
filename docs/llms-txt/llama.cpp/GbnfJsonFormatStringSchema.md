# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GbnfJsonFormatStringSchema.md

---
url: /api/type-aliases/GbnfJsonFormatStringSchema.md
---
# Type Alias: GbnfJsonFormatStringSchema

```ts
type GbnfJsonFormatStringSchema = {
  type: "string";
  format: "date-time" | "time" | "date";
  description?: string;
};
```

Defined in: [utils/gbnfJson/types.ts:84](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L84)

## Properties

### type

```ts
readonly type: "string";
```

Defined in: [utils/gbnfJson/types.ts:85](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L85)

***

### format

```ts
readonly format: "date-time" | "time" | "date";
```

Defined in: [utils/gbnfJson/types.ts:86](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L86)

***

### description?

```ts
readonly optional description: string;
```

Defined in: [utils/gbnfJson/types.ts:93](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L93)

A description of what you expect the model to set this value to.

Only passed to the model when using function calling, and has no effect when using JSON Schema grammar directly.
