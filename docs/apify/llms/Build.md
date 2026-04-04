# Source: https://docs.apify.com/api/client/js/reference/interface/Build.md

# Build<!-- -->

Represents an Actor build.

Builds compile Actor source code and prepare it for execution. Each build has a unique ID and can be tagged (e.g., 'latest', 'beta') for easy reference.

## Index[**](#Index)

### Properties

* [**actId](#actId)
* [**actorDefinition](#actorDefinition)
* [**buildNumber](#buildNumber)
* [**finishedAt](#finishedAt)
* [**id](#id)
* [**inputSchema](#inputSchema)
* [**meta](#meta)
* [**options](#options)
* [**readme](#readme)
* [**startedAt](#startedAt)
* [**stats](#stats)
* [**status](#status)
* [**usage](#usage)
* [**usageTotalUsd](#usageTotalUsd)
* [**usageUsd](#usageUsd)
* [**userId](#userId)

## Properties<!-- -->[**](#Properties)

### [**](#actId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L221)actId

**actId: string

### [**](#actorDefinition)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L241)optionalactorDefinition

**actorDefinition?

<!-- -->

: [ActorDefinition](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorDefinition.md)

### [**](#buildNumber)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L237)buildNumber

**buildNumber: string

### [**](#finishedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L224)optionalfinishedAt

**finishedAt?

<!-- -->

: Date

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L220)id

**id: string

### [**](#inputSchema)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L232)optionalinputSchema

**inputSchema?

<!-- -->

: string

* **@deprecated**

  This property is deprecated in favor of `actorDefinition.input`.

### [**](#meta)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L226)meta

**meta: [BuildMeta](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildMeta.md)

### [**](#options)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L228)optionaloptions

**options?

<!-- -->

: [BuildOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildOptions.md)

### [**](#readme)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L236)optionalreadme

**readme?

<!-- -->

: string

* **@deprecated**

  This property is deprecated in favor of `actorDefinition.readme`.

### [**](#startedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L223)startedAt

**startedAt: Date

### [**](#stats)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L227)optionalstats

**stats?

<!-- -->

: [BuildStats](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildStats.md)

### [**](#status)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L225)status

**status: SUCCEEDED | FAILED | ABORTED | TIMED-OUT

### [**](#usage)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L238)optionalusage

**usage?

<!-- -->

: [BuildUsage](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildUsage.md)

### [**](#usageTotalUsd)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L239)optionalusageTotalUsd

**usageTotalUsd?

<!-- -->

: number

### [**](#usageUsd)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L240)optionalusageUsd

**usageUsd?

<!-- -->

: [BuildUsage](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildUsage.md)

### [**](#userId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L222)userId

**userId: string
