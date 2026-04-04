# Source: https://docs.apify.com/sdk/js/reference/interface/ConfigurationOptions.md

# ConfigurationOptions<!-- -->

### Hierarchy

* ConfigurationOptions
  * *ConfigurationOptions*

## Index[**](#Index)

### Properties

* [**actorEventsWsUrl](#actorEventsWsUrl)
* [**actorId](#actorId)
* [**actorRunId](#actorRunId)
* [**actorTaskId](#actorTaskId)
* [**apiBaseUrl](#apiBaseUrl)
* [**apiPublicBaseUrl](#apiPublicBaseUrl)
* [**availableMemoryRatio](#availableMemoryRatio)
* [**containerized](#containerized)
* [**containerPort](#containerPort)
* [**containerUrl](#containerUrl)
* [**defaultBrowserPath](#defaultBrowserPath)
* [**defaultDatasetId](#defaultDatasetId)
* [**defaultKeyValueStoreId](#defaultKeyValueStoreId)
* [**defaultRequestQueueId](#defaultRequestQueueId)
* [**disableBrowserSandbox](#disableBrowserSandbox)
* [**eventManager](#eventManager)
* [**headless](#headless)
* [**chromeExecutablePath](#chromeExecutablePath)
* [**inputKey](#inputKey)
* [**inputSecretsPrivateKeyFile](#inputSecretsPrivateKeyFile)
* [**inputSecretsPrivateKeyPassphrase](#inputSecretsPrivateKeyPassphrase)
* [**isAtHome](#isAtHome)
* [**logLevel](#logLevel)
* [**maxTotalChargeUsd](#maxTotalChargeUsd)
* [**maxUsedCpuRatio](#maxUsedCpuRatio)
* [**memoryMbytes](#memoryMbytes)
* [**metamorphAfterSleepMillis](#metamorphAfterSleepMillis)
* [**metaOrigin](#metaOrigin)
* [**persistStateIntervalMillis](#persistStateIntervalMillis)
* [**persistStorage](#persistStorage)
* [**proxyHostname](#proxyHostname)
* [**proxyPassword](#proxyPassword)
* [**proxyPort](#proxyPort)
* [**proxyStatusUrl](#proxyStatusUrl)
* [**purgeOnStart](#purgeOnStart)
* [**standbyPort](#standbyPort)
* [**standbyUrl](#standbyUrl)
* [**storageClient](#storageClient)
* [**storageClientOptions](#storageClientOptions)
* [**systemInfoIntervalMillis](#systemInfoIntervalMillis)
* [**systemInfoV2](#systemInfoV2)
* [**testPayPerEvent](#testPayPerEvent)
* [**token](#token)
* [**useChargingLogDataset](#useChargingLogDataset)
* [**userId](#userId)
* [**xvfb](#xvfb)

## Properties<!-- -->[**](#Properties)

### [**](#actorEventsWsUrl)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L13)optionalactorEventsWsUrl

**actorEventsWsUrl?

<!-- -->

: string

### [**](#actorId)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L15)optionalactorId

**actorId?

<!-- -->

: string

### [**](#actorRunId)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L16)optionalactorRunId

**actorRunId?

<!-- -->

: string

### [**](#actorTaskId)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L17)optionalactorTaskId

**actorTaskId?

<!-- -->

: string

### [**](#apiBaseUrl)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L18)optionalapiBaseUrl

**apiBaseUrl?

<!-- -->

: string

### [**](#apiPublicBaseUrl)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L21)optionalapiPublicBaseUrl

**apiPublicBaseUrl?

<!-- -->

: string

### [**](#availableMemoryRatio)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L66)externaloptionalinheritedavailableMemoryRatio

**availableMemoryRatio?

<!-- -->

: number = 0.25

Inherited from CoreConfigurationOptions.availableMemoryRatio

Sets the ratio, defining the amount of system memory that could be used by the AutoscaledPool. When the memory usage is more than the provided ratio, the memory is considered overloaded.

Alternative to `CRAWLEE_AVAILABLE_MEMORY_RATIO` environment variable.

### [**](#containerized)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L150)externaloptionalinheritedcontainerized

**containerized?

<!-- -->

: boolean

Inherited from CoreConfigurationOptions.containerized

Used in place of `isContainerized()` when collecting system metrics.

Alternative to `CRAWLEE_CONTAINERIZED` environment variable.

### [**](#containerPort)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L22)optionalcontainerPort

**containerPort?

<!-- -->

: number

### [**](#containerUrl)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L23)optionalcontainerUrl

**containerUrl?

<!-- -->

: string

### [**](#defaultBrowserPath)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L119)externaloptionalinheriteddefaultBrowserPath

**defaultBrowserPath?

<!-- -->

: string

Inherited from CoreConfigurationOptions.defaultBrowserPath

Defines a path to default browser executable.

Alternative to `CRAWLEE_DEFAULT_BROWSER_PATH` environment variable.

### [**](#defaultDatasetId)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L31)externaloptionalinheriteddefaultDatasetId

**defaultDatasetId?

<!-- -->

: string = ‘default’

Inherited from CoreConfigurationOptions.defaultDatasetId

Default dataset id.

Alternative to `CRAWLEE_DEFAULT_DATASET_ID` environment variable.

### [**](#defaultKeyValueStoreId)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L45)externaloptionalinheriteddefaultKeyValueStoreId

**defaultKeyValueStoreId?

<!-- -->

: string = ‘default’

Inherited from CoreConfigurationOptions.defaultKeyValueStoreId

Default key-value store id.

Alternative to `CRAWLEE_DEFAULT_KEY_VALUE_STORE_ID` environment variable.

### [**](#defaultRequestQueueId)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L52)externaloptionalinheriteddefaultRequestQueueId

**defaultRequestQueueId?

<!-- -->

: string = ‘default’

Inherited from CoreConfigurationOptions.defaultRequestQueueId

Default request queue id.

Alternative to `CRAWLEE_DEFAULT_REQUEST_QUEUE_ID` environment variable.

### [**](#disableBrowserSandbox)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L125)externaloptionalinheriteddisableBrowserSandbox

**disableBrowserSandbox?

<!-- -->

: boolean

Inherited from CoreConfigurationOptions.disableBrowserSandbox

Defines whether to disable browser sandbox by adding `--no-sandbox` flag to `launchOptions`.

Alternative to `CRAWLEE_DISABLE_BROWSER_SANDBOX` environment variable.

### [**](#eventManager)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L19)externaloptionalinheritedeventManager

**eventManager?

<!-- -->

: EventManager = EventManager

Inherited from CoreConfigurationOptions.eventManager

Defines the Event Manager to be used.

### [**](#headless)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L100)externaloptionalinheritedheadless

**headless?

<!-- -->

: boolean = true

Inherited from CoreConfigurationOptions.headless

Defines whether web browsers launched by Crawlee will run in the headless mode.

Alternative to `CRAWLEE_HEADLESS` environment variable.

### [**](#chromeExecutablePath)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L113)externaloptionalinheritedchromeExecutablePath

**chromeExecutablePath?

<!-- -->

: string

Inherited from CoreConfigurationOptions.chromeExecutablePath

Defines a path to Chrome executable.

Alternative to `CRAWLEE_CHROME_EXECUTABLE_PATH` environment variable.

### [**](#inputKey)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L93)externaloptionalinheritedinputKey

**inputKey?

<!-- -->

: string = ‘INPUT’

Inherited from CoreConfigurationOptions.inputKey

Defines the default input key, i.e. the key that is used to get the crawler input value from the default [KeyValueStore](https://docs.apify.com/sdk/js/sdk/js/reference/class/KeyValueStore.md) associated with the current crawler run.

Alternative to `CRAWLEE_INPUT_KEY` environment variable.

### [**](#inputSecretsPrivateKeyFile)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L36)optionalinputSecretsPrivateKeyFile

**inputSecretsPrivateKeyFile?

<!-- -->

: string

### [**](#inputSecretsPrivateKeyPassphrase)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L35)optionalinputSecretsPrivateKeyPassphrase

**inputSecretsPrivateKeyPassphrase?

<!-- -->

: string

### [**](#isAtHome)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L33)optionalisAtHome

**isAtHome?

<!-- -->

: boolean

### [**](#logLevel)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L132)externaloptionalinheritedlogLevel

**logLevel?

<!-- -->

: [LogLevel](https://docs.apify.com/sdk/js/sdk/js/reference/enum/LogLevel.md) | (radix) => string | (fractionDigits) => string | (fractionDigits) => string | (precision) => string | () => number | ({ (locales, options): string; (locales, options): string }) = [LogLevel](https://docs.apify.com/sdk/js/sdk/js/reference/enum/LogLevel.md) | (radix) => string | (fractionDigits) => string | (fractionDigits) => string | (precision) => string | () => number | ({ (locales, options): string; (locales, options): string })

Inherited from CoreConfigurationOptions.logLevel

Sets the log level to the given value.

Alternative to `CRAWLEE_LOG_LEVEL` environment variable.

### [**](#maxTotalChargeUsd)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L37)optionalmaxTotalChargeUsd

**maxTotalChargeUsd?

<!-- -->

: number

### [**](#maxUsedCpuRatio)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L58)externaloptionalinheritedmaxUsedCpuRatio

**maxUsedCpuRatio?

<!-- -->

: number = 0.95

Inherited from CoreConfigurationOptions.maxUsedCpuRatio

Sets the ratio, defining the maximum CPU usage. When the CPU usage is higher than the provided ratio, the CPU is considered overloaded.

### [**](#memoryMbytes)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L73)externaloptionalinheritedmemoryMbytes

**memoryMbytes?

<!-- -->

: number

Inherited from CoreConfigurationOptions.memoryMbytes

Sets the amount of system memory in megabytes to be used by the AutoscaledPool. By default, the maximum memory is set to one quarter of total system memory.

Alternative to `CRAWLEE_MEMORY_MBYTES` environment variable.

### [**](#metamorphAfterSleepMillis)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L12)optionalmetamorphAfterSleepMillis

**metamorphAfterSleepMillis?

<!-- -->

: number

### [**](#metaOrigin)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L38)optionalmetaOrigin

**metaOrigin?

<!-- -->

: DEVELOPMENT | WEB | API | SCHEDULER | TEST | WEBHOOK | ACTOR | CLI | STANDBY

### [**](#persistStateIntervalMillis)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L80)externaloptionalinheritedpersistStateIntervalMillis

**persistStateIntervalMillis?

<!-- -->

: number = 60\_000

Inherited from CoreConfigurationOptions.persistStateIntervalMillis

Defines the interval of emitting the `persistState` event.

Alternative to `CRAWLEE_PERSIST_STATE_INTERVAL_MILLIS` environment variable.

### [**](#persistStorage)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L138)externaloptionalinheritedpersistStorage

**persistStorage?

<!-- -->

: boolean

Inherited from CoreConfigurationOptions.persistStorage

Defines whether the storage client used should persist the data it stores.

Alternative to `CRAWLEE_PERSIST_STORAGE` environment variable.

### [**](#proxyHostname)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L24)optionalproxyHostname

**proxyHostname?

<!-- -->

: string

### [**](#proxyPassword)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L25)optionalproxyPassword

**proxyPassword?

<!-- -->

: string

### [**](#proxyPort)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L26)optionalproxyPort

**proxyPort?

<!-- -->

: number

### [**](#proxyStatusUrl)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L27)optionalproxyStatusUrl

**proxyStatusUrl?

<!-- -->

: string

### [**](#purgeOnStart)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L38)externaloptionalinheritedpurgeOnStart

**purgeOnStart?

<!-- -->

: boolean = true

Inherited from CoreConfigurationOptions.purgeOnStart

Defines whether to purge the default storage folders before starting the crawler run.

Alternative to `CRAWLEE_PURGE_ON_START` environment variable.

### [**](#standbyPort)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L31)optionalstandbyPort

**standbyPort?

<!-- -->

: number

* **@deprecated**

  use `containerPort` instead

### [**](#standbyUrl)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L32)optionalstandbyUrl

**standbyUrl?

<!-- -->

: string

### [**](#storageClient)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L14)externaloptionalinheritedstorageClient

**storageClient?

<!-- -->

: StorageClient = StorageClient

Inherited from CoreConfigurationOptions.storageClient

Defines storage client to be used.

### [**](#storageClientOptions)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L24)externaloptionalinheritedstorageClientOptions

**storageClientOptions?

<!-- -->

: Dictionary

Inherited from CoreConfigurationOptions.storageClientOptions

Could be used to adjust the storage client behavior e.g. MemoryStorageOptions could be used to adjust the MemoryStorage behavior.

### [**](#systemInfoIntervalMillis)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L85)externaloptionalinheritedsystemInfoIntervalMillis

**systemInfoIntervalMillis?

<!-- -->

: number = 1\_000

Inherited from CoreConfigurationOptions.systemInfoIntervalMillis

Defines the interval of emitting the `systemInfo` event.

### [**](#systemInfoV2)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L144)externaloptionalinheritedsystemInfoV2

**systemInfoV2?

<!-- -->

: boolean

Inherited from CoreConfigurationOptions.systemInfoV2

Defines whether to use the systemInfoV2 metric collection experiment.

Alternative to `CRAWLEE_SYSTEM_INFO_V2` environment variable.

### [**](#testPayPerEvent)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L39)optionaltestPayPerEvent

**testPayPerEvent?

<!-- -->

: boolean

### [**](#token)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L14)optionaltoken

**token?

<!-- -->

: string

### [**](#useChargingLogDataset)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L40)optionaluseChargingLogDataset

**useChargingLogDataset?

<!-- -->

: boolean

### [**](#userId)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/configuration.ts#L34)optionaluserId

**userId?

<!-- -->

: string

### [**](#xvfb)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/configuration.d.ts#L107)externaloptionalinheritedxvfb

**xvfb?

<!-- -->

: boolean = false

Inherited from CoreConfigurationOptions.xvfb

Defines whether to run X virtual framebuffer on the web browsers launched by Crawlee.

Alternative to `CRAWLEE_XVFB` environment variable.
