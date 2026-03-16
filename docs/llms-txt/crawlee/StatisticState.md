# Source: https://crawlee.dev/js/api/core/interface/StatisticState.md

# StatisticState<!-- -->

Contains the statistics state

## Index[**](#Index)

### Properties

* [**crawlerFinishedAt](#crawlerFinishedAt)
* [**crawlerRuntimeMillis](#crawlerRuntimeMillis)
* [**crawlerStartedAt](#crawlerStartedAt)
* [**errors](#errors)
* [**requestMaxDurationMillis](#requestMaxDurationMillis)
* [**requestMinDurationMillis](#requestMinDurationMillis)
* [**requestsFailed](#requestsFailed)
* [**requestsFailedPerMinute](#requestsFailedPerMinute)
* [**requestsFinished](#requestsFinished)
* [**requestsFinishedPerMinute](#requestsFinishedPerMinute)
* [**requestsRetries](#requestsRetries)
* [**requestsWithStatusCode](#requestsWithStatusCode)
* [**requestTotalFailedDurationMillis](#requestTotalFailedDurationMillis)
* [**requestTotalFinishedDurationMillis](#requestTotalFinishedDurationMillis)
* [**retryErrors](#retryErrors)
* [**statsPersistedAt](#statsPersistedAt)

## Properties<!-- -->[**](#Properties)

### [**](#crawlerFinishedAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L507)crawlerFinishedAt

**crawlerFinishedAt: null | string | Date

### [**](#crawlerRuntimeMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L508)crawlerRuntimeMillis

**crawlerRuntimeMillis: number

### [**](#crawlerStartedAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L506)crawlerStartedAt

**crawlerStartedAt: null | string | Date

### [**](#errors)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L510)errors

**errors: Record\<string, unknown>

### [**](#requestMaxDurationMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L503)requestMaxDurationMillis

**requestMaxDurationMillis: number

### [**](#requestMinDurationMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L502)requestMinDurationMillis

**requestMinDurationMillis: number

### [**](#requestsFailed)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L498)requestsFailed

**requestsFailed: number

### [**](#requestsFailedPerMinute)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L500)requestsFailedPerMinute

**requestsFailedPerMinute: number

### [**](#requestsFinished)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L497)requestsFinished

**requestsFinished: number

### [**](#requestsFinishedPerMinute)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L501)requestsFinishedPerMinute

**requestsFinishedPerMinute: number

### [**](#requestsRetries)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L499)requestsRetries

**requestsRetries: number

### [**](#requestsWithStatusCode)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L512)requestsWithStatusCode

**requestsWithStatusCode: Record\<string, number>

### [**](#requestTotalFailedDurationMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L504)requestTotalFailedDurationMillis

**requestTotalFailedDurationMillis: number

### [**](#requestTotalFinishedDurationMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L505)requestTotalFinishedDurationMillis

**requestTotalFinishedDurationMillis: number

### [**](#retryErrors)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L511)retryErrors

**retryErrors: Record\<string, unknown>

### [**](#statsPersistedAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L509)statsPersistedAt

**statsPersistedAt: null | string | Date
