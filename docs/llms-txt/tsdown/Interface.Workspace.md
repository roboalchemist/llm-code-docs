# Source: https://tsdown.dev/reference/api/Interface.Workspace.md

---
url: /reference/api/Interface.Workspace.md
---
# Interface: Workspace

Defined in: [src/config/types.ts:107](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L107)

## Properties

### config?

```ts
optional config: string | boolean;
```

Defined in: [src/config/types.ts:123](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L123)

Path to the workspace configuration file.

***

### exclude?

```ts
optional exclude: Arrayable<string>;
```

Defined in: [src/config/types.ts:118](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L118)

Exclude directories from workspace.
Defaults to all `node_modules`, `dist`, `test`, `tests`, `temp`, and `tmp` directories.

***

### include?

```ts
optional include: Arrayable<string>;
```

Defined in: [src/config/types.ts:113](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L113)

Workspace directories. Glob patterns are supported.

* `auto`: Automatically detect `package.json` files in the workspace.

#### Default

```ts
'auto'
```
