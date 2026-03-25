# Source: https://clerc.so1ve.dev/reference/api/core/Interface.FlagCustomOptions.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Interface.FlagCustomOptions.md

---

url: /reference/api/clerc/Interface.FlagCustomOptions.md
---

# Interface: FlagCustomOptions

Defined in: [packages/core/src/types/flag.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/flag.ts#L3)

## Properties

&#x20;`completions?`

`object`

Completions options for the flag.

[packages/plugin-completions/src/index.ts:34](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L34)

`completions.handler?`

`OptionHandler`

Handler to provide custom completions for the flag.

[packages/plugin-completions/src/index.ts:44](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L44)

`completions.show?`

`boolean`

Whether to show the flag in completions output.

**Default**

```ts twoslash
// @include: imports
true;
```

[packages/plugin-completions/src/index.ts:40](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L40)

&#x20;`help?`

[`FlagHelpOptions`](Interface.FlagHelpOptions.md)

Help options for the flag.

[packages/plugin-help/src/index.ts:54](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L54)
