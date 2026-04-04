# Source: https://smartcar.com/docs/api-reference/tesla/control-trunk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Trunk

> Open or close the trunk of the Tesla vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_trunk`

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
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/security/trunk" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"action" : "OPEN"}'
  ```

  ```python Python theme={null}
  trunk = vehicle.request(
    "POST", 
    "{make}/security/trunk", 
    {"action" : "OPEN"}
  )
  ```

  ```js Node theme={null}
  const trunk = vehicle.request(
    "POST", 
    "{make}/security/trunk", 
    {"action" : "OPEN"}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/security/trunk")
        .addBodyParameter("action" : "OPEN")
        .build();
  VehicleResponse trunk =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  trunk =  vehicle.request(
    "POST", 
    "{make}/security/trunk", 
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
