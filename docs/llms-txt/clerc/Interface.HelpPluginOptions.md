# Source: https://clerc.so1ve.dev/reference/api/plugin-help/Interface.HelpPluginOptions.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Interface.HelpPluginOptions.md

---

url: /reference/api/clerc/Interface.HelpPluginOptions.md
---

# Interface: HelpPluginOptions

Defined in: [packages/plugin-help/src/index.ts:58](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L58)

## Properties

&#x20;`command?`

`boolean`

Whether to register the `help` command.

**Default**

```ts twoslash
// @include: imports
true;
```

[packages/plugin-help/src/index.ts:64](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L64)

&#x20;`examples?`

`MaybeAsyncGetter`<\[`string`, `string`]\[]>

Examples to show in the help output. Each example is a tuple of `[command,
description]`.

[packages/plugin-help/src/index.ts:85](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L85)

&#x20;`flag?`

`boolean`

Whether to register the `--help` global flag.

**Default**

```ts twoslash
// @include: imports
true;
```

[packages/plugin-help/src/index.ts:70](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L70)

&#x20;`footer?`

`MaybeAsyncGetter`<`string` | `void` | `undefined`>

Footer to show after the help output.

[packages/plugin-help/src/index.ts:93](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L93)

&#x20;`formatters?`

`Partial`<`Formatters`>

Custom formatters for rendering help.

[packages/plugin-help/src/index.ts:97](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L97)

&#x20;`groups?`

[`GroupsOptions`](Interface.GroupsOptions.md)

Group definitions for commands and flags. Groups allow organizing commands
and flags into logical sections in help output. Each group is defined as
`[key, name]` where `key` is the identifier used in help options and `name`
is the display name shown in help output.

[packages/plugin-help/src/index.ts:104](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L104)

&#x20;`header?`

`MaybeAsyncGetter`<`string` | `void` | `undefined`>

Header to show before the help output.

[packages/plugin-help/src/index.ts:89](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L89)

&#x20;`notes?`

`MaybeAsyncGetter`<`string`\[]>

Notes to show in the help output.

[packages/plugin-help/src/index.ts:80](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L80)

&#x20;`showHelpWhenNoCommandSpecified?`

`boolean`

Whether to show help when no command is specified.

**Default**

```ts twoslash
// @include: imports
true;
```

[packages/plugin-help/src/index.ts:76](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L76)
