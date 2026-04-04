# Source: https://smartcar.com/docs/api-reference/signals/location.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Location Signals

### IsAtHome

Signal code: `location-isathome`

A boolean indicating if the vehicle is at home. Vehicle owners can set their home location in their OEM application.

<ParamField path="value" type="boolean" required={false}>
  Boolean indicating if the vehicle is at the configured home location
</ParamField>

```json Example theme={null}
{
  "value": true
}
```

### Location

Signal code: `location-preciselocation`

An object containing information about a vehicle's precise location.

<ParamField path="heading" type="number" required={false}>
  The precise angular heading of the vehicle.
</ParamField>

<ParamField path="latitude" type="number" required={false}>
  The vehicle's current geographic latitude coordinate.
</ParamField>

<ParamField path="direction" type="string" required={false}>
  A cardinal or intercardinal direction representing the vehicle's current heading or orientation.

  **Possible values:** `N`, `NE`, `E`, `SE`, `S`, `SW`, `W`, `NW`
</ParamField>

<ParamField path="longitude" type="number" required={false}>
  The vehicle's current geographic longitude coordinate.
</ParamField>

<ParamField path="locationType" type="string" required={false}>
  Indicates whether the location-related fields are expected to update in real time or when the vehicle is parked.

  **Possible values:** `LAST_PARKED`, `CURRENT`
</ParamField>

```json Example theme={null}
{
  "heading": 45.5,
  "latitude": 37.7749,
  "longitude": -122.4194,
  "direction": "NE",
  "locationType": "CURRENT"
}
```
