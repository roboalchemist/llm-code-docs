# Source: https://smartcar.com/docs/api-reference/tesla/get-migration-status.md

# Migration Status

> Indicates if the vehicle needs to migrate to Tesla's new API. See [Tesla - What's New](https://smartcar.com/docs/help/oem-integrations/tesla/whats-new) for more details.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_vehicle_info`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/migration" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  status = vehicle.request(
        "GET", 
        "{make}/migration"
  )
  ```

  ```js Node theme={null}
  const status = await vehicle.request(
        "GET", 
        "{make}/migration"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/migration")
        .build();
  VehicleResponse status = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  status = vehicle.request(
        "GET", 
        "{make}/migration"
  )
  ```
</RequestExample>

## Response

<ResponseField name="requiresMigration" type="boolean">
  Set to `false` if the vehicle is connected to Smartcar via Tesla's new integration. See [Tesla - What's New](/help/oem-integrations/tesla/whats-new) for more details.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "requiresMigration": false
  }
  ```
</ResponseExample>
