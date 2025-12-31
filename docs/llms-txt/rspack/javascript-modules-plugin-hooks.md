# Source: https://rspack.dev/api/plugin-api/javascript-modules-plugin-hooks.md

import { Collapse, CollapsePanel } from '@components/Collapse';

# JavascriptModulesPlugin

## `chunkHash`

`SyncHook<[Chunk, Hash]>`

Called when computing the chunk hash for JavaScript chunks.

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

  <CollapsePanel className="collapse-code-panel" header="Hash.ts" key="Hash">
    <>
      ```ts
      type Hash = {
        update(data: string | Buffer, inputEncoding?: string): Hash;
        digest(encoding?: string): string | Buffer;
      };
      ```
    </>
  </CollapsePanel>
</Collapse>
