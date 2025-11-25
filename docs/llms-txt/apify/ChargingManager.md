# Source: https://docs.apify.com/sdk/python/reference/class/ChargingManager.md

# Source: https://docs.apify.com/sdk/js/reference/class/ChargingManager.md

# Source: https://docs.apify.com/sdk/python/reference/class/ChargingManager.md

# Source: https://docs.apify.com/sdk/js/reference/class/ChargingManager.md

# ChargingManager<!-- -->

Handles pay-per-event charging.

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**calculateMaxEventChargeCountWithinLimit](#calculateMaxEventChargeCountWithinLimit)
* [**getChargedEventCount](#getChargedEventCount)
* [**getMaxTotalChargeUsd](#getMaxTotalChargeUsd)
* [**getPricingInfo](#getPricingInfo)
* [**charge](#charge)
* [**init](#init)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/charging.ts#L28)constructor

* ****new ChargingManager**(configuration, apifyClient): [ChargingManager](https://docs.apify.com/sdk/js/sdk/js/reference/class/ChargingManager.md)

- #### Parameters

  * ##### configuration: [Configuration](https://docs.apify.com/sdk/js/sdk/js/reference/class/Configuration.md)
  * ##### apifyClient: [ApifyClient](https://docs.apify.com/sdk/js/sdk/js/reference/class/ApifyClient.md)

  #### Returns [ChargingManager](https://docs.apify.com/sdk/js/sdk/js/reference/class/ChargingManager.md)

## Methods<!-- -->[**](#Methods)

### [**](#calculateMaxEventChargeCountWithinLimit)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/charging.ts#L264)calculateMaxEventChargeCountWithinLimit

* ****calculateMaxEventChargeCountWithinLimit**(eventName): number

- How many events of a given type can still be charged for before reaching the limit; If the event is not registered, returns Infinity (free of charge)

  ***

  #### Parameters

  * ##### eventName: string

  #### Returns number

### [**](#getChargedEventCount)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/charging.ts#L230)getChargedEventCount

* ****getChargedEventCount**(eventName): number

- Get the number of events with given name that the Actor has charged for so far.

  ***

  #### Parameters

  * ##### eventName: string

  #### Returns number

### [**](#getMaxTotalChargeUsd)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/charging.ts#L241)getMaxTotalChargeUsd

* ****getMaxTotalChargeUsd**(): number

- Get the maximum amount of money that the Actor is allowed to charge.

  ***

  #### Returns number

### [**](#getPricingInfo)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/charging.ts#L129)getPricingInfo

* ****getPricingInfo**(): [ActorPricingInfo](https://docs.apify.com/sdk/js/sdk/js/reference/interface/ActorPricingInfo.md)

- Get information about the pricing for this Actor.

  ***

  #### Returns [ActorPricingInfo](https://docs.apify.com/sdk/js/sdk/js/reference/interface/ActorPricingInfo.md)

### [**](#charge)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/charging.ts#L149)charge

* ****charge**(options): Promise<[ChargeResult](https://docs.apify.com/sdk/js/sdk/js/reference/interface/ChargeResult.md)>

- Charge for a specified number of events - sub-operations of the Actor.

  ***

  #### Parameters

  * ##### options: [ChargeOptions](https://docs.apify.com/sdk/js/sdk/js/reference/interface/ChargeOptions.md)

    The name of the event to charge for and the number of events to be charged.

  #### Returns Promise<[ChargeResult](https://docs.apify.com/sdk/js/sdk/js/reference/interface/ChargeResult.md)>

### [**](#init)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/charging.ts#L57)init

* ****init**(): Promise\<void>

- Initialize the ChargingManager by loading pricing information and charging state via Apify API.

  ***

  #### Returns Promise\<void>
