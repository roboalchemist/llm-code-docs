# Source: https://smartcar.com/docs/help/oem-integrations/bmw/energy-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# BMW Energy APIs for European Markets

> Access charging data and remote charge control for BMW and MINI EVs in Europe through Smartcar's BMW Energy API integration.

Smartcar's integration with BMW's Energy API gives you access to charging data and remote charge control for BMW and MINI electric vehicles across Europe. This integration is designed for energy providers building smart charging, demand response, and fleet management solutions.

## Capabilities

With this integration, you can:

* **Monitor charging status** — Get visibility into charging state, energy flow, and battery level.
* **Control AC charging** — Remotely start and stop AC charging sessions.
* **Build smart charging solutions** — Support use cases like dynamic load balancing, demand response, off-peak optimization, and charge cost tracking.

## Supported Data

The BMW Energy integration provides charging and battery data through Smartcar's standardized signal schema.

| Data Category       | Available Data                                                                    |
| ------------------- | --------------------------------------------------------------------------------- |
| Charging            | Connector type, cable connection status, charging state, detailed charging status |
| Charging Parameters | Charge timers, charge limits, time to complete, charging wattage                  |
| Battery             | State of charge (SOC), remaining electric range, nominal capacity                 |
| Location            | High-precision GPS position (when vehicle is within Geofence)                     |

### Smartcar Signals

* [`Charge.ChargingConnectorType`](/api-reference/signals/charge#charging-connector-type)
* [`Charge.IsChargingCableConnected`](/api-reference/signals/charge#is-charging-cable-connected)
* [`Charge.IsCharging`](/api-reference/signals/charge#is-charging)
* [`Charge.DetailedChargingStatus`](/api-reference/signals/charge#detailed-charging-status)
* [`Charge.ChargeTimers`](/api-reference/signals/charge#charge-timers)
* [`Charge.ChargeLimits`](/api-reference/signals/charge#charge-limits)
* [`Charge.TimeToComplete`](/api-reference/signals/charge#time-to-complete)
* [`Charge.Wattage`](/api-reference/signals/charge#wattage)
* [`TractionBattery.StateOfCharge`](/api-reference/signals/tractionbattery#state-of-charge)
* [`TractionBattery.Range`](/api-reference/signals/tractionbattery#range)
* [`TractionBattery.NominalCapacity`](/api-reference/signals/tractionbattery#nominal-capacities)
* [`Location.PreciseLocation`](/api-reference/signals/location#location)

### Commands

* [Start Charge](/api-reference/evs/control-charge)
* [Stop Charge](/api-reference/evs/control-charge)

## Coverage

### Supported Vehicles

This integration supports all Battery Electric Vehicles (BEV) and Plug-in Hybrid Electric Vehicles (PHEV) from BMW and MINI.

### Supported Markets

The integration is available in 17 European markets: Austria, Belgium, Denmark, Finland, France, Germany, Great Britain, Ireland, Italy, Luxembourg, Netherlands, Norway, Poland, Portugal, Spain, Sweden, and Switzerland.

## Geofence restriction

<Warning>
  Data and commands are only available when the vehicle is within approximately 200 meters of the consented address. Data streaming from BMW to Smartcar and from Smartcar to your app automatically stops when the vehicle exits the Geofence.
</Warning>

When vehicle owners grant consent, they specify a single address where managed charging will occur. This Geofence defines where data streaming and charge commands are available. This design ensures data privacy and compliance with BMW's requirements.

## Consent Flow

Vehicle owners grant consent through the BMW Connected Drive Portal as part of the Smartcar Connect flow. During this process, they:

1. Log in with their BMW ID
2. Select the vehicle(s) to connect
3. Specify the address where managed charging will occur
4. Accept BMW's terms for data sharing

## Limitations

<Info>
  Keep these constraints in mind when building your integration.
</Info>

* **Charging-only scope** — This integration focuses on charging and battery data. Broader vehicle data (odometer, tire pressure, etc.) is not available through the Energy API.
* **Geofence-restricted** — Data and commands only work within the \~200m Geofence radius.
* **AC charging only** — Remote charge control is limited to AC charging sessions.
* **No public charging data** — Data from public charging sessions is not supported.
* **No cross-border data** — Cross-border data streaming is not currently supported.
* **Charge stop rate limit** — BMW enforces a rolling 30-day limit of 80 charge stop commands per vehicle.

If you have any questions about these limitations or need additional capabilities, please our support team. We're continuously working with BMW to expand the integration's features and coverage.
