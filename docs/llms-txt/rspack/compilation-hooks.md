# Source: https://rspack.dev/api/plugin-api/compilation-hooks.md

# Compilation hooks

Compilation hooks are the primary extension method for Rspack plugins. These hooks enable developers to intervene at various stages of the build process.

This document lists the available Compilation hooks in Rspack, detailing their triggering timing, parameters, and usage examples.

:::tip
See the [Compilation](/api/javascript-api/compilation.md) for more information about the Compilation object.
:::

:::info
The main compilation logic of Rspack runs on the Rust side. For factors such as stability, performance, and architecture, after the Rust side compilation objects are transferred to the JavaScript side when using hooks, the modifications on these objects will not be synchronized to the Rust side. Therefore, most of hooks are "read-only".
:::

## Overview


## `buildModule`

Read-only
Triggered before a module build has started.

- **Type:** `SyncHook<[Module]>`
- **Arguments:**
  - `Module`: module instance

Module.ts
## `executeModule`

Read-only
If there exists compiled-time execution modules, this hook will be called when they are executed.

- **Type:** `SyncHook<[ExecuteModuleArgument, ExecuteModuleContext]>`
- **Arguments:**
  - `ExecuteModuleArgument`: arguments of compiled-time execution module
  - `ExecuteModuleContext`: context of compiled-time execution module

ExecuteModuleArgument.tsExecuteModuleContext.ts
## `succeedModule`

Read-only
Executed when a module has been built successfully.

- **Type:** `SyncHook<[Module]>`
- **Arguments:**
  - `Module`: module instance

Module.ts
## `finishModules`

Read-only
Called when all modules have been built without errors.

- **Type:** `AsyncSeriesHook<[Module[]]>`
- **Arguments:**
  - `Module[]`: List of module instances

Module.ts
## `seal`

Called when the compilation stops accepting new modules and starts to optimize modules.

- **Type:** `SyncHook<[]>`

## `optimizeModules`

Read-only
Called at the beginning of the module optimization phase.

- **Type:** `SyncBailHook<[Module[]]>`
- **Arguments:**
  - `Module[]`: list of module instances

Module.ts
## `afterOptimizeModules`

Read-only
Called after modules optimization has completed.

- **Type:** `SyncBailHook<[Module[]]>`
- **Arguments:**
  - `Module[]`: list of module instances

Module.ts
## `optimizeTree`

Read-only
Called before optimizing the dependency tree.

- **Type:** `AsyncSeriesHook<[Chunk[], Module[]]>`
- **Arguments:**
  - `Chunk[]`: list of chunk instances
  - `Module[]`: list of module instances

Chunk.tsModule.ts
## `optimizeChunkModules`

Read-only
Called after the tree optimization, at the beginning of the chunk modules optimization.

- **Type:** `AsyncSeriesBailHook<[Chunk[], Module[]]>`
- **Arguments:**
  - `Chunk[]`: list of chunk instances
  - `Module[]`: list of module instances

Chunk.tsModule.ts
## `additionalTreeRuntimeRequirements`

Called after the tree runtime requirements collection.

- **Type:** `SyncHook<[Chunk, Set<RuntimeGlobals>]>`
- **Arguments:**
  - `Chunk`: chunk instance
  - `Set<RuntimeGlobals>`: runtime requirements

Additional builtin runtime modules can be added here by modifying the runtime requirements set.

```js title="rspack.config.mjs"
export default {
  entry: './index.js',
  plugins: [
    {
      apply(compiler) {
        const { RuntimeGlobals } = compiler.rspack;
        compiler.hooks.thisCompilation.tap('CustomPlugin', (compilation) => {
          compilation.hooks.additionalTreeRuntimeRequirements.tap(
            'CustomPlugin',
            (_, set) => {
              // add a runtime module which define `__webpack_require__.h`
              set.add(RuntimeGlobals.getFullHash);
            },
          );
        });
      },
    },
  ],
};
```

```js title="index.js"
// will print hash of this compilation
console.log(__webpack_require__.h);
```

## `runtimeRequirementInTree`

