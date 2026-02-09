# Source: https://smartcar.com/docs/api-reference/signals/schema.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Smartcar Signals & Attributes Overview

> Smartcar's standard list of vehicle signals and attributes across all compatible OEMs.

Below are the list of signals and attributes supported by Smartcar.

## Attributes

Attributes are static vehicle data that typically does not change in value.

* [Surveillance](/api-reference/signals/surveillance)
* [VehicleIdentification](/api-reference/signals/vehicleidentification)
* [Wheel](/api-reference/signals/wheel)

## Signals

With Smartcar you can configure your application to receive a webhook when the value of any of these signals change. Some change more frequently than others.

Below you will find the signal groups and their respective signals. Each signal has a code that you can use to [request the latest value](/api-reference/get-the-values-for-an-individual-signal) for that signal.

* [Charge](/api-reference/signals/charge)
* [Climate](/api-reference/signals/climate)
* [Closure](/api-reference/signals/closure)
* [ConnectivitySoftware](/api-reference/signals/connectivitysoftware)
* [ConnectivityStatus](/api-reference/signals/connectivitystatus)
* [Diagnostics](/api-reference/signals/diagnostics)
* [HVAC](/api-reference/signals/hvac)
* [InternalCombustionEngine](/api-reference/signals/internalcombustionengine)
* [Location](/api-reference/signals/location)
* [LowVoltageBattery](/api-reference/signals/lowvoltagebattery)
* [Motion](/api-reference/signals/motion)
* [Odometer](/api-reference/signals/odometer)
* [Service](/api-reference/signals/service)
* [Surveillance](/api-reference/signals/surveillance)
* [TractionBattery](/api-reference/signals/tractionbattery)
* [Transmission](/api-reference/signals/transmission)
* [VehicleIdentification](/api-reference/signals/vehicleidentification)
* [VehicleUserAccount](/api-reference/signals/vehicleuseraccount)
* [Wheel](/api-reference/signals/wheel)

***

## Next Steps

Now that you know what vehicle data is available, learn how to receive it in your application:

<CardGroup cols={2}>
  <Card title="Webhooks (Recommended)" icon="webhook" href="/integrations/webhooks/overview">
    Real-time vehicle data pushed to your application
  </Card>

  <Card title="REST API" icon="code" href="/api-reference/vehicles-api-intro">
    Request vehicle data on-demand via HTTP requests
  </Card>

  <Card title="Integration Overview" icon="book" href="/getting-started/integration-overview">
    Compare webhooks vs REST API to choose the right approach
  </Card>

  <Card title="Check Compatibility" icon="car" href="/api-reference/compatibility-api-intro">
    See which vehicles support specific signals
  </Card>
</CardGroup>
