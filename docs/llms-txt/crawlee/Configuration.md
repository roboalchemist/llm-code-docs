# Source: https://crawlee.dev/js/api/core/class/Configuration.md

# Configuration<!-- -->

`Configuration` is a value object holding Crawlee configuration. By default, there is a global singleton instance of this class available via `Configuration.getGlobalConfig()`. Places that depend on a configurable behaviour depend on this class, as they have the global instance as the default value.

*Using global configuration:*

```
import { BasicCrawler, Configuration } from 'crawlee';

// Get the global configuration
const config = Configuration.getGlobalConfig();
// Set the 'persistStateIntervalMillis' option
// of global configuration to 10 seconds
config.set('persistStateIntervalMillis', 10_000);

// No need to pass the configuration to the crawler,
// as it's using the global configuration by default
const crawler = new BasicCrawler();
```

*Using custom configuration:*

```
import { BasicCrawler, Configuration } from 'crawlee';

// Create a new configuration
const config = new Configuration({ persistStateIntervalMillis: 30_000 });
// Pass the configuration to the crawler
const crawler = new BasicCrawler({ ... }, config);
```

The configuration provided via environment variables always takes precedence. We can also define the `crawlee.json` file in the project root directory which will serve as a baseline, so the options provided in constructor will override those. In other words, the precedence is:

```
crawlee.json < constructor options < environment variables
```

## Supported Configuration Options

| Key                          | Environment Variable                    | Default Value |
| :--------------------------- | :-------------------------------------- | :------------ |
| `memoryMbytes`               | `CRAWLEE_MEMORY_MBYTES`                 | -             |
| `logLevel`                   | `CRAWLEE_LOG_LEVEL`                     | -             |
| `headless`                   | `CRAWLEE_HEADLESS`                      | `true`        |
| `defaultDatasetId`           | `CRAWLEE_DEFAULT_DATASET_ID`            | `'default'`   |
| `defaultKeyValueStoreId`     | `CRAWLEE_DEFAULT_KEY_VALUE_STORE_ID`    | `'default'`   |
| `defaultRequestQueueId`      | `CRAWLEE_DEFAULT_REQUEST_QUEUE_ID`      | `'default'`   |
| `persistStateIntervalMillis` | `CRAWLEE_PERSIST_STATE_INTERVAL_MILLIS` | `60_000`      |
| `purgeOnStart`               | `CRAWLEE_PURGE_ON_START`                | `true`        |
| `persistStorage`             | `CRAWLEE_PERSIST_STORAGE`               | `true`        |

## Advanced Configuration Options

