# Source: https://smartcar.com/docs/api-reference/get-service-records.md

# Service History

> Retrieve service records tracked by the vehicle's dealer or manually added by the vehicle owner. Currently supporting Ford, Lincoln, Toyota, Lexus, Mazda and Volkswagen (US)

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_service_history`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/service/history" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  service = vehicle.request(
        "GET", 
        "service/history"
  )
  ```

  ```js Node theme={null}
  const service = await vehicle.request(
        "GET", 
        "service/history"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("service/history")
        .build();
  VehicleResponse service =vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  Service = vehicle.request(
        "GET", 
        "service/history"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

## Response

<ResponseField name="serviceID" type="string | null">
  A unique identifier of the service record.
</ResponseField>

<ResponseField name="serviceDate" type="timestamp | null">
  The date and time the vehicle was serviced
</ResponseField>

<ResponseField name="odometerDistance" type="string | null">
  The odometer of the vehicle at time of service in kilometers.
</ResponseField>

<Expandable title="serviceTasks" description="An overview of specific tasks completed in the service event.">
  <ResponseField name="taskID" type="string | null">
    The unique identifier of the tasks completed as part of the service event.
  </ResponseField>

  <ResponseField name="taskDescription" type="string | null">
    Tasks completed as part of the service event. Note that not all makes provide service tasks.
  </ResponseField>
</Expandable>

Additional service details.

<Expandable title="service details">
  <ResponseField name="type" type="string | null">
    Indicates if the service event was completed by a dealership or manually entered by the vehicle owner.
  </ResponseField>
</Expandable>

An overview of service costs.

<Expandable title="service cost">
  <ResponseField name="totalCost" type="string | null">
    The total cost of the service event. Note that not all makes provide service cost.
  </ResponseField>

  <ResponseField name="currency" type="string | null">
    Identifies the currency used for service cost.
  </ResponseField>
</Expandable>

<ResponseExample>
  ```json Example Response  theme={null}
  {
        "serviceId": null,
        "odometerDistance": 46047.22,
        "serviceDate": "2023-06-28T22:21:41.583Z",
        "serviceTasks": [
              {
              "taskId": "3262",
              "taskDescription": "Service Task 0"
              },
              {
              "taskId": "3041",
              "taskDescription": null
              },
              {
              "taskId": null,
              "taskDescription": null
              }
        ],
        "serviceDetails": [
              {
              "type": "Service Details Type 0",
              "value": "Service Details Value 0"
              },
              {
              "type": "Service Details Type 1",
              "value": null
              }
        ],
        "serviceCost": {
              "totalCost": null,
              "currency": null
        }
  }
  ```
</ResponseExample>
