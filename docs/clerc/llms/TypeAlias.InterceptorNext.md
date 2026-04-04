# Source: https://clerc.so1ve.dev/reference/api/core/TypeAlias.InterceptorNext.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/TypeAlias.InterceptorNext.md

---

url: /reference/api/clerc/TypeAlias.InterceptorNext.md
---

# Type Alias: InterceptorNext()

```ts twoslash
// @include: imports
type InterceptorNext = () => void | Promise<void>;
```

Defined in: [packages/core/src/types/interceptor.ts:15](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L15)

Function to call the next interceptor in the chain. **MUST** be awaited.

## Returns

`void` | `Promise`<`void`>
