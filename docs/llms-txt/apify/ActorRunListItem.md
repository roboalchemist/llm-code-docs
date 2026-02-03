# Source: https://docs.apify.com/api/client/js/reference/interface/ActorRunListItem.md

# ActorRunListItem<!-- -->

Simplified Actor run information used in list results.

Contains basic information about a run without detailed statistics.

### Hierarchy

* *ActorRunListItem*
  * [ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)

## Index[**](#Index)

### Properties

* [**actId](#actId)
* [**actorTaskId](#actorTaskId)
* [**buildId](#buildId)
* [**buildNumber](#buildNumber)
* [**defaultDatasetId](#defaultDatasetId)
* [**defaultKeyValueStoreId](#defaultKeyValueStoreId)
* [**defaultRequestQueueId](#defaultRequestQueueId)
* [**finishedAt](#finishedAt)
* [**id](#id)
* [**meta](#meta)
* [**startedAt](#startedAt)
* [**status](#status)
* [**usageTotalUsd](#usageTotalUsd)

## Properties<!-- -->[**](#Properties)

### [**](#actId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L688)actId

**actId: string

### [**](#actorTaskId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L689)optionalactorTaskId

**actorTaskId?

<!-- -->

: string

### [**](#buildId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L694)buildId

**buildId: string

### [**](#buildNumber)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L695)buildNumber

**buildNumber: string

### [**](#defaultDatasetId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L697)defaultDatasetId

**defaultDatasetId: string

### [**](#defaultKeyValueStoreId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L696)defaultKeyValueStoreId

**defaultKeyValueStoreId: string

### [**](#defaultRequestQueueId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L698)defaultRequestQueueId

**defaultRequestQueueId: string

### [**](#finishedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L691)finishedAt

**finishedAt: Date

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L687)id

**id: string

### [**](#meta)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L693)meta

**meta: [ActorRunMeta](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRunMeta.md)

### [**](#startedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L690)startedAt

**startedAt: Date

### [**](#status)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L692)status

**status: READY | RUNNING | SUCCEEDED | FAILED | ABORTING | ABORTED | TIMING-OUT | TIMED-OUT

### [**](#usageTotalUsd)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L699)optionalusageTotalUsd

**usageTotalUsd?

<!-- -->

: number
