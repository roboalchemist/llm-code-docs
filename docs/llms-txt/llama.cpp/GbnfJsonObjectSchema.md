# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GbnfJsonObjectSchema.md

---
url: /api/type-aliases/GbnfJsonObjectSchema.md
---
# Type Alias: GbnfJsonObjectSchema\<Keys, Defs>

```ts
type GbnfJsonObjectSchema<Keys, Defs> = {
  type: "object";
  properties?: { readonly [key in Keys]: GbnfJsonSchema<NoInfer<Defs>> };
  additionalProperties?:   | boolean
     | GbnfJsonSchema<NoInfer<Defs>>;
  minProperties?: number;
  maxProperties?: number;
  required?: readonly Keys[];
  description?: string;
  $defs?: Defs;
};
```

Defined in: [utils/gbnfJson/types.ts:95](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L95)

## Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `Keys` *extends* `string` | `string` |
| `Defs` *extends* `GbnfJsonDefList`<[`NoInfer`](https://www.typescriptlang.org/docs/handbook/utility-types.html#noinfertype)<`Defs`>> | { } |

## Properties

### type

```ts
readonly type: "object";
```

Defined in: [utils/gbnfJson/types.ts:99](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L99)

***

### properties?

```ts
readonly optional properties: { readonly [key in Keys]: GbnfJsonSchema<NoInfer<Defs>> };
```

Defined in: [utils/gbnfJson/types.ts:100](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L100)

***

### additionalProperties?

```ts
readonly optional additionalProperties: 
  | boolean
  | GbnfJsonSchema<NoInfer<Defs>>;
```

Defined in: [utils/gbnfJson/types.ts:105](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L105)

Unlike the JSON Schema spec, `additionalProperties` defaults to `false` to avoid breaking existing code.

***

### minProperties?

```ts
readonly optional minProperties: number;
```

Defined in: [utils/gbnfJson/types.ts:114](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L114)

Make sure you define `additionalProperties` for this to have any effect.

When using `minProperties` and/or `maxProperties`,
ensure to inform the model as part of the prompt what your expectations are regarding the number of keys in the object.
Not doing this may lead to hallucinations.

***

### maxProperties?

```ts
readonly optional maxProperties: number;
```

Defined in: [utils/gbnfJson/types.ts:123](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L123)

Make sure you define `additionalProperties` for this to have any effect.

When using `minProperties` and/or `maxProperties`,
ensure to inform the model as part of the prompt what your expectations are regarding the number of keys in the object.
Not doing this may lead to hallucinations.

***

### ~~required?~~

```ts
readonly optional required: readonly Keys[];
```

Defined in: [utils/gbnfJson/types.ts:134](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L134)

`required` is always set to all keys in `properties`, and setting it has no effect.

This limitation is due to how the generation works, and may be fixed in the future.

This key is part of the type to avoid breaking exiting code (though it was never actually used in the past),
and will be removed in the future.

#### Deprecated

***

### description?

```ts
readonly optional description: string;
```

Defined in: [utils/gbnfJson/types.ts:141](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L141)

A description of what you expect the model to set this value to.

Only passed to the model when using function calling, and has no effect when using JSON Schema grammar directly.

***

### $defs?

```ts
readonly optional $defs: Defs;
```

Defined in: [utils/gbnfJson/types.ts:143](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L143)
