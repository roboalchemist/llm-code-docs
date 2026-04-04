# Source: https://smartcar.com/docs/api-reference/tesla/get-ext-vehicle-info.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Extended Vehicle Info

> Returns detailed configuration information for a vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_extended_vehicle_info`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/attributes" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  attributes = vehicle.request(
        "GET", 
        "{make}/attributes"
  )
  ```

  ```js Node theme={null}
  const attributes = await vehicle.request(
        "GET", 
        "{make}/attributes"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/attributes")
        .build();
  VehicleResponse attributes = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  attributes = vehicle.request(
        "GET", 
        "{make}/attributes"
  )
  ```
</RequestExample>

## Response

<ResponseField name="id" type="string">
  A vehicle ID (UUID v4).
</ResponseField>

<ResponseField name="make" type="string">
  The manufacturer of the vehicle.
</ResponseField>

<ResponseField name="model" type="string">
  The model of the vehicle.
</ResponseField>

<ResponseField name="year" type="integer">
  The model year.
</ResponseField>

<ResponseField name="firmwareVersion" type="string">
  Vehicle's current firmware.
</ResponseField>

<ResponseField name="trimBadging" type="string">
  Indicates the Tesla's trim.
</ResponseField>

<ResponseField name="efficiencyPackage" type="string">
  Efficiency package.
</ResponseField>

<ResponseField name="performancePackage" type="string">
  Performance package.
</ResponseField>

<ResponseField name="nickname" type="string">
  Vehicle's nickname.
</ResponseField>

<ResponseField name="driverAssistVersion" type="string">
  Driver Assist version.
</ResponseField>

<ResponseField name="atHome" type="bool">
  Indicates `true` if the vehicle is currently at the home address set in the vehicle. `False` indicates the vehicle is not at home or home location is not set. This value is `null` if `atHome` status could not be determined.
  This field comes back as `null` if the vehicle is not capable of supporting Tesla's Telemetry API (streaming).
</ResponseField>

<ResponseField name="sentryMode" type="object">
  Sentry Mode status and availability.

  <Expandable>
    <ResponseField name="available" type="bool">
      Does the vehicle support Sentry Mode.
    </ResponseField>

    <ResponseField name="enabled" type="bool">
      Is Sentry Mode currently enabled for a vehicle.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="style" type="object">
  Descriptors of the vehicle's interior and exterior.

  <Expandable>
    <ResponseField name="exteriorColor" type="string">
      Exterior color.
    </ResponseField>

    <ResponseField name="exteriorTrim" type="string">
      Exterior trim.
    </ResponseField>

    <ResponseField name="interiorTrim" type="string">
      Interior trim.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="wheel" type="object">
  Descriptors of the vehicle's wheel.

  <Expandable>
    <ResponseField name="style" type="string">
      Style of the wheel.
    </ResponseField>

    <ResponseField name="diameter" type="number" default="millimeters">
      Diameter of the wheel.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="driveUnit" type="object">
  Details on the vehicle's drive unit(s).

  <Expandable>
    <ResponseField name="rear" type="string">
      Rear drive unit.
    </ResponseField>

    <ResponseField name="front" type="string">
      Front drive unit.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
      "driveUnit": {
          "front": "PM216MOSFET",
          "rear": "NoneOrSmall"
      },
      "driverAssistVersion": "TeslaAP3",
      "efficiencyPackage": "MY2021",
      "firmwareVersion": "2022.8.10.12 0ce482dac45d",
      "id": "36ab27d0-fd9d-4455-823a-ce30af709ffc",
      "make": "TESLA",
      "model": "Model S",
      "nickname": "Tommy",
      "performancePackage": "Base",
      "sentryMode": {
          "available": false,
          "enabled": true
      },
      "style": {
          "exteriorColor": "SolidBlack",
          "exteriorTrim": "Black",
          "interiorTrim": "Black2"
      },
      "trimBadging": "74d",
      "wheel": {
          "diameter": 482.6,
          "style": "Apollo"
      },
      "year": 2022,
      "atHome": true
  }
  ```
</ResponseExample>