[Added in v1.0.6](https://github.com/web-infra-dev/rspack/releases/tag/v1.0.6)
Called during adding runtime modules to the compilation.

- **Type:** `HookMap<SyncBailHook<[Chunk, Set<RuntimeGlobals>]>>`
- **Arguments:**
  - `Chunk`: chunk instance
  - `Set<RuntimeGlobals>`: runtime requirements

Additional builtin runtime modules can be added here by modifying the runtime requirements set or calling [`compilation.addRuntimeModule`](/api/javascript-api/compilation.md#addruntimemodule) to add custom runtime modules.

```js title="rspack.config.mjs"
export default {
  entry: './index.js',
  plugins: [
    {
      apply(compiler) {
        const { RuntimeGlobals, RuntimeModule } = compiler.rspack;
        class CustomRuntimeModule extends RuntimeModule {
          constructor() {
            super('custom');
          }

          generate() {
            const compilation = this.compilation;
            return `
            __webpack_require__.mock = function(file) {
              return ${RuntimeGlobals.publicPath} + "/subpath/" + file;
            };
          `;
          }
        }

        compiler.hooks.thisCompilation.tap('CustomPlugin', (compilation) => {
          compilation.hooks.runtimeRequirementInTree
            .for(RuntimeGlobals.ensureChunkHandlers)
            .tap('CustomPlugin', (chunk, set) => {
              // add a runtime module to access public path
              set.add(RuntimeGlobals.publicPath);
              compilation.addRuntimeModule(chunk, new CustomRuntimeModule());
            });
        });
      },
    },
  ],
};
```

```js title="index.js"
// will print "/subpath/index.js"
console.log(__webpack_require__.mock('index.js'));
```

## `runtimeModule`

Called after a runtime module is added into the compilation.

- **Type:** `SyncHook<[RuntimeModule, Chunk]>`
- **Arguments:**
  - `RuntimeModule`: runtime module instance
  - `Chunk`: chunk instance

Generated code of this runtime module can be modified through its `source` property.

```js title="rspack.config.mjs"
export default {
  plugins: [
    {
      apply(compiler) {
        const { RuntimeGlobals } = compiler.rspack;
        compiler.hooks.compilation.tap('CustomPlugin', (compilation) => {
          compilation.hooks.runtimeModule.tap(
            'CustomPlugin',
            (module, chunk) => {
              if (module.name === 'public_path' && chunk.name === 'main') {
                const originSource = module.source.source.toString('utf-8');
                module.source.source = Buffer.from(
                  `${RuntimeGlobals.publicPath} = "/override/public/path";\n`,
                  'utf-8',
                );
              }
            },
          );
        });
      },
    },
  ],
};
```

```js title="index.js"
// will print "/override/public/path"
console.log(__webpack_require__.p);
```

RuntimeModule.ts
## `processAssets`

Process the assets before emit.

- **Type:** `AsyncSeriesHook<Assets>`
- **Hook parameters:**
  - `name: string` — a name of the plugin
  - `stage: Stage` — a stage to tap into (see the [process assets stages](#process-assets-stages) below)
- **Arguments:**
  - `Assets: Record<string, Source>`: a plain object, where key is the asset's pathname, and the value is data of the asset represented by the [Source](https://github.com/webpack/webpack-sources#source).

Source.ts
### Process assets examples

- Emit a new asset in the `PROCESS_ASSETS_STAGE_ADDITIONAL` stage:

```js
compiler.hooks.thisCompilation.tap('MyPlugin', (compilation) => {
  const { Compilation } = compiler.rspack;
  compilation.hooks.processAssets.tap(
    {
      name: 'MyPlugin',
      stage: Compilation.PROCESS_ASSETS_STAGE_ADDITIONAL,
    },
    (assets) => {
      const { RawSource } = compiler.rspack.sources;
      const source = new RawSource('This is a new asset!');
      compilation.emitAsset('new-asset.txt', source);
    },
  );
});
```

- Updating an existing asset:

```js
compiler.hooks.thisCompilation.tap('MyPlugin', (compilation) => {
  const { Compilation } = compiler.rspack;
  compilation.hooks.processAssets.tap(
    {
      name: 'MyPlugin',
      stage: Compilation.PROCESS_ASSETS_STAGE_ADDITIONS,
    },
    (assets) => {
      const asset = assets['foo.js'];
      if (!asset) {
        return;
      }

      const { RawSource } = compiler.rspack.sources;
      const oldContent = asset.source();
      const newContent = oldContent + '\nconsole.log("hello world!")';
      const source = new RawSource(newContent);

      compilation.updateAsset(assetName, source);
    },
  );
});
```

- Removing an asset:

```js
compiler.hooks.thisCompilation.tap('MyPlugin', (compilation) => {
  const { Compilation } = compiler.rspack;
  compilation.hooks.processAssets.tap(
    {
      name: 'MyPlugin',
      stage: Compilation.PROCESS_ASSETS_STAGE_OPTIMIZE,
    },
    (assets) => {
      const assetName = 'unwanted-script.js';
      if (assets[assetName]) {
        compilation.deleteAsset(assetName);
      }
    },
  );
});
```

### Process assets stages

Here's the list of supported stages. Rspack will execute these stages sequentially from top to bottom. Please select the appropriate stage based on the operation you need to perform.

- `PROCESS_ASSETS_STAGE_ADDITIONAL` — add additional assets to the compilation.
- `PROCESS_ASSETS_STAGE_PRE_PROCESS` — basic preprocessing of the assets.
- `PROCESS_ASSETS_STAGE_DERIVED` — derive new assets from the existing assets.
- `PROCESS_ASSETS_STAGE_ADDITIONS` — add additional sections to the existing assets e.g. banner or initialization code.
- `PROCESS_ASSETS_STAGE_OPTIMIZE` — optimize existing assets in a general way.
- `PROCESS_ASSETS_STAGE_OPTIMIZE_COUNT` — optimize the count of existing assets, e.g. by merging them.
- `PROCESS_ASSETS_STAGE_OPTIMIZE_COMPATIBILITY` — optimize the compatibility of existing assets, e.g. add polyfills or vendor prefixes.
- `PROCESS_ASSETS_STAGE_OPTIMIZE_SIZE` — optimize the size of existing assets, e.g. by minimizing or omitting whitespace.
- `PROCESS_ASSETS_STAGE_DEV_TOOLING` — add development tooling to the assets, e.g. by extracting a source map.
- `PROCESS_ASSETS_STAGE_OPTIMIZE_INLINE` — optimize the numbers of existing assets by inlining assets into other assets.
- `PROCESS_ASSETS_STAGE_SUMMARIZE` — summarize the list of existing assets.
- `PROCESS_ASSETS_STAGE_OPTIMIZE_HASH` — optimize the hashes of the assets, e.g. by generating real hashes of the asset content.
- `PROCESS_ASSETS_STAGE_OPTIMIZE_TRANSFER` — optimize the transfer of existing assets, e.g. by preparing a compressed (gzip) file as separate asset.
- `PROCESS_ASSETS_STAGE_ANALYSE` — analyze the existing assets.
- `PROCESS_ASSETS_STAGE_REPORT` — creating assets for the reporting purposes.

## `afterProcessAssets`

Read-only
Called after the [processAssets](#processAssets) hook had finished without error.

- **Type:** `SyncHook<Assets>`
- **Arguments:**
  - `Assets: Record<string, Source>`: list of asset instances

Source.ts
- **Example:**

```js
compilation.hooks.afterProcessAssets.tap('MyPlugin', (assets) => {
  console.log('assets', Object.keys(assets));
});
```

## `afterSeal`

Read-only
Called after the seal phase.

- **Type:** `AsyncSeriesHook<[]>`

## `chunkHash`

Read-only
Triggered to emit the hash for each chunk.

- **Type:** `SyncHook<[Chunk, Hash]>`
- **Arguments:**
  - `Chunk`: chunk instance
  - `Hash`: chunk hash instance

Chunk.tsHash.ts
## `chunkAsset`

Read-only
Triggered when an asset from a chunk was added to the compilation.

- **Type:** `SyncHook<[Chunk, string]>`
- **Arguments:**
  - `Chunk`: chunk instance
  - `string`: asset filename

Chunk.ts
## `childCompiler`

Read-only
Executed after setting up a child compiler.

- **Type:** `SyncHook<[Compiler, string, number]>`
- **Arguments:**
  - `Compiler`: child compiler instance
  - `string`: child compiler name
  - `number`: child compiler index

Compiler.ts
## `statsPreset`

Read-only
This hook is like a list of actions that gets triggered when a preset is used. It takes in an options object. When a plugin manages a preset, it should change settings in this object carefully without replacing existing ones.

- **Type:** `SyncHook<[Partial<StatsOptions>, CreateStatsOptionsContext]>`
- **Arguments:**
  - `Partial<StatsOptions>`: stats options
  - `CreateStatsOptionsContext`: stats context

Here's an illustrative plugin example:

```js
compilation.hooks.statsPreset.for('my-preset').tap('MyPlugin', (options) => {
  if (options.all === undefined) options.all = true;
});
```

This plugin ensures that for the preset `"my-preset"`, if the `all` option is undefined, it defaults to `true`.

StatsOptions.tsCreateStatsOptionsContext.ts
## `statsNormalize`

Read-only
This hook is used to transform an options object into a consistent format that can be easily used by subsequent hooks. It also ensures that missing options are set to their default values.

- **Type:** `SyncHook<[Partial<StatsOptions>, CreateStatsOptionsContext]>`
- **Arguments:**
  - `Partial<StatsOptions>`: stats options
  - `CreateStatsOptionsContext`: stats context

Here's an illustrative plugin example:

```js
compilation.hooks.statsNormalize.tap('MyPlugin', (options) => {
  if (options.myOption === undefined) options.myOption = [];

  if (!Array.isArray(options.myOption)) options.myOptions = [options.myOptions];
});
```

In this plugin, if the `myOption` is missing, it sets it to `[]`. Additionally, it ensures that `myOption` is always an array even if it was originally defined as a single value.

StatsOptions.tsCreateStatsOptionsContext.ts
## `statsFactory`

Read-only
This hook provides access to the StatsFactory class for specific options.

- **Type:** `SyncHook<[StatsFactory, StatsOptions]>`
- **Arguments:**
  - `StatsFactory`: stats factory instance, see [Stats Factory Hooks](/api/plugin-api/stats-hooks.md#statsfactory) for more details
  - `StatsOptions`: stats options

StatsFactory.tsStatsOptions.ts
## `statsPrinter`

Read-only
This hook provides access to the StatsPrinter class for specific options.

- **Type:** `SyncHook<[StatsPrinter, StatsOptions]>`
- **Arguments:**
  - `StatsPrinter`: stats printer instance, see [Stats Printer Hooks](/api/plugin-api/stats-hooks.md#statsprinter) for more details.
  - `StatsOptions`: stats options

StatsPrinter.tsStatsOptions.ts