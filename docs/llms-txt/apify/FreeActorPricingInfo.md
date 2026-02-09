# Source: https://docs.apify.com/sdk/python/reference/class/FreeActorPricingInfo.md

# Source: https://docs.apify.com/api/client/js/reference/interface/FreeActorPricingInfo.md

# FreeActorPricingInfo<!-- -->

Pricing information for free Actors.

### Hierarchy

* CommonActorPricingInfo
  * *FreeActorPricingInfo*

## Index[**](#Index)

### Properties

* [**apifyMarginPercentage](#apifyMarginPercentage)
* [**createdAt](#createdAt)
* [**notifiedAboutChangeAt](#notifiedAboutChangeAt)
* [**notifiedAboutFutureChangeAt](#notifiedAboutFutureChangeAt)
* [**pricingModel](#pricingModel)
* [**reasonForChange](#reasonForChange)
* [**startedAt](#startedAt)

## Properties<!-- -->[**](#Properties)

### [**](#apifyMarginPercentage)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L846)inheritedapifyMarginPercentage

**apifyMarginPercentage: number

Inherited from CommonActorPricingInfo.apifyMarginPercentage

In \[0, 1], fraction of pricePerUnitUsd that goes to Apify

### [**](#createdAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L848)inheritedcreatedAt

**createdAt: Date

Inherited from CommonActorPricingInfo.createdAt

When this pricing info record has been created

### [**](#notifiedAboutChangeAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L852)optionalinheritednotifiedAboutChangeAt

**notifiedAboutChangeAt?

<!-- -->

: Date

Inherited from CommonActorPricingInfo.notifiedAboutChangeAt

### [**](#notifiedAboutFutureChangeAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L851)optionalinheritednotifiedAboutFutureChangeAt

**notifiedAboutFutureChangeAt?

<!-- -->

: Date

Inherited from CommonActorPricingInfo.notifiedAboutFutureChangeAt

### [**](#pricingModel)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L860)pricingModel

**pricingModel: FREE

### [**](#reasonForChange)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L853)optionalinheritedreasonForChange

**reasonForChange?

<!-- -->

: string

Inherited from CommonActorPricingInfo.reasonForChange

### [**](#startedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L850)inheritedstartedAt

**startedAt: Date

Inherited from CommonActorPricingInfo.startedAt

Since when is this pricing info record effective for a given Actor
