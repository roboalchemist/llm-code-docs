# Source: https://docs.apify.com/sdk/python/reference/class/Actor.md

# Source: https://docs.apify.com/sdk/js/reference/class/Actor.md

# Source: https://docs.apify.com/api/client/js/reference/interface/Actor.md

# Actor<!-- -->

Represents an Actor in the Apify platform.

Actors are serverless computing units that can perform arbitrary tasks such as web scraping, data processing, automation, and more. Each Actor has versions, builds, and can be executed with different configurations.

## Index[**](#Index)

### Properties

* [**actorPermissionLevel](#actorPermissionLevel)
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

### [**](#actorPermissionLevel)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L493)actorPermissionLevel

**actorPermissionLevel: ACTOR\_PERMISSION\_LEVEL

Permission level of the Actor on Apify platform

### [**](#actorStandby)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L489)optionalactorStandby

**actorStandby?

<!-- -->

: [ActorStandby](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorStandby.md) & { isEnabled: boolean }

Standby mode configuration for keeping Actor warm and responsive

### [**](#categories)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L487)optionalcategories

**categories?

<!-- -->

: string\[]

Categories the Actor belongs to (e.g., 'ECOMMERCE', 'SCRAPING')

### [**](#createdAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L461)createdAt

**createdAt: Date

Timestamp when the Actor was created

### [**](#defaultRunOptions)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L471)defaultRunOptions

**defaultRunOptions: [ActorDefaultRunOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorDefaultRunOptions.md)

Default configuration options for Actor runs

### [**](#deploymentKey)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L477)deploymentKey

**deploymentKey: string

Deployment key used for automated deployments

### [**](#description)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L453)optionaldescription

**description?

<!-- -->

: string

Detailed description of what the Actor does

### [**](#exampleRunInput)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L473)optionalexampleRunInput

**exampleRunInput?

<!-- -->

: [ActorExampleRunInput](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorExampleRunInput.md)

Example input to help users understand how to use the Actor

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L445)id

**id: string

Unique Actor ID

### [**](#isAnonymouslyRunnable)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L459)optionalisAnonymouslyRunnable

**isAnonymouslyRunnable?

<!-- -->

: boolean

Whether the Actor can be run by anonymous users without authentication

### [**](#isDeprecated)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L475)optionalisDeprecated

**isDeprecated?

<!-- -->

: boolean

Whether the Actor is deprecated and should not be used

### [**](#isPublic)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L457)isPublic

**isPublic: boolean

Whether the Actor is publicly available in Apify Store

### [**](#modifiedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L463)modifiedAt

**modifiedAt: Date

Timestamp when the Actor was last modified

### [**](#name)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L449)name

**name: string

Unique name of the Actor (used in API paths, e.g., 'my-actor')

### [**](#pricingInfos)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L469)optionalpricingInfos

**pricingInfos?

<!-- -->

: [ActorRunPricingInfo](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorRunPricingInfo)\[]

Pricing information for pay-per-result or pay-per-event Actors

### [**](#restartOnError)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L455)optionalrestartOnError

**restartOnError?

<!-- -->

: boolean

* **@deprecated**

  Use defaultRunOptions.restartOnError instead

### [**](#seoDescription)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L485)optionalseoDescription

**seoDescription?

<!-- -->

: string

SEO-optimized description for the Actor's public page

### [**](#seoTitle)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L483)optionalseoTitle

**seoTitle?

<!-- -->

: string

SEO-optimized title for the Actor's public page

### [**](#stats)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L465)stats

**stats: [ActorStats](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorStats.md)

Usage and run statistics for the Actor

### [**](#taggedBuilds)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L481)optionaltaggedBuilds

**taggedBuilds?

<!-- -->

: [ActorTaggedBuilds](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorTaggedBuilds)

Mapping of tags to specific builds (e.g., 'latest', 'beta')

### [**](#title)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L479)optionaltitle

**title?

<!-- -->

: string

Human-readable title of the Actor (displayed in UI)

### [**](#userId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L447)userId

**userId: string

ID of the user who owns the Actor

### [**](#username)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L451)username

**username: string

Username of the Actor's owner

### [**](#versions)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L467)versions

**versions: [ActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorVersion)\[]

All versions of this Actor
