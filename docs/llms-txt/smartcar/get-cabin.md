# Source: https://smartcar.com/docs/api-reference/tesla/get-cabin.md

# Cabin Climate

> Returns the current state and target temperature setting of a vehicle's cabin climate system.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_climate`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/cabin" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  cabin = vehicle.request(
        "GET", 
        "{make}/climate/cabin"
  )
  ```

  ```js Node theme={null}
  const chargeCompletion = await vehicle.request(
        "GET", 
        "{make}/climate/cabin"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/climate/cabin")
        .build();
  VehicleResponse chargeCompletion = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  chargeCompletion = vehicle.request(
        "GET", 
        "{make}/climate/cabin"
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  The current state of the climate cabin system.
</ResponseField>

<ResponseField name="temperature" type="number">
  The target temperature setting of the vehicle when the climate system is on (in Celsius by default or in Fahrenheit using the sc-unit-system).
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "status": "ON",
    "temperature": 20
  }
  ```
</ResponseExample>
