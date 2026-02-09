# Source: https://smartcar.com/docs/api-reference/tesla/get-speedometer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Speed

> Returns the current speed of the vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_speedometer`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/speedometer" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  speed = vehicle.request(
        "GET", 
        "{make}/speedometer"
  )
  ```

  ```js Node theme={null}
  const speed = await vehicle.request(
        "GET", 
        "{make}/speedometer"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/speedometer")
        .build();
  VehicleResponse speed = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  speed = vehicle.request(
        "GET", 
        "{make}/speedometer"
  )
  ```
</RequestExample>

## Response

<ResponseField name="speed" default="km/h" type="number">
  The current speed of the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "speed": 84.32
  }
  ```
</ResponseExample>
