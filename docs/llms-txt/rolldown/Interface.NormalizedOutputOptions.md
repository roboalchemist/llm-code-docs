# Source: https://rolldown.rs/reference/Interface.NormalizedOutputOptions.md

---
url: /reference/Interface.NormalizedOutputOptions.md
---
# Interface: NormalizedOutputOptions

## Properties

### assetFileNames

* **Type**: `string` | (`chunkInfo`) => `string`

#### See

[`assetFileNames`](Interface.OutputOptions.md#assetfilenames)

***

### banner()

* **Type**: (`chunk`) => `string` | `Promise`<`string`>

#### Parameters

##### chunk

[`RenderedChunk`](Interface.RenderedChunk.md)

#### Returns

`string` | `Promise`<`string`>

#### See

[`banner`](Interface.OutputOptions.md#banner)

***

### chunkFileNames

* **Type**: `string` | (`chunkInfo`) => `string`

#### See

[`chunkFileNames`](Interface.OutputOptions.md#chunkfilenames)

***

### codeSplitting

* **Type**: `boolean`

#### See

[`codeSplitting`](Interface.OutputOptions.md#codesplitting)

***

### comments

* **Type**: `Required`<[`CommentsOptions`](Interface.CommentsOptions.md)>

#### See

[`comments`](Interface.OutputOptions.md#comments)

***

### dir

* **Type**: `string` | `undefined`

#### See

[`dir`](Interface.OutputOptions.md#dir)

***

### dynamicImportInCjs

* **Type**: `boolean`

#### See

[`dynamicImportInCjs`](Interface.OutputOptions.md#dynamicimportincjs)

***

### entryFileNames

* **Type**: `string` | (`chunkInfo`) => `string`

#### See

[`entryFileNames`](Interface.OutputOptions.md#entryfilenames)

***

### esModule

* **Type**: `boolean` | `"if-default-prop"`

#### See

[`esModule`](Interface.OutputOptions.md#esmodule)

***

### exports

* **Type**: `NonNullable`<`"auto"` | `"named"` | `"default"` | `"none"` | `undefined`>

#### See

[`exports`](Interface.OutputOptions.md#exports)

***

### extend

* **Type**: `boolean`

#### See

[`extend`](Interface.OutputOptions.md#extend)

***

### externalLiveBindings

* **Type**: `boolean`

#### See

[`externalLiveBindings`](Interface.OutputOptions.md#externallivebindings)

***

### file

* **Type**: `string` | `undefined`

#### See

[`file`](Interface.OutputOptions.md#file)

***

### footer()

* **Type**: (`chunk`) => `string` | `Promise`<`string`>

#### Parameters

##### chunk

[`RenderedChunk`](Interface.RenderedChunk.md)

#### Returns

`string` | `Promise`<`string`>

#### See

[`footer`](Interface.OutputOptions.md#footer)

***

### format

* **Type**: [`InternalModuleFormat`](TypeAlias.InternalModuleFormat.md)

#### See

[`format`](Interface.OutputOptions.md#format)

***

### globals

* **Type**: `Record`<`string`, `string`> | (`name`) => `string`

#### See

[`globals`](Interface.OutputOptions.md#globals)

***

### hashCharacters

* **Type**: `"base64"` | `"base36"` | `"hex"`

#### See

[`hashCharacters`](Interface.OutputOptions.md#hashcharacters)

***

### ~~inlineDynamicImports~~

* **Type**: `boolean`

#### Deprecated

Use `codeSplitting` instead.

***

### intro()

* **Type**: (`chunk`) => `string` | `Promise`<`string`>

#### Parameters

##### chunk

[`RenderedChunk`](Interface.RenderedChunk.md)

#### Returns

`string` | `Promise`<`string`>

#### See

[`intro`](Interface.OutputOptions.md#intro)

***

### ~~legalComments~~

* **Type**: `"none"` | `"inline"`

#### Deprecated

Use `comments.legal` instead.

#### See

[`legalComments`](Interface.OutputOptions.md#legalcomments)

***

### minify

* **Type**: `false` | [`MinifyOptions`](TypeAlias.MinifyOptions.md) | `"dce-only"`

#### See

[`minify`](Interface.OutputOptions.md#minify)

***

### minifyInternalExports?

* **Type**: `boolean`
* **Optional**

#### See

[`minifyInternalExports`](Interface.OutputOptions.md#minifyinternalexports)

***

### name

* **Type**: `string` | `undefined`

#### See

[`name`](Interface.OutputOptions.md#name)

***

### outro()

* **Type**: (`chunk`) => `string` | `Promise`<`string`>

#### Parameters

##### chunk

[`RenderedChunk`](Interface.RenderedChunk.md)

#### Returns

`string` | `Promise`<`string`>

#### See

[`outro`](Interface.OutputOptions.md#outro)

***

### paths

* **Type**: `Record`<`string`, `string`> | `PathsFunction` | `undefined`

#### See

[`paths`](Interface.OutputOptions.md#paths)

***

### plugins

* **Type**: [`RolldownPlugin`](TypeAlias.RolldownPlugin.md)\[]

#### See

[`plugins`](Interface.OutputOptions.md#plugins)

***

### polyfillRequire

* **Type**: `boolean`

#### See

[`polyfillRequire`](Interface.OutputOptions.md#polyfillrequire)

***

### postBanner()

* **Type**: (`chunk`) => `string` | `Promise`<`string`>

#### Parameters

##### chunk

[`RenderedChunk`](Interface.RenderedChunk.md)

#### Returns

`string` | `Promise`<`string`>

#### See

[`postBanner`](Interface.OutputOptions.md#postbanner)

***

### postFooter()

* **Type**: (`chunk`) => `string` | `Promise`<`string`>

#### Parameters

##### chunk

[`RenderedChunk`](Interface.RenderedChunk.md)

#### Returns

`string` | `Promise`<`string`>

#### See

[`postFooter`](Interface.OutputOptions.md#postfooter)

***

### preserveModules

* **Type**: `boolean`

#### See

[`preserveModules`](Interface.OutputOptions.md#preservemodules)

***

### preserveModulesRoot?

* **Type**: `string`
* **Optional**

#### See

[`preserveModulesRoot`](Interface.OutputOptions.md#preservemodulesroot)

***

### sourcemap

* **Type**: `boolean` | `"inline"` | `"hidden"`

#### See

[`sourcemap`](Interface.OutputOptions.md#sourcemap)

***

### sourcemapBaseUrl

* **Type**: `string` | `undefined`

#### See

[`sourcemapBaseUrl`](Interface.OutputOptions.md#sourcemapbaseurl)

***

### sourcemapDebugIds

* **Type**: `boolean`

#### See

[`sourcemapDebugIds`](Interface.OutputOptions.md#sourcemapdebugids)

***

### sourcemapIgnoreList

* **Type**: `boolean` | `string` | `RegExp` | (`relativeSourcePath`, `sourcemapPath`) => `boolean` | `undefined`

#### Type Declaration

`boolean`

`string` | `RegExp`

(`relativeSourcePath`, `sourcemapPath`) => `boolean`

#### Parameters

##### relativeSourcePath

`string`

The relative path from the generated `.map` file to the corresponding source file.

##### sourcemapPath

`string`

The fully resolved path of the generated sourcemap file.

#### Returns

`boolean`

`undefined`

#### See

[`sourcemapIgnoreList`](Interface.OutputOptions.md#sourcemapignorelist)

***

### sourcemapPathTransform

* **Type**: (`relativeSourcePath`, `sourcemapPath`) => `string` | `undefined`

#### Type Declaration

(`relativeSourcePath`, `sourcemapPath`) => `string`

#### Parameters

##### relativeSourcePath

`string`

The relative path from the generated `.map` file to the corresponding source file.

##### sourcemapPath

`string`

The fully resolved path of the generated sourcemap file.

#### Returns

`string`

`undefined`

#### See

[`sourcemapPathTransform`](Interface.OutputOptions.md#sourcemappathtransform)

***

### topLevelVar?

* **Type**: `boolean`
* **Optional**

#### See

[`topLevelVar`](Interface.OutputOptions.md#toplevelvar)

***

### virtualDirname

* **Type**: `string`

#### See

[`virtualDirname`](Interface.OutputOptions.md#virtualdirname)
