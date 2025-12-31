# Source: https://docs.apify.com/sdk/python/reference/class/ChargingManagerImplementation.md

# ChargingManagerImplementation<!-- -->

Implementation of the `ChargingManager` Protocol - this is only meant to be instantiated internally.

### Hierarchy

* [ChargingManager](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManager.md)
  * *ChargingManagerImplementation*

## Index[**](#Index)

### Methods

* [**\_\_aenter\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManagerImplementation.md#__aenter__)
* [**\_\_aexit\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManagerImplementation.md#__aexit__)
* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManagerImplementation.md#__init__)
* [**calculate\_max\_event\_charge\_count\_within\_limit](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManagerImplementation.md#calculate_max_event_charge_count_within_limit)
* [**calculate\_total\_charged\_amount](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManagerImplementation.md#calculate_total_charged_amount)
* [**charge](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManagerImplementation.md#charge)
* [**get\_charged\_event\_count](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManagerImplementation.md#get_charged_event_count)
* [**get\_max\_total\_charge\_usd](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManagerImplementation.md#get_max_total_charge_usd)
* [**get\_pricing\_info](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManagerImplementation.md#get_pricing_info)

### Properties

* [**LOCAL\_CHARGING\_LOG\_DATASET\_NAME](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManagerImplementation.md#LOCAL_CHARGING_LOG_DATASET_NAME)

## Methods<!-- -->[**](#Methods)

### [**](#__aenter__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/_charging.py#L140)\_\_aenter\_\_

* **async **\_\_aenter\_\_**(): None

- Initialize the charging manager - this is called by the `Actor` class and shouldn't be invoked manually.

  ***

  #### Returns None

### [**](#__aexit__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/_charging.py#L192)\_\_aexit\_\_

* **async **\_\_aexit\_\_**(exc\_type, exc\_value, exc\_traceback): None

- #### Parameters

  * ##### exc\_type: type\[BaseException] | None
  * ##### exc\_value: BaseException | None
  * ##### exc\_traceback: TracebackType | None

  #### Returns None

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/_charging.py#L123)\_\_init\_\_

* ****\_\_init\_\_**(configuration, client): None

- #### Parameters

  * ##### configuration: [Configuration](https://docs.apify.com/sdk/python/sdk/python/reference/class/Configuration.md)
  * ##### client: ApifyClientAsync

  #### Returns None

### [**](#calculate_max_event_charge_count_within_limit)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/_charging.py#L302)calculate\_max\_event\_charge\_count\_within\_limit

* ****calculate\_max\_event\_charge\_count\_within\_limit**(event\_name): int | None

- Overrides [ChargingManager.calculate\_max\_event\_charge\_count\_within\_limit](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManager.md#calculate_max_event_charge_count_within_limit)

  Calculate how many instances of an event can be charged before we reach the configured limit.

  ***

  #### Parameters

  * ##### event\_name: str

    Name of the inspected event.

  #### Returns int | None

### [**](#calculate_total_charged_amount)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/_charging.py#L295)calculate\_total\_charged\_amount

* ****calculate\_total\_charged\_amount**(): Decimal

- Overrides [ChargingManager.calculate\_total\_charged\_amount](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManager.md#calculate_total_charged_amount)

  Calculate the total amount of money charged for pay-per-event events so far.

  ***

  #### Returns Decimal

### [**](#charge)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/_charging.py#L204)charge

* **async **charge**(event\_name, count): [ChargeResult](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargeResult.md)

- Overrides [ChargingManager.charge](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManager.md#charge)

  Charge for a specified number of events - sub-operations of the Actor.

  This is relevant only for the pay-per-event pricing model.

  ***

  #### Parameters

  * ##### event\_name: str

    Name of the event to be charged for.

  * ##### optionalcount: int = <!-- -->1

    Number of events to charge for.

  #### Returns [ChargeResult](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargeResult.md)

### [**](#get_charged_event_count)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/_charging.py#L332)get\_charged\_event\_count

* ****get\_charged\_event\_count**(event\_name): int

- Overrides [ChargingManager.get\_charged\_event\_count](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManager.md#get_charged_event_count)

  Get the number of events with the given name that were charged so far.

  ***

  #### Parameters

  * ##### event\_name: str

    Name of the inspected event.

  #### Returns int

### [**](#get_max_total_charge_usd)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/_charging.py#L337)get\_max\_total\_charge\_usd

* ****get\_max\_total\_charge\_usd**(): Decimal

- Overrides [ChargingManager.get\_max\_total\_charge\_usd](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManager.md#get_max_total_charge_usd)

  Get the configured maximum total charge for this Actor run.

  ***

  #### Returns Decimal

### [**](#get_pricing_info)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/_charging.py#L319)get\_pricing\_info

* ****get\_pricing\_info**(): [ActorPricingInfo](https://docs.apify.com/sdk/python/sdk/python/reference/class/ActorPricingInfo.md)

- Overrides [ChargingManager.get\_pricing\_info](https://docs.apify.com/sdk/python/sdk/python/reference/class/ChargingManager.md#get_pricing_info)

  Retrieve detailed information about the effective pricing of the current Actor run.

  This can be used for instance when your code needs to support multiple pricing models in transition periods.

  ***

  #### Returns [ActorPricingInfo](https://docs.apify.com/sdk/python/sdk/python/reference/class/ActorPricingInfo.md)

## Properties<!-- -->[**](#Properties)

### [**](#LOCAL_CHARGING_LOG_DATASET_NAME)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/_charging.py#L121)LOCAL\_CHARGING\_LOG\_DATASET\_NAME

**LOCAL\_CHARGING\_LOG\_DATASET\_NAME: Undefined
