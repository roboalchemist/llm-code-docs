# Source: https://clerc.so1ve.dev/reference/api/plugin-help/Interface.GroupsOptions.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Interface.GroupsOptions.md

---

url: /reference/api/clerc/Interface.GroupsOptions.md
---

# Interface: GroupsOptions

Defined in: [packages/plugin-help/src/types.ts:18](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L18)

Options for defining groups in help output.

## Properties

&#x20;`commands?`

[`GroupDefinition`](TypeAlias.GroupDefinition.md)\[]

Groups for commands. Each group is defined as `[key, name]`.

[packages/plugin-help/src/types.ts:22](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L22)

&#x20;`flags?`

[`GroupDefinition`](TypeAlias.GroupDefinition.md)\[]

Groups for command-specific flags. Each group is defined as `[key, name]`.

[packages/plugin-help/src/types.ts:26](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L26)

&#x20;`globalFlags?`

[`GroupDefinition`](TypeAlias.GroupDefinition.md)\[]

Groups for global flags. Each group is defined as `[key, name]`.

[packages/plugin-help/src/types.ts:30](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L30)
