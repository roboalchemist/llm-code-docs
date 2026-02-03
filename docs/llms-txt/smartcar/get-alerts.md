# Source: https://smartcar.com/docs/api-reference/tesla/get-alerts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Alerts

> Returns recent alerts from the vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_alerts`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/alerts" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  alerts = vehicle.request(
        "GET", 
        "{make}/alerts"
  )
  ```

  ```js Node theme={null}
  const alerts = await vehicle.request(
        "GET", 
        "{make}/alerts"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/alerts")
        .build();
  VehicleResponse alerts =vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  alerts = vehicle.request(
        "GET", 
        "{make}/alerts"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

## Response

<ResponseField name="alerts" type="[alert] | null">
  <Expandable title="alert">
    <ResponseField name="name" type="string | null">
      The name of the alert.
    </ResponseField>

    <ResponseField name="dateTime" type="timestamp | null">
      Date and time of the alert.
    </ResponseField>

    <ResponseField name="audience" type="[string] | null">
      Indicates recipients of the alert.
    </ResponseField>

    <ResponseField name="userText" type="[string] | null">
      Additional context related to the alert.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "alerts" : [
            {
                  "name": "Name_Of_The_Alert",
                  "dateTime": "2022-07-10T16:20:00.000Z",
                  "audience": [
                        "service-fix",
                        "customer"
                  ],
                  "userText": "additional description text"
            }
      ]
  }
  ```
</ResponseExample>
