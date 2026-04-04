# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GbnfJsonArraySchema.md

---
url: /api/type-aliases/GbnfJsonArraySchema.md
---
# Type Alias: GbnfJsonArraySchema\<Defs>

```ts
type GbnfJsonArraySchema<Defs> = {
  type: "array";
  items?: GbnfJsonSchema<NoInfer<Defs>>;
  prefixItems?: readonly GbnfJsonSchema<NoInfer<Defs>>[];
  minItems?: number;
  maxItems?: number;
  description?: string;
  $defs?: Defs;
};
```

Defined in: [utils/gbnfJson/types.ts:145](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L145)

## Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `Defs` *extends* `GbnfJsonDefList`<[`NoInfer`](https://www.typescriptlang.org/docs/handbook/utility-types.html#noinfertype)<`Defs`>> | { } |

## Properties

### type

```ts
readonly type: "array";
```

Defined in: [utils/gbnfJson/types.ts:146](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L146)

***

### items?

```ts
readonly optional items: GbnfJsonSchema<NoInfer<Defs>>;
```

Defined in: [utils/gbnfJson/types.ts:147](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L147)

***

### prefixItems?

```ts
readonly optional prefixItems: readonly GbnfJsonSchema<NoInfer<Defs>>[];
```

Defined in: [utils/gbnfJson/types.ts:148](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L148)

***

### minItems?

```ts
readonly optional minItems: number;
```

Defined in: [utils/gbnfJson/types.ts:155](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L155)

When using `minItems` and/or `maxItems`,
ensure to inform the model as part of the prompt what your expectations are regarding the length of the array.
Not doing this may lead to hallucinations.

***

### maxItems?

```ts
readonly optional maxItems: number;
```

Defined in: [utils/gbnfJson/types.ts:162](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L162)

When using `minItems` and/or `maxItems`,
ensure to inform the model as part of the prompt what your expectations are regarding the length of the array.
Not doing this may lead to hallucinations.

***

### description?

```ts
readonly optional description: string;
```

Defined in: [utils/gbnfJson/types.ts:169](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L169)

A description of what you expect the model to set this value to.

Only passed to the model when using function calling, and has no effect when using JSON Schema grammar directly.

***

### $defs?

```ts
readonly optional $defs: Defs;
```

Defined in: [utils/gbnfJson/types.ts:171](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L171)
