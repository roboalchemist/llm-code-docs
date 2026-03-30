# Source: https://rolldown.rs/reference/Interface.TransformOptions-1.md

---
url: /reference/Interface.TransformOptions-1.md
---
# Interface: TransformOptions

Options for transforming a code.

## Extends

* `BindingEnhancedTransformOptions`

## Properties

### assumptions?

* **Type**: `CompilerAssumptions`
* **Optional**

Set assumptions in order to produce smaller output.

#### Inherited from

`BindingEnhancedTransformOptions.assumptions`

***

### cwd?

* **Type**: `string`
* **Optional**

The current working directory. Used to resolve relative paths in other
options.

#### Inherited from

`BindingEnhancedTransformOptions.cwd`

***

### decorator?

* **Type**: `DecoratorOptions`
* **Optional**

Decorator plugin

#### Inherited from

`BindingEnhancedTransformOptions.decorator`

***

### define?

* **Type**: `Record`<`string`, `string`>
* **Optional**

Define Plugin

#### See

<https://oxc.rs/docs/guide/usage/transformer/global-variable-replacement#define>

#### Inherited from

`BindingEnhancedTransformOptions.define`

***

### helpers?

* **Type**: `Helpers`
* **Optional**

Behaviour for runtime helpers.

#### Inherited from

`BindingEnhancedTransformOptions.helpers`

***

### inject?

* **Type**: `Record`<`string`, `string` | \[`string`, `string`]>
* **Optional**

Inject Plugin

#### See

<https://oxc.rs/docs/guide/usage/transformer/global-variable-replacement#inject>

#### Inherited from

`BindingEnhancedTransformOptions.inject`

***

### inputMap?

* **Type**: `SourceMap`
* **Optional**

An input source map to collapse with the output source map.

#### Inherited from

`BindingEnhancedTransformOptions.inputMap`

***

### jsx?

* **Type**: `"preserve"` | `JsxOptions`
* **Optional**

Configure how TSX and JSX are transformed.

#### See

<https://oxc.rs/docs/guide/usage/transformer/jsx>

#### Inherited from

`BindingEnhancedTransformOptions.jsx`

***

### lang?

* **Type**: `"js"` | `"jsx"` | `"ts"` | `"tsx"` | `"dts"`
* **Optional**

Treat the source text as 'js', 'jsx', 'ts', 'tsx', or 'dts'.

#### Inherited from

`BindingEnhancedTransformOptions.lang`

***

### plugins?

* **Type**: `PluginsOptions`
* **Optional**

Third-party plugins to use.

#### See

<https://oxc.rs/docs/guide/usage/transformer/plugins>

#### Inherited from

`BindingEnhancedTransformOptions.plugins`

***

### sourcemap?

* **Type**: `boolean`
* **Optional**

Enable source map generation.

When `true`, the `sourceMap` field of transform result objects will be populated.

#### Default

```ts
false
```

#### Inherited from

`BindingEnhancedTransformOptions.sourcemap`

***

### sourceType?

* **Type**: `"module"` | `"commonjs"` | `"script"` | `"unambiguous"`
* **Optional**

Treat the source text as 'script', 'module', 'commonjs', or 'unambiguous'.

#### Inherited from

`BindingEnhancedTransformOptions.sourceType`

***

### target?

* **Type**: `string` | `string`\[]
* **Optional**

Sets the target environment for the generated JavaScript.

The lowest target is `es2015`.

Example:

* `'es2015'`
* `['es2020', 'chrome58', 'edge16', 'firefox57', 'node12', 'safari11']`

#### Default

`esnext` (No transformation)

#### See

<https://oxc.rs/docs/guide/usage/transformer/lowering#target>

#### Inherited from

`BindingEnhancedTransformOptions.target`

***

### tsconfig?

* **Type**: `boolean` | [`TsconfigRawOptions`](Interface.TsconfigRawOptions.md)
* **Optional**

Configure tsconfig handling.

* true: Auto-discover and load the nearest tsconfig.json
* TsconfigRawOptions: Use the provided inline tsconfig options

#### Inherited from

`BindingEnhancedTransformOptions.tsconfig`

***

### typescript?

* **Type**: `TypeScriptOptions`
* **Optional**

Configure how TypeScript is transformed.

#### See

<https://oxc.rs/docs/guide/usage/transformer/typescript>

#### Inherited from

`BindingEnhancedTransformOptions.typescript`
