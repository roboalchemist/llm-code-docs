# Source: https://rolldown.rs/reference/Interface.TsconfigCompilerOptions.md

---
url: /reference/Interface.TsconfigCompilerOptions.md
---
# Interface: TsconfigCompilerOptions

TypeScript compiler options for inline tsconfig configuration.

## Properties

### emitDecoratorMetadata?

* **Type**: `boolean`
* **Optional**

Enables decorator metadata emission.

***

### experimentalDecorators?

* **Type**: `boolean`
* **Optional**

Enables experimental decorators.

***

### ~~importsNotUsedAsValues?~~

* **Type**: `"error"` | `"preserve"` | `"remove"`
* **Optional**

#### Deprecated

Use verbatimModuleSyntax instead.

***

### jsx?

* **Type**: `"react"` | `"react-jsx"` | `"preserve"` | `"react-jsxdev"` | `"react-native"`
* **Optional**

Specifies the JSX factory function to use.

***

### jsxFactory?

* **Type**: `string`
* **Optional**

Specifies the JSX factory function.

***

### jsxFragmentFactory?

* **Type**: `string`
* **Optional**

Specifies the JSX fragment factory function.

***

### jsxImportSource?

* **Type**: `string`
* **Optional**

Specifies the module specifier for JSX imports.

***

### ~~preserveValueImports?~~

* **Type**: `boolean`
* **Optional**

#### Deprecated

Use verbatimModuleSyntax instead.

***

### target?

* **Type**: `string`
* **Optional**

The ECMAScript target version.

***

### useDefineForClassFields?

* **Type**: `boolean`
* **Optional**

Configures how class fields are emitted.

***

### verbatimModuleSyntax?

* **Type**: `boolean`
* **Optional**

Preserves module structure of imports/exports.
