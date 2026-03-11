# Source: https://rolldown.rs/reference/Function.build.md

---
url: /reference/Function.build.md
---
# Function: build()

The API similar to esbuild's `build` function.

## Example

```js
import { build } from 'rolldown';

const result = await build({
  input: 'src/main.js',
  output: {
    file: 'bundle.js',
  },
});
console.log(result);
```

## Call Signature

* **Type**: (`options`: [`BuildOptions`](TypeAlias.BuildOptions.md)) => `Promise`<[`RolldownOutput`](Interface.RolldownOutput.md)>
* **Experimental**

Build a single output.

### Parameters

#### options

[`BuildOptions`](TypeAlias.BuildOptions.md)

The build options.

### Returns

`Promise`<[`RolldownOutput`](Interface.RolldownOutput.md)>

A Promise that resolves to the build output.

## Call Signature

* **Type**: (`options`: [`BuildOptions`](TypeAlias.BuildOptions.md)\[]) => `Promise`<[`RolldownOutput`](Interface.RolldownOutput.md)\[]>
* **Experimental**

Build multiple outputs **sequentially**.

### Parameters

#### options

[`BuildOptions`](TypeAlias.BuildOptions.md)\[]

The build options.

### Returns

`Promise`<[`RolldownOutput`](Interface.RolldownOutput.md)\[]>

A Promise that resolves to the build outputs for each option.
