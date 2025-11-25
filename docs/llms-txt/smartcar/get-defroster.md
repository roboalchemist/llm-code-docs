# Source: https://smartcar.com/docs/api-reference/tesla/get-defroster.md

# Defroster

> Returns the current state of a vehicle's front and rear defroster.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_climate`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/defroster" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  defroster = vehicle.request(
        "GET", 
        "{make}/climate/defroster"
  )
  ```

  ```js Node theme={null}
  const defroster = await vehicle.request(
        "GET", 
        "{make}/climate/defroster"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/climate/defroster")
        .build();
  VehicleResponse defroster = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  defroster = vehicle.request(
        "GET", 
        "{make}/climate/defroster"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

## Response

<ResponseField name="frontStatus" type="string">
  The current state of the front defroster.
</ResponseField>

<ResponseField name="rearStatus" type="string">
  The current state of the rear defroster.
</ResponseField>

<ResponseExample>
  ```json Example Response   theme={null}
  {
    "frontStatus": "ON",
    "rearStatus": "OFF"
  }
  ```
</ResponseExample>
