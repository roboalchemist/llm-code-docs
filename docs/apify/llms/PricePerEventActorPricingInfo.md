# Source: https://docs.apify.com/api/client/js/reference/interface/PricePerEventActorPricingInfo.md

# PricePerEventActorPricingInfo<!-- -->

Pricing information for pay-per-event Actors.

These Actors charge based on specific events (e.g., emails sent, API calls made).

### Hierarchy

* CommonActorPricingInfo
  * *PricePerEventActorPricingInfo*

## Index[**](#Index)

### Properties

* [**apifyMarginPercentage](#apifyMarginPercentage)
* [**createdAt](#createdAt)
* [**minimalMaxTotalChargeUsd](#minimalMaxTotalChargeUsd)
* [**notifiedAboutChangeAt](#notifiedAboutChangeAt)
* [**notifiedAboutFutureChangeAt](#notifiedAboutFutureChangeAt)
* [**pricingModel](#pricingModel)
* [**pricingPerEvent](#pricingPerEvent)
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

### [**](#minimalMaxTotalChargeUsd)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L910)optionalminimalMaxTotalChargeUsd

**minimalMaxTotalChargeUsd?

<!-- -->

: number

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

### [**](#pricingModel)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L906)pricingModel

**pricingModel: PAY\_PER\_EVENT

### [**](#pricingPerEvent)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L907)pricingPerEvent

**pricingPerEvent: { actorChargeEvents: [ActorChargeEvents](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorChargeEvents) }

#### Type declaration

* ##### actorChargeEvents: [ActorChargeEvents](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorChargeEvents)

### [**](#reasonForChange)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L853)optionalinheritedreasonForChange

**reasonForChange?

<!-- -->

: string

Inherited from CommonActorPricingInfo.reasonForChange

### [**](#startedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L850)inheritedstartedAt

**startedAt: Date

Inherited from CommonActorPricingInfo.startedAt

Since when is this pricing info record effective for a given Actor
