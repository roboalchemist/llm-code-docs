# Source: https://rolldown.rs/reference/Interface.PartialResolvedId.md

---
url: /reference/Interface.PartialResolvedId.md
---
# Interface: PartialResolvedId

## Extends

* `SpecifiedModuleOptions`.`Partial`<[`PartialNull`](TypeAlias.PartialNull.md)<[`ModuleOptions`](Interface.ModuleOptions.md)>>

## Properties

### external?

* **Type**: `boolean` | `"absolute"` | `"relative"`
* **Optional**

Whether this id should be treated as external.

Relative external ids, i.e. ids starting with `./` or `../`, will not be internally
converted to an absolute id and converted back to a relative id in the output,
but are instead included in the output unchanged.
If you want relative ids to be re-normalized and deduplicated instead, return
an absolute file system location as id and choose `external: "relative"`.

* If `true`, absolute ids will be converted to relative ids based on the user's choice for the [`makeAbsoluteExternalsRelative`](Interface.InputOptions.md#makeabsoluteexternalsrelative) option.
* If `'relative'`, absolute ids will always be converted to relative ids.
* If `'absolute'`, absolute ids will always be kept as absolute ids.

***

### id

* **Type**: `string`

***

### invalidate?

* **Type**: `boolean` | `null`
* **Optional**

#### Inherited from

[`ModuleOptions`](Interface.ModuleOptions.md).[`invalidate`](Interface.ModuleOptions.md#invalidate)

***

### meta?

* **Type**: [`CustomPluginOptions`](Interface.CustomPluginOptions.md) | `null`
* **Optional**

See [Custom module meta-data section](/apis/plugin-api/inter-plugin-communication#custom-module-meta-data) for more details.

#### Inherited from

[`ModuleOptions`](Interface.ModuleOptions.md).[`meta`](Interface.ModuleOptions.md#meta)

***

### moduleSideEffects?

* **Type**: `ModuleSideEffects`
* **Optional**

Indicates whether the module has side effects to Rolldown.

* If `false` is set and no other module imports anything from this module, then this module will not be included in the bundle even if the module would have side effects.
* If `true` is set, Rolldown will use its default algorithm to include all statements in the module that has side effects.
* If `"no-treeshake"` is set, treeshaking will be disabled for this module, and this module will be included in one of the chunks even if it is empty.

The precedence of this option is as follows (highest to lowest):

1. [`transform`](Interface.Plugin.md#transform) hook's returned `moduleSideEffects` option
2. [`load`](Interface.Plugin.md#load) hook's returned `moduleSideEffects` option
3. [`resolveId`](Interface.Plugin.md#resolveid) hook's returned `moduleSideEffects` option
4. [`treeshake.moduleSideEffects`](TypeAlias.TreeshakingOptions.md#modulesideeffects) option
5. `sideEffects` field in the `package.json` file
6. `true` (default)

#### Inherited from

`SpecifiedModuleOptions.moduleSideEffects`

***

### packageJsonPath?

* **Type**: `string` | `null`
* **Optional**

#### Inherited from

[`ModuleOptions`](Interface.ModuleOptions.md).[`packageJsonPath`](Interface.ModuleOptions.md#packagejsonpath)
