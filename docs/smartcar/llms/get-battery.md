# Source: https://smartcar.com/docs/api-reference/tesla/get-battery.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tesla: Battery Status

> Returns all battery related data for a Tesla vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

<Warning>
  The following fields are not supported for streaming vehicles:

  * TeslaBatteryPercentRemainingUsable
  * TeslaBatteryMaxRangeChargeCounter
</Warning>

## Permission

`read_battery`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/battery" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  battery =  vehicle.request(
        "GET", 
        "{make}/battery"
  )
  ```

  ```js Node theme={null}
  const battery =  await vehicle.request(
        "GET", 
        "{make}/battery"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/battery")
        .build();
  VehicleResponse battery = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  battery =  vehicle.request(
        "GET", 
        "{make}/battery"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

## Response

<ResponseField name="percentRemaining" type="number | null">
  The EV’s state of charge as a percentage.
</ResponseField>

<ResponseField name="range" type="number | null">
  The distance the vehicle can travel powered by it’s high voltage battery.
</ResponseField>

<ResponseField name="heaterOn" type="bool | null">
  Indicates if the battery heater is on.
</ResponseField>

<ResponseField name="rangeEstimated" type="number | null">
  The estimated remaining distance the vehicle can travel powered by it’s high voltage battery as determined by Tesla.
</ResponseField>

<ResponseField name="rangeIdeal" type="number | null">
  The ideal remaining distance the vehicle can travel powered by it’s high voltage battery as determined by Tesla.
</ResponseField>

<ResponseField name="percentRemainingUsable" type="number | null">
  The EV’s useable state of charge as a percentage as reported by Tesla.
</ResponseField>

<ResponseField name="maxRangeChargeCounter" type="number | null">
  The number of times the vehicle has been charged to 100% as reported by Tesla.
</ResponseField>

<ResponseField name="notEnoughPowerToHeat" type="bool | null">
  Indicates if there is enough power to heat the battery.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "heaterOn": null,
      "maxRangeChargeCounter" : null,
      "notEnoughPowerToHeat" : true, 
      "percentRemaining": 0.3,
      "percentRemainingUsable" : 0.29,
      "range": 40.5,
      "rangeEstimated": 39.01,
      "rangeIdeal" : 40.5
  }
  ```
</ResponseExample>
