# Source: https://crawlee.dev/js/api/core/interface/ConfigurationOptions.md

# ConfigurationOptions<!-- -->

## Index[**](#Index)

### Properties

* [**availableMemoryRatio](#availableMemoryRatio)
* [**chromeExecutablePath](#chromeExecutablePath)
* [**containerized](#containerized)
* [**defaultBrowserPath](#defaultBrowserPath)
* [**defaultDatasetId](#defaultDatasetId)
* [**defaultKeyValueStoreId](#defaultKeyValueStoreId)
* [**defaultRequestQueueId](#defaultRequestQueueId)
* [**disableBrowserSandbox](#disableBrowserSandbox)
* [**eventManager](#eventManager)
* [**headless](#headless)
* [**inputKey](#inputKey)
* [**logLevel](#logLevel)
* [**maxUsedCpuRatio](#maxUsedCpuRatio)
* [**memoryMbytes](#memoryMbytes)
* [**persistStateIntervalMillis](#persistStateIntervalMillis)
* [**persistStorage](#persistStorage)
* [**purgeOnStart](#purgeOnStart)
* [**storageClient](#storageClient)
* [**storageClientOptions](#storageClientOptions)
* [**systemInfoIntervalMillis](#systemInfoIntervalMillis)
* [**systemInfoV2](#systemInfoV2)
* [**xvfb](#xvfb)

## Properties<!-- -->[**](#Properties)

### [**](#availableMemoryRatio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L81)optionalavailableMemoryRatio

**availableMemoryRatio?

<!-- -->

: number = 0.25

Sets the ratio, defining the amount of system memory that could be used by the [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md). When the memory usage is more than the provided ratio, the memory is considered overloaded.

Alternative to `CRAWLEE_AVAILABLE_MEMORY_RATIO` environment variable.

### [**](#chromeExecutablePath)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L135)optionalchromeExecutablePath

**chromeExecutablePath?

<!-- -->

: string

Defines a path to Chrome executable.

Alternative to `CRAWLEE_CHROME_EXECUTABLE_PATH` environment variable.

### [**](#containerized)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L178)optionalcontainerized

**containerized?

<!-- -->

: boolean

Used in place of `isContainerized()` when collecting system metrics.

Alternative to `CRAWLEE_CONTAINERIZED` environment variable.

### [**](#defaultBrowserPath)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L142)optionaldefaultBrowserPath

**defaultBrowserPath?

<!-- -->

: string

Defines a path to default browser executable.

Alternative to `CRAWLEE_DEFAULT_BROWSER_PATH` environment variable.

### [**](#defaultDatasetId)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L41)optionaldefaultDatasetId

**defaultDatasetId?

<!-- -->

: string = ‘default’

Default dataset id.

Alternative to `CRAWLEE_DEFAULT_DATASET_ID` environment variable.

### [**](#defaultKeyValueStoreId)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L57)optionaldefaultKeyValueStoreId

**defaultKeyValueStoreId?

<!-- -->

: string = ‘default’

Default key-value store id.

Alternative to `CRAWLEE_DEFAULT_KEY_VALUE_STORE_ID` environment variable.

### [**](#defaultRequestQueueId)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L65)optionaldefaultRequestQueueId

**defaultRequestQueueId?

<!-- -->

: string = ‘default’

Default request queue id.

Alternative to `CRAWLEE_DEFAULT_REQUEST_QUEUE_ID` environment variable.

### [**](#disableBrowserSandbox)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L149)optionaldisableBrowserSandbox

**disableBrowserSandbox?

<!-- -->

: boolean

Defines whether to disable browser sandbox by adding `--no-sandbox` flag to `launchOptions`.

Alternative to `CRAWLEE_DISABLE_BROWSER_SANDBOX` environment variable.

### [**](#eventManager)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L27)optionaleventManager

**eventManager?

<!-- -->

: [EventManager](https://crawlee.dev/js/api/core/class/EventManager.md) = [EventManager](https://crawlee.dev/js/api/core/class/EventManager.md)

Defines the Event Manager to be used.

### [**](#headless)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L120)optionalheadless

**headless?

<!-- -->

: boolean = true

Defines whether web browsers launched by Crawlee will run in the headless mode.

Alternative to `CRAWLEE_HEADLESS` environment variable.

### [**](#inputKey)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L112)optionalinputKey

**inputKey?

<!-- -->

: string = ‘INPUT’

Defines the default input key, i.e. the key that is used to get the crawler input value from the default [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md) associated with the current crawler run.

Alternative to `CRAWLEE_INPUT_KEY` environment variable.

### [**](#logLevel)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L157)optionallogLevel

**logLevel?

<!-- -->

: [LogLevel](https://crawlee.dev/js/api/core/enum/LogLevel.md) | (radix) => string | (fractionDigits) => string | (fractionDigits) => string | (precision) => string | () => number | ({ (locales, options): string; (locales, options): string }) = [LogLevel](https://crawlee.dev/js/api/core/enum/LogLevel.md) | (radix) => string | (fractionDigits) => string | (fractionDigits) => string | (precision) => string | () => number | ({ (locales, options): string; (locales, options): string })

Sets the log level to the given value.

Alternative to `CRAWLEE_LOG_LEVEL` environment variable.

### [**](#maxUsedCpuRatio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L72)optionalmaxUsedCpuRatio

**maxUsedCpuRatio?

<!-- -->

: number = 0.95

Sets the ratio, defining the maximum CPU usage. When the CPU usage is higher than the provided ratio, the CPU is considered overloaded.

### [**](#memoryMbytes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L89)optionalmemoryMbytes

**memoryMbytes?

<!-- -->

: number

Sets the amount of system memory in megabytes to be used by the [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md). By default, the maximum memory is set to one quarter of total system memory.

Alternative to `CRAWLEE_MEMORY_MBYTES` environment variable.

### [**](#persistStateIntervalMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L97)optionalpersistStateIntervalMillis

**persistStateIntervalMillis?

<!-- -->

: number = 60\_000

Defines the interval of emitting the `persistState` event.

Alternative to `CRAWLEE_PERSIST_STATE_INTERVAL_MILLIS` environment variable.

### [**](#persistStorage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L164)optionalpersistStorage

**persistStorage?

<!-- -->

: boolean

Defines whether the storage client used should persist the data it stores.

Alternative to `CRAWLEE_PERSIST_STORAGE` environment variable.

### [**](#purgeOnStart)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L49)optionalpurgeOnStart

**purgeOnStart?

<!-- -->

: boolean = true

Defines whether to purge the default storage folders before starting the crawler run.

Alternative to `CRAWLEE_PURGE_ON_START` environment variable.

### [**](#storageClient)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L21)optionalstorageClient

**storageClient?

<!-- -->

: [StorageClient](https://crawlee.dev/js/api/core/interface/StorageClient.md) = [StorageClient](https://crawlee.dev/js/api/core/interface/StorageClient.md)

Defines storage client to be used.

### [**](#storageClientOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L33)optionalstorageClientOptions

**storageClientOptions?

<!-- -->

: Dictionary

Could be used to adjust the storage client behavior e.g. [MemoryStorageOptions](https://crawlee.dev/js/api/memory-storage/interface/MemoryStorageOptions.md) could be used to adjust the [MemoryStorage](https://crawlee.dev/js/api/memory-storage/class/MemoryStorage.md) behavior.

### [**](#systemInfoIntervalMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L103)optionalsystemInfoIntervalMillis

**systemInfoIntervalMillis?

<!-- -->

: number = 1\_000

Defines the interval of emitting the `systemInfo` event.

### [**](#systemInfoV2)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L171)optionalsystemInfoV2

**systemInfoV2?

<!-- -->

: boolean

Defines whether to use the systemInfoV2 metric collection experiment.

Alternative to `CRAWLEE_SYSTEM_INFO_V2` environment variable.

### [**](#xvfb)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L128)optionalxvfb

**xvfb?

<!-- -->

: boolean = false

Defines whether to run X virtual framebuffer on the web browsers launched by Crawlee.

Alternative to `CRAWLEE_XVFB` environment variable.
