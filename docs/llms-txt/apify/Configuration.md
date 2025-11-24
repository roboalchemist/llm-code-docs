# Source: https://docs.apify.com/sdk/python/reference/class/Configuration.md

# Source: https://docs.apify.com/sdk/js/reference/class/Configuration.md

# Configuration<!-- -->

`Configuration` is a value object holding the SDK configuration. We can use it in two ways:

1. When using `Actor` class, we can get the instance configuration via `sdk.config`
   ```
   import { Actor } from 'apify';
   import { BasicCrawler } from 'crawlee';

   const sdk = new Actor({ token: '123' });
   console.log(sdk.config.get('token')); // '123'

   const crawler = new BasicCrawler({
       // ... crawler options
   }, sdk.config);
   ```
2. To get the global configuration (singleton instance). It will respect the environment variables.
   <!-- -->
   ```
   import { BasicCrawler, Configuration } from 'crawlee';

   // Get the global configuration
   const config = Configuration.getGlobalConfig();
   // Set the 'persistStateIntervalMillis' option
   // of global configuration to 30 seconds
   config.set('persistStateIntervalMillis', 30_000);

   // No need to pass the configuration to the crawler,
   // as it's using the global configuration by default
   const crawler = new BasicCrawler();
   ```

## Supported Configuration Options

| Key                          | Environment Variable                  | Default Value |
| :--------------------------- | :------------------------------------ | :------------ |
| `memoryMbytes`               | `ACTOR_MEMORY_MBYTES`                 | -             |
| `headless`                   | `APIFY_HEADLESS`                      | -             |
| `persistStateIntervalMillis` | `APIFY_PERSIST_STATE_INTERVAL_MILLIS` | `60e3`        |
| `token`                      | `APIFY_TOKEN`                         | -             |
| `isAtHome`                   | `APIFY_IS_AT_HOME`                    | -             |
| `defaultDatasetId`           | `ACTOR_DEFAULT_DATASET_ID`            | `'default'`   |
| `defaultKeyValueStoreId`     | `ACTOR_DEFAULT_KEY_VALUE_STORE_ID`    | `'default'`   |
| `defaultRequestQueueId`      | `ACTOR_DEFAULT_REQUEST_QUEUE_ID`      | `'default'`   |

## Advanced Configuration Options

| Key                         | Environment Variable                 | Default Value              |
| :-------------------------- | :----------------------------------- | :------------------------- |
| `actorEventsWsUrl`          | `ACTOR_EVENTS_WEBSOCKET_URL`         | -                          |
| `actorId`                   | `ACTOR_ID`                           | -                          |
| `actorRunId`                | `ACTOR_RUN_ID`                       | -                          |
| `actorTaskId`               | `ACTOR_TASK_ID`                      | -                          |
| `apiBaseUrl`                | `APIFY_API_BASE_URL`                 | `'https://api.apify.com'`  |
| `containerPort`             | `ACTOR_WEB_SERVER_PORT`              | `4321`                     |
| `containerUrl`              | `ACTOR_WEB_SERVER_URL`               | `'http://localhost:4321'`  |
| `inputKey`                  | `ACTOR_INPUT_KEY`                    | `'INPUT'`                  |
| `metamorphAfterSleepMillis` | `APIFY_METAMORPH_AFTER_SLEEP_MILLIS` | `300e3`                    |
| `metaOrigin`                | `APIFY_META_ORIGIN`                  | -                          |
| `proxyHostname`             | `APIFY_PROXY_HOSTNAME`               | `'proxy.apify.com'`        |
| `proxyPassword`             | `APIFY_PROXY_PASSWORD`               | -                          |
| `proxyPort`                 | `APIFY_PROXY_PORT`                   | `8000`                     |
| `proxyStatusUrl`            | `APIFY_PROXY_STATUS_URL`             | `'http://proxy.apify.com'` |
| `userId`                    | `APIFY_USER_ID`                      | -                          |
| `xvfb`                      | `APIFY_XVFB`                         | -                          |
| `standbyPort`               | `ACTOR_STANDBY_PORT`                 | `4321`                     |
| `standbyUrl`                | `ACTOR_STANDBY_URL`                  | -                          |
| `chromeExecutablePath`      | `APIFY_CHROME_EXECUTABLE_PATH`       | -                          |
| `defaultBrowserPath`        | `APIFY_DEFAULT_BROWSER_PATH`         | -                          |

### Hierarchy

