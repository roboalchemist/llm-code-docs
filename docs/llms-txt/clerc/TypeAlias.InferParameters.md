# Source: https://clerc.so1ve.dev/reference/api/core/TypeAlias.InferParameters.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/TypeAlias.InferParameters.md

---

url: /reference/api/clerc/TypeAlias.InferParameters.md
---

# Type Alias: InferParameters\<T>

```ts twoslash
// @include: imports
type InferParameters<T> = T extends readonly infer U[] ? Prettify<UnionToIntersection<InferParameter<U>>> : never;
```

Defined in: [packages/core/src/types/parameter.ts:24](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L24)

## Type Parameters

`T` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]
