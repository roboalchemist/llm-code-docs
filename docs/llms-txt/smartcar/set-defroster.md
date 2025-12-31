# Source: https://smartcar.com/docs/api-reference/tesla/set-defroster.md

# Defroster

> Start or stop the front and rear defroster for a vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_climate`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="action" type="string" required>
  Indicate whether to start or stop defrosting the vehicle.
  Options: `START` or `STOP`
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/defroster" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"action" : "STOP"}'
  ```

  ```python Python theme={null}
  defroster = vehicle.request(
    "POST", 
    "{make}/climate/defroster", 
    {"action" : "STOP"}
  )
  ```

  ```js Node theme={null}
  const defroster = vehicle.request(
    "POST", 
    "{make}/climate/defroster", 
    {"action" : "STOP"}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/climate/defroster")
        .addBodyParameter("action" : "STOP")
        .build();
  VehicleResponse defroster = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  defroster = vehicle.request(
    "POST", 
    "{make}/climate/defroster", 
    {"action" : "STOP"}
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return `status` containing the action sent to the
  climate defroster system of the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response   theme={null}
  {
    "status": "START"
  }
  ```
</ResponseExample>
