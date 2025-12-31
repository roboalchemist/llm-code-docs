# Source: https://rspack.dev/api/javascript-api/compilation.md

import WebpackLicense from '@components/WebpackLicense';

import { Collapse, CollapsePanel } from '@components/Collapse';
import { ApiMeta } from '@components/ApiMeta';

<WebpackLicense from="https://webpack.js.org/api/compilation-object/" />

# Compilation

The Compilation object is one of the core objects used in the Rspack build process. Whenever Rspack performs a build (including rebuilds in watch mode), a new Compilation instance is created, which contains all the information about the current build.

This page lists the available methods and properties of the Compilation object. You can also refer to [Compilation Hooks](/api/plugin-api/compilation-hooks.md) to learn about the hooks provided by the Compilation object.

:::warning Notice
In Rspack, the real compilation object runs on the Rust side, and the JavaScript compilation object is only a **proxy object** used to communicate with the Rust compilation object.

Therefore, some complex data structures and methods will not be supported on the JavaScript compilation object, the data is **read-only** and the structure may differ from webpack.
:::

## Get compilation object

You can get the current compilation object via [compiler.hooks.thisCompilation](/api/plugin-api/compiler-hooks.md#thiscompilation) or [compiler.hooks.compilation](/api/plugin-api/compiler-hooks.md#compilation) hooks.

```js
class ExamplePlugin {
  apply(compiler) {
    compiler.hooks.thisCompilation.tap('ExamplePlugin', (compilation) => {
      console.log('thisCompilation hook called:', compilation);
    });

    compiler.hooks.compilation.tap('ExamplePlugin', (compilation) => {
      console.log('compilation hook called:', compilation);
    });
  }
}
```

## Compilation methods

### emitAsset

Emit a new asset, throw an error if the asset already exists.

```ts
emitAsset(
  filename: string, // filename of the new asset
  source: Source, // content of the new asset
  info?: AssetInfo // asset info of the new asset
): void;
```

The following code will add a new asset named `asset-name.js` and will not be compressed:

```js
compiler.hooks.thisCompilation.tap('MyPlugin', (compilation) => {
  const { RawSource } = compiler.rspack.sources;
  compilation.hooks.processAssets.tap('MyPlugin', () => {
    const buffer = Buffer.from(
      'i am content of emit asset, do not minimize me',
    );
    const source = new RawSource(buffer, false);
    compilation.emitAsset('asset-name.js', source, {
      minimized: true,
    });
  });
});
```

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Source.ts" key="Source">
    <>
      ```ts
      type Source = {
        source(): string | ArrayBuffer;
        buffer(): Buffer;
        size(): number;
        map(options?: MapOptions): RawSourceMap | null;
        sourceAndMap(options?: MapOptions): SourceAndMapResult;
      };
      ```
    </>
  </CollapsePanel>

  <CollapsePanel className="collapse-code-panel" header="AssetInfo.ts" key="AssetInfo">
    <>
      ```ts
      type AssetInfo = {
        immutable: boolean;
        minimized: boolean;
        fullhash: Array<string>;
        chunkhash: Array<string>;
        contenthash: Array<string>;
        sourceFilename?: string;
        development: boolean;
        hotModuleReplacement: boolean;
        javascriptModule?: boolean;
        related: JsAssetInfoRelated;
        cssUnusedIdents?: Array<string>;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### updateAsset

Update an existing asset, throw an error if the asset does not exist.

```ts
updateAsset(
  filename: string, // filename of the updating asset
  source: Source | ((source: Source) => Source), // the new content or a function returns the new content
  info?:  // the new info or a function returns the new info
    | AssetInfo
    | ((assetInfo: AssetInfo) => AssetInfo)
): void;
```

The following code replaces the content of `main.js` and not to minimize it:

```js
compiler.hooks.thisCompilation.tap('MyPlugin', (compilation) => {
  const { RawSource } = compiler.rspack.sources;
  compilation.hooks.processAssets.tap('MyPlugin', () => {
    const updatedSource = new RawSource(
      `module.exports = "This is the updated"`,
    );
    compilation.updateAsset('main.js', updatedSource, {
      minimized: true,
    });
  });
});
```

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Source.ts" key="Source">
    <>
      ```ts
      type Source = {
        source(): string | ArrayBuffer;
        buffer(): Buffer;
        size(): number;
        map(options?: MapOptions): RawSourceMap | null;
        sourceAndMap(options?: MapOptions): SourceAndMapResult;
      };
      ```
    </>
  </CollapsePanel>

  <CollapsePanel className="collapse-code-panel" header="AssetInfo.ts" key="AssetInfo">
    <>
      ```ts
      type AssetInfo = {
        immutable: boolean;
        minimized: boolean;
        fullhash: Array<string>;
        chunkhash: Array<string>;
        contenthash: Array<string>;
        sourceFilename?: string;
        development: boolean;
        hotModuleReplacement: boolean;
        javascriptModule?: boolean;
        related: JsAssetInfoRelated;
        cssUnusedIdents?: Array<string>;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### renameAsset

Rename an existing asset.

```ts
renameAsset(
  filename: string, // filename of the renaming asset
  newFilename: string // new filename
): void;
```

The following code renames the asset named `main.js` to `my-asset-name.js`:

```js
compiler.hooks.thisCompilation.tap('MyPlugin', (compilation) => {
  compilation.hooks.processAssets.tap('MyPlugin', () => {
    compilation.renameAsset('main.js', 'my-asset-name.js');
  });
});
```

### deleteAsset

Delete an existing asset.

```ts
deleteAsset(
  filename: string // filename of the deleting asset
): void;
```

The following code will delete the asset named `no-need.js`:

```js
compiler.hooks.thisCompilation.tap('MyPlugin', (compilation) => {
  compilation.hooks.processAssets.tap('MyPlugin', () => {
    compilation.deleteAsset('no-need.js');
  });
});
```

### getAssets

Get the list of asset objects.

```ts
getAssets(): ReadonlyArray<{
  filename: string;
  source: Source;
  info: AssetInfo;
}>;
```

The following code will print the total size of all assets:

```js
compiler.hooks.compilation.tap('MyPlugin', (compilation) => {
  compilation.hooks.processAssets.tap('MyPlugin', () => {
    const assets = compilation.getAssets();
    const totalSize = assets.reduce(
      (total, asset) => total + asset.source.size(),
      0,
    );
    console.log(`total size: ${totalSize}`);
  });
});
```

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Source.ts" key="Source">
    <>
      ```ts
      type Source = {
        source(): string | ArrayBuffer;
        buffer(): Buffer;
        size(): number;
        map(options?: MapOptions): RawSourceMap | null;
        sourceAndMap(options?: MapOptions): SourceAndMapResult;
      };
      ```
    </>
  </CollapsePanel>

  <CollapsePanel className="collapse-code-panel" header="AssetInfo.ts" key="AssetInfo">
    <>
      ```ts
      type AssetInfo = {
        immutable: boolean;
        minimized: boolean;
        fullhash: Array<string>;
        chunkhash: Array<string>;
        contenthash: Array<string>;
        sourceFilename?: string;
        development: boolean;
        hotModuleReplacement: boolean;
        javascriptModule?: boolean;
        related: JsAssetInfoRelated;
        cssUnusedIdents?: Array<string>;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### getAsset

Get the asset object with the specified name.

```ts
getAsset(
  filename: string // filename of the getting asset
): Readonly<{
  filename: string;
  source: Source;
  info: AssetInfo;
}> | void;
```

The following code will print the size of the asset named `main.js`:

```js
compiler.hooks.compilation.tap('MyPlugin', (compilation) => {
  compilation.hooks.processAssets.tap('MyPlugin', () => {
    const assetSize = compilation.getAsset('main.js')?.source.size();
    console.log(`main size: ${assetSize}`);
  });
});
```

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Source.ts" key="Source">
    <>
      ```ts
      type Source = {
        source(): string | ArrayBuffer;
        buffer(): Buffer;
        size(): number;
        map(options?: MapOptions): RawSourceMap | null;
        sourceAndMap(options?: MapOptions): SourceAndMapResult;
      };
      ```
    </>
  </CollapsePanel>

  <CollapsePanel className="collapse-code-panel" header="AssetInfo.ts" key="AssetInfo">
    <>
      ```ts
      type AssetInfo = {
        immutable: boolean;
        minimized: boolean;
        fullhash: Array<string>;
        chunkhash: Array<string>;
        contenthash: Array<string>;
        sourceFilename?: string;
        development: boolean;
        hotModuleReplacement: boolean;
        javascriptModule?: boolean;
        related: JsAssetInfoRelated;
        cssUnusedIdents?: Array<string>;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### getPath

Generate path string based on the Filename template, see [Filename placeholders](/config/filename-placeholders.md) for the template rules.

```ts
getPath(
  filename: Filename, // filename template
  data: PathData = {} // generating path data
): string;
```

The following code will replace the placeholder in the template to generate the path:

```js
const path = compilation.getPath('[contenthash]-[fullhash].js', {
  contentHash: 'some1',
  hash: 'some2',
});
console.log(path); // "some1-some2.js"
```

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Filename.ts" key="FileName">
    <>
      ```ts
      type Filename = string | (data: PathData, info: AssetInfo) => string;
      ```
    </>
  </CollapsePanel>

  <CollapsePanel className="collapse-code-panel" header="PathData.ts" key="PathData">
    <>
      ```ts
      type PathData = {
        filename?: string;
        hash?: string;
        contentHash?: string;
        runtime?: string;
        url?: string;
        id?: string;
        chunk?: JsChunkPathData;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### getPathWithInfo

Generate path string and asset info based on the Filename template, see [Filename placeholders](/config/filename-placeholders.md).

```ts
getPathWithInfo(
  filename: Filename, // filename template
  data: PathData = {} // generating path data
): {
  path: string;
  info: AssetInfo;
};
```

The following code will replace the placeholder in the template to generate the path and asset info:

```ts
const { path, info } = compilation.getPathWithInfo(
  '[contenthash]-[fullhash].js',
  {
    contentHash: 'some1',
    hash: 'some2',
  },
);
console.log(path); // "some1-some2.js"
console.log(info);
/* Object {
  immutable: true,
  minimized: false,
  fullhash: [ 'some2' ],
  chunkhash: [],
  contenthash: [ 'some1' ],
  development: false,
  hotModuleReplacement: false,
  related: {},
  extras: {}
} */
```

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Filename.ts" key="FileName">
    <>
      ```ts
      type Filename = string | (data: PathData, info: AssetInfo) => string;
      ```
    </>
  </CollapsePanel>

  <CollapsePanel className="collapse-code-panel" header="PathData.ts" key="PathData">
    <>
      ```ts
      type PathData = {
        filename?: string;
        hash?: string;
        contentHash?: string;
        runtime?: string;
        url?: string;
        id?: string;
        chunk?: JsChunkPathData;
      };
      ```
    </>
  </CollapsePanel>

  <CollapsePanel className="collapse-code-panel" header="AssetInfo.ts" key="AssetInfo">
    <>
      ```ts
      type AssetInfo = {
        immutable: boolean;
        minimized: boolean;
        fullhash: Array<string>;
        chunkhash: Array<string>;
        contenthash: Array<string>;
        sourceFilename?: string;
        development: boolean;
        hotModuleReplacement: boolean;
        javascriptModule?: boolean;
        related: JsAssetInfoRelated;
        cssUnusedIdents?: Array<string>;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### getStats

Get the stats object of current compilation:

```ts
getStats(): Stats;
```

The following code prints the total number of modules:

```js
compiler.hooks.emit.tapAsync('MyPlugin', (compilation) => {
  const modules = compilation.getStats().toJson({ modules: true }).modules;
  console.log(`Total modules: ${modules.length}`);
});
```

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Stats.ts" key="Stats">
    <>
      ```ts
      type Stats = {
        compilation: Compilation;
        hash: Readonly<string | null>;
        startTime?: number;
        endTime?: number;
        hasErrors(): bool;
        hasWarnings(): bool;
        toJson(opts?: StatsValue): StatsCompilation;
        toString(opts?: StatsValue): string;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### createChildCompiler

Allows running another instance of Rspack inside of Rspack. However, as a child with different settings and configurations applied. It copies all hooks and plugins from the parent (or top-level compiler) and creates a child `Compiler` instance. Returns the created `Compiler`.

```ts
createChildCompiler(
  name: string, // name for the child `Compiler`
  outputOptions: OutputNormalized, // Output options object
  plugins: RspackPluginInstance[] // Plugins that will be applied
): Compiler;
```

The following code will start a child compiler with `child-entry.js` as the entry, and output to `dist/child`:

```js
compiler.hooks.make.tap('MyPlugin', (compilation) => {
  const childCompiler = compilation.createChildCompiler(
    'ChildCompiler',
    {
      path: 'dist/child',
    },
    [new compiler.rspack.EntryPlugin(compiler.context, './child-entry.js')],
  );
  childCompiler.compile((err, childCompilation) => {});
});
```

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Compiler.ts" key="Compiler">
    <>
      ```ts
      type Compiler = {
        hooks: CompilerHooks;
        inputFileSystem: InputFileSystem | null;
        outputFileSystem: OutputFileSystem | null;
        watchFileSystem: WatchFileSystem | null;
        options: RspackOptionsNormalized;
        watching: Watching;

        getInfrastructureLogger(name: string | (() => string)): Logger;
        getCache(name: string): CacheFacade;
        watch(
          watchOptions: Watchpack.WatchOptions,
          handler: liteTapable.Callback<Error, Stats>,
        ): Watching;
        run(callback: liteTapable.Callback<Error, Stats>): void;
        runAsChild(
          callback: (
            err?: null | Error,
            entries?: Chunk[],
            compilation?: Compilation,
          ) => any,
        ): void;
        createChildCompiler(
          compilation: Compilation,
          compilerName: string,
          compilerIndex: number,
          outputOptions: OutputNormalized,
          plugins: RspackPluginInstance[],
        ): Compiler;
        compile(callback: liteTapable.Callback<Error, Compilation>): void;
        close(callback: (error?: Error | null) => void): void;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### addRuntimeModule

<ApiMeta addedVersion="1.0.6" />

Add a custom runtime module to the compilation.

```ts
addRuntimeModule(
  c: Chunk, // the runtime chunk which to add the runtime module
  m: RuntimeModule, // the runtime module instance to add
): void;
```

The following code will add a runtime module which define `__webpack_require__.mock` to the `"main"` chunk:

```js title="rspack.config.mjs"
export default {
  entry: './index.js',
  plugins: [
    {
      apply(compiler) {
        const { RuntimeModule } = compiler.rspack;

        class CustomRuntimeModule extends RuntimeModule {
          constructor() {
            super('custom');
          }

          generate() {
            const compilation = this.compilation;
            return `
            __webpack_require__.mock = function() {
              // ...
            };
          `;
          }
        }

        compiler.hooks.thisCompilation.tap('CustomPlugin', (compilation) => {
          compilation.hooks.runtimeRequirementInTree
            .for(RuntimeGlobals.ensureChunkHandlers)
            .tap('CustomPlugin', (chunk, set) => {
              if (chunk.name === 'main') {
                compilation.addRuntimeModule(chunk, new CustomRuntimeModule());
              }
            });
        });
      },
    },
  ],
};
```

When implementing a custom runtime module class, the following methods/properties can be overridden to control the behavior of the runtime module:

* Pass the `name` and `stage` parameters in the constructor to specify the module name and the insertion stage.
* Override the `generate()` method to control the generated code of the module.
* Override the `shouldIsolate()` method to control whether the module is wrapped in an IIFE.
* Override the `attach()` method to modify the behavior when the module is added.
* Modify its `fullHash` or `dependentHash` properties to control whether the module can be cached.

### rebuildModule

Triggers a re-build of the module.

```ts
rebuildModule(
  m: Module, // module to be rebuilt
  f: (err: Error | null, m: Module | null) => void //  function to be invoked when the module finishes rebuilding
): void;
```

The following code will rebuild the module ending with `a.js`:

```js
compiler.hooks.compilation.tap('MyPlugin', (compilation) => {
  compilation.hooks.finishModules.tapPromise('MyPlugin', async (modules) => {
    const oldModule = Array.from(modules).find((item) =>
      item.resource.endsWith('a.js'),
    );
    compilation.rebuildModule(oldModule, (err, m) => {
      console.log(`Rebuilt ${m.identifier()}.`);
    });
  });
});
```

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Module.ts" key="Module">
    <>
      ```ts
      type Module = {
        context?: string;
        resource?: string;
        request?: string;
        userRequest?: string;
        rawRequest?: string;
        factoryMeta?: JsFactoryMeta;
        buildInfo: Record<string, any>;
        buildMeta: Record<string, any>;
        originalSource(): {
          isRaw: boolean;
          isBuffer: boolean;
          source: Buffer;
          map?: Buffer;
        } | null;
        identifier(): string;
        nameForCondition(): string | null;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### getLogger

Get a log output utility object with the specified name, which can be used to print logs with unified format in the plugin.

```ts
getLogger(name: string | (() => string)): Logger;
```

The following code prints the asset to the debug log in `processAssets`:

```js
compiler.hooks.compilation.tap('MyPlugin', (compilation) => {
  const logger = compilation.getLogger('MyPlugin');

  compilation.hooks.processAssets.tap('MyPlugin', () => {
    for (const asset of compilation.getAssets()) {
      logger.debug(`asset name: ${asset.name}`);
      logger.debug(`asset info: ${asset.info}`);
    }
  });
});
```

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Logger.ts" key="Logger">
    <>
      > See [Logger API](/api/javascript-api/logger.md) for more details

      ```ts
      type Logger = {
        getChildLogger: (name: string | (() => string)) => Logger; // create a child logger
        error(...args: any[]): void; // display errors
        warn(...args: any[]): void; //  display warnings
        info(...args: any[]): void; // display important information
        log(...args: any[]): void; // display unimportant information
        debug(...args: string[]): void; // display debug information
        assert(assertion: any, ...args: any[]): void; // display errors if assertion failed
        trace(): void; // display a stack trace
        clear(): void; // clear all logs
        status(...args: any[]): void; // display status information
        group(...args: any[]): void; // start a logging group
        groupEnd(...args: any[]): void; // end a logging group
        groupCollapsed(...args: any[]): void; // group logs together
        profile(label: any): void; // start capturing a profile
        profileEnd(label: any): void; // end capturing a profile
        time(label: any): void; // start a timer
        timeLog(label: any): void; // not end the timer and record the time difference
        timeEnd(label: any): void; // end the timer and record the time difference
        timeAggregate(label: any): void; // aggregate capture the time difference
        timeAggregateEnd(label: any): void; // end the aggregate capturing
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### getCache

Get a cache object with the specified name, which can be used for the plugin to share data during multiple compilations.

```ts
getCache(name: string): CacheFacade;
```

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Cache.ts" key="Cache">
    <>
      > See [cache object](/api/javascript-api/cache.md) for more details.

      ```ts
      type CacheFacade = {
        getChildCache(name: string): CacheFacade; // create a named child cache object
        getItemCache(identifier, etag): ItemCacheFacade; // create a cache object for an data item
        getLazyHashedEtag(obj: HashableObject): Etag; // create a lazy computed etag
        mergeEtags(a: Etag, b: Etag): Etag; // merge two etags
        get<T>( // async data getter, callback by function
          identifier: string,
          etag: Etag,
          callback: (err: Error, result: T) => void,
        ): void;
        getPromise<T>( // async data getter, callback by promise
          identifier: string,
          etag: Etag,
        ): Promise<T>;
        store<T>( // async data setter, callback by function
          identifier: string,
          etag: Etag,
          data: T,
          callback: (err: Error) => void,
        ): void;
        storePromise<T>( // async data setter, callback by promise
          identifier: string,
          etag: Etag,
          data: T,
        ): Promise<void>;
        provide<T>( // try to get the data, use function to compute if not exists, callback by function
          identifier: string,
          etag: Etag,
          computer: () => T | Promise<T>,
          callback: (err: Error, result: T) => void,
        ): void;
        providePromise<T>( // try to get the data, use function to compute if not exists, callback by function
          identifier: string,
          etag: Etag,
          computer: () => T | Promise<T>,
        ): Promise<T>;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

## Compilation properties

### options

**Type**: `RspackOptionsNormalized`

The normalized options used by this Compilation, see [Configure Rspack](/config/index.md) for details.

### compiler

**Type**: `Compiler`

Current [compiler object](/api/javascript-api/index.md).

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Compiler.ts" key="Compiler">
    <>
      ```ts
      type Compiler = {
        hooks: CompilerHooks;
        inputFileSystem: InputFileSystem | null;
        outputFileSystem: OutputFileSystem | null;
        watchFileSystem: WatchFileSystem | null;
        options: RspackOptionsNormalized;
        watching: Watching;

        getInfrastructureLogger(name: string | (() => string)): Logger;
        getCache(name: string): CacheFacade;
        watch(
          watchOptions: Watchpack.WatchOptions,
          handler: liteTapable.Callback<Error, Stats>,
        ): Watching;
        run(callback: liteTapable.Callback<Error, Stats>): void;
        runAsChild(
          callback: (
            err?: null | Error,
            entries?: Chunk[],
            compilation?: Compilation,
          ) => any,
        ): void;
        createChildCompiler(
          compilation: Compilation,
          compilerName: string,
          compilerIndex: number,
          outputOptions: OutputNormalized,
          plugins: RspackPluginInstance[],
        ): Compiler;
        compile(callback: liteTapable.Callback<Error, Compilation>): void;
        close(callback: (error?: Error | null) => void): void;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### hooks

The [Compilation hooks](/api/plugin-api/compilation-hooks.md).

### hash/fullhash

**Type**: `Readonly<string | null>`

The hash of this compilation.

### assets

**Type**: `Record<string, Source>`

The mapping from asset filenames and content sources.

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Source.ts" key="Source">
    <>
      ```ts
      type Source = {
        source(): string | ArrayBuffer;
        buffer(): Buffer;
        size(): number;
        map(options?: MapOptions): RawSourceMap | null;
        sourceAndMap(options?: MapOptions): SourceAndMapResult;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### chunkGroups

**Type**: `ReadonlyArray<ChunkGroup>`

The list of chunk group objects, with the structure as follows:

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="ChunkGroup.ts" key="ChunkGroup">
    <>
      ```ts
      type ChunkGroup = {
        name?: Readonly<string>; // name of this chunk group
        index?: Readonly<number>; // creating index of chunk group
        chunks: ReadonlyArray<Chunk>; // chunks in this chunk group
        origins: ReadonlyArray<{
          // where this chunk group is imported
          module?: Module;
          request?: string;
        }>;
        isInitial(): boolean; // whether this chunk group will be loaded on initial page load
        getFiles(): ReadonlyArray<string>; // the files contained this chunk group
        getParents(): ReadonlyArray<ChunkGroup>; // returns the parent chunk groups
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### entrypoints

**Type**: `ReadonlyMap<string, Entrypoint>`

The mapping from name to entrypoint, which is a special chunk group and include a runtime chunk.

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Entrypoint.ts" key="entrypoint">
    <>
      ```ts
      type Entrypoint = {
        name?: Readonly<string>; // name of this chunk group
        index?: Readonly<number>; // creating index of chunk group
        chunks: ReadonlyArray<Chunk>; // chunks in this chunk group
        origins: ReadonlyArray<{
          // the origin request of this entrypoint
          module?: Module;
          request?: string;
        }>;
        isInitial(): boolean; // whether this chunk group will be loaded on initial page load
        getFiles(): ReadonlyArray<string>; // the files contained this chunk group
        getParents(): ReadonlyArray<ChunkGroup>; // returns the parent chunk groups
        getRuntimeChunk(): Readonly<Chunk | null>; // get the runtime chunk of this entrypoint (runtime chunk refers to a chunk that contains runtime code. Generally, the runtime chunk and the entrypoint chunk are the same chunk. Only when the runtime is split into a separate chunk via `dependOn` or `optimization.runtimeChunk` do they refer to different chunks)
        getEntrypointChunk(): Readonly<Chunk | null>; // get the entrypoint chunk of this entrypoint (entrypoint chunk refers to a chunk that contains entry modules)
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### namedChunkGroups

**Type**: `ReadonlyMap<string, Readonly<ChunkGroup>>`

The mapping from names to chunk groups.

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="ChunkGroup.ts" key="ChunkGroup">
    <>
      ```ts
      type ChunkGroup = {
        name?: Readonly<string>; // name of this chunk group
        index?: Readonly<number>; // creating index of chunk group
        chunks: ReadonlyArray<Chunk>; // chunks in this chunk group
        origins: ReadonlyArray<{
          // where this chunk group is imported
          module?: Module;
          request?: string;
        }>;
        isInitial(): boolean; // whether this chunk group will be loaded on initial page load
        getFiles(): ReadonlyArray<string>; // the files contained this chunk group
        getParents(): ReadonlyArray<ChunkGroup>; // returns the parent chunk groups
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### modules

**Type:** `ReadonlySet<Module>`

List of all modules, with the structure as follows:

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Module.ts" key="Module">
    <>
      ```ts
      type Module = {
        context?: string;
        resource?: string;
        request?: string;
        userRequest?: string;
        rawRequest?: string;
        factoryMeta?: JsFactoryMeta;
        buildInfo: Record<string, any>;
        buildMeta: Record<string, any>;
        originalSource(): {
          isRaw: boolean;
          isBuffer: boolean;
          source: Buffer;
          map?: Buffer;
        } | null;
        identifier(): string;
        nameForCondition(): string | null;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### builtModules

**Type:** `ReadonlySet<Module>`

List of built modules that were not be cached, with the structure as follows:

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Module.ts" key="Module">
    <>
      ```ts
      type Module = {
        context?: string;
        resource?: string;
        request?: string;
        userRequest?: string;
        rawRequest?: string;
        factoryMeta?: JsFactoryMeta;
        buildInfo: Record<string, any>;
        buildMeta: Record<string, any>;
        originalSource(): {
          isRaw: boolean;
          isBuffer: boolean;
          source: Buffer;
          map?: Buffer;
        } | null;
        identifier(): string;
        nameForCondition(): string | null;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### chunks

**Type:** `ReadonlySet<Chunk>`

List of all chunks, with the structure as follows:

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Chunk.ts" key="Chunk">
    <>
      ```ts
      type Chunk = {
        auxiliaryFiles: ReadonlySet<string>;
        canBeInitial(): boolean;
        chunkReason?: Readonly<string>;
        contentHash: Readonly<Record<string, string>>;
        cssFilenameTemplate?: Readonly<string>;
        filenameTemplate?: Readonly<string>;
        files: ReadonlySet<string>;
        getAllAsyncChunks(): Iterable<Chunk>;
        getAllInitialChunks(): Iterable<Chunk>;
        getAllReferencedChunks(): Iterable<Chunk>;
        getEntryOptions(): EntryOptions | undefined;
        get groupsIterable(): Iterable<ChunkGroup>;
        hash?: Readonly<string>;
        hasRuntime(): boolean;
        id?: Readonly<string>;
        idNameHints: ReadonlyArray<string>;
        ids: ReadonlyArray<string>;
        isOnlyInitial(): boolean;
        name?: Readonly<string>;
        renderedHash?: Readonly<string>;
        runtime: ReadonlySet<string>;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### namedChunks

**Type:** `ReadonlyMap<string, Readonly<Chunk>>`

The mapping from names to chunks.

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="Chunk.ts" key="Chunk">
    <>
      ```ts
      type Chunk = {
        auxiliaryFiles: ReadonlySet<string>;
        canBeInitial(): boolean;
        chunkReason?: Readonly<string>;
        contentHash: Readonly<Record<string, string>>;
        cssFilenameTemplate?: Readonly<string>;
        filenameTemplate?: Readonly<string>;
        files: ReadonlySet<string>;
        getAllAsyncChunks(): Iterable<Chunk>;
        getAllInitialChunks(): Iterable<Chunk>;
        getAllReferencedChunks(): Iterable<Chunk>;
        getEntryOptions(): EntryOptions | undefined;
        get groupsIterable(): Iterable<ChunkGroup>;
        hash?: Readonly<string>;
        hasRuntime(): boolean;
        id?: Readonly<string>;
        idNameHints: ReadonlyArray<string>;
        ids: ReadonlyArray<string>;
        isOnlyInitial(): boolean;
        name?: Readonly<string>;
        renderedHash?: Readonly<string>;
        runtime: ReadonlySet<string>;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### fileDependencies

**Type:** `CompilationDependencies`

List of files this compilation depends on.

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="CompilationDependencies.ts" key="CompilationDependencies">
    <>
      ```ts
      type CompilationDependencies = {
        has(dep: string): boolean;
        add(dep: string): void;
        addAll(deps: Iterable<string>): void;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### contextDependencies

**Type:** `CompilationDependencies`

List of directories this compilation depends on.

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="CompilationDependencies.ts" key="CompilationDependencies">
    <>
      ```ts
      type CompilationDependencies = {
        has(dep: string): boolean;
        add(dep: string): void;
        addAll(deps: Iterable<string>): void;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### missingDependencies

**Type:** `CompilationDependencies`

List of not existing files this compilation depends on.

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="CompilationDependencies.ts" key="CompilationDependencies">
    <>
      ```ts
      type CompilationDependencies = {
        has(dep: string): boolean;
        add(dep: string): void;
        addAll(deps: Iterable<string>): void;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### buildDependencies

**Type:** `CompilationDependencies`

List of build dependencies this compilation depends on.

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="CompilationDependencies.ts" key="CompilationDependencies">
    <>
      ```ts
      type CompilationDependencies = {
        has(dep: string): boolean;
        add(dep: string): void;
        addAll(deps: Iterable<string>): void;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### errors

**Type:** `RspackError[]`

List of emitted errors during this compilation, with the structure as follows:

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="RspackError.ts" key="RspackError">
    <>
      ```ts
      type RspackError = {
        name: string;
        message: string;
        moduleIdentifier?: string;
        file?: string;
        stack?: string;
        hideStack?: boolean;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>

### warnings

**Type:** `RspackError[]`

List of emitted warnings during this compilation.

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="RspackError.ts" key="RspackError">
    <>
      ```ts
      type RspackError = {
        name: string;
        message: string;
        moduleIdentifier?: string;
        file?: string;
        stack?: string;
        hideStack?: boolean;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>
