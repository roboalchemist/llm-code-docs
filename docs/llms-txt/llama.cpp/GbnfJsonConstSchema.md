# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GbnfJsonConstSchema.md

---
url: /api/type-aliases/GbnfJsonConstSchema.md
---
# Type Alias: GbnfJsonConstSchema

```ts
type GbnfJsonConstSchema = {
  const: string | number | boolean | null;
  description?: string;
};
```

Defined in: [utils/gbnfJson/types.ts:27](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L27)

## Properties

### const

```ts
readonly const: string | number | boolean | null;
```

Defined in: [utils/gbnfJson/types.ts:28](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L28)

***

### description?

```ts
readonly optional description: string;
```

Defined in: [utils/gbnfJson/types.ts:35](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L35)

A description of what you expect the model to set this value to.

Only passed to the model when using function calling, and has no effect when using JSON Schema grammar directly.
