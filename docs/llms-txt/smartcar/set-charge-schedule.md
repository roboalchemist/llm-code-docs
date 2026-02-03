# Source: https://smartcar.com/docs/api-reference/tesla/set-charge-schedule.md

# Source: https://smartcar.com/docs/api-reference/nissan/set-charge-schedule.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Charge Schedule

> Sets the charging schedule for a vehicle.

<Note>
  This endpoint is currently available for `nissan` EVs on the `MyNISSAN` platform
</Note>

## Permission

`control_charge`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="chargeSchedules" type="array" required>
  An array of charge schedules. A maximum of 3 schedules can be set.

  <Expandable defaultOpen="true">
    <ParamField body="start" type="string" required>
      HH:mm in UTC for a schedule start time.
    </ParamField>

    <ParamField body="end" type="string" required>
      HH:mm in UTC for a schedule start time.
    </ParamField>

    <ParamField body="days" type="[days]" required>
      An array of days for the schedule to be applied.
      Options: `MONDAY` `TUESDAY` `WEDNESDAY` `THURSDAY` `FRIDAY` `SATURDAY` `SUNDAY`
    </ParamField>
  </Expandable>
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/schedule" \
  -H "Authorization: Bearer {token}" \
  -X "PUT" \
  -H "Content-Type: application/json" \
  -d '{
      "chargeSchedules": [
          {
              "start": "08:00",
              "end": "12:00",
              "days": ["MONDAY", "WEDNESDAY", "FRIDAY"]
          },
          {
              "start": "14:00",
              "end": "18:00",
              "days": ["TUESDAY", "THURSDAY", "SATURDAY"]
          }
      ]
  }'
  ```

  ```python Python theme={null}
  charge_schedule = vehicle.request("PUT", "{make}/charge/schedule", {
      "chargeSchedules": [
          {
              "start": "08:00",
              "end": "12:00",
              "days": ["MONDAY", "WEDNESDAY", "FRIDAY"]
          },
          {
              "start": "14:00",
              "end": "18:00",
              "days": ["TUESDAY", "THURSDAY", "SATURDAY"]
          }
      ]
  })
  ```

  ```js Node theme={null}
  const chargeSchedule = vehicle.request("PUT", "{make}/charge/schedule", {
      "chargeSchedules": [
          {
              "start": "08:00",
              "end": "12:00",
              "days": ["MONDAY", "WEDNESDAY", "FRIDAY"]
          },
          {
              "start": "14:00",
              "end": "18:00",
              "days": ["TUESDAY", "THURSDAY", "SATURDAY"]
          }
      ]
  });
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
      .method("PUT")
      .path("{make}/charge/schedule")
      .addBodyParameter("chargeSchedules", [
          {
              "start": "08:00",
              "end": "12:00",
              "days": ["MONDAY", "WEDNESDAY", "FRIDAY"]
          },
          {
              "start": "14:00",
              "end": "18:00",
              "days": ["TUESDAY", "THURSDAY", "SATURDAY"]
          }
      ])
      .build();
  ChargeSchedule chargeSchedule = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  charge_schedule = vehicle.request("PUT", "{make}/charge/schedule", {
      "chargeSchedules": [
          {
              "start": "08:00",
              "end": "12:00",
              "days": ["MONDAY", "WEDNESDAY", "FRIDAY"]
          },
          {
              "start": "14:00",
              "end": "18:00",
              "days": ["TUESDAY", "THURSDAY", "SATURDAY"]
          }
      ]
  })
  ```
</RequestExample>

## Response

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message.
</ResponseField>

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return `success`.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "message": "Successfully sent request to vehicle",
    "status": "success"
  }
  ```
</ResponseExample>
