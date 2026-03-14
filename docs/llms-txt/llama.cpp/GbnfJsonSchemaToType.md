# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/GbnfJsonSchemaToType.md

---
url: /api/type-aliases/GbnfJsonSchemaToType.md
---
# Type Alias: GbnfJsonSchemaToType\<T>

```ts
type GbnfJsonSchemaToType<T> = 0 extends 1 & T ? any : GbnfJsonSchemaToTSType<T>;
```

Defined in: [utils/gbnfJson/types.ts:192](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/types.ts#L192)

Converts a GBNF JSON schema to a TypeScript type

## Type Parameters

| Type Parameter |
| ------ |
| `T` |
