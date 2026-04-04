# Source: https://docs.apify.com/sdk/python/reference/class/ActorRun.md

# Source: https://docs.apify.com/sdk/js/reference/interface/ActorRun.md

# Source: https://docs.apify.com/api/client/js/reference/interface/ActorRun.md

# ActorRun<!-- -->

Complete Actor run information including statistics and usage details.

Represents a single execution of an Actor with all its configuration, status, and resource usage information.

### Hierarchy

* [ActorRunListItem](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRunListItem.md)
  * *ActorRun*

## Index[**](#Index)

### Properties

* [**actId](#actId)
* [**actorTaskId](#actorTaskId)
* [**buildId](#buildId)
* [**buildNumber](#buildNumber)
* [**chargedEventCounts](#chargedEventCounts)
* [**containerUrl](#containerUrl)
* [**defaultDatasetId](#defaultDatasetId)
* [**defaultKeyValueStoreId](#defaultKeyValueStoreId)
* [**defaultRequestQueueId](#defaultRequestQueueId)
* [**exitCode](#exitCode)
* [**finishedAt](#finishedAt)
* [**generalAccess](#generalAccess)
* [**gitBranchName](#gitBranchName)
* [**id](#id)
* [**isContainerServerReady](#isContainerServerReady)
* [**meta](#meta)
* [**options](#options)
* [**pricingInfo](#pricingInfo)
* [**startedAt](#startedAt)
* [**stats](#stats)
* [**status](#status)
* [**statusMessage](#statusMessage)
* [**usage](#usage)
* [**usageTotalUsd](#usageTotalUsd)
* [**usageUsd](#usageUsd)
* [**userId](#userId)

## Properties<!-- -->[**](#Properties)

### [**](#actId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L688)inheritedactId

**actId: string

Inherited from ActorRunListItem.actId

### [**](#actorTaskId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L689)optionalinheritedactorTaskId

**actorTaskId?

<!-- -->

: string

Inherited from ActorRunListItem.actorTaskId

### [**](#buildId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L694)inheritedbuildId

**buildId: string

Inherited from ActorRunListItem.buildId

### [**](#buildNumber)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L695)inheritedbuildNumber

**buildNumber: string

Inherited from ActorRunListItem.buildNumber

### [**](#chargedEventCounts)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L720)optionalchargedEventCounts

**chargedEventCounts?

<!-- -->

: Record\<string, number>

### [**](#containerUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L714)containerUrl

**containerUrl: string

### [**](#defaultDatasetId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L697)inheriteddefaultDatasetId

**defaultDatasetId: string

Inherited from ActorRunListItem.defaultDatasetId

### [**](#defaultKeyValueStoreId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L696)inheriteddefaultKeyValueStoreId

**defaultKeyValueStoreId: string

Inherited from ActorRunListItem.defaultKeyValueStoreId

### [**](#defaultRequestQueueId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L698)inheriteddefaultRequestQueueId

**defaultRequestQueueId: string

Inherited from ActorRunListItem.defaultRequestQueueId

### [**](#exitCode)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L713)optionalexitCode

**exitCode?

<!-- -->

: number

### [**](#finishedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L691)inheritedfinishedAt

**finishedAt: Date

Inherited from ActorRunListItem.finishedAt

### [**](#generalAccess)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L721)optionalgeneralAccess

**generalAccess?

<!-- -->

: null | RUN\_GENERAL\_ACCESS

### [**](#gitBranchName)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L716)optionalgitBranchName

**gitBranchName?

<!-- -->

: string

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L687)inheritedid

**id: string

Inherited from ActorRunListItem.id

### [**](#isContainerServerReady)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L715)optionalisContainerServerReady

**isContainerServerReady?

<!-- -->

: boolean

### [**](#meta)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L693)inheritedmeta

**meta: [ActorRunMeta](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRunMeta.md)

Inherited from ActorRunListItem.meta

### [**](#options)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L712)options

**options: [ActorRunOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRunOptions.md)

### [**](#pricingInfo)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L719)optionalpricingInfo

**pricingInfo?

<!-- -->

: [ActorRunPricingInfo](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorRunPricingInfo)

### [**](#startedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L690)inheritedstartedAt

**startedAt: Date

Inherited from ActorRunListItem.startedAt

### [**](#stats)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L711)stats

**stats: [ActorRunStats](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRunStats.md)

### [**](#status)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L692)inheritedstatus

**status: READY | RUNNING | SUCCEEDED | FAILED | ABORTING | ABORTED | TIMING-OUT | TIMED-OUT

Inherited from ActorRunListItem.status

### [**](#statusMessage)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L710)optionalstatusMessage

**statusMessage?

<!-- -->

: string

### [**](#usage)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L717)optionalusage

**usage?

<!-- -->

: [ActorRunUsage](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRunUsage.md)

### [**](#usageTotalUsd)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L699)optionalinheritedusageTotalUsd

**usageTotalUsd?

<!-- -->

: number

Inherited from ActorRunListItem.usageTotalUsd

### [**](#usageUsd)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L718)optionalusageUsd

**usageUsd?

<!-- -->

: [ActorRunUsage](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRunUsage.md)

### [**](#userId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L709)userId

**userId: string
