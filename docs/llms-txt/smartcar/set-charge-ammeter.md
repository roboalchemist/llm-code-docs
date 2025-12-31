# Source: https://smartcar.com/docs/api-reference/tesla/set-charge-ammeter.md

# Amperage

> Set the amperage drawn by the vehicle from the EVSE for the current charging session. If the vehicle is not plugged in, this endpoint results in a vehicle state error.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_charge`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="amperage" type="number" required>
  The target amperage to be drawn by the vehicle from the charging point (in amperes). If the value passed is greater than what is supported by the charger, it will be set to the maximum.
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/ammeter" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"amperage": 48}'
  ```

  ```python Python theme={null}
  ammeter = vehicle.request(
    "POST", 
    "{make}/charge/ammeter", 
    {"amperage": 48}
  )
  ```

  ```js Node theme={null}
  const ammeter = vehicle.request(
    "POST", 
    "{make}/charge/ammeter", 
    {"amperage": 48}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/charge/ammeter")
        .addBodyParameter("amperage": 48)
        .build();
  VehicleResponse ammeter = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  ammeter = vehicle.request(
    "POST", 
    "{make}/charge/ammeter", 
    {"amperage": 48}
  )
  ```
</RequestExample>

## Response

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return “success” (HTTP 200 status). If the amperage passed was greater than what is supported by the charger, it will be set to the maximum which will be shown here.
</ResponseField>

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return a message (HTTP 200 status) containing the amperage set to be drawn from the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "message": "Successfully sent the following amperage: 48",
    "status": "success"
  }
  ```
</ResponseExample>
