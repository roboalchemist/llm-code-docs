# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GbnfJsonEnumSchema.md

---
url: /api/type-aliases/GbnfJsonEnumSchema.md
---
# Type Alias: GbnfJsonEnumSchema

```ts
type GbnfJsonEnumSchema = {
  enum: readonly (string | number | boolean | null)[];
  description?: string;
};
```

Defined in: [utils/gbnfJson/types.ts:37](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L37)

## Properties

### enum

```ts
readonly enum: readonly (string | number | boolean | null)[];
```

Defined in: [utils/gbnfJson/types.ts:38](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L38)

***

### description?

```ts
readonly optional description: string;
```

Defined in: [utils/gbnfJson/types.ts:45](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L45)

A description of what you expect the model to set this value to.

Only passed to the model when using function calling, and has no effect when using JSON Schema grammar directly.
