# Source: https://smartcar.com/docs/api-reference/tesla/get-virtual-key-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Virtual Key Status

> Indicates if a vehicle has the appropriate virtual key installed. See [Tesla - What's New](https://smartcar.com/docs/help/oem-integrations/tesla/whats-new#if-your-application-issues-commands) for more details on Tesla's virtual key requirements.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_vehicle_info`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/virtual_key" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  virtual_key = vehicle.request(
        "GET", 
        "{make}/virtual_key"
  )
  ```

  ```js Node theme={null}
  const virtualKey = await vehicle.request(
        "GET", 
        "{make}/virtual_key"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/virtual_key")
        .build();
  VehicleResponse virtualKey = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  virtual_key = vehicle.request(
        "GET", 
        "{make}/virtual_key"
  )
  ```
</RequestExample>

## Response

<ResponseField name="isPaired" type="boolean">
  Returns `true` if the vehicle has the appropriate Virtual Key installed. See [Tesla - What's New](/help/oem-integrations/tesla/whats-new#if-your-application-issues-commands) for more details on Tesla's virtual key requirements.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "isPaired": true
  }
  ```
</ResponseExample>

## Notes

* This endpoint will throw a [COMPATIBILITY:PLATFORM\_NOT\_CAPABLE](/errors/api-errors/compatibility-errors#platform-not-capable) error if a vehicle is connected to your application via Tesla's legacy integration.
* This endpoint will throw a [CONNECTED\_SERVICES\_ACCOUNT:VEHICLE\_MISSING](/errors/api-errors/compatibility-errors#vehicle-missing) error if the Tesla account connected to Smartcar is **not** the Owner of the vehicle. See our [FAQs](/help/oem-integrations/tesla/faqs#can-owner-and-driver-accounts-authorize-access-with-smartcar-through-connect) for more information on Owner and Driver account types.
