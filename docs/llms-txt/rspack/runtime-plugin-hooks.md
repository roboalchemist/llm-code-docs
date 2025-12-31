# Source: https://rspack.dev/api/plugin-api/runtime-plugin-hooks.md

import { Collapse, CollapsePanel } from '@components/Collapse';

# RuntimePlugin hooks

`RuntimePlugin` is used to generate the code for the Rspack startup. It provides the following hooks that can be used to modify these runtime codes.

You can obtain these hooks like below:

```js title="rspack.config.mjs"
export default {
  //...
  plugins: [
    {
      apply: (compiler) => {
        const { RuntimePlugin } = compiler.rspack;
        compiler.hooks.compilation.tap('MyPlugin', (compilation) => {
          const hooks = RuntimePlugin.getCompilationHooks(compilation);
          //...
        });
      },
    },
  ],
};
```

## `createScript`

`SyncWaterallHook<[string, chunk]>`

Can modify the code executed when creating the `<script>` tag.

As in the following code, the `crossorigin` attribute can be added to the `<script>` tag:

```js
hooks.createScript.tap('MyPlugin', (code, chunk) => {
  return `
    ${code}
    script.crossorigin = 'anonymous';
  `;
});
```

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="CreateScript.ts" key="CreateScript">
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

## `linkPrefetch`

`SyncWaterallHook<[string, chunk]>`

Can modify the code executed when creating the [prefetch](/guide/optimization/code-splitting.md#prefetchingpreloading-modules) `<link rel="prefetch">` tag.

As in the following code, the `crossorigin` attribute can be added to the `<link>` tag for prefetching:

```js
hooks.linkPrefetch.tap('MyPlugin', (code, chunk) => {
  return `
    ${code}
    link.crossorigin = 'anonymous';
  `;
});
```

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="CreateScript.ts" key="CreateScript">
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

## `linkPreload`

`SyncWaterallHook<[string, chunk]>`

Can modify the code executed when creating the [preload](/guide/optimization/code-splitting.md#prefetchingpreloading-modules) `<link rel="preload">` tag.

As in the following code, the `crossorigin` attribute can be added to the `<link>` tag for preloading:

```js
hooks.linkPreload.tap('MyPlugin', (code, chunk) => {
  return `
    ${code}
    link.crossorigin = 'anonymous';
  `;
});
```

<Collapse>
  <CollapsePanel className="collapse-code-panel" header="CreateScript.ts" key="CreateScript">
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
