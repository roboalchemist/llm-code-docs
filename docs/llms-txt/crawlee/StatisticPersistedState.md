# Source: https://crawlee.dev/js/api/core/interface/StatisticPersistedState.md

# StatisticPersistedState<!-- -->

Format of the persisted stats

### Hierarchy

* Omit<[StatisticState](https://crawlee.dev/js/api/core/interface/StatisticState.md), statsPersistedAt>
  * *StatisticPersistedState*

## Index[**](#Index)

### Properties

* [**crawlerFinishedAt](#crawlerFinishedAt)
* [**crawlerLastStartTimestamp](#crawlerLastStartTimestamp)
* [**crawlerRuntimeMillis](#crawlerRuntimeMillis)
* [**crawlerStartedAt](#crawlerStartedAt)
* [**errors](#errors)
* [**requestAvgFailedDurationMillis](#requestAvgFailedDurationMillis)
* [**requestAvgFinishedDurationMillis](#requestAvgFinishedDurationMillis)
* [**requestMaxDurationMillis](#requestMaxDurationMillis)
* [**requestMinDurationMillis](#requestMinDurationMillis)
* [**requestRetryHistogram](#requestRetryHistogram)
* [**requestsFailed](#requestsFailed)
* [**requestsFailedPerMinute](#requestsFailedPerMinute)
* [**requestsFinished](#requestsFinished)
* [**requestsFinishedPerMinute](#requestsFinishedPerMinute)
* [**requestsRetries](#requestsRetries)
* [**requestsTotal](#requestsTotal)
* [**requestsWithStatusCode](#requestsWithStatusCode)
* [**requestTotalDurationMillis](#requestTotalDurationMillis)
* [**requestTotalFailedDurationMillis](#requestTotalFailedDurationMillis)
* [**requestTotalFinishedDurationMillis](#requestTotalFinishedDurationMillis)
* [**retryErrors](#retryErrors)
* [**statsId](#statsId)
* [**statsPersistedAt](#statsPersistedAt)

## Properties<!-- -->[**](#Properties)

### [**](#crawlerFinishedAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L507)inheritedcrawlerFinishedAt

**crawlerFinishedAt: null | string | Date

Inherited from Omit.crawlerFinishedAt

### [**](#crawlerLastStartTimestamp)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L489)crawlerLastStartTimestamp

**crawlerLastStartTimestamp: number

### [**](#crawlerRuntimeMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L508)inheritedcrawlerRuntimeMillis

**crawlerRuntimeMillis: number

Inherited from Omit.crawlerRuntimeMillis

### [**](#crawlerStartedAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L506)inheritedcrawlerStartedAt

**crawlerStartedAt: null | string | Date

Inherited from Omit.crawlerStartedAt

### [**](#errors)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L510)inheritederrors

**errors: Record\<string, unknown>

Inherited from Omit.errors

### [**](#requestAvgFailedDurationMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L485)requestAvgFailedDurationMillis

**requestAvgFailedDurationMillis: number

### [**](#requestAvgFinishedDurationMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L486)requestAvgFinishedDurationMillis

**requestAvgFinishedDurationMillis: number

### [**](#requestMaxDurationMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L503)inheritedrequestMaxDurationMillis

**requestMaxDurationMillis: number

Inherited from Omit.requestMaxDurationMillis

### [**](#requestMinDurationMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L502)inheritedrequestMinDurationMillis

**requestMinDurationMillis: number

Inherited from Omit.requestMinDurationMillis

### [**](#requestRetryHistogram)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L483)requestRetryHistogram

**requestRetryHistogram: number\[]

### [**](#requestsFailed)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L498)inheritedrequestsFailed

**requestsFailed: number

Inherited from Omit.requestsFailed

### [**](#requestsFailedPerMinute)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L500)inheritedrequestsFailedPerMinute

**requestsFailedPerMinute: number

Inherited from Omit.requestsFailedPerMinute

### [**](#requestsFinished)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L497)inheritedrequestsFinished

**requestsFinished: number

Inherited from Omit.requestsFinished

### [**](#requestsFinishedPerMinute)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L501)inheritedrequestsFinishedPerMinute

**requestsFinishedPerMinute: number

Inherited from Omit.requestsFinishedPerMinute

### [**](#requestsRetries)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L499)inheritedrequestsRetries

**requestsRetries: number

Inherited from Omit.requestsRetries

### [**](#requestsTotal)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L488)requestsTotal

**requestsTotal: number

### [**](#requestsWithStatusCode)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L512)inheritedrequestsWithStatusCode

**requestsWithStatusCode: Record\<string, number>

Inherited from Omit.requestsWithStatusCode

### [**](#requestTotalDurationMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L487)requestTotalDurationMillis

**requestTotalDurationMillis: number

### [**](#requestTotalFailedDurationMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L504)inheritedrequestTotalFailedDurationMillis

**requestTotalFailedDurationMillis: number

Inherited from Omit.requestTotalFailedDurationMillis

### [**](#requestTotalFinishedDurationMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L505)inheritedrequestTotalFinishedDurationMillis

**requestTotalFinishedDurationMillis: number

Inherited from Omit.requestTotalFinishedDurationMillis

### [**](#retryErrors)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L511)inheritedretryErrors

**retryErrors: Record\<string, unknown>

Inherited from Omit.retryErrors

### [**](#statsId)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L484)statsId

**statsId: number

### [**](#statsPersistedAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L490)statsPersistedAt

**statsPersistedAt: string
