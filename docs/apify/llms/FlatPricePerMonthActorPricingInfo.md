# Source: https://docs.apify.com/sdk/python/reference/class/FlatPricePerMonthActorPricingInfo.md

# Source: https://docs.apify.com/api/client/js/reference/interface/FlatPricePerMonthActorPricingInfo.md

# FlatPricePerMonthActorPricingInfo<!-- -->

Pricing information for Actors with a flat monthly subscription fee.

### Hierarchy

* CommonActorPricingInfo
  * *FlatPricePerMonthActorPricingInfo*

## Index[**](#Index)

### Properties

* [**apifyMarginPercentage](#apifyMarginPercentage)
* [**createdAt](#createdAt)
* [**notifiedAboutChangeAt](#notifiedAboutChangeAt)
* [**notifiedAboutFutureChangeAt](#notifiedAboutFutureChangeAt)
* [**pricePerUnitUsd](#pricePerUnitUsd)
* [**pricingModel](#pricingModel)
* [**reasonForChange](#reasonForChange)
* [**startedAt](#startedAt)
* [**trialMinutes](#trialMinutes)

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

### [**](#pricePerUnitUsd)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L871)pricePerUnitUsd

**pricePerUnitUsd: number

Monthly flat price in USD

### [**](#pricingModel)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L867)pricingModel

**pricingModel: FLAT\_PRICE\_PER\_MONTH

### [**](#reasonForChange)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L853)optionalinheritedreasonForChange

**reasonForChange?

<!-- -->

: string

Inherited from CommonActorPricingInfo.reasonForChange

### [**](#startedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L850)inheritedstartedAt

**startedAt: Date

Inherited from CommonActorPricingInfo.startedAt

Since when is this pricing info record effective for a given Actor

### [**](#trialMinutes)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L869)optionaltrialMinutes

**trialMinutes?

<!-- -->

: number

For how long this Actor can be used for free in trial period
