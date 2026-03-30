# Source: https://rolldown.rs/reference/TypeAlias.ExternalOptionFunction.md

---
url: /reference/TypeAlias.ExternalOptionFunction.md
---
# Type Alias: ExternalOptionFunction()

* **Type**: (`id`, `parentId`, `isResolved`) => `NullValue`<`boolean`>

## Parameters

### id

`string`

The id of the module being checked.

### parentId

The id of the module importing the id being checked.

`string` | `undefined`

### isResolved

`boolean`

Whether the id has been resolved.

## Returns

`NullValue`<`boolean`>

Whether the module should be treated as external.
