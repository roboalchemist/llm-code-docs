# Source: https://clerc.so1ve.dev/reference/api/plugin-help/Interface.FlagHelpOptions.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Interface.FlagHelpOptions.md

---

url: /reference/api/clerc/Interface.FlagHelpOptions.md
---

# Interface: FlagHelpOptions

Defined in: [packages/plugin-help/src/index.ts:40](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L40)

## Extends

* [`HelpOptions`](Interface.HelpOptions.md)

## Properties

&#x20;`group?`

`string`

The group this item belongs to. The group must be defined in the `groups`
option of `helpPlugin()`.

[`HelpOptions`](Interface.HelpOptions.md).[`group`](Interface.HelpOptions.md#group)

[packages/plugin-help/src/index.ts:25](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L25)

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
