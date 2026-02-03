# Source: https://rspack.dev/config/performance.md

CC 4.0 License> The content of this section is derived from the content of the following links and is subject to the CC BY 4.0 license.
> 
> - [https://webpack.js.org/configuration/performance/](https://webpack.js.org/configuration/performance/)
> 
> The following contents can be assumed to be the result of modifications and deletions based on the original contents if not specifically stated.
> 
> 


# Performance

These options allows you to control how Rspack notifies you of assets and entry points that exceed a specific file limit.

## performance

- Type: `false | object`


Configure how performance hints are shown. For example if you have an asset that is over 250kb, Rspack will emit a warning notifying you of this.

### performance.assetFilter

- Type: `(assetFilename: string) => boolean`


This property allows Rspack to control what files are used to calculate performance hints.

### performance.hints

- Type: `false | 'error' | 'warning'`
- Default:[production mode](/config/mode#production) is`warning`, [development mode](/config/mode#development) is`false`


Turns hints on/off. In addition, tells Rspack to throw either an error or a warning when hints are found.

### performance.maxAssetSize

- Type: `number`
- Default:`250000`


An asset is any emitted file from Rspack. This option controls when Rspack emits a performance hint based on individual asset size in bytes.

### performance.maxEntrypointSize

- Type: `number`
- Default:`250000`


An entry point represents all assets that would be utilized during initial load time for a specific entry. This option controls when Rspack should emit performance hints based on the maximum entry point size in bytes.
