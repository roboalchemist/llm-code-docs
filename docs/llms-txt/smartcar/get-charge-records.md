# Source: https://smartcar.com/docs/api-reference/bmw/get-charge-records.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Charge Records

> Returns data associated with completed charging sessions for a vehicle. Limited to the last 30 days or when the owner first granted your application access, which ever is shorter.

<Note>
  This endpoint is currently available for `bmw` and `mini`
</Note>

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

## Response

<ResponseField name="records" type="[object]">
  An array of charge records for the vehicle.

  <Expandable defaultOpen="true">
    <ResponseField name="chargeStart" type="string">
      The start date of the charging record, formatted in ISO 8601 standard
    </ResponseField>

    <ResponseField name="chargeEnd" type="string">
      The end date of the charging record, formatted in ISO 8601 standard
    </ResponseField>

    <ResponseField name="location" type="string">
      Location of the charge session.
    </ResponseField>

    <ResponseField name="energy" type="number" default="kWh">
      The amount of energy consumed during the charging session.
    </ResponseField>

    <ResponseField name="isPublic" type="bool">
      Indicates whether the charging location is public or not.
    </ResponseField>

    <ResponseField name="startPercentRemaining" type="number">
      The remaining battery soc at the start of the charging session.
    </ResponseField>

    <ResponseField name="endPercentRemaining" type="number">
      The remaining battery soc at the end of the charging session.
    </ResponseField>

    <ResponseField name="chargingType" type="string">
      The type of charger used for the session.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "records": [
      {
        "chargeStart" : "2023-03-08T12:54:44Z",
        "chargeEnd" : "2023-03-08T14:14:44Z",
        "location": "Cockfosters Road, Barnet, EN4 0",
        "energy"  : 34.22998046875,
        "isPublic" : true,
        "startPercentRemaining" : 0.57,
        "endPercentRemaining" : 1, 
        "chargingType" : "DC" 
      }
    ]
  }
  ```
</ResponseExample>
