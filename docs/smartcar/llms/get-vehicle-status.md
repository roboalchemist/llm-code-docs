# Source: https://smartcar.com/docs/api-reference/tesla/get-vehicle-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vehicle Status

> Returns the status for the vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_extended_vehicle_info`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/status" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  status = vehicle.request(
        "GET", 
        "{make}/status"
  )
  ```

  ```js Node theme={null}
  const status = await vehicle.request(
        "GET", 
        "{make}/status"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/status")
        .build();
  VehicleResponse status = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  status = vehicle.request(
        "GET", 
        "{make}/status"
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  The current status of the vehicle. If the vehicle is asleep, this request will not wake the vehicle.
</ResponseField>

<ResponseField name="inService" type="bool">
  Indicates if the vehicle is in service mode.
</ResponseField>

<ResponseField name="gear" type="string">
  Indicates the current gear shift position.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
  "status": "ASLEEP",
  "inService": true,
  "gear": "DRIVE"
  }
  ```
</ResponseExample>
