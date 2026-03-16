# Source: https://crawlee.dev/js/api/utils/interface/MemoryInfo.md

# MemoryInfo<!-- -->

Describes memory usage of the process.

## Index[**](#Index)

### Properties

* [**childProcessesBytes](#childProcessesBytes)
* [**freeBytes](#freeBytes)
* [**mainProcessBytes](#mainProcessBytes)
* [**totalBytes](#totalBytes)
* [**usedBytes](#usedBytes)

## Properties<!-- -->[**](#Properties)

### [**](#childProcessesBytes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/memory-info.ts#L42)childProcessesBytes

**childProcessesBytes: number

Amount of memory used by child processes of the current Node.js process

### [**](#freeBytes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/memory-info.ts#L33)freeBytes

**freeBytes: number

Amount of free memory in the system or container

### [**](#mainProcessBytes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/memory-info.ts#L39)mainProcessBytes

**mainProcessBytes: number

Amount of memory used the current Node.js process

### [**](#totalBytes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/memory-info.ts#L30)totalBytes

**totalBytes: number

Total memory available in the system or container

### [**](#usedBytes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/memory-info.ts#L36)usedBytes

**usedBytes: number

Amount of memory used (= totalBytes - freeBytes)
