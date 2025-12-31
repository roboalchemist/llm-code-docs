# Source: https://rspack.dev/plugins/webpack/runtime-chunk-plugin.md

# RuntimeChunkPlugin

Used to control how the runtime chunk is generated, it is used by [`optimization.runtimeChunk`](/config/optimization.md#optimizationruntimechunk) under the hood.

## Options

### name

Used to configure the name of the runtime chunk; it can be a string or a function that returns a string, where the function parameter is the name of the entry.

* **Type:** `string | ((entrypoint: { name: string }) => string)`

```js
new rspack.optimize.RuntimeChunkPlugin({
  name: ({ name }) => `runtime~${name}`,
});
```
