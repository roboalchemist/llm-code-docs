# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GbnfJsonSchema.md

---
url: /api/type-aliases/GbnfJsonSchema.md
---
# Type Alias: GbnfJsonSchema\<Defs>

```ts
type GbnfJsonSchema<Defs> = 
  | GbnfJsonBasicSchema
  | GbnfJsonConstSchema
  | GbnfJsonEnumSchema
  | GbnfJsonOneOfSchema<Defs>
  | GbnfJsonStringSchema
  | GbnfJsonObjectSchema<string, Defs>
  | GbnfJsonArraySchema<Defs>
  | keyof Defs extends string ? keyof NoInfer<Defs> extends never ? never : GbnfJsonRefSchema<Defs> : never;
```

Defined in: [utils/gbnfJson/types.ts:3](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L3)

## Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `Defs` *extends* `GbnfJsonDefList`<`Defs`> | [`Record`](https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type)<`any`, `any`> |
