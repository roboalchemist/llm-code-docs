# Source: https://smartcar.com/docs/api-reference/evs/control-charge.md

# Start & Stop Charge

> Start or stop the vehicle charging.

<Note>
  2.0 is still the only supported version for sending remote commands. If you need to send commands, please continue using v2.0 until commands are supported in the latest version later this year.
</Note>

## Permission

`control_charge`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

**Body**

<ParamField body="action" type="string" initialValue="START" required>
  `START` or `STOP` the vehicle charging.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/control-charge.mdx" />
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return “success”.
</ResponseField>

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
      {
          "message": "Successfully sent request to vehicle",
          "status": "success"
      }   
  ```
</ResponseExample>

## Notes

**BMW and MINI**<br />
Vehicle needs to be on OS Version 8+

**Ford and Lincoln**<br />
Issuing a start command while the vehicle has a schedule in place for its current charging location will result in the vehicle charging to 100%.

Please see [charge schedule by location](/api-reference/ford/set-charge-schedule-by-location) for details on setting a charge limit with preferred charging times
or clearing schedules.

**Nissan**<br />
Currently only START charge commands are supported in the US. See [Set Charge Schedule](/api-reference/nissan/set-charge-schedule) for details on setting a charge schedule for Nissan vehicles.

**Chevrolet, GMC, Buick and Cadillac**<br />
These vehicles require a minimum charge of 50% in order to be able to start or stop charging via the API.
