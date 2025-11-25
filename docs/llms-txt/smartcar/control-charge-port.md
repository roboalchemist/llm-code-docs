# Source: https://smartcar.com/docs/api-reference/tesla/control-charge-port.md

# Charge Port

> Open or close the vehicle's charge port door.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_charge`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="action" type="string" required>
  Indicate whether to open or close the charge port door.
  Options: `OPEN` or `CLOSE`
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/charge_port_door" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"action" : "OPEN"}'
  ```

  ```python Python theme={null}
  charge_port = vehicle.request(
    "POST", 
    "{make}/charge/charge_port_door", 
    {"action" : "OPEN"}
  )
  ```

  ```js Node theme={null}
  const chargePort = vehicle.request(
    "POST", 
    "{make}/charge/charge_port_door", 
    {"action" : "OPEN"}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/charge/charge_port_door")
        .addBodyParameter("action" : "OPEN")
        .build();
  VehicleResponse chargePort =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  charge_port =  vehicle.request(
    "POST", 
    "{make}/charge/charge_port_door", 
    {"action" : "OPEN"}
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return “success”.
</ResponseField>

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
      {
          "message": "Successfully sent request to vehicle",
          "status": "success"
      }   
  ```
</ResponseExample>
