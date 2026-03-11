# Source: https://node-llama-cpp.withcat.ai/api/type-aliases/OverridesObject.md

---
url: /api/type-aliases/OverridesObject.md
---
# Type Alias: OverridesObject\<T, AllowedValueTypes>

```ts
type OverridesObject<T, AllowedValueTypes> = T extends object ? { [P in keyof T]?: OverridesObject<T[P], AllowedValueTypes> } : T extends infer I[] ? AllowedValueTypes extends any[] ? OverridesObject<I, AllowedValueTypes>[] : never : T extends ReadonlyArray<infer I> ? AllowedValueTypes extends ReadonlyArray<any> ? ReadonlyArray<OverridesObject<I, AllowedValueTypes>> : never : AllowedValueTypes extends T ? T : never;
```

Defined in: [utils/OverridesObject.ts:5](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/OverridesObject.ts#L5)

Makes all the properties of an object optional, including nested objects,
and strips all keys that their value is not of the specified allowed value types.

## Type Parameters

| Type Parameter |
| ------ |
| `T` |
| `AllowedValueTypes` |
