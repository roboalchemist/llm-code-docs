# Source: https://smartcar.com/docs/api-reference/tesla/set-steering-heater.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Steering Heater

> Start or stop heating a vehicle's steering wheel.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_climate`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="action" type="string" required>
  Indicate whether to start or stop heating the vehicle's steering wheel.
  Options: `START` or `STOP`
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/steering_wheel" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"action" : "STOP"}'
  ```

  ```python Python theme={null}
  steering_wheel = vehicle.request(
    "POST", 
    "{make}/climate/steering_wheel", 
    {"action" : "STOP"}
  )
  ```

  ```js Node theme={null}
  const steeringWheel = vehicle.request(
    "POST", 
    "{make}/climate/steering_wheel", 
    {"action" : "STOP"}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/climate/steering_wheel")
        .addBodyParameter("action" : "STOP")
        .build();
  VehicleResponse steeringWheel =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  steering_wheel =  vehicle.request(
    "POST", 
    "{make}/climate/steering_wheel", 
    {"action" : "STOP"}
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return status containing the action sent to the vehicle.
  `UNAVAILABLE` indicates the vehicle is not equipped with a steering wheel heater.
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "status": "START",
  }
  ```
</ResponseExample>
