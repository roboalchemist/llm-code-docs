# Source: https://docs.apify.com/sdk/js/reference/interface/ApifyEnv.md

# ApifyEnv<!-- -->

Parsed representation of the Apify environment variables. This object is returned by the [Actor.getEnv](https://docs.apify.com/sdk/js/sdk/js/reference/class/Actor.md#getEnv) function.

## Index[**](#Index)

### Properties

* [**actorBuildId](#actorBuildId)
* [**actorBuildNumber](#actorBuildNumber)
* [**actorEventsWsUrl](#actorEventsWsUrl)
* [**actorId](#actorId)
* [**actorMaxPaidDatasetItems](#actorMaxPaidDatasetItems)
* [**actorRunId](#actorRunId)
* [**actorTaskId](#actorTaskId)
* [**apiBaseUrl](#apiBaseUrl)
* [**apiPublicBaseUrl](#apiPublicBaseUrl)
* [**containerPort](#containerPort)
* [**containerUrl](#containerUrl)
* [**dedicatedCpus](#dedicatedCpus)
* [**defaultDatasetId](#defaultDatasetId)
* [**defaultKeyValueStoreId](#defaultKeyValueStoreId)
* [**defaultRequestQueueId](#defaultRequestQueueId)
* [**disableOutdatedWarning](#disableOutdatedWarning)
* [**fact](#fact)
* [**headless](#headless)
* [**chromeExecutablePath](#chromeExecutablePath)
* [**inputKey](#inputKey)
* [**inputSecretsPrivateKeyFile](#inputSecretsPrivateKeyFile)
* [**inputSecretsPrivateKeyPassphrase](#inputSecretsPrivateKeyPassphrase)
* [**isAtHome](#isAtHome)
* [**localStorageDir](#localStorageDir)
* [**logFormat](#logFormat)
* [**logLevel](#logLevel)
* [**memoryMbytes](#memoryMbytes)
* [**metaOrigin](#metaOrigin)
* [**proxyHostname](#proxyHostname)
* [**proxyPassword](#proxyPassword)
* [**proxyPort](#proxyPort)
* [**proxyStatusUrl](#proxyStatusUrl)
* [**sdkLatestVersion](#sdkLatestVersion)
* [**startedAt](#startedAt)
* [**systemInfoIntervalMillis](#systemInfoIntervalMillis)
* [**timeoutAt](#timeoutAt)
* [**token](#token)
* [**userId](#userId)
* [**workflowKey](#workflowKey)

## Properties<!-- -->[**](#Properties)

### [**](#actorBuildId)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1779)actorBuildId

**actorBuildId: null | string

ID of the Actor build used in the run. (ACTOR\_BUILD\_ID)

### [**](#actorBuildNumber)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1881)actorBuildNumber

**actorBuildNumber: null | string

### [**](#actorEventsWsUrl)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1882)actorEventsWsUrl

**actorEventsWsUrl: null | string

### [**](#actorId)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1764)actorId

**actorId: null | string

ID of the Actor (ACTOR\_ID)

### [**](#actorMaxPaidDatasetItems)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1883)actorMaxPaidDatasetItems

**actorMaxPaidDatasetItems: null | number

### [**](#actorRunId)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1769)actorRunId

**actorRunId: null | string

ID of the Actor run (ACTOR\_RUN\_ID)

### [**](#actorTaskId)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1774)actorTaskId

**actorTaskId: null | string

ID of the Actor task (ACTOR\_TASK\_ID)

### [**](#apiBaseUrl)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1844)apiBaseUrl

**apiBaseUrl: null | string

### [**](#apiPublicBaseUrl)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1845)apiPublicBaseUrl

**apiPublicBaseUrl: null | string

### [**](#containerPort)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1884)containerPort

**containerPort: null | number

### [**](#containerUrl)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1885)containerUrl

**containerUrl: null | string

### [**](#dedicatedCpus)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1847)dedicatedCpus

**dedicatedCpus: null | string

### [**](#defaultDatasetId)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1813)defaultDatasetId

**defaultDatasetId: null | string

ID of the dataset where input and output data of this Actor is stored (ACTOR\_DEFAULT\_DATASET\_ID)

### [**](#defaultKeyValueStoreId)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1807)defaultKeyValueStoreId

**defaultKeyValueStoreId: null | string

ID of the key-value store where input and output data of this Actor is stored (ACTOR\_DEFAULT\_KEY\_VALUE\_STORE\_ID)

### [**](#defaultRequestQueueId)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1886)defaultRequestQueueId

**defaultRequestQueueId: null | string

### [**](#disableOutdatedWarning)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1848)disableOutdatedWarning

**disableOutdatedWarning: null | 1

### [**](#fact)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1849)fact

**fact: null | string

### [**](#headless)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1825)headless

**headless: null | string

If set to "1", the web browsers inside the Actor should run in headless mode because there is no windowing system available. (APIFY\_HEADLESS)

### [**](#chromeExecutablePath)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1846)chromeExecutablePath

**chromeExecutablePath: null | string

### [**](#inputKey)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1877)inputKey

**inputKey: null | string

The key of the input record in the Actor’s default key-value store (ACTOR\_INPUT\_KEY)

### [**](#inputSecretsPrivateKeyFile)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1850)inputSecretsPrivateKeyFile

**inputSecretsPrivateKeyFile: null | string

### [**](#inputSecretsPrivateKeyPassphrase)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1851)inputSecretsPrivateKeyPassphrase

**inputSecretsPrivateKeyPassphrase: null | string

### [**](#isAtHome)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1831)isAtHome

**isAtHome: null | string

Is set to "1" if the Actor is running on Apify servers. (APIFY\_IS\_AT\_HOME)

### [**](#localStorageDir)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1859)localStorageDir

**localStorageDir: null | string

Defines the path to a local directory where KeyValueStore, Dataset, and RequestQueue store their data. Typically, it is set to ./storage. If omitted, you should define the APIFY\_TOKEN environment variable instead. See more info on combination of this and APIFY\_TOKEN [here](https://docs.apify.com/sdk/js/sdk/js/docs/guides/environment-variables.md#combinations-of-apify_local_storage_dir-and-apify_token)(CRAWLEE\_STORAGE\_DIR)

### [**](#logFormat)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1866)logFormat

**logFormat: null | string

### [**](#logLevel)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1865)logLevel

**logLevel: null | string

Specifies the minimum log level, which can be one of the following values (in order of severity): DEBUG, INFO, WARNING and ERROR (APIFY\_LOG\_LEVEL)

### [**](#memoryMbytes)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1819)memoryMbytes

**memoryMbytes: null | number

Amount of memory allocated for the Actor, in megabytes (ACTOR\_MEMORY\_MBYTES)

### [**](#metaOrigin)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1872)metaOrigin

**metaOrigin: null | string

Origin for the Actor run, i.e. how it was started. See [here](https://docs.apify.com/sdk/python/reference/enum/MetaOrigin) for more details. (APIFY\_META\_ORIGIN)

### [**](#proxyHostname)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1837)proxyHostname

**proxyHostname: null | string

### [**](#proxyPassword)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1836)proxyPassword

**proxyPassword: null | string

The Apify Proxy password of the user who started the Actor. (APIFY\_PROXY\_PASSWORD)

### [**](#proxyPort)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1838)proxyPort

**proxyPort: null | string

### [**](#proxyStatusUrl)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1843)proxyStatusUrl

**proxyStatusUrl: null | string

You can visit this page to troubleshoot your proxy connection. (APIFY\_PROXY\_STATUS\_URL)

### [**](#sdkLatestVersion)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1878)sdkLatestVersion

**sdkLatestVersion: null | string

### [**](#startedAt)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1796)startedAt

**startedAt: null | Date

Date when the Actor was started (ACTOR\_STARTED\_AT)

### [**](#systemInfoIntervalMillis)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1879)systemInfoIntervalMillis

**systemInfoIntervalMillis: null | string

### [**](#timeoutAt)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1801)timeoutAt

**timeoutAt: null | Date

Date when the Actor will time out (ACTOR\_TIMEOUT\_AT)

### [**](#token)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1791)token

**token: null | string

Authentication token representing privileges given to the Actor run, it can be passed to various Apify APIs (APIFY\_TOKEN)

### [**](#userId)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1785)userId

**userId: null | string

ID of the user who started the Actor - note that it might be different than the owner of the Actor (APIFY\_USER\_ID)

### [**](#workflowKey)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1880)workflowKey

**workflowKey: null | string
