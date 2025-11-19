# Source: https://docs.apify.com/api/client/js/reference/interface/Build.md

# Build<!-- -->

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

### [**](#actId)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L124)actId

**actId: string

### [**](#actorDefinition)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L144)optionalactorDefinition

**actorDefinition?

<!-- -->

: [ActorDefinition](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorDefinition.md)

### [**](#buildNumber)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L140)buildNumber

**buildNumber: string

### [**](#finishedAt)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L127)optionalfinishedAt

**finishedAt?

<!-- -->

: Date

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L123)id

**id: string

### [**](#inputSchema)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L135)optionalinputSchema

**inputSchema?

<!-- -->

: string

* **@deprecated**

  This property is deprecated in favor of `actorDefinition.input`.

### [**](#meta)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L129)meta

**meta: [BuildMeta](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildMeta.md)

### [**](#options)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L131)optionaloptions

**options?

<!-- -->

: [BuildOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildOptions.md)

### [**](#readme)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L139)optionalreadme

**readme?

<!-- -->

: string

* **@deprecated**

  This property is deprecated in favor of `actorDefinition.readme`.

### [**](#startedAt)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L126)startedAt

**startedAt: Date

### [**](#stats)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L130)optionalstats

**stats?

<!-- -->

: [BuildStats](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildStats.md)

### [**](#status)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L128)status

**status: SUCCEEDED | FAILED | ABORTED | TIMED-OUT

### [**](#usage)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L141)optionalusage

**usage?

<!-- -->

: [BuildUsage](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildUsage.md)

### [**](#usageTotalUsd)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L142)optionalusageTotalUsd

**usageTotalUsd?

<!-- -->

: number

### [**](#usageUsd)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L143)optionalusageUsd

**usageUsd?

<!-- -->

: [BuildUsage](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildUsage.md)

### [**](#userId)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L125)userId

**userId: string
