# Source: https://smartcar.com/docs/api-reference/tesla/get-charge-wattmeter.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wattage

> When the vehicle is charging, returns the instant charging wattage as measured by the vehicle. When the vehicle is not charging, this endpoint results in a vehicle state error.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_charge`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/wattmeter" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  wattmeter = vehicle.request(
        "GET", 
        "{make}/charge/wattmeter"
  )
  ```

  ```js Node theme={null}
  const wattmeter = await vehicle.request(
        "GET", 
        "{make}/charge/wattmeter"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/charge/wattmeter")
        .build();
  VehicleResponse wattmeter = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  wattmeter = vehicle.request(
        "GET", 
        "{make}/charge/wattmeter"
  )
  ```
</RequestExample>

## Response

<ResponseField name="wattage" type="number">
  The instant power measured by the vehicle (in kilowatts).
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "wattage": 3.5
  }
  ```
</ResponseExample>
