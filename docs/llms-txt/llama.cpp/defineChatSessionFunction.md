# Source: https://node-llama-cpp.withcat.ai/api/functions/defineChatSessionFunction.md

---
url: /api/functions/defineChatSessionFunction.md
---
# Function: defineChatSessionFunction()

```ts
function defineChatSessionFunction<Params, Defs>(functionDefinition: {
  description?: string;
  params?: Readonly<Params> & GbnfJsonSchema<Defs>;
  handler: (params: GbnfJsonSchemaToType<NoInfer<Params>>) => any;
}): ChatSessionModelFunction<NoInfer<Params>>;
```

Defined in: [evaluator/LlamaChatSession/utils/defineChatSessionFunction.ts:12](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaChatSession/utils/defineChatSessionFunction.ts#L12)

Define a function that can be used by the model in a chat session, and return it.

This is a helper function to facilitate defining functions with full TypeScript type information.

The handler function can return a Promise, and the return value will be awaited before being returned to the model.

## Type Parameters

| Type Parameter |
| ------ |
| `Params` *extends* | [`GbnfJsonBasicSchema`](../type-aliases/GbnfJsonBasicSchema.md) | [`GbnfJsonConstSchema`](../type-aliases/GbnfJsonConstSchema.md) | [`GbnfJsonEnumSchema`](../type-aliases/GbnfJsonEnumSchema.md) | [`GbnfJsonBasicStringSchema`](../type-aliases/GbnfJsonBasicStringSchema.md) | [`GbnfJsonFormatStringSchema`](../type-aliases/GbnfJsonFormatStringSchema.md) | [`GbnfJsonOneOfSchema`](../type-aliases/GbnfJsonOneOfSchema.md)<`Defs`> | [`GbnfJsonObjectSchema`](../type-aliases/GbnfJsonObjectSchema.md)<`string`, `Defs`> | [`GbnfJsonArraySchema`](../type-aliases/GbnfJsonArraySchema.md)<`Defs`> | `GbnfJsonRefSchema`<`Defs`> |
| `Defs` *extends* `GbnfJsonDefList`<`Defs`> |

## Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `functionDefinition` | { `description?`: `string`; `params?`: Readonly\<Params> & GbnfJsonSchema\<Defs>; `handler`: (`params`: [`GbnfJsonSchemaToType`](../type-aliases/GbnfJsonSchemaToType.md)<[`NoInfer`](https://www.typescriptlang.org/docs/handbook/utility-types.html#noinfertype)<`Params`>>) => `any`; } | - |
| `functionDefinition.description?` | `string` | - |
| `functionDefinition.params?` | Readonly\<Params> & GbnfJsonSchema\<Defs> | - |
| `functionDefinition.handler` | (`params`: [`GbnfJsonSchemaToType`](../type-aliases/GbnfJsonSchemaToType.md)<[`NoInfer`](https://www.typescriptlang.org/docs/handbook/utility-types.html#noinfertype)<`Params`>>) => `any` | - |

## Returns

[`ChatSessionModelFunction`](../type-aliases/ChatSessionModelFunction.md)<[`NoInfer`](https://www.typescriptlang.org/docs/handbook/utility-types.html#noinfertype)<`Params`>>
