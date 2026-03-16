# Source: https://crawlee.dev/js/api/memory-storage/interface/MemoryStorageOptions.md

# MemoryStorageOptions<!-- -->

## Index[**](#Index)

### Properties

* [**localDataDirectory](#localDataDirectory)
* [**persistStorage](#persistStorage)
* [**writeMetadata](#writeMetadata)

## Properties<!-- -->[**](#Properties)

### [**](#localDataDirectory)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L23)optionallocalDataDirectory

**localDataDirectory?

<!-- -->

: string = process.env.CRAWLEE\_STORAGE\_DIR ?? ‘./storage’

Path to directory where the data will also be saved.

### [**](#persistStorage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L37)optionalpersistStorage

**persistStorage?

<!-- -->

: boolean = true

Whether the memory storage should also write its stored content to the disk.

You can also disable this by setting the `CRAWLEE_PERSIST_STORAGE` environment variable to `false`.

### [**](#writeMetadata)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L29)optionalwriteMetadata

**writeMetadata?

<!-- -->

: boolean = process.env.DEBUG?.includes(‘\*’) ?? process.env.DEBUG?.includes(‘crawlee:memory-storage’) ?? false

Whether to also write optional metadata files when storing to disk.
