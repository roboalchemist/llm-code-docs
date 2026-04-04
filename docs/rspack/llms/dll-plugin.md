# Source: https://rspack.dev/plugins/webpack/dll-plugin.md

CC 4.0 License> The content of this section is derived from the content of the following links and is subject to the CC BY 4.0 license.
> 
> - [https://webpack.js.org/plugins/dll-plugin/](https://webpack.js.org/plugins/dll-plugin/)
> 
> The following contents can be assumed to be the result of modifications and deletions based on the original contents if not specifically stated.
> 
> 


# DllPlugin

The `DllPlugin` is used in a separate rspack configuration exclusively to create a dll-only-bundle.

## Options

- **Type:**

```ts
type DllPluginOptions = {
  context?: string;
  entryOnly?: boolean;
  format?: boolean;
  name?: string;
  path: string;
  type?: string;
};
```

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `context` | `string` | The rspack compiler context | context of requests in the manifest file |
| `path` | `string` | undefined | absolute path to the manifest json file |
| `entryOnly` | `boolean` | `true` | if `true`, only entry points will be exposed |
| `format` | `boolean` | undefined | Whether or not format manifest json |
| `name` | `string` | undefined | The expose dll function name |
| `type` | `string` | undefined | type of the dll bundle |


## Examples

```js
new rspack.DllPlugin({
  path: path.resolve(__dirname, 'manifest.json'),
  name: '[name]_dll_lib',
});
```

The Plugin will create a `manifest.json` which is written to the given path.
It contains mappings from require and import requests to module ids.

The `manifest.json` is used by the [DllReferencePlugin](/plugins/webpack/dll-reference-plugin.md)

Combine this plugin with `output.library` options to expose the dll function.
