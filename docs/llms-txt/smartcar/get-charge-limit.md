# Source: https://smartcar.com/docs/api-reference/evs/get-charge-limit.md

# Charge Limit

> Returns the charge limit configuration for the vehicle.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_charge`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-charge-limit.mdx" />
</RequestExample>

## Response

<ResponseField name="limit" type="number">
  The level at which the vehicle will stop charging and be considered fully charged as a percentage.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "limit": 0.8,
  }
  ```
</ResponseExample>

## Notes

This endpoint will return a [`CHARGING_PLUG_NOT_CONNECTED`](/errors/api-errors/vehicle-state-errors#charging-plug-not-connected)
error if the OEM is unable to provide a charge limit unless the vehicle is plugged in.

**Ford and Lincoln**<br />
If a vehicle starts charging as a result of a [start charge](/api-reference/evs/control-charge) request, this endpoint will always return `1` if the charging location has a schedule in place.

For the vehicle to respect its charge limit, please set one along with preferred charge times or clear the schedule through through the [charge schedule by location](/api-reference/ford/set-charge-schedule-by-location) endpoint.

**BMW and MINI**<br />
Vehicle needs to be on OS Version 8+
