# Source: https://smartcar.com/docs/api-reference/tesla/get-charge-completion-time.md

# Source: https://smartcar.com/docs/api-reference/gm/get-charge-completion-time.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Charge Completion Time

> When the vehicle is charging, returns the date and time the vehicle expects to "complete" this charging session.  When the vehicle is not charging, this endpoint results in a vehicle state error.

<Note>
  This endpoint is currently available for `cadillac` and `chevrolet`.
</Note>

## Permission

`read_charge`

## Request

<ParamField path="id" type="string" required>
  `vehicle_id` of the vehicle you are making the request to.
</ParamField>

<ParamField path="make" type="string" required>
  The make to pass in the URL.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/bse/get-charge-completion-time.mdx" />
</RequestExample>

## Response

<ResponseField name="time" type="string">
  An ISO8601 formatted datetime (`YYYY-MM-DDTHH:mm:ss.SSSZ`) for the time at which the vehicle expects to complete this charging session.
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "time": "2022-01-13T22:52:55.358Z"
  }
  ```
</ResponseExample>
