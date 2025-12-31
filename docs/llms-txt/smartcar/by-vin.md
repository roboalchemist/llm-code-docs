# Source: https://smartcar.com/docs/api-reference/compatibility/by-vin.md

# By VIN

> Compatibility will vary by model, year, and trim. This API is for reference purposes only and it showcases vehicle makes and models that may be compatible with Smartcar and it does not guarantee that a specific vehicle will be compatible.

<Info>
  The Compatibility API is an Enterprise feature. Please [contact us](https://smartcar.com/pricing/) to upgrade your plan.
</Info>

Compatibility by VIN allows developers to determine if a specific vehicle could be compatible with Smartcar.

A vehicle is capable of a given feature if:

1. The vehicle supports the feature (e.g., a Ford Escape supports /fuel but a Mustang Mach-e does not)
2. Smartcar supports the feature for the vehicle's make

This endpoint only supports checking capabilities for vehicles sold in the United States. It **does not** support checking `capabilities` for VINs in Canada and Europe.

## Request

**Headers**

<Snippet file="header-basic-auth.mdx" />

**Parameters**

<ParamField query="vin" type="string" required>
  The VIN (Vehicle Identification Number) of the vehicle.
</ParamField>

<ParamField query="scope" type="string" required>
  A space-separated list of permissions.
</ParamField>

<ParamField query="country" default="US" type="string">
  An optional country code string according to ISO 3166-1 alpha-2.
</ParamField>

<RequestExample />

## Response

<ResponseField name="compatible" type="boolean">
  `true` if the vehicle is likely compatible, `false` otherwise.
</ResponseField>

<ResponseField name="reason" type="string | null">
  One of the reasons described below if compatible is `false`, `null` otherwise

  <Expandable title="reasons">
    <ResponseField name="VEHICLE_NOT_COMPATIBLE">
      The vehicle does not have the hardware required for internet connectivity
    </ResponseField>

    <ResponseField name="MAKE_NOT_COMPATIBLE">
      Smartcar is not yet compatible with the vehicle's make in the specified country
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="capabilities" type="array">
  An array containing capability objects for the set of endpoints that the provided scope value can provide authorization for.
  This array will be empty if `compatible` is `false`.

  <Expandable title="Capability object">
    <ResponseField name="permission" type="string">
      One of the permissions provided in the scope parameter
    </ResponseField>

    <ResponseField name="endpoint" type="string">
      One of the endpoints that the permission authorizes access to
    </ResponseField>

    <ResponseField name="capable" type="boolean">
      `true` if the vehicle is likely capable of this feature, `false` otherwise
    </ResponseField>

    <ResponseField name="reason" type="string | null">
      One of the reasons described below if capable is `false`, `null` otherwise

      <Expandable title="reasons">
        <ResponseField name="VEHICLE_NOT_CAPABLE">
          The vehicle does not support this feature
        </ResponseField>

        <ResponseField name="SMARTCAR_NOT_CAPABLE">
          Smartcar is not capable of supporting the given feature on the vehicle's make
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
    {
    "compatible": true,
    "reason": null,
    "capabilities": [
      {
        "capable": false,
        "endpoint": "/engine/oil",
        "permission": "read_engine_oil",
        "reason": "SMARTCAR_NOT_CAPABLE"
      },
      {
        "capable": true,
        "endpoint": "/battery",
        "permission": "read_battery",
        "reason": null
      },
      {
        "capable": true,
        "endpoint": "/battery/capacity",
        "permission": "read_battery",
        "reason": null
      },
      {
        "capable": true,
        "endpoint": "/vin",
        "permission": "read_vin",
        "reason": null
      }
    ]
  }
  ```
</ResponseExample>

<Info>
  A vehicle's compatibility depends on many factors such as its make, model, model year, trim, etc. The API optimizes returning false positives.
</Info>