| Key                     | Environment Variable              | Default Value |
| :---------------------- | :-------------------------------- | :------------ |
| `inputKey`              | `CRAWLEE_INPUT_KEY`               | `'INPUT'`     |
| `xvfb`                  | `CRAWLEE_XVFB`                    | -             |
| `chromeExecutablePath`  | `CRAWLEE_CHROME_EXECUTABLE_PATH`  | -             |
| `defaultBrowserPath`    | `CRAWLEE_DEFAULT_BROWSER_PATH`    | -             |
| `disableBrowserSandbox` | `CRAWLEE_DISABLE_BROWSER_SANDBOX` | -             |
| `availableMemoryRatio`  | `CRAWLEE_AVAILABLE_MEMORY_RATIO`  | `0.25`        |
| `systemInfoV2`          | `CRAWLEE_SYSTEM_INFO_V2`          | false         |
| \`containerized         | \`CRAWLEE\_CONTAINERIZED          | -             |

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**storageManagers](#storageManagers)

### Methods

* [**get](#get)
* [**getEventManager](#getEventManager)
* [**set](#set)
* [**useEventManager](#useEventManager)
* [**useStorageClient](#useStorageClient)
* [**getEventManager](#getEventManager)
* [**getGlobalConfig](#getGlobalConfig)
* [**getStorageClient](#getStorageClient)
* [**resetGlobalState](#resetGlobalState)
* [**set](#set)
* [**useStorageClient](#useStorageClient)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L318)constructor

* ****new Configuration**(options): [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)

- Creates new `Configuration` instance with provided options. Env vars will have precedence over those.

  ***

  #### Parameters

  * ##### options: [ConfigurationOptions](https://crawlee.dev/js/api/core/interface/ConfigurationOptions.md) = <!-- -->{}

  #### Returns [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)

## Properties<!-- -->[**](#Properties)

### [**](#storageManagers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L313)publicreadonlystorageManagers

**storageManagers: Map\<Constructor, StorageManager<[IStorage](https://crawlee.dev/js/api/core/interface/IStorage.md)>> =

<!-- -->

...

## Methods<!-- -->[**](#Methods)

### [**](#get)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L340)get

* ****get**\<T, U>(key, defaultValue): U

- Returns configured value. First checks the environment variables, then provided configuration, fallbacks to the `defaultValue` argument if provided, otherwise uses the default value as described in the above section.

  ***

  #### Parameters

  * ##### key: T
  * ##### optionaldefaultValue: U

  #### Returns U

### [**](#getEventManager)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L421)getEventManager

* ****getEventManager**(): [EventManager](https://crawlee.dev/js/api/core/class/EventManager.md)

- #### Returns [EventManager](https://crawlee.dev/js/api/core/class/EventManager.md)

### [**](#set)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L391)set

* ****set**(key, value): void

- Sets value for given option. Only affects this `Configuration` instance, the value will not be propagated down to the env var. To reset a value, we can omit the `value` argument or pass `undefined` there.

  ***

  #### Parameters

  * ##### key: keyof<!-- --> [ConfigurationOptions](https://crawlee.dev/js/api/core/interface/ConfigurationOptions.md)
  * ##### optionalvalue: any

  #### Returns void

### [**](#useEventManager)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L465)useEventManager

* ****useEventManager**(events): void

- #### Parameters

  * ##### events: [EventManager](https://crawlee.dev/js/api/core/class/EventManager.md)

  #### Returns void

### [**](#useStorageClient)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L457)useStorageClient

* ****useStorageClient**(client): void

- #### Parameters

  * ##### client: [StorageClient](https://crawlee.dev/js/api/core/interface/StorageClient.md)

  #### Returns void

### [**](#getEventManager)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L491)staticgetEventManager

* ****getEventManager**(): [EventManager](https://crawlee.dev/js/api/core/class/EventManager.md)

- Gets default [EventManager](https://crawlee.dev/js/api/core/class/EventManager.md) instance.

  ***

  #### Returns [EventManager](https://crawlee.dev/js/api/core/class/EventManager.md)

### [**](#getGlobalConfig)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L472)staticgetGlobalConfig

* ****getGlobalConfig**(): [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)

- Returns the global configuration instance. It will respect the environment variables.

  ***

  #### Returns [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)

### [**](#getStorageClient)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L484)staticgetStorageClient

* ****getStorageClient**(): [StorageClient](https://crawlee.dev/js/api/core/interface/StorageClient.md)

- Gets default [StorageClient](https://crawlee.dev/js/api/core/interface/StorageClient.md) instance.

  ***

  #### Returns [StorageClient](https://crawlee.dev/js/api/core/interface/StorageClient.md)

### [**](#resetGlobalState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L499)staticresetGlobalState

* ****resetGlobalState**(): void

- Resets global configuration instance. The default instance holds configuration based on env vars, if we want to change them, we need to first reset the global state. Used mainly for testing purposes.

  ***

  #### Returns void

### [**](#set)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L399)staticset

* ****set**(key, value): void

- Sets value for given option. Only affects the global `Configuration` instance, the value will not be propagated down to the env var. To reset a value, we can omit the `value` argument or pass `undefined` there.

  ***

  #### Parameters

  * ##### key: keyof<!-- --> [ConfigurationOptions](https://crawlee.dev/js/api/core/interface/ConfigurationOptions.md)
  * ##### optionalvalue: any

  #### Returns void

### [**](#useStorageClient)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L461)staticuseStorageClient

* ****useStorageClient**(client): void

- #### Parameters

  * ##### client: [StorageClient](https://crawlee.dev/js/api/core/interface/StorageClient.md)

  #### Returns void
