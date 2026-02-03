# Source: https://smartcar.com/docs/api-reference/tesla/get-compass-heading.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Compass

> Returns the current compass heading and direction of the vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_compass`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/compass" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  compass = vehicle.request(
        "GET", 
        "{make}/compass"
  )
  ```

  ```js Node theme={null}
  const compass = await vehicle.request(
        "GET", 
        "{make}/compass"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/compass")
        .build();
  VehicleResponse compass = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  compass = vehicle.request(
        "GET", 
        "{make}/compass"
  )
  ```
</RequestExample>

## Response

<ResponseField name="direction" type="string">
  The current direction of the vehicle.
</ResponseField>

<ResponseField name="heading" type="number">
  The current compass heading of the vehicle (in degrees).
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "direction": "SW",
    "heading": 185
  }
  ```
</ResponseExample>
