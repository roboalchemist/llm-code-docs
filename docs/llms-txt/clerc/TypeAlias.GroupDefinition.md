# Source: https://clerc.so1ve.dev/reference/api/plugin-help/TypeAlias.GroupDefinition.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/TypeAlias.GroupDefinition.md

---

url: /reference/api/clerc/TypeAlias.GroupDefinition.md
---

# Type Alias: GroupDefinition

```ts twoslash
// @include: imports
type GroupDefinition = [string, string];
```

Defined in: [packages/plugin-help/src/types.ts:13](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L13)

A group definition as a tuple of \[key, displayName]. The key is used in help
options to assign items to groups. The displayName is shown in the help
output.
