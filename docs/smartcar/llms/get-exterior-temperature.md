# Source: https://smartcar.com/docs/api-reference/tesla/get-exterior-temperature.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exterior Temperature

> Returns the vehicle’s last known exterior thermometer reading. See our [climate setting](/docs/api-reference/tesla/get-cabin) endpoints for managing a cabin temperature.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_thermometer`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/thermometer/exterior" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  temperature = vehicle.request(
        "GET", 
        "{make}/thermometer/exterior"
  )
  ```

  ```js Node theme={null}
  const temperature = await vehicle.request(
        "GET", 
        "{make}/thermometer/exterior"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/thermometer/exterior")
        .build();
  VehicleResponse temperature = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  temperature = vehicle.request(
        "GET", 
        "{make}/thermometer/exterior"
  )
  ```
</RequestExample>

## Response

<ResponseField name="temperature" default="celsius" type="number">
  The current exterior temperature of the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "temperature": 33.42
  }
  ```
</ResponseExample>
