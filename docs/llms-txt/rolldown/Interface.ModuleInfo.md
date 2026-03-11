# Source: https://rolldown.rs/reference/Interface.ModuleInfo.md

---
url: /reference/Interface.ModuleInfo.md
---
# Interface: ModuleInfo

## Extends

* [`ModuleOptions`](Interface.ModuleOptions.md)

## Properties

### code

* **Type**: `string` | `null`

The source code of the module.

`null` if external or not yet available.

***

### dynamicallyImportedIds

* **Type**: `string`\[]

The module ids dynamically imported by this module.

***

### dynamicImporters

* **Type**: `string`\[]

The ids of all modules that dynamically import this module.

***

### exports

* **Type**: `string`\[]

All exported variables

***

### id

* **Type**: `string`

The id of the module for convenience

***

### importedIds

* **Type**: `string`\[]

The module ids statically imported by this module.

***

### importers

* **Type**: `string`\[]

The ids of all modules that statically import this module.

***

### inputFormat

* **Type**: `"es"` | `"cjs"` | `"unknown"`
* **Experimental**

The detected format of the module, based on both its syntax and module definition
metadata (such as `package.json` `type` and file extensions like `.mjs`/`.cjs`/`.mts`/`.cts`).

* "esm" for ES modules (has `import`/`export` statements or is defined as ESM by module metadata)
* "cjs" for CommonJS modules (uses `module.exports`, `exports`, top-level `return`, or is defined as CommonJS by module metadata)
* "unknown" when the format could not be determined from either syntax or module definition metadata

***

### invalidate?

* **Type**: `boolean`
* **Optional**

#### Inherited from

[`ModuleOptions`](Interface.ModuleOptions.md).[`invalidate`](Interface.ModuleOptions.md#invalidate)

***

### isEntry

* **Type**: `boolean`

Whether this module is a user- or plugin-defined entry point.

***

### meta

* **Type**: [`CustomPluginOptions`](Interface.CustomPluginOptions.md)

See [Custom module meta-data section](/apis/plugin-api/inter-plugin-communication#custom-module-meta-data) for more details.

#### Inherited from

[`ModuleOptions`](Interface.ModuleOptions.md).[`meta`](Interface.ModuleOptions.md#meta)

***

### moduleSideEffects

* **Type**: `ModuleSideEffects`

#### Inherited from

[`ModuleOptions`](Interface.ModuleOptions.md).[`moduleSideEffects`](Interface.ModuleOptions.md#modulesideeffects)

***

### packageJsonPath?

* **Type**: `string`
* **Optional**

#### Inherited from

[`ModuleOptions`](Interface.ModuleOptions.md).[`packageJsonPath`](Interface.ModuleOptions.md#packagejsonpath)
