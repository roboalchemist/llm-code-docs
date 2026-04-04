# Source: https://rspack.dev/api/javascript-api/stats.md

# Source: https://rspack.dev/config/stats.md

CC 4.0 License> The content of this section is derived from the content of the following links and is subject to the CC BY 4.0 license.
> 
> - [https://webpack.js.org/configuration/stats/](https://webpack.js.org/configuration/stats/)
> 
> The following contents can be assumed to be the result of modifications and deletions based on the original contents if not specifically stated.
> 
> 


# Stats

Generate packaging information that can be used to analyze module dependencies and optimize compilation speed.

:::info Output JSON file of stats

- Using `@rspack/cli`, `rspack build --json stats.json`.
- Using Rspack's JavaScript API, `stats.toJson(options)`, `stats.toString(options)`.

:::

- Type: `boolean | string | Object`
- Default:`{"preset":"errors-warnings","timings":true}`


## Stats presets

| Preset              | Description                                                    |
| ------------------- | -------------------------------------------------------------- |
| `'normal'` (`true`) | Output by default value of stats options                       |
| `'none'` (`false`)  | Output nothing                                                 |
| `'verbose'`         | Output everything                                              |
| `'errors-only'`     | Output only error-related information                          |
| `'errors-warnings'` | Output only error and warning related information              |
| `'minimal'`         | Output only when errors or new compilation happen              |
| `'detailed'`        | Output everything except `chunkModules` and `chunkRootModules` |
| `'summary'`         | Output only the summary information                            |

You can specify exactly which packing information to output, all the following fields are optional.

## Preset options

### stats.all

- Type: `boolean`
- Default:`undefined`


A fallback value for stats options when an option is not defined. It has precedence over local Rspack defaults.

:::warning
Enabling `stats.all` will lead to a large amount of data transmission between Rust and JavaScript, which will significantly increase the time consumption for stats generation. Please use it with caution.
:::

### stats.preset

- Type: `boolean | string`
- Default:`undefined`


Sets the [preset](/config/stats.md#stats-presets) for the type of information that gets displayed. It is useful for [extending stats behaviours](/config/stats.md#extending-stats-behaviours).

## Asset options

### stats.assets

- Type: `boolean`
- Default:`true`


Whether to display the asset information. See [Asset Object](/api/javascript-api/stats-json.md#asset-object) for more details.

### stats.assetsSort

- Type: `string`
- Default:`"id"`


Sort the assets by a given field. All of the [sorting fields](/config/stats.md#sorting-fields) are allowed to be used. Use `!` prefix in the value to reverse the sort order by a given field.

### stats.assetsSpace

- Type: `number`
- Default:`15`


How many items of assets should be displayed (groups will be collapsed to fit this space).

### stats.relatedAssets

- Type: `boolean`
- Default:`false`


Whether to display information about assets that are related to other assets (like SourceMaps for assets).

### stats.excludeAssets

- Type: `Array<string | RegExp | (name: string) => boolean> | string | RegExp | (name: string) => boolean | false`
- Default:`false`


Exclude the matching assets information. This can be done with a string, a RegExp, a function that is getting the assets name as an argument and returns a boolean. `stats.excludeAssets` can be an array of any of the above.

### stats.cachedAssets

- Type: `boolean`
- Default:`true`


Whether to display information about the cached assets. Setting `stats.cachedAssets` to `false` will tell stats to only show the emitted files (not the ones that were built).

## Asset grouping options

### stats.groupAssetsByChunk

- Type: `boolean`


Whether to group assets by how their are related to chunks.

### stats.groupAssetsByEmitStatus

- Type: `boolean`


Whether to group assets by their status (emitted, compared for emit or cached).

### stats.groupAssetsByExtension

- Type: `boolean`


Whether to group assets by their extension.

### stats.groupAssetsByInfo

- Type: `boolean`


Whether to group assets by their asset info (immutable, development, hotModuleReplacement, etc).

### stats.groupAssetsByPath

- Type: `boolean`


Whether to group assets by their asset path.

## Chunk options

### stats.chunks

- Type: `boolean`
- Default:`true`


Whether to display information about the chunk, see [chunk object](/api/javascript-api/stats-json.md#chunk-object) for more details.

### stats.chunkModules

- Type: `boolean`
- Default:`true`


Whether to display information about the built modules to information about the chunk.

### stats.chunkModulesSpace

- Type: `number`
- Default:`10`


How many items of chunk modules should be displayed (groups will be collapsed to fit this space).

### stats.dependentModules

- Type: `boolean`
- Default:`false`


Whether to display chunk modules that are dependencies of other modules of the chunk.

### stats.chunkOrigins

- Type: `boolean`
- Default:`true`


Whether to display information about the origins of chunks and chunk merging.

### stats.chunkRelations

- Type: `boolean`
- Default:`false`


Whether to display chunk parents, children and siblings.

### stats.chunksSort

- Type: `string`
- Default:`"id"`


Sort the chunks by a given field. All of the [sorting fields](/config/stats.md#sorting-fields) are allowed to be used. Use `!` prefix in the value to reverse the sort order by a given field.

### stats.ids

- Type: `boolean`
- Default:`false`


Whether to display IDs of modules and chunks.

## ChunkGroup options

### stats.chunkGroups

- Type: `boolean`
- Default:`true`


Whether to display information about the `namedChunkGroups`, see [chunk group object](/api/javascript-api/stats-json.md#entrychunkgroup-object) for more details.

### stats.chunkGroupAuxiliary

- Type: `boolean`
- Default:`true`


Whether to display auxiliary assets in chunk groups.

### stats.chunkGroupChildren

- Type: `boolean`
- Default:`true`


Whether to display children of the chunk groups (e.g. prefetched, preloaded chunks and assets).

### stats.chunkGroupMaxAssets

- Type: `number`
- Default:`5`


How many assets should be displayed in chunk groups.

### stats.entrypoints

- Type: `boolean | 'auto'`
- Default:`false`


Whether to display the entry points with the corresponding bundles, , see [entrypoint object](/api/javascript-api/stats-json.md#entrychunkgroup-object) for more details.

When `stats.entrypoints` is set to `'auto'`, Rspack will decide automatically whether to display the entry points in the stats output.

## Module options

### stats.modules

- Type: `boolean`
- Default:`true`


Whether to display information about the built modules, see [module object](/api/javascript-api/stats-json.md#module-object) for more details.

### stats.moduleTrace

- Type: `boolean`
- Default:`true`


Whether to display dependencies and the origin of warnings/errors.

### stats.moduleAssets

- Type: `boolean`
- Default:`true`


Whether to add information about assets inside modules.

### stats.modulesSpace

- Type: `number`
- Default:`15`


How many items of modules should be displayed (groups will be collapsed to fit this space).

### stats.modulesSort

- Type: `string`
- Default:`"id"`


Sort the modules by a given field. All of the [sorting fields](/config/stats.md#sorting-fields) are allowed to be used. Use `!` prefix in the value to reverse the sort order by a given field.

### stats.reasons

- Type: `boolean`
- Default:`true`


Whether to display information about the reasons of why modules are included.

### stats.reasonsSpace

- Type: `number`
- Default:`1000`


How many characters should the reasons be displayed (groups will be collapsed to fit this space).

### stats.source

- Type: `boolean`
- Default:`false`


Whether to display the source code of modules.

### stats.depth

- Type: `boolean`
- Default:`false`


Whether to display the distance from the entry point for each module.

### stats.orphanModules

- Type: `boolean`
- Default:`false`


Whether to display the orphan modules.

> A module is an orphan if it is not included in any chunk.

### stats.runtimeModules

- Type: `boolean`
- Default:`true`


Whether to display information about runtime modules.

> The runtime modules are built-in modules of Rspack, used to provide various runtime capabilities.

### stats.cachedModules

- Type: `boolean`
- Default:`true`


Whether to display information about cached (not built) modules.

### stats.excludeModules

- Type: `Array<string | RegExp | (name: string) => boolean> | string | RegExp | (name: string) => boolean | false`
- Default:`false`


Exclude the matching modules information. This can be done with a string, a RegExp, a function that is getting the modules name as an argument and returns a boolean. `stats.excludeAssets` can be an array of any of the above.

### stats.nestedModules

- Type: `boolean`
- Default:`true`


Whether to display information about modules nested in other modules (like with module concatenation).

### stats.nestedModulesSpace

- Type: `number`
- Default:`10`


How many items of nested modules should be displayed (groups will be collapsed to fit this space).

## Module grouping options

### stats.groupModulesByAttributes

- Type: `boolean`


Whether to group modules by their attributes (errors, warnings, assets, optional, orphan, or dependent).

### stats.groupModulesByCacheStatus

- Type: `boolean`


Whether to group modules by their cache status (cached or built and cacheable).

### stats.groupModulesByExtension

- Type: `boolean`


Whether to group modules by their extension.

### stats.groupModulesByPath

- Type: `boolean`


Whether to group modules by their path.

### stats.groupModulesByType

- Type: `boolean`


Whether to group modules by their type.

### stats.groupModulesByLayer

- Type: `boolean`


Whether to group modules by their layer.

### stats.groupReasonsByOrigin

- Type: `boolean`


Group reasons by their origin module to avoid large set of reasons.

## Optimization options

### stats.providedExports

- Type: `boolean`
- Default:`false`


Whether to display the exports of the modules.

### stats.usedExports

- Type: `boolean`
- Default:`false`


Whether to display which exports of a module are used.

### stats.optimizationBailout

- Type: `boolean`
- Default:`false`


Whether to display the reasons why optimization bailed out for modules.

## Error/Warning options

### stats.errors

- Type: `boolean`
- Default:`true`


Whether to display the errors.

### stats.errorsCount

- Type: `boolean`
- Default:`true`


Whether to display the errors count.

### stats.errorDetails

- Type: `boolean`
- Default:`false`


Whether to display the details to the errors. It defaults to `'auto'` which will show error details when there're only 2 or less errors.

### stats.errorsSpace

- Type: `number`
- Default:`5`


How many lines should an error be displayed.

### stats.errorStack

- Type: `boolean`
- Default:`true`


Whether to display stack trace of errors.

### stats.warnings

- Type: `boolean`
- Default:`true`


Whether to display the warnings.

### stats.warningsCount

- Type: `boolean`
- Default:`true`


Whether to display the warnings count.

### stats.warningsSpace

- Type: `number`
- Default:`5`


How many lines should a warning be displayed.

## Logging options

### stats.logging

- Type: `'info' | 'none' | 'error' | 'warn' | 'log' | 'verbose' | boolean`


Whether to add logging output:

- `'none'`, `false`: disable logging
- `'error'`: errors only
- `'warn'`: errors and warnings only
- `'info'`: errors, warnings, and info messages
- `'log'`, `true`: errors, warnings, info messages, log messages, groups, clears. Collapsed groups are displayed in a collapsed state.
- `'verbose'`: log everything except debug and trace. Collapsed groups are displayed in expanded state.

### stats.loggingDebug

- Type: `Array<string | RegExp | function (name) => boolean>`


Whether to display the debug information of the specified [loggers](/api/javascript-api/logger.md) such as Plugins or Loaders. When `stats.logging` is set to `false`, `stats.loggingDebug` option is ignored.

```js title="rspack.config.mjs"
export default {
  //...
  stats: {
    loggingDebug: [
      'MyPlugin',
      /rspack/, // To get core logging
    ],
  },
};
```

### stats.loggingTrace

- Type: `boolean`
- Default:`true`


Whether to display stack traces in the logging output for errors, warnings and traces.

### stats.colors

- Type: `boolean`
- Default:`false`


Whether to output in the different colors.

Defaults to `true` when executing `rspack build` in an environment that supports color output.

## Compilation options

### stats.hash

- Type: `boolean`
- Default:`true`


Whether to display information about the hash of the compilation.

### stats.env

- Type: `boolean`
- Default:`false`


Whether to display the `--env` information.

### stats.builtAt

- Type: `boolean`
- Default:`true`


Whether to display the build date and the build time information.

### stats.version

- Type: `boolean`
- Default:`true`


Whether to add information about the Rspack version used.

### stats.context

- Type: `string`


Whether to display the [base directory](/config/context.md) as an absolute path for shortening the module specifier.

### stats.publicPath

- Type: `boolean`
- Default:`true`


Whether to display the [`publicPath`](/config/output.md#outputpublicpath).

### stats.outputPath

- Type: `boolean`
- Default:`true`


Whether to display the [`output.path`](/config/output.md#outputpath).

### stats.children

- Type: `boolean`
- Default:`true`


Whether to display the [`output.path`](/config/output.md#outputpath).

### stats.performance

- Type: `boolean`
- Default:`true`


Whether to display performance hint when the file size exceeds [`performance.maxAssetSize`](/config/performance.md#performancemaxassetsize).

### stats.timings

- Type: `boolean`
- Default:`true`


Whether to display the timing information.

## Sorting fields

For `assetsSort`, `chunksSort` and `modulesSort` there are several possible fields that you can sort items by:

- `'id'`: the item's id, an item is an asset, a module or a chunk.
- `'name'`: the item's name that was assigned to it upon importing.
- `'size'`: the size of item in bytes.
- `'chunks'`: what chunks the item originates from (for example, if there are multiple subchunks for one chunk: the subchunks will be grouped according to their main chunk).
- `'errors'`: number of errors in items.
- `'warnings'`: number of warnings in items.
- `'failed'`: whether the item has failed compilation.
- `'cacheable'`: whether the item is cacheable.
- `'built'`: whether the item has been built.
- `'prefetched'`: whether the item will be prefetched.
- `'optional'`: whether the item is optional.
- `'identifier'`: identifier of the item.
- `'index'`: item's processing index.
- `'issuer'`: the identifier of the issuer.
- `'issuerId'`: the id of the issuer.
- `'issuerName'`: the name of the issuer.
- `'issuerPath'`: the full issuer path.

## Extending stats behaviours

If you want to use the preset output behavior but want to output more or less of individual fields, you can customize the output behavior of the fields after specifying preset or all.

For example, only the error and the reason why the module was introduced are output.

```js title="rspack.config.mjs"
export default {
  stats: {
    preset: 'errors-only',
    reasons: true,
  },
};
```
