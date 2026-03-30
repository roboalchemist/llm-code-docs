# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GbnfJsonBasicSchema.md

---
url: /api/type-aliases/GbnfJsonBasicSchema.md
---
# Type Alias: GbnfJsonBasicSchema

```ts
type GbnfJsonBasicSchema = {
  type:   | GbnfJsonSchemaImmutableType
     | readonly GbnfJsonSchemaImmutableType[];
  description?: string;
};
```

Defined in: [utils/gbnfJson/types.ts:17](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L17)

## Properties

### type

```ts
readonly type: 
  | GbnfJsonSchemaImmutableType
  | readonly GbnfJsonSchemaImmutableType[];
```

Defined in: [utils/gbnfJson/types.ts:18](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L18)

***

### description?

```ts
readonly optional description: string;
```

Defined in: [utils/gbnfJson/types.ts:25](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L25)

A description of what you expect the model to set this value to.

Only passed to the model when using function calling, and has no effect when using JSON Schema grammar directly.
