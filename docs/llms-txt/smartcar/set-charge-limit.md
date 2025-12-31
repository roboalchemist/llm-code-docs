# Source: https://smartcar.com/docs/api-reference/evs/set-charge-limit.md

# Charge Limit

> Set the  charge limit of an electric vehicle.

<Note>
  2.0 is still the only supported version for sending remote commands. If you need to send commands, please continue using v2.0 until commands are supported in the latest version later this year.
</Note>

## Permission

`control_charge`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

**Body**

<ParamField body="limit" type="number" initialValue="0.7" required>
  The level at which the vehicle should stop charging and be considered fully charged.
  Cannot be less than `0.5`, or greater than `1`.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/set-charge-limit.mdx" />
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return “success” (HTTP 200 status).
</ResponseField>

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message (HTTP 200 status).
</ResponseField>

## Notes

This endpoint will return a [`CHARGING_PLUG_NOT_CONNECTED`](/errors/api-errors/vehicle-state-errors#charging-plug-not-connected) error if
the OEM is unable to set a charge limit while the vehicle is unpluged.

**Ford and Lincoln**<br />
If a vehicle starts charging as a result of a [start charge](/api-reference/evs/control-charge) request it will always charge to 100%
if the charging location has a schedule in place.

For the vehicle to respect its charge limit, please set one along with preferred charge
times or clear the schedule through the [charge schedule by location](/api-reference/ford/set-charge-schedule-by-location) endpoint.

**BMW and MINI**<br />
Vehicle needs to be on OS Version 8+

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "message": "Successfully sent request to vehicle",
      "status": "success"
  }   
  ```
</ResponseExample>
