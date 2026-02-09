# Source: https://rspack.dev/plugins/webpack/no-emit-on-errors-plugin.md

# NoEmitOnErrorsPlugin

[Added in v1.0.0](https://github.com/web-infra-dev/rspack/releases/tag/v1.0.0)
This plugin is used to prevent the assets emitting when there are compilation errors. [`optimization.emitOnErrors`](/config/optimization.md#optimizationemitonerrors) uses this plugin.

```js
new rspack.NoEmitOnErrorsPlugin();
```
