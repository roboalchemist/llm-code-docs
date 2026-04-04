# Source: https://clerc.so1ve.dev/reference/api/plugin-help/Interface.CommandHelpOptions.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Interface.CommandHelpOptions.md

---

url: /reference/api/clerc/Interface.CommandHelpOptions.md
---

# Interface: CommandHelpOptions

Defined in: [packages/plugin-help/src/index.ts:28](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L28)

## Extends

* [`HelpOptions`](Interface.HelpOptions.md)

## Properties

&#x20;`examples?`

`MaybeAsyncGetter`<\[`string`, `string`]\[]>

Examples to show in the help output. Each example is a tuple of `[command,
description]`.

‐

[packages/plugin-help/src/index.ts:37](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L37)

&#x20;`group?`

`string`

The group this item belongs to. The group must be defined in the `groups`
option of `helpPlugin()`.

[`HelpOptions`](Interface.HelpOptions.md).[`group`](Interface.HelpOptions.md#group)

[packages/plugin-help/src/index.ts:25](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L25)

&#x20;`notes?`

`MaybeAsyncGetter`<`string`\[]>

Notes to show in the help output.

‐

[packages/plugin-help/src/index.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L32)

&#x20;`show?`

`boolean`

Whether to show this item in help output.

**Default**

```ts twoslash
// @include: imports
true;
```

[`HelpOptions`](Interface.HelpOptions.md).[`show`](Interface.HelpOptions.md#show)

[packages/plugin-help/src/index.ts:20](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L20)
