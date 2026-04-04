# Source: https://smartcar.com/docs/api-reference/tesla/get-charge-records-billing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Charge Billing Records

> Returns information about charging sessions for Tesla vehicles at public Tesla chargers including cost and charging site.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_charge_records`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Query**

<ParamField query="startDate">
  Date of the first record to return in YYYY-MM-DD format.
  Defaults to 30 days prior  or when the owner first granted your application access, whichever is shorter.
</ParamField>

<ParamField query="endDate">
  Date of the final record to return in YYYY-MM-DD format. Defaults to the date of the request.
</ParamField>

<ParamField query="page">
  The page number to fetch from Tesla where page 1 contains the most recent records.
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/records/billing?page=12&startDate=2023-08-24" \
      -H "Authorization: Bearer {token}" \
      -X "GET" \
      -H "Content-Type: application/json" \
  ```

  ```python Python theme={null}
  billing = vehicle.request(
    "GET", 
    "{make}/charge/records/billing?startDate=2023-08-24&page=12"
  )
  ```

  ```js Node theme={null}
  const billing = vehicle.request(
    "GET", 
    "{make}/charge/records/billing?startDate=2023-08-24&page=12"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request =
      new SmartcarVehicleRequest.Builder()
          .method("GET")
          .path("ford/charge/schedule_by_location")
          .addQueryParameter("startDate", "2023-08-24")
          .addQueryParameter("page", "12")
          .build();

  VehicleResponse billing = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  billing = vehicle.request(
    "GET", 
    "{make}/charge/records/billing?startDate=2023-08-24&page=12"
  )
  ```
</RequestExample>

## Response

<ResponseField name="records" type="[object]">
  An array of billing records for the vehicle associated with charging at public Tesla charging stations.

  Can be empty if the specified page does not contain any records for the vehicle.
  This **does not** mean that subsequent pages will also contain no records. Please check the `hasMoreData` field for confirmation instead.

  <Expandable defaultOpen="true">
    <ResponseField name="chargeStart" type="string">
      The date and time of charging session start, formatted in ISO 8601 standard.
    </ResponseField>

    <ResponseField name="chargeEnd" type="string">
      The date and time of charging session end, formatted in ISO 8601 standard.
    </ResponseField>

    <ResponseField name="energyConsumed" type="number" default="kWh">
      Energy consumed in the charging session.
    </ResponseField>

    <ResponseField name="cost" type="object">
      A cost breakout of the charging session.

      <Expandable defaultOpen="true">
        <ResponseField name="currency" type="string">
          The currency code for the fees.
        </ResponseField>

        <ResponseField name="energy" type="number">
          Fess associated with charging the vehicle.
        </ResponseField>

        <ResponseField name="other" type="number">
          Fees associated with the session other than charging the vehicle e.g. parking.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="location" type="string">
      The name of the charging site.
    </ResponseField>

    <ResponseField name="recordId" type="string">
      Tesla’s id for this charging session.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="hasMoreData" type="bool">
  Indicates if there are any more records to fetch from Tesla for this vehicle. **Does not** guarantee a non-empty list for the next page when `true`.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "records": [
        {
            "chargeEnd": "2022-07-10T16:20:00.000Z",
            "chargeStart": "2022-07-10T15:40:00.000Z",
            "energyConsumed": 44.10293884
            "cost": {
                "currency": "USD",
                "energy": "41",
                "other": "41"
            },
            "location": "Los Gatos, CA",
            "recordId": "GF220075000028-3-1682903685"
        }
    ],
    "hasMoreData" : false
  }
  ```
</ResponseExample>
