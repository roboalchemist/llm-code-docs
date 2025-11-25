# Source: https://smartcar.com/docs/api-reference/tesla/set-cabin.md

# Cabin Climate

> Set the temperature and control the cabin climate system for a vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_climate`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="action" type="string" required>
  Indicate whether to start or stop the cabin climate control system, or set the temperature.
  If starting or stopping the system, `temperature` is optional and will use the vehicle's current setting by default.

  <Expandable title="status">
    <ResponseField name="START" type="string" />

    <ResponseField name="STOP" type="string" />

    <ResponseField name="SET" type="string">
      Use `SET` to set the `temperature` without changing the climate systems status.
    </ResponseField>
  </Expandable>
</ParamField>

<ParamField body="temperature" type="string">
  Indicate what temperature to set (in Celsius by default or in Fahrenheit using the sc-unit-system).
  If the provided temperature is out of the bounds allowed by the vehicle's climate control system,
  the request will fail with the upper and lower limits in the error response message.
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/cabin" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"action": "SET", "temperature": 20}'
  ```

  ```python Python theme={null}
  set_climate_cabin = vehicle.request(
    "POST", 
    "{make}/climate/cabin", 
    {
      "action": "SET", 
      "temperature": 18
    }
  )

  ```

  ```js Node theme={null}
  const vehicleStopCabin = vehicle.request(
    "POST", 
    "{make}/climate/cabin", 
    {"action": "STOP"}
  );

  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/climate/cabin")
        .addBodyParameter("action", "START")
        .build();
  VehicleResponse startClimateCabin = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  setChargeScheduleByLocation = vehicle.request(
    "POST", 
    "{make}/climate/cabin", 
    {"action" : "START"}
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return `"success"` (HTTP 200 status) containing the current state of the climate cabin system.
</ResponseField>

<ResponseField name="temperature" type="number">
  The target temperature setting of the vehicle when the climate system is on (in Celsius by default or in Fahrenheit using the sc-unit-system).
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "status": "ON",
    "temperature": 24
  }
  ```
</ResponseExample>
