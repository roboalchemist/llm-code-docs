# Source: https://rolldown.rs/reference/Interface.SourceDescription.md

---
url: /reference/Interface.SourceDescription.md
---
# Interface: SourceDescription

## Extends

* `SpecifiedModuleOptions`.`Partial`<[`PartialNull`](TypeAlias.PartialNull.md)<[`ModuleOptions`](Interface.ModuleOptions.md)>>

## Properties

### code

* **Type**: `string`

***

### invalidate?

* **Type**: `boolean` | `null`
* **Optional**

#### Inherited from

[`ModuleOptions`](Interface.ModuleOptions.md).[`invalidate`](Interface.ModuleOptions.md#invalidate)

***

### map?

* **Type**: `null` | `string` | [`ExistingRawSourceMap`](Interface.ExistingRawSourceMap.md)
* **Optional**

The source map for the transformation.

If the transformation does not move code, you can preserve existing sourcemaps by setting this to `null`.

See [Source Code Transformations section](/apis/plugin-api/transformations#source-code-transformations) for more details.

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

### moduleType?

* **Type**: [`ModuleType`](TypeAlias.ModuleType.md)
* **Optional**

***

### packageJsonPath?

* **Type**: `string` | `null`
* **Optional**

#### Inherited from

[`ModuleOptions`](Interface.ModuleOptions.md).[`packageJsonPath`](Interface.ModuleOptions.md#packagejsonpath)
