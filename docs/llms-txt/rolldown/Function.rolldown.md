# Source: https://rolldown.rs/reference/Function.rolldown.md

---
url: /reference/Function.rolldown.md
---
# Function: rolldown()

* **Type**: (`input`: [`InputOptions`](Interface.InputOptions.md)) => `Promise`<[`RolldownBuild`](Interface.RolldownBuild.md)>

The API compatible with Rollup's `rollup` function.

Unlike Rollup, the module graph is not built until the methods of the bundle object are called.

## Parameters

### input

[`InputOptions`](Interface.InputOptions.md)

The input options object.

## Returns

`Promise`<[`RolldownBuild`](Interface.RolldownBuild.md)>

A Promise that resolves to a bundle object.

## Example

```js
import { rolldown } from 'rolldown';

let bundle, failed = false;
try {
  bundle = await rolldown({
    input: 'src/main.js',
  });
  await bundle.write({
    format: 'esm',
  });
} catch (e) {
  console.error(e);
  failed = true;
}
if (bundle) {
  await bundle.close();
}
process.exitCode = failed ? 1 : 0;
```
