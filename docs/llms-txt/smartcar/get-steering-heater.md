# Source: https://smartcar.com/docs/api-reference/tesla/get-steering-heater.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Steering Heater

> Returns the current state of a vehicle's steering wheel heater system.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_climate`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/steering_wheel" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  steering_wheel = vehicle.request(
        "GET", 
        "{make}/climate/steering_wheel"
  )
  ```

  ```js Node theme={null}
  const steeringWheel = await vehicle.request(
        "GET", 
        "{make}/climate/steering_wheel"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/climate/steering_wheel")
        .build();
  VehicleResponse steeringWheel = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  steering_wheel = vehicle.request(
        "GET", 
        "{make}/climate/steering_wheel"
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="enum">
  The current state of the steering wheel heater system. `UNAVAILABLE` indicates the vehicle is not equipped with a steering wheel heater.
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "status": "ON",
  }
  ```
</ResponseExample>
