# Source: https://smartcar.com/docs/api-reference/tesla/clear-pin-to-drive.md

# Clear PIN to Drive

> Disables this feature on the vehicle and resets the PIN.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_pin`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/pin" \
  -H "Authorization: Bearer {token}" \
  -X "DELETE" \
  -H "Content-Type: application/json" \
  ```

  ```python Python theme={null}
  pin = vehicle.request(
    "DELETE", 
    "{make}/pin"
  )
  ```

  ```js Node theme={null}
  const pin = vehicle.request(
    "DELETE", 
    "{make}/pin"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("DELETE")
        .path("{make}/pin")
        .build();
  VehicleResponse pin =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  pin =  vehicle.request(
    "DELETE", 
    "{make}/pin"
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

* Call `POST` [PIN to Drive](/api-reference/tesla/set-pin-to-drive) in order to enable this feature and set the PIN
* Currently both owner and driver account types can clear a PIN for the vehicle and disable the feature via the API.
