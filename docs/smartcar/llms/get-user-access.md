# Source: https://smartcar.com/docs/api-reference/tesla/get-user-access.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# User Access

> Returns the account type and permissions for the connected Tesla account.

<Snippet file="api-reference/note-bse-tesla.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/user/access" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  access = vehicle.request(
        "GET", 
        "{make}/user/access"
  )
  ```

  ```js Node theme={null}
  const access = await vehicle.request(
        "GET", 
        "{make}/user/access"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/user/access")
        .build();
  VehicleResponse access =vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  access = vehicle.request(
        "GET", 
        "{make}/user/access"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

## Response

<ResponseField name="accessType" type="string | null">
  Returns the type of Tesla account connected. Can be either `OWNER` or `DRIVER`. Please see our [Tesla FAQs](/help/oem-integrations/tesla/faqs) for details on the differences between account types.
</ResponseField>

<ResponseField name="permissions" type="[string] | null">
  Returns a list of permissions granted by the user with their Tesla account. Please see [this page](/help/oem-integrations/tesla/developers#permission-mappings) on the mapping from Smartcar permissions to Tesla's.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "accessType": "OWNER",
    "permissions" : ["vehicle_cmds", "vehicle_device_data"]
  }
  ```
</ResponseExample>

## Notes

* If you're receiving a [SERVER:INTERNAL](/errors/api-errors/server-errors#internal) error please have the user reconnect their vehicle.
