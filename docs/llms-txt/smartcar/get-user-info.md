# Source: https://smartcar.com/docs/api-reference/tesla/get-user-info.md

# User Info

> Returns the email associated with the connected Tesla account.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_user_profile`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/user/info" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  info = vehicle.request(
        "GET", 
        "{make}/user/info"
  )
  ```

  ```js Node theme={null}
  const info = await vehicle.request(
        "GET", 
        "{make}/user/info"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/user/info")
        .build();
  VehicleResponse info =vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  info = vehicle.request(
        "GET", 
        "{make}/user/info"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

## Response

<ResponseField name="email" type="string | null">
  The email associated with the connected Tesla account.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
      {
          "email" : "api@smartcar.com"
      }
  ```
</ResponseExample>
