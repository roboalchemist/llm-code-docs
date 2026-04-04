# Source: https://clerc.so1ve.dev/reference/api/plugin-help/Interface.HelpOptions.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Interface.HelpOptions.md

---

url: /reference/api/clerc/Interface.HelpOptions.md
---

# Interface: HelpOptions

Defined in: [packages/plugin-help/src/index.ts:14](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L14)

## Extended by

* [`CommandHelpOptions`](Interface.CommandHelpOptions.md)
* [`FlagHelpOptions`](Interface.FlagHelpOptions.md)

## Properties

&#x20;`group?`

`string`

The group this item belongs to. The group must be defined in the `groups`
option of `helpPlugin()`.

[packages/plugin-help/src/index.ts:25](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L25)

&#x20;`show?`

`boolean`

Whether to show this item in help output.

**Default**

```ts twoslash
// @include: imports
true;
```

[packages/plugin-help/src/index.ts:20](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L20)
