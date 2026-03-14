# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GbnfJsonOneOfSchema.md

---
url: /api/type-aliases/GbnfJsonOneOfSchema.md
---
# Type Alias: GbnfJsonOneOfSchema\<Defs>

```ts
type GbnfJsonOneOfSchema<Defs> = {
  oneOf: readonly GbnfJsonSchema<NoInfer<Defs>>[];
  description?: string;
  $defs?: Defs;
};
```

Defined in: [utils/gbnfJson/types.ts:47](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L47)

## Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `Defs` *extends* `GbnfJsonDefList`<[`NoInfer`](https://www.typescriptlang.org/docs/handbook/utility-types.html#noinfertype)<`Defs`>> | { } |

## Properties

### oneOf

```ts
readonly oneOf: readonly GbnfJsonSchema<NoInfer<Defs>>[];
```

Defined in: [utils/gbnfJson/types.ts:48](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L48)

***

### description?

```ts
readonly optional description: string;
```

Defined in: [utils/gbnfJson/types.ts:55](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L55)

A description of what you expect the model to set this value to.

Only passed to the model when using function calling, and has no effect when using JSON Schema grammar directly.

***

### $defs?

```ts
readonly optional $defs: Defs;
```

Defined in: [utils/gbnfJson/types.ts:57](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L57)
