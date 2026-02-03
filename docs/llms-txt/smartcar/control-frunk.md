# Source: https://smartcar.com/docs/api-reference/tesla/control-frunk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Frunk

> Open or close the frunk (front trunk) of the Tesla vehicle.

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
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/security/frunk" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"action" : "OPEN"}'
  ```

  ```python Python theme={null}
  frunk = vehicle.request(
    "POST", 
    "{make}/security/frunk", 
    {"action" : "OPEN"}
  )
  ```

  ```js Node theme={null}
  const frunk = vehicle.request(
    "POST", 
    "{make}/security/frunk", 
    {"action" : "OPEN"}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/security/frunk")
        .addBodyParameter("action" : "OPEN")
        .build();
  VehicleResponse frunk =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  frunk =  vehicle.request(
    "POST", 
    "{make}/security/frunk", 
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
