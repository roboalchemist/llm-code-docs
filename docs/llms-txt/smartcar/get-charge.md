# Source: https://smartcar.com/docs/api-reference/tesla/get-charge.md

# Source: https://smartcar.com/docs/api-reference/audi/get-charge.md

# Source: https://smartcar.com/docs/api-reference/tesla/get-charge.md

# Source: https://smartcar.com/docs/api-reference/audi/get-charge.md

# Source: https://smartcar.com/docs/api-reference/tesla/get-charge.md

# Source: https://smartcar.com/docs/api-reference/audi/get-charge.md

# Source: https://smartcar.com/docs/api-reference/tesla/get-charge.md

# Source: https://smartcar.com/docs/api-reference/audi/get-charge.md

# Audi: Charge Status

> Returns all charging related data for an Audi vehicle.

<Snippet file="api-reference/note-bse-audi.mdx" />

## Permission

`read_charge`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  charge =  vehicle.request(
        "GET", 
        "{make}/charge"
  )
  ```

  ```js Node theme={null}
  const charge =  await vehicle.request(
        "GET", 
        "{make}/charge"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/charge")
        .build();
  VehicleResponse charge =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  charge =  vehicle.request(
        "GET", 
        "{make}/charge"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

## Response

<ResponseField name="chargingStatus" type="string | null">
  Indicates the charging status of the vehicle
</ResponseField>

<ResponseField name="isPluggedIn" type="bool | null">
  Indicates if the vehicle is plugged in
</ResponseField>

<ResponseField name="wattage" type="number | null">
  The instant power measured by the vehicle (in kilowatts).
</ResponseField>

<ResponseField name="chargeRate" type="number | null">
  The rate of range added in the charging session (in kilometers added / hour).
</ResponseField>

<ResponseField name="chargeType" type="string | null">
  Indicates the type of charger.
</ResponseField>

<ResponseField name="chargePortColor" type="string | null">
  The indicator light color of the connector.
</ResponseField>

<ResponseField name="chargePortLatch" type="string | null">
  Indicates if the charge port latch status.
</ResponseField>

<ResponseField name="completionTime" type="string | null">
  An ISO8601 formatted datetime (YYYY-MM-DDTHH:mm:ss.SSSZ) for the time at which the vehicle expects to complete this charging session.
</ResponseField>

<ResponseField name="chargeMode" type="string | null">
  Indicates if the vehicle is set to charge on a timer. One of `manual` or `timer`.
</ResponseField>

<ResponseField name="socLimit" type="number | null">
  Indicates the level at which the vehicle will stop charging and be considered fully charged as a percentage.
</ResponseField>

<ResponseField name="externalPowerStatus" type="string | null">
  When plugged in indicates if the charging station is able to provide power to the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
      {
            "chargingStatus": "CHARGING",
            "isPluggedIn": null,
            "chargeRate": 21,
            "chargeType": "ac",
            "chargePortColor": "green",
            "chargePortLatch": "locked",
            "completionTime": "2022-01-13T22:52:55.358Z",
            "chargeMode": "manual",
            "socLimit": 0.8,
            "externalPowerStatus": "active",
            "wattage" : 1.5
      }
  ```
</ResponseExample>
