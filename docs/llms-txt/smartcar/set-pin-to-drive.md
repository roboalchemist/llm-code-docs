# Source: https://smartcar.com/docs/api-reference/tesla/set-pin-to-drive.md

# Set PIN to Drive

> Enables this feature on the vehicle and sets the PIN needed in order to drive it.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_pin`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="pin" type="string" required>
  A four digit numeric PIN
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/pin" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"pin" : "1234"}'
  ```

  ```python Python theme={null}
  pin = vehicle.request(
    "POST", 
    "{make}/pin", 
    {"pin" : "1234"}
  )
  ```

  ```js Node theme={null}
  const pin = vehicle.request(
    "POST", 
    "{make}/pin", 
    {"pin" : "1234"}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/pin")
        .addBodyParameter("pin" : "1234")
        .build();
  VehicleResponse pin =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  pin =  vehicle.request(
    "POST", 
    "{make}/pin", 
    {"pin" : "1234"}
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

## Notes

* Calling this endpoint will override an existing PIN on the vehicle.
* Call `DELETE` [PIN to Drive](/api-reference/tesla/clear-pin-to-drive) in order to enable this feature and set the PIN
* Currently both owner and driver account types can set a PIN for the vehicle and enable the feature via the API.
* Only account owners can disable this feature from the Tesla app.
