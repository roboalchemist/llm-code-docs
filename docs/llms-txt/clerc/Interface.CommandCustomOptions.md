# Source: https://clerc.so1ve.dev/reference/api/core/Interface.CommandCustomOptions.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Interface.CommandCustomOptions.md

---

url: /reference/api/clerc/Interface.CommandCustomOptions.md
---

# Interface: CommandCustomOptions

Defined in: [packages/core/src/types/command.ts:8](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L8)

## Extended by

* [`CommandOptions`](Interface.CommandOptions.md)

## Properties

&#x20;`completions?`

`object`

Completions options for the command.

[packages/plugin-completions/src/index.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L17)

`completions.handler?`

(`command`) => `void`

Handler to provide custom completions for the command.

[packages/plugin-completions/src/index.ts:27](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L27)

`completions.show?`

`boolean`

Whether to show the command in completions output.

**Default**

```ts twoslash
// @include: imports
true;
```

[packages/plugin-completions/src/index.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L23)

&#x20;`help?`

[`CommandHelpOptions`](Interface.CommandHelpOptions.md)

Help options for the command.

[packages/plugin-help/src/index.ts:47](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L47)