* Configuration
  * *Configuration*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**storageManagers](#storageManagers)
* [**globalConfig](#globalConfig)

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

### [**](#constructor)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L241)externalconstructor

* ****new Configuration**(options): [Configuration](https://docs.apify.com/sdk/js/sdk/js/reference/class/Configuration.md)

- Inherited from CoreConfiguration.constructor

  Creates new `Configuration` instance with provided options. Env vars will have precedence over those.

  ***

  #### Parameters

  * ##### externaloptionaloptions: ConfigurationOptions

  #### Returns [Configuration](https://docs.apify.com/sdk/js/sdk/js/reference/class/Configuration.md)

## Properties<!-- -->[**](#Properties)

### [**](#storageManagers)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L237)externalreadonlyinheritedstorageManagers

**storageManagers: Map\<Constructor, StorageManager\<IStorage>>

Inherited from CoreConfiguration.storageManagers

### [**](#globalConfig)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L116)staticoptionalglobalConfig

**globalConfig?

<!-- -->

: [Configuration](https://docs.apify.com/sdk/js/sdk/js/reference/class/Configuration.md)

Overrides CoreConfiguration.globalConfig

* **@inheritDoc**

## Methods<!-- -->[**](#Methods)

### [**](#get)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L206)get

* ****get**\<T, U>(key, defaultValue): U

- Overrides CoreConfiguration.get

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### key: T
  * ##### optionaldefaultValue: U

  #### Returns U

### [**](#getEventManager)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L269)externalinheritedgetEventManager

* ****getEventManager**(): EventManager

- Inherited from CoreConfiguration.getEventManager

  #### Returns EventManager

### [**](#set)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L213)set

* ****set**(key, value): void

- Overrides CoreConfiguration.set

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### key: keyof<!-- --> [ConfigurationOptions](https://docs.apify.com/sdk/js/sdk/js/reference/interface/ConfigurationOptions.md)
  * ##### optionalvalue: any

  #### Returns void

### [**](#useEventManager)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L277)externalinheriteduseEventManager

* ****useEventManager**(events): void

- Inherited from CoreConfiguration.useEventManager

  #### Parameters

  * ##### externalevents: EventManager

  #### Returns void

### [**](#useStorageClient)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L275)externalinheriteduseStorageClient

* ****useStorageClient**(client): void

- Inherited from CoreConfiguration.useStorageClient

  #### Parameters

  * ##### externalclient: StorageClient

  #### Returns void

### [**](#getEventManager)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L289)staticexternalinheritedgetEventManager

* ****getEventManager**(): EventManager

- Inherited from CoreConfiguration.getEventManager

  Gets default EventManager instance.

  ***

  #### Returns EventManager

### [**](#getGlobalConfig)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L220)staticgetGlobalConfig

* ****getGlobalConfig**(): [Configuration](https://docs.apify.com/sdk/js/sdk/js/reference/class/Configuration.md)

- Overrides CoreConfiguration.getGlobalConfig

  * **@inheritDoc**

  ***

  #### Returns [Configuration](https://docs.apify.com/sdk/js/sdk/js/reference/class/Configuration.md)

### [**](#getStorageClient)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L285)staticexternalinheritedgetStorageClient

* ****getStorageClient**(): StorageClient

- Inherited from CoreConfiguration.getStorageClient

  Gets default StorageClient instance.

  ***

  #### Returns StorageClient

### [**](#resetGlobalState)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L233)staticresetGlobalState

* ****resetGlobalState**(): void

- Overrides CoreConfiguration.resetGlobalState

  Resets global configuration instance. The default instance holds configuration based on env vars, if we want to change them, we need to first reset the global state. Used mainly for testing purposes.

  ***

  #### Returns void

### [**](#set)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L258)staticexternalinheritedset

* ****set**(key, value): void

- Inherited from CoreConfiguration.set

  Sets value for given option. Only affects the global `Configuration` instance, the value will not be propagated down to the env var. To reset a value, we can omit the `value` argument or pass `undefined` there.

  ***

  #### Parameters

  * ##### externalkey: keyof<!-- --> ConfigurationOptions
  * ##### externaloptionalvalue: any

  #### Returns void

### [**](#useStorageClient)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L276)staticexternalinheriteduseStorageClient

* ****useStorageClient**(client): void

- Inherited from CoreConfiguration.useStorageClient

  #### Parameters

  * ##### externalclient: StorageClient

  #### Returns void
