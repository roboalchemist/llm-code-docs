# Source: https://docs.apify.com/sdk/python/reference/class/Actor.md

# Source: https://docs.apify.com/sdk/js/reference/class/Actor.md

# Source: https://docs.apify.com/api/client/js/reference/interface/Actor.md

# Source: https://docs.apify.com/sdk/python/reference/class/Actor.md

# Source: https://docs.apify.com/sdk/js/reference/class/Actor.md

# Source: https://docs.apify.com/api/client/js/reference/interface/Actor.md

# Actor<!-- -->

## Index[**](#Index)

### Properties

* [**actorStandby](#actorStandby)
* [**categories](#categories)
* [**createdAt](#createdAt)
* [**defaultRunOptions](#defaultRunOptions)
* [**deploymentKey](#deploymentKey)
* [**description](#description)
* [**exampleRunInput](#exampleRunInput)
* [**id](#id)
* [**isAnonymouslyRunnable](#isAnonymouslyRunnable)
* [**isDeprecated](#isDeprecated)
* [**isPublic](#isPublic)
* [**modifiedAt](#modifiedAt)
* [**name](#name)
* [**pricingInfos](#pricingInfos)
* [**restartOnError](#restartOnError)
* [**seoDescription](#seoDescription)
* [**seoTitle](#seoTitle)
* [**stats](#stats)
* [**taggedBuilds](#taggedBuilds)
* [**title](#title)
* [**userId](#userId)
* [**username](#username)
* [**versions](#versions)

## Properties<!-- -->[**](#Properties)

### [**](#actorStandby)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L301)optionalactorStandby

**actorStandby?

<!-- -->

: [ActorStandby](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorStandby.md) & { isEnabled: boolean }

### [**](#categories)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L300)optionalcategories

**categories?

<!-- -->

: string\[]

### [**](#createdAt)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L287)createdAt

**createdAt: Date

### [**](#defaultRunOptions)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L292)defaultRunOptions

**defaultRunOptions: [ActorDefaultRunOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorDefaultRunOptions.md)

### [**](#deploymentKey)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L295)deploymentKey

**deploymentKey: string

### [**](#description)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L282)optionaldescription

**description?

<!-- -->

: string

### [**](#exampleRunInput)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L293)optionalexampleRunInput

**exampleRunInput?

<!-- -->

: [ActorExampleRunInput](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorExampleRunInput.md)

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L278)id

**id: string

### [**](#isAnonymouslyRunnable)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L286)optionalisAnonymouslyRunnable

**isAnonymouslyRunnable?

<!-- -->

: boolean

### [**](#isDeprecated)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L294)optionalisDeprecated

**isDeprecated?

<!-- -->

: boolean

### [**](#isPublic)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L285)isPublic

**isPublic: boolean

### [**](#modifiedAt)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L288)modifiedAt

**modifiedAt: Date

### [**](#name)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L280)name

**name: string

### [**](#pricingInfos)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L291)optionalpricingInfos

**pricingInfos?

<!-- -->

: [ActorRunPricingInfo](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorRunPricingInfo)\[]

### [**](#restartOnError)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L284)optionalrestartOnError

**restartOnError?

<!-- -->

: boolean

* **@deprecated**

  Use defaultRunOptions.restartOnError instead

### [**](#seoDescription)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L299)optionalseoDescription

**seoDescription?

<!-- -->

: string

### [**](#seoTitle)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L298)optionalseoTitle

**seoTitle?

<!-- -->

: string

### [**](#stats)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L289)stats

**stats: [ActorStats](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorStats.md)

### [**](#taggedBuilds)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L297)optionaltaggedBuilds

**taggedBuilds?

<!-- -->

: [ActorTaggedBuilds](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorTaggedBuilds)

### [**](#title)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L296)optionaltitle

**title?

<!-- -->

: string

### [**](#userId)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L279)userId

**userId: string

### [**](#username)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L281)username

**username: string

### [**](#versions)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L290)versions

**versions: [ActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorVersion)\[]
