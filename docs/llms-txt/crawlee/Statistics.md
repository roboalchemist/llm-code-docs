# Source: https://crawlee.dev/js/api/core/class/Statistics.md

# Statistics<!-- -->

The statistics class provides an interface to collecting and logging run statistics for requests.

All statistic information is saved on key value store under the key `SDK_CRAWLER_STATISTICS_*`, persists between migrations and abort/resurrect

## Index[**](#Index)

### Properties

* [**errorTracker](#errorTracker)
* [**errorTrackerRetry](#errorTrackerRetry)
* [**id](#id)
* [**requestRetryHistogram](#requestRetryHistogram)
* [**state](#state)

### Methods

* [**calculate](#calculate)
* [**persistState](#persistState)
* [**registerStatusCode](#registerStatusCode)
* [**reset](#reset)
* [**resetStore](#resetStore)
* [**startCapturing](#startCapturing)
* [**stopCapturing](#stopCapturing)
* [**toJSON](#toJSON)

## Properties<!-- -->[**](#Properties)

### [**](#errorTracker)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L65)errorTracker

**errorTracker: [ErrorTracker](https://crawlee.dev/js/api/core/class/ErrorTracker.md)

An error tracker for final retry errors.

### [**](#errorTrackerRetry)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L70)errorTrackerRetry

**errorTrackerRetry: [ErrorTracker](https://crawlee.dev/js/api/core/class/ErrorTracker.md)

An error tracker for retry errors prior to the final retry.

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L75)readonlyid

**id: number =

<!-- -->

...

Statistic instance id.

### [**](#requestRetryHistogram)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L85)readonlyrequestRetryHistogram

**requestRetryHistogram: number\[] =

<!-- -->

\[]

Contains the current retries histogram. Index 0 means 0 retries, index 2, 2 retries, and so on

### [**](#state)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L80)state

**state: [StatisticState](https://crawlee.dev/js/api/core/interface/StatisticState.md)

Current statistic state used for doing calculations on [Statistics.calculate](https://crawlee.dev/js/api/core/class/Statistics.md#calculate) calls

## Methods<!-- -->[**](#Methods)

### [**](#calculate)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L253)calculate

* ****calculate**(): { crawlerRuntimeMillis: number; requestAvgFailedDurationMillis: number; requestAvgFinishedDurationMillis: number; requestsFailedPerMinute: number; requestsFinishedPerMinute: number; requestsTotal: number; requestTotalDurationMillis: number }

- Calculate the current statistics

  ***

  #### Returns { crawlerRuntimeMillis: number; requestAvgFailedDurationMillis: number; requestAvgFinishedDurationMillis: number; requestsFailedPerMinute: number; requestsFinishedPerMinute: number; requestsTotal: number; requestTotalDurationMillis: number }

  * ##### crawlerRuntimeMillis: number
  * ##### requestAvgFailedDurationMillis: number
  * ##### requestAvgFinishedDurationMillis: number
  * ##### requestsFailedPerMinute: number
  * ##### requestsFinishedPerMinute: number
  * ##### requestsTotal: number
  * ##### requestTotalDurationMillis: number

### [**](#persistState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L320)persistState

* ****persistState**(options): Promise\<void>

- Persist internal state to the key value store

  ***

  #### Parameters

  * ##### optionaloptions: [PersistenceOptions](https://crawlee.dev/js/api/core/interface/PersistenceOptions.md)

    Override the persistence options provided in the constructor

  #### Returns Promise\<void>

### [**](#registerStatusCode)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L198)registerStatusCode

* ****registerStatusCode**(code): void

- Increments the status code counter.

  ***

  #### Parameters

  * ##### code: number

  #### Returns void

### [**](#reset)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L150)reset

* ****reset**(): void

- Set the current statistic instance to pristine values

  ***

  #### Returns void

### [**](#resetStore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L183)resetStore

* ****resetStore**(options): Promise\<void>

- #### Parameters

  * ##### optionaloptions: [PersistenceOptions](https://crawlee.dev/js/api/core/interface/PersistenceOptions.md)

    Override the persistence options provided in the constructor

  #### Returns Promise\<void>

### [**](#startCapturing)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L279)startCapturing

* ****startCapturing**(): Promise\<void>

- Initializes the key value store for persisting the statistics, displaying the current state in predefined intervals

  ***

  #### Returns Promise\<void>

### [**](#stopCapturing)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L302)stopCapturing

* ****stopCapturing**(): Promise\<void>

- Stops logging and remove event listeners, then persist

  ***

  #### Returns Promise\<void>

### [**](#toJSON)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L404)toJSON

* ****toJSON**(): [StatisticPersistedState](https://crawlee.dev/js/api/core/interface/StatisticPersistedState.md)

- Make this class serializable when called with `JSON.stringify(statsInstance)` directly or through `keyValueStore.setValue('KEY', statsInstance)`

  ***

  #### Returns [StatisticPersistedState](https://crawlee.dev/js/api/core/interface/StatisticPersistedState.md)
