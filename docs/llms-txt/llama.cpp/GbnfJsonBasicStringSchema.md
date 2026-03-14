# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GbnfJsonBasicStringSchema.md

---
url: /api/type-aliases/GbnfJsonBasicStringSchema.md
---
# Type Alias: GbnfJsonBasicStringSchema

```ts
type GbnfJsonBasicStringSchema = {
  type: "string";
  minLength?: number;
  maxLength?: number;
  description?: string;
};
```

Defined in: [utils/gbnfJson/types.ts:60](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L60)

## Properties

### type

```ts
readonly type: "string";
```

Defined in: [utils/gbnfJson/types.ts:61](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L61)

***

### minLength?

```ts
readonly optional minLength: number;
```

Defined in: [utils/gbnfJson/types.ts:68](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L68)

When using `minLength` and/or `maxLength`,
ensure to inform the model as part of the prompt what your expectations are regarding the length of the string.
Not doing this may lead to hallucinations.

***

### maxLength?

```ts
readonly optional maxLength: number;
```

Defined in: [utils/gbnfJson/types.ts:75](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L75)

When using `minLength` and/or `maxLength`,
ensure to inform the model as part of the prompt what your expectations are regarding the length of the string.
Not doing this may lead to hallucinations.

***

### description?

```ts
readonly optional description: string;
```

Defined in: [utils/gbnfJson/types.ts:82](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L82)

A description of what you expect the model to set this value to.

Only passed to the model when using function calling, and has no effect when using JSON Schema grammar directly.
