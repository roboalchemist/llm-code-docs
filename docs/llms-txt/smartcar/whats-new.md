# Source: https://smartcar.com/docs/help/oem-integrations/vw/whats-new.md

# Source: https://smartcar.com/docs/help/oem-integrations/volvo/whats-new.md

# Source: https://smartcar.com/docs/help/oem-integrations/tesla/whats-new.md

# Source: https://smartcar.com/docs/help/oem-integrations/mercedes/whats-new.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Important Updates

> Updates regarding the Mercedes-Benz Smartcar Integration.

## December 15th, 2025

Smartcar is excited to announce the availability of the Mercedes-Benz Connectivity Services partner integration. This integration enables developers to connect Mercedes-Benz electric vehicles in Europe and access vehicle data for smart charging, energy management, and mobility applications.

### VIN Verification in Connect Flow

When connecting a Mercedes-Benz vehicle through Smartcar Connect, vehicle owners will be prompted to enter their Vehicle Identification Number (VIN) as part of the authentication process. This additional verification step is a requirement from Mercedes to enroll a vehicle.

<Frame type="simple" caption="Prompt in Smartcar Connect to enter VIN">
  <img src="https://mintcdn.com/smartcar-docs/v9G7Qw0FU2IgW59i/images/help-center/oem-integrations/mercedes/mercedes-vin.png?fit=max&auto=format&n=v9G7Qw0FU2IgW59i&q=85&s=b7378594e095bbbfad98a1768020273d" width="400" data-og-width="750" data-og-height="1624" data-path="images/help-center/oem-integrations/mercedes/mercedes-vin.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/v9G7Qw0FU2IgW59i/images/help-center/oem-integrations/mercedes/mercedes-vin.png?w=280&fit=max&auto=format&n=v9G7Qw0FU2IgW59i&q=85&s=5339ab590eddcf1a9129b7372cebcf46 280w, https://mintcdn.com/smartcar-docs/v9G7Qw0FU2IgW59i/images/help-center/oem-integrations/mercedes/mercedes-vin.png?w=560&fit=max&auto=format&n=v9G7Qw0FU2IgW59i&q=85&s=0b5b1be7fb8b79a80de638a96dd62218 560w, https://mintcdn.com/smartcar-docs/v9G7Qw0FU2IgW59i/images/help-center/oem-integrations/mercedes/mercedes-vin.png?w=840&fit=max&auto=format&n=v9G7Qw0FU2IgW59i&q=85&s=f01e31b332ed489a015cdf060dff0701 840w, https://mintcdn.com/smartcar-docs/v9G7Qw0FU2IgW59i/images/help-center/oem-integrations/mercedes/mercedes-vin.png?w=1100&fit=max&auto=format&n=v9G7Qw0FU2IgW59i&q=85&s=6590751276ac41a89fa2efde1f3a9776 1100w, https://mintcdn.com/smartcar-docs/v9G7Qw0FU2IgW59i/images/help-center/oem-integrations/mercedes/mercedes-vin.png?w=1650&fit=max&auto=format&n=v9G7Qw0FU2IgW59i&q=85&s=a6856fbd7921c031fbc473c7297f1afb 1650w, https://mintcdn.com/smartcar-docs/v9G7Qw0FU2IgW59i/images/help-center/oem-integrations/mercedes/mercedes-vin.png?w=2500&fit=max&auto=format&n=v9G7Qw0FU2IgW59i&q=85&s=fca18dfe920033499727699ad4738693 2500w" />
</Frame>

<Note>
  The VIN can be found in various places such as the Mercedes mobile app, Mercedes web portal, the vehicle's registration documents, insurance papers, or on the vehicle itself (typically on the driver's side dashboard or door jamb).
</Note>

### Supported Vehicle Types

Currently, the Mercedes-Benz integration supports the following powertrain types for **new connections**:

* **BEV (Battery Electric Vehicles)** - Fully electric Mercedes-Benz vehicles
* **PHEV (Plug-in Hybrid Electric Vehicles)** - Mercedes-Benz plug-in hybrid vehicles

### Need Support for Other Vehicle Types?

**Existing Connections**: If you have existing connections to Mercedes-Benz vehicles with other powertrain types (such as traditional internal combustion engine vehicles), these connections will continue to work, but re-authentication is not supported at this time. If your application requires support for Mercedes-Benz vehicles with other powertrain types, please [contact our team](mailto:support@smartcar.com) to discuss your specific requirements. We're continuously working with Mercedes to expand compatibility across different vehicle types and would love to hear about your use case.

### Supported Smartcar Signals:

* [Charge.IsChargingCableConnected](/api-reference/signals/charge#is-charging-cable-connected)
* [Charge.IsCharging](/api-reference/signals/charge#is-charging)
* [Charge.DetailedChargingStatus](/api-reference/signals/charge#detailed-charging-status)
* [Charge.ChargeTimers](/api-reference/signals/charge#charge-timers)
* [Charge.ChargeLimits](/api-reference/signals/charge#charge-limits)
* [Charge.TimeToComplete](/api-reference/signals/charge#time-to-complete)
* [Charge.Wattage](/api-reference/signals/charge#wattage)
* [TractionBattery.StateOfCharge](/api-reference/signals/tractionbattery#state-of-charge)
* [TractionBattery.Range](/api-reference/signals/tractionbattery#range)
* [TractionBattery.NominalCapacity](/api-reference/signals/tractionbattery#nominal-capacities)
* [Location.PreciseLocation](/api-reference/signals/location#location)
* [Odometer.TraveledDistance](/api-reference/signals/odometer#traveled-distance)

### Smartcar Legacy API v2 Endpoints Supported:

* [/odometer](/api-reference/get-odometer)
* [/location](/api-reference/get-location)
* [/battery](/api-reference/evs/get-battery-level)
* [/battery/capacity](/api-reference/get-nominal-capacity)
* [/charge](/api-reference/evs/get-charge-limit)

### Supported Commands:

* [Charge Start](/api-reference/evs/control-charge)
* [Charge Stop](/api-reference/evs/control-charge)

### Notes

This Mercedes-Benz integration is automatically enabled for your application when connecting vehicles out of Europe.

* Supported European markets: Reach customers in Austria, Belgium, Denmark, Finland, France, Germany, Great Britain, Ireland, Italy, Luxembourg, Netherlands, Norway, Poland, Portugal, Spain, Sweden, and Switzerland
* As part of this integration, drivers will be asked to enter their Vehicle Identification Number (VIN) during the new consent authentication flow. We recommend preparing your customer guidance and support content accordingly
* If charge control permissions are requested by the connecting application only EQA, EQB, EQE and EQS vehicles are compatible
* Only EQ models support control charge at this time. For EQE and EQS models, if the state of charge is lower than 20%, stop commands are rejected by Mercedes. For all other EQ models, if the state of charge is below 50%, stopping the charging process is rejected by Mercedes and the car will continue to charge until it reaches at least 50% for vehicle reliability reasons,

For more information about compatible vehicle data and features, see the [compatibility matrix](https://smartcar.com/product/compatible-vehicles).
