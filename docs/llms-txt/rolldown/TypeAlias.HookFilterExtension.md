# Source: https://rolldown.rs/reference/TypeAlias.HookFilterExtension.md

---
url: /reference/TypeAlias.HookFilterExtension.md
---
# Type Alias: HookFilterExtension\<K>

* **Type**: `K` *extends* `"transform"` ? { `filter?`: [`HookFilter`](Interface.HookFilter.md) | `TopLevelFilterExpression`\[]; } : `K` *extends* `"load"` ? { `filter?`: `Pick`<[`HookFilter`](Interface.HookFilter.md), `"id"`> | `TopLevelFilterExpression`\[]; } : `K` *extends* `"resolveId"` ? { `filter?`: { `id?`: [`GeneralHookFilter`](TypeAlias.GeneralHookFilter.md)<`RegExp`>; } | `TopLevelFilterExpression`\[]; } : `K` *extends* `"renderChunk"` ? { `filter?`: `Pick`<[`HookFilter`](Interface.HookFilter.md), `"code"`> | `TopLevelFilterExpression`\[]; } : { }

## Type Parameters

### K

`K` *extends* keyof [`FunctionPluginHooks`](Interface.FunctionPluginHooks.md)
