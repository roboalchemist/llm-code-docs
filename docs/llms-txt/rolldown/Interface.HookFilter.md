# Source: https://rolldown.rs/reference/Interface.HookFilter.md

---
url: /reference/Interface.HookFilter.md
---
# Interface: HookFilter

A filter to be used to do a pre-test to determine whether the hook should be called.

See [Plugin Hook Filters page](/apis/plugin-api/hook-filters) for more details.

## Properties

### code?

* **Type**: [`GeneralHookFilter`](TypeAlias.GeneralHookFilter.md)<`string` | `RegExp`>
* **Optional**

A filter based on the module's code.

Only available for [`transform`](Interface.Plugin.md#transform) hook.

***

### id?

* **Type**: [`GeneralHookFilter`](TypeAlias.GeneralHookFilter.md)<`string` | `RegExp`>
* **Optional**

A filter based on the module `id`.

If the value is a string, it is treated as a glob pattern.
The string type is not available for [`resolveId`](Interface.Plugin.md#resolveid) hook.

#### Examples

Include all `id`s that contain `node_modules` in the path.

```js
{ id: '**'+'/node_modules/**' }
```

Include all `id`s that contain `node_modules` or `src` in the path.

```js
{ id: ['**'+'/node_modules/**', '**'+'/src/**'] }
```

Include all `id`s that start with `http`

```js
{ id: /^http/ }
```

Exclude all `id`s that contain `node_modules` in the path.

```js
{ id: { exclude: '**'+'/node_modules/**' } }
```

Formal pattern to define includes and excludes.

```js
{ id : {
  include: ['**'+'/foo/**', /bar/],
  exclude: ['**'+'/baz/**', /qux/]
}}
```

***

### moduleType?

* **Type**: [`ModuleTypeFilter`](TypeAlias.ModuleTypeFilter.md)
* **Optional**

A filter based on the module's `moduleType`.

Only available for [`transform`](Interface.Plugin.md#transform) hook.
