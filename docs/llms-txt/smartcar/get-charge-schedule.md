# Source: https://smartcar.com/docs/api-reference/tesla/get-charge-schedule.md

# Source: https://smartcar.com/docs/api-reference/nissan/get-charge-schedule.md

# Source: https://smartcar.com/docs/api-reference/tesla/get-charge-schedule.md

# Source: https://smartcar.com/docs/api-reference/nissan/get-charge-schedule.md

# Source: https://smartcar.com/docs/api-reference/tesla/get-charge-schedule.md

# Source: https://smartcar.com/docs/api-reference/nissan/get-charge-schedule.md

# Source: https://smartcar.com/docs/api-reference/tesla/get-charge-schedule.md

# Source: https://smartcar.com/docs/api-reference/nissan/get-charge-schedule.md

# Charge Schedule

> Returns the charging schedule of a vehicle. The response contains the start time and departure time of the vehicle's charging schedule.

<Note>
  This endpoint is currently available for `nissan` EVs on the `MyNISSAN` platform.
</Note>

## Permission

`read_charge`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  <Snippet file="api-reference/bse/get-charge-schedule.mdx" />
</RequestExample>

## Response

<ResponseField name="chargeSchedules" type="array">
  An array of charge schedules. Maximum of 3 schedules, empty if no schedules are set.

  <Expandable>
    <ResponseField name="start" type="array">
      HH:mm in UTC for a schedule start time.
    </ResponseField>

    <ResponseField name="end" type="array">
      HH:mm in UTC for a schedule end time.
    </ResponseField>

    <ResponseField name="days" type="array">
      An array of days the schedule applies to.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "chargeSchedules": [
      {
        "end": "2020-01-01T02:00:00.000Z",
        "start": "2020-01-01T01:00:00.000Z",
        "days": [
          "MONDAY",
          "WEDNESDAY",
          "FRIDAY"
        ]
      }
    ]
  }
  ```
</ResponseExample>
