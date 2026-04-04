# Source: https://clerc.so1ve.dev/reference/api/core/Parser.TypeAlias.InferFlags.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Parser.TypeAlias.InferFlags.md

---

url: /reference/api/clerc/Parser.TypeAlias.InferFlags.md
---

# Type Alias: InferFlags\<T>

```ts twoslash
// @include: imports
type InferFlags<T> = Prettify<_InferFlags<T>>;
```

Defined in: [packages/parser/src/types.ts:208](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L208)

An advanced utility type that infers the exact type of the `flags` object in
the parsed result, based on the provided `flags` configuration object T.

## Type Parameters

`T` *extends* [`FlagsDefinition`](Parser.TypeAlias.FlagsDefinition.md)

The type of the flags configuration object.
