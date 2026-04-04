# Source: https://rspack.dev/plugins/webpack/javascript-modules-plugin.md

# JavascriptModulesPlugin

[Added in v1.0.0-alpha.0](https://github.com/web-infra-dev/rspack/releases/tag/v1.0.0-alpha.0)
Handles the bundling of JavaScript, usually used to access the [hooks of the JavascriptModulesPlugin](/api/plugin-api/javascript-modules-plugin-hooks.md):

```js
class MyJsMinimizerPlugin {
  apply(compiler) {
    compiler.hooks.compilation.tap(MyJsMinimizerPlugin.name, (compilation) => {
      // Access the chunkHash hooks of JavascriptModulesPlugin
      const hooks =
        compiler.rspack.javascript.JavascriptModulesPlugin.getCompilationHooks(
          compilation,
        );
      // Since the JS chunk has been optimized and its content has changed, the chunk hash for the JS chunk needs to be updated
      hooks.chunkHash.tap(MyJsMinimizerPlugin.name, (chunk, hash) => {
        hash.update(`minimized by ${MyJsMinimizerPlugin.name}`);
      });
      // Optimize the JS chunk
      compilation.hooks.processAssets.tap(
        MyJsMinimizerPlugin.name,
        (assets) => {
          optimize(assets);
        },
      );
    });
  }
}
```
