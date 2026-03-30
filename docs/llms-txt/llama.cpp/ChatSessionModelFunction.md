# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/ChatSessionModelFunction.md

---
url: /api/type-aliases/ChatSessionModelFunction.md
---
# Type Alias: ChatSessionModelFunction\<Params>

```ts
type ChatSessionModelFunction<Params> = {
  description?: string;
  params?: Params;
  handler: (params: GbnfJsonSchemaToType<NoInfer<Params>>) => any;
};
```

Defined in: [types.ts:373](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L373)

## Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `Params` *extends* [`GbnfJsonSchema`](GbnfJsonSchema.md) | `undefined` | [`GbnfJsonSchema`](GbnfJsonSchema.md) | `undefined` |

## Properties

### description?

```ts
readonly optional description: string;
```

Defined in: [types.ts:374](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L374)

***

### params?

```ts
readonly optional params: Params;
```

Defined in: [types.ts:375](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L375)

***

### handler()

```ts
readonly handler: (params: GbnfJsonSchemaToType<NoInfer<Params>>) => any;
```

Defined in: [types.ts:376](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/types.ts#L376)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `params` | [`GbnfJsonSchemaToType`](GbnfJsonSchemaToType.md)<[`NoInfer`](https://www.typescriptlang.org/docs/handbook/utility-types.html#noinfertype)<`Params`>> |

#### Returns

`any`
