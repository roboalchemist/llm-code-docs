# Source: https://rolldown.rs/reference/Interface.TransformPluginContext.md

---
url: /reference/Interface.TransformPluginContext.md
---
# Interface: TransformPluginContext

## Extends

* [`PluginContext`](Interface.PluginContext.md)

## Properties

### fs

* **Type**: [`RolldownFsModule`](Interface.RolldownFsModule.md)

Provides abstract access to the file system.

#### Inherited from

[`PluginContext`](Interface.PluginContext.md).[`fs`](Interface.PluginContext.md#fs)

***

### meta

* **Type**: [`PluginContextMeta`](Interface.PluginContextMeta.md)

An object containing potentially useful metadata.

#### Inherited from

[`PluginContext`](Interface.PluginContext.md).[`meta`](Interface.PluginContext.md#meta)

## Methods

### getModuleInfo()

* **Type**: (`moduleId`) => [`ModuleInfo`](Interface.ModuleInfo.md) | `null`

Get additional information about the module in question.

During the build, this object represents currently available information about the module which may be inaccurate before the [`buildEnd`](/reference/Interface.Plugin#buildend) hook:

* [`id`](/reference/Interface.ModuleInfo#id) will never change.
* [`code`](/reference/Interface.ModuleInfo#code), [`exports`](/reference/Interface.ModuleInfo#exports) are only available after parsing, i.e. in the [`moduleParsed`](/reference/Interface.Plugin#moduleparsed) hook or after awaiting [`this.load`](/reference/Interface.PluginContext#load). At that point, they will no longer change.
* [`isEntry`](/reference/Interface.ModuleInfo#isentry) is `true`, it will no longer change. It is however possible for modules to become entry points after they are parsed, either via [`this.emitFile`](/reference/Interface.PluginContext#emitfile) or because a plugin inspects a potential entry point via [`this.load`](/reference/Interface.PluginContext#load) in the [`resolveId`](/reference/Interface.Plugin#resolveid) hook when resolving an entry point. Therefore, it is not recommended relying on this flag in the [`transform`](/reference/Interface.Plugin#transform) hook. It will no longer change after [`buildEnd`](/reference/Interface.Plugin#buildend).
* [`importers`](/reference/Interface.ModuleInfo#importers) and [`dynamicImporters`](/reference/Interface.ModuleInfo#dynamicimporters) will start as empty arrays, which receive additional entries as new importers and are discovered. They will no longer change after [`buildEnd`](/reference/Interface.Plugin#buildend).
* [`importedIds`](/reference/Interface.ModuleInfo#importedids) and [`dynamicallyImportedIds`](/reference/Interface.ModuleInfo#dynamicallyimportedids) are available when a module has been parsed and its dependencies have been resolved. This is the case in the [`moduleParsed`](/reference/Interface.Plugin#moduleparsed) hook or after awaiting [`this.load`](/reference/Interface.PluginContext#load) with the `resolveDependencies` flag. At that point, they will no longer change.
* [`meta`](/reference/Interface.ModuleInfo#meta) and [`moduleSideEffects`](/reference/Interface.ModuleInfo#modulesideeffects) can be changed by [`load`](/reference/Interface.PluginContext#load) and [`transform`](/reference/Interface.Plugin#transform) hooks. Moreover, while most properties are read-only, these properties are writable and changes will be picked up if they occur before the [`buildEnd`](/reference/Interface.Plugin#buildend) hook is triggered. meta itself should not be overwritten, but it is ok to mutate its properties at any time to store meta information about a module. The advantage of doing this instead of keeping state in a plugin is that meta is persisted to and restored from the cache if it is used, e.g. when using watch mode from the CLI.

#### Parameters

##### moduleId

`string`

#### Returns

[`ModuleInfo`](Interface.ModuleInfo.md) | `null`

Module information for that module. `null` if the module could not be found.

#### Inherited from

[`PluginContext`](Interface.PluginContext.md).[`getModuleInfo`](Interface.PluginContext.md#getmoduleinfo)

***

### addWatchFile()

* **Type**: (`id`: `string`) => `void`

Adds additional files to be monitored in watch mode so that changes to these files will trigger rebuilds.

Note that when emitting assets that correspond to an existing file, it is recommended to set the [`originalFileName`](/reference/Interface.EmittedAsset#originalfilename) property in the [`this.emitFile`](/reference/Interface.PluginContext#emitfile) call instead as that will not only watch the file but also make the connection transparent to other plugins.

Note: Usually in watch mode to improve rebuild speed, the transform hook will only be triggered for a given module if its contents actually changed. Using `this.addWatchFile` from within the transform hook will make sure the transform hook is also reevaluated for this module if the watched file changes.

In general, it is recommended to use `this.addWatchFile` from within the hook that depends on the watched file.

#### Parameters

##### id

`string`

The path to be monitored.

This can be an absolute path to a file or directory or a path relative to the current working directory.

#### Returns

`void`

#### Inherited from

[`PluginContext`](Interface.PluginContext.md).[`addWatchFile`](Interface.PluginContext.md#addwatchfile)

***

### emitFile()

* **Type**: (`file`: [`EmittedAsset`](Interface.EmittedAsset.md) | [`EmittedChunk`](Interface.EmittedChunk.md) | [`EmittedPrebuiltChunk`](Interface.EmittedPrebuiltChunk.md)) => `string`

Emits a new file that is included in the build output.
You can emit chunks, prebuilt chunks or assets.

#### In-depth (`type: 'chunk'`)

If the `type` is `'chunk'`, this emits a new chunk with the given module `id` as entry point. This will not result in duplicate modules in the graph, instead if necessary, existing chunks will be split or a facade chunk with reexports will be created. Chunks with a specified [`fileName`](/reference/Interface.EmittedChunk#filename) will always generate separate chunks while other emitted chunks may be deduplicated with existing chunks even if the name does not match. If such a chunk is not deduplicated, the [`output.chunkFileNames`](/reference/OutputOptions.chunkFileNames) pattern will be used.

You can reference the URL of an emitted file in any code returned by a [`load`](/reference/Interface.Plugin#load) or [`transform`](/reference/Interface.Plugin#transform) plugin hook via `import.meta.ROLLUP_FILE_URL_referenceId` (returns a string). See [File URLs](/apis/plugin-api/file-urls) for more details and an example.

You can use [`this.getFileName(referenceId)`](/reference/Interface.PluginContext#getfilename) to determine the file name as soon as it is available. If the file name is not set explicitly, then:

* asset file names are available starting with the [`renderStart`](/reference/Interface.Plugin#renderstart) hook. For assets that are emitted later, the file name will be available immediately after emitting the asset.
* chunk file names that do not contain a hash are available as soon as chunks are created after the [`renderStart`](/reference/Interface.Plugin#renderstart) hook.
* if a chunk file name would contain a hash, using [`getFileName`](/reference/Interface.PluginContext#getfilename) in any hook before [`generateBundle`](/reference/Interface.Plugin#generatebundle) will return a name containing a placeholder instead of the actual name. If you use this file name or parts of it in a chunk you transform in [`renderChunk`](/reference/Interface.Plugin#renderchunk), Rolldown will replace the placeholder with the actual hash before [`generateBundle`](/reference/Interface.Plugin#generatebundle), making sure the hash reflects the actual content of the final generated chunk including all referenced file hashes.

#### In-depth (`type: 'prebuilt-chunk'`)

If the `type` is `'prebuilt-chunk'`, this emits a chunk with fixed contents provided by the [`code`](/reference/Interface.EmittedPrebuiltChunk#code) property.

To reference a prebuilt chunk in imports, we need to mark the "module" as external in the [`resolveId`](/reference/Interface.Plugin#resolveid) hook as prebuilt chunks are not part of the module graph. Instead, they behave like assets with chunk meta-data:

```js
function emitPrebuiltChunkPlugin() {
  return {
    name: 'emit-prebuilt-chunk',
    resolveId: {
      filter: { id: /^\.\/my-prebuilt-chunk\.js$/ },
      handler(source) {
        return {
          id: source,
          external: true,
        };
      },
    },
    buildStart() {
      this.emitFile({
        type: 'prebuilt-chunk',
        fileName: 'my-prebuilt-chunk.js',
        code: 'export const foo = "foo"',
        exports: ['foo'],
      });
    },
  };
}
```

Then you can reference the prebuilt chunk in your code by `import { foo } from './my-prebuilt-chunk.js';`.

#### In-depth (`type: 'asset'`)

If the `type` is `'asset'`, this emits an arbitrary new file with the given source as content. Assets with a specified [`fileName`](/reference/Interface.EmittedAsset#filename) will always generate separate files while other emitted assets may be deduplicated with existing assets if they have the same source even if the name does not match. If an asset without a [`fileName`](/reference/Interface.EmittedAsset#filename) is not deduplicated, the [`output.assetFileNames`](/reference/OutputOptions.assetFileNames) pattern will be used.

#### Parameters

##### file

[`EmittedAsset`](Interface.EmittedAsset.md) | [`EmittedChunk`](Interface.EmittedChunk.md) | [`EmittedPrebuiltChunk`](Interface.EmittedPrebuiltChunk.md)

#### Returns

`string`

A `referenceId` for the emitted file that can be used in various places to reference the emitted file.

#### Inherited from

[`PluginContext`](Interface.PluginContext.md).[`emitFile`](Interface.PluginContext.md#emitfile)

***

### getCombinedSourcemap()

* **Type**: () => [`SourceMap`](Interface.SourceMap.md)

Get the combined source maps of all previous plugins.

#### Returns

[`SourceMap`](Interface.SourceMap.md)

***

### getFileName()

* **Type**: (`referenceId`: `string`) => `string`

Get the file name of a chunk or asset that has been emitted via
[`this.emitFile`](Interface.PluginContext.md#emitfile).

#### Parameters

##### referenceId

`string`

#### Returns

`string`

The file name of the emitted file. Relative to [`output.dir`](Interface.OutputOptions.md#dir).

#### Inherited from

[`PluginContext`](Interface.PluginContext.md).[`getFileName`](Interface.PluginContext.md#getfilename)

***

### getModuleIds()

* **Type**: () => `IterableIterator`<`string`>

Get all module ids in the current module graph.

#### Returns

`IterableIterator`<`string`>

An iterator of module ids. It can be iterated via

```js
for (const moduleId of this.getModuleIds()) {
  // ...
}
```

or converted into an array via `Array.from(this.getModuleIds())`.

#### Inherited from

[`PluginContext`](Interface.PluginContext.md).[`getModuleIds`](Interface.PluginContext.md#getmoduleids)

***

### load()

* **Type**: (`options`: { `id`: `string`; `resolveDependencies?`: `boolean`; } & `Partial`<[`PartialNull`](TypeAlias.PartialNull.md)<[`ModuleOptions`](Interface.ModuleOptions.md)>>) => `Promise`<[`ModuleInfo`](Interface.ModuleInfo.md)>

Loads and parses the module corresponding to the given id, attaching additional
meta information to the module if provided. This will trigger the same
[`load`](Interface.Plugin.md#load), [`transform`](Interface.Plugin.md#transform) and
[`moduleParsed`](Interface.Plugin.md#moduleparsed) hooks as if the module was imported
by another module.

This allows you to inspect the final content of modules before deciding how to resolve them in the [`resolveId`](/reference/Interface.Plugin#resolveid) hook and e.g. resolve to a proxy module instead. If the module becomes part of the graph later, there is no additional overhead from using this context function as the module will not be parsed again. The signature allows you to directly pass the return value of [`this.resolve`](/reference/Interface.PluginContext#resolve) to this function as long as it is neither `null` nor external.

The returned Promise will resolve once the module has been fully transformed and parsed but before any imports have been resolved. That means that the resulting [`ModuleInfo`](/reference/Interface.ModuleInfo) will have empty [`importedIds`](/reference/Interface.ModuleInfo#importedids) and [`dynamicallyImportedIds`](/reference/Interface.ModuleInfo#dynamicallyimportedids). This helps to avoid deadlock situations when awaiting `this.load` in a [`resolveId`](/reference/Interface.Plugin#resolveid) hook. If you are interested in [`importedIds`](/reference/Interface.ModuleInfo#importedids) and [`dynamicallyImportedIds`](/reference/Interface.ModuleInfo#dynamicallyimportedids), you can either implement a [`moduleParsed`](/reference/Interface.Plugin#moduleparsed) hook or pass the `resolveDependencies` flag, which will make the Promise returned by `this.load` wait until all dependency ids have been resolved.

Note that with regard to the `meta` and `moduleSideEffects` options, the same restrictions apply as for the [`resolveId`](/reference/Interface.Plugin#resolveid) hook: Their values only have an effect if the module has not been loaded yet. Thus, it is very important to use [`this.resolve`](/reference/Interface.PluginContext#resolve) first to find out if any plugins want to set special values for these options in their [`resolveId`](/reference/Interface.Plugin#resolveid) hook, and pass these options on to `this.load` if appropriate. The example below showcases how this can be handled to add a proxy module for modules containing a special code comment. Note the special handling for re-exporting the default export:

```js
export default function addProxyPlugin() {
  return {
    async resolveId(source, importer, options) {
      if (importer?.endsWith('?proxy')) {
        // Do not proxy ids used in proxies
        return null;
      }
      // We make sure to pass on any resolveId options to
      // this.resolve to get the module id
      const resolution = await this.resolve(source, importer, options);
      // We can only pre-load existing and non-external ids
      if (resolution && !resolution.external) {
        // we pass on the entire resolution information
        const moduleInfo = await this.load(resolution);
        if (moduleInfo.code.includes('/* use proxy */')) {
          return `${resolution.id}?proxy`;
        }
      }
      // As we already fully resolved the module, there is no reason
      // to resolve it again
      return resolution;
    },
    load: {
      filter: { id: /\?proxy$/ },
      handler(id) {
        const importee = id.slice(0, -'?proxy'.length);
        // Note that namespace reexports do not reexport default exports
        let code =
          `console.log('proxy for ${importee}'); ` + `export * from ${JSON.stringify(importee)};`;
        // We know that while resolving the proxy, importee was
        // already fully loaded and parsed, so we can rely on `exports`
        if (this.getModuleInfo(importee).exports.includes('default')) {
          code += `export { default } from ${JSON.stringify(importee)};`;
        }
        return code;
      },
    },
  };
}
```

If the module was already loaded, `this.load` will just wait for the parsing to complete and then return its module information. If the module was not yet imported by another module, it will not automatically trigger loading other modules imported by this module. Instead, static and dynamic dependencies will only be loaded once this module has actually been imported at least once.

::: warning Deadlocks caused by awaiting `this.load` in cyclic dependencies

While it is safe to use `this.load` in a [`resolveId`](/reference/Interface.Plugin#resolveid) hook, you should be very careful when awaiting it in a [`load`](/reference/Interface.Plugin#load) or [`transform`](/reference/Interface.Plugin#transform) hook. If there are cyclic dependencies in the module graph, this can easily lead to a deadlock, so any plugin needs to manually take care to avoid waiting for `this.load` inside the [`load`](/reference/Interface.Plugin#load) or [`transform`](/reference/Interface.Plugin#transform) of the any module that is in a cycle with the loaded module.

:::

#### Parameters

##### options

{ `id`: `string`; `resolveDependencies?`: `boolean`; } & `Partial`<[`PartialNull`](TypeAlias.PartialNull.md)<[`ModuleOptions`](Interface.ModuleOptions.md)>>

#### Returns

`Promise`<[`ModuleInfo`](Interface.ModuleInfo.md)>

#### Inherited from

[`PluginContext`](Interface.PluginContext.md).[`load`](Interface.PluginContext.md#load)

***

### parse()

* **Type**: (`input`: `string`, `options?`: `ParserOptions` | `null`) => `Program`

Use Rolldown's internal parser to parse code to an [ESTree-compatible](https://github.com/estree/estree) AST.

#### Parameters

##### input

`string`

##### options?

`ParserOptions` | `null`

#### Returns

`Program`

#### Inherited from

[`PluginContext`](Interface.PluginContext.md).[`parse`](Interface.PluginContext.md#parse)

***

### resolve()

* **Type**: (`source`: `string`, `importer?`: `string`, `options?`: [`PluginContextResolveOptions`](Interface.PluginContextResolveOptions.md)) => `Promise`<[`ResolvedId`](Interface.ResolvedId.md) | `null`>

Resolve imports to module ids (i.e. file names) using the same plugins that Rolldown uses,
and determine if an import should be external.

When calling this function from a [`resolveId`](Interface.Plugin.md#resolveid) hook, you should
always check if it makes sense for you to pass along the
[options](Interface.PluginContextResolveOptions.md).

#### Parameters

##### source

`string`

##### importer?

`string`

##### options?

[`PluginContextResolveOptions`](Interface.PluginContextResolveOptions.md)

#### Returns

`Promise`<[`ResolvedId`](Interface.ResolvedId.md) | `null`>

If `Promise<null>` is returned, the import could not be resolved by Rolldown or any plugin
but was not explicitly marked as external by the user.
If an absolute external id is returned that should remain absolute in the output either
via the
[`makeAbsoluteExternalsRelative`](Interface.InputOptions.md#makeabsoluteexternalsrelative)
option or by explicit plugin choice in the [`resolveId`](Interface.Plugin.md#resolveid) hook,
`external` will be `"absolute"` instead of `true`.

#### Inherited from

[`PluginContext`](Interface.PluginContext.md).[`resolve`](Interface.PluginContext.md#resolve)

## Logging Methods

### debug()

* **Type**: (`log`, `pos?`) => `void`

Same as [`PluginContext.debug`](Interface.MinimalPluginContext.md#debug), but a `position` param can be supplied.

#### Parameters

##### log

`string` | [`RolldownLog`](Interface.RolldownLog.md) | () => `string` | [`RolldownLog`](Interface.RolldownLog.md)

##### pos?

A character index or file location which will be used to augment the log with
[`pos`](Interface.RolldownError.md#pos), [`loc`](Interface.RolldownError.md#loc) and
[`frame`](Interface.RolldownError.md#frame).

`number` | { `column`: `number`; `line`: `number`; }

#### Returns

`void`

#### Overrides

[`PluginContext`](Interface.PluginContext.md).[`debug`](Interface.PluginContext.md#debug)

***

### info()

* **Type**: (`log`, `pos?`) => `void`

Same as [`PluginContext.info`](Interface.MinimalPluginContext.md#info), but a `position` param can be supplied.

#### Parameters

##### log

`string` | [`RolldownLog`](Interface.RolldownLog.md) | () => `string` | [`RolldownLog`](Interface.RolldownLog.md)

##### pos?

A character index or file location which will be used to augment the log with
[`pos`](Interface.RolldownError.md#pos), [`loc`](Interface.RolldownError.md#loc) and
[`frame`](Interface.RolldownError.md#frame).

`number` | { `column`: `number`; `line`: `number`; }

#### Returns

`void`

#### Overrides

[`PluginContext`](Interface.PluginContext.md).[`info`](Interface.PluginContext.md#info)

***

### warn()

* **Type**: (`log`, `pos?`) => `void`

Same as [`PluginContext.warn`](Interface.MinimalPluginContext.md#warn), but a `position` param can be supplied.

#### Parameters

##### log

`string` | [`RolldownLog`](Interface.RolldownLog.md) | () => `string` | [`RolldownLog`](Interface.RolldownLog.md)

##### pos?

A character index or file location which will be used to augment the log with
[`pos`](Interface.RolldownError.md#pos), [`loc`](Interface.RolldownError.md#loc) and
[`frame`](Interface.RolldownError.md#frame).

`number` | { `column`: `number`; `line`: `number`; }

#### Returns

`void`

#### Overrides

[`PluginContext`](Interface.PluginContext.md).[`warn`](Interface.PluginContext.md#warn)

***

### error()

* **Type**: (`e`: `string` | [`RolldownError`](Interface.RolldownError.md), `pos?`: `number` | { `column`: `number`; `line`: `number`; }) => `never`

Same as [`PluginContext.error`](Interface.MinimalPluginContext.md#error), but the `id` of the current module will
also be added and a `position` param can be supplied.

#### Parameters

##### e

`string` | [`RolldownError`](Interface.RolldownError.md)

##### pos?

A character index or file location which will be used to augment the log with
[`pos`](Interface.RolldownError.md#pos), [`loc`](Interface.RolldownError.md#loc) and
[`frame`](Interface.RolldownError.md#frame).

`number` | { `column`: `number`; `line`: `number`; }

#### Returns

`never`

#### Overrides

`PluginContext.error`
