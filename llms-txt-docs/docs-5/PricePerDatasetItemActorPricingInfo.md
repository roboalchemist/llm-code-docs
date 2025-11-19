# Source: https://docs.apify.com/sdk/python/reference/class/PricePerDatasetItemActorPricingInfo.md

# Source: https://docs.apify.com/api/client/js/reference/interface/PricePerDatasetItemActorPricingInfo.md

# PricePerDatasetItemActorPricingInfo<!-- -->

### Hierarchy

* CommonActorPricingInfo
  * *PricePerDatasetItemActorPricingInfo*

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
* [**unitName](#unitName)

## Properties<!-- -->[**](#Properties)

### [**](#apifyMarginPercentage)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L543)inheritedapifyMarginPercentage

**apifyMarginPercentage: number

Inherited from CommonActorPricingInfo.apifyMarginPercentage

In \[0, 1], fraction of pricePerUnitUsd that goes to Apify

### [**](#createdAt)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L545)inheritedcreatedAt

**createdAt: Date

Inherited from CommonActorPricingInfo.createdAt

When this pricing info record has been created

### [**](#notifiedAboutChangeAt)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L549)optionalinheritednotifiedAboutChangeAt

**notifiedAboutChangeAt?

<!-- -->

: Date

Inherited from CommonActorPricingInfo.notifiedAboutChangeAt

### [**](#notifiedAboutFutureChangeAt)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L548)optionalinheritednotifiedAboutFutureChangeAt

**notifiedAboutFutureChangeAt?

<!-- -->

: Date

Inherited from CommonActorPricingInfo.notifiedAboutFutureChangeAt

### [**](#pricePerUnitUsd)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L569)pricePerUnitUsd

**pricePerUnitUsd: number

### [**](#pricingModel)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L566)pricingModel

**pricingModel: PRICE\_PER\_DATASET\_ITEM

### [**](#reasonForChange)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L550)optionalinheritedreasonForChange

**reasonForChange?

<!-- -->

: string

Inherited from CommonActorPricingInfo.reasonForChange

### [**](#startedAt)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L547)inheritedstartedAt

**startedAt: Date

Inherited from CommonActorPricingInfo.startedAt

Since when is this pricing info record effective for a given Actor

### [**](#unitName)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L568)optionalunitName

**unitName?

<!-- -->

: string

Name of the unit that is being charged
