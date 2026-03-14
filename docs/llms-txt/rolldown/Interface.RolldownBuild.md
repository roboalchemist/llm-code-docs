# Source: https://rolldown.rs/reference/Interface.RolldownBuild.md

---
url: /reference/Interface.RolldownBuild.md
---
# Interface: RolldownBuild

The bundle object returned by [`rolldown`](Function.rolldown.md) function.

## Accessors

### closed

#### Get Signature

* **Type**: () => `boolean`

Whether the bundle has been closed.

If the bundle is closed, calling other methods will throw an error.

##### Returns

`boolean`

## Methods

### close()

* **Type**: () => `Promise`<`void`>

Close the bundle and free resources.

This method is called automatically when using `using` syntax.

#### Returns

`Promise`<`void`>

#### Example

```js
import { rolldown } from 'rolldown';

{
  using bundle = await rolldown({ input: 'src/main.js' });
  const output = await bundle.generate({ format: 'esm' });
  console.log(output);
  // bundle.close() is called automatically here
}
```

***

### generate()

* **Type**: (`outputOptions`: [`OutputOptions`](Interface.OutputOptions.md)) => `Promise`<[`RolldownOutput`](Interface.RolldownOutput.md)>

Generate bundles in-memory.

If you directly want to write bundles to disk, use the [`write`](#write) method instead.

#### Parameters

##### outputOptions?

[`OutputOptions`](Interface.OutputOptions.md) = `{}`

The output options.

#### Returns

`Promise`<[`RolldownOutput`](Interface.RolldownOutput.md)>

The generated bundle.

#### Throws

[`BundleError`](TypeAlias.BundleError.md) When an error occurs during the build.

***

### write()

* **Type**: (`outputOptions`: [`OutputOptions`](Interface.OutputOptions.md)) => `Promise`<[`RolldownOutput`](Interface.RolldownOutput.md)>

Generate and write bundles to disk.

If you want to generate bundles in-memory, use the [`generate`](#generate) method instead.

#### Parameters

##### outputOptions?

[`OutputOptions`](Interface.OutputOptions.md) = `{}`

The output options.

#### Returns

`Promise`<[`RolldownOutput`](Interface.RolldownOutput.md)>

The generated bundle.

#### Throws

[`BundleError`](TypeAlias.BundleError.md) When an error occurs during the build.
