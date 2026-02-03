# Source: https://smartcar.com/docs/api-reference/compatibility/by-region-and-make.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# By Region and Make

> Compatibility will vary by model, year, and trim. This API is for reference purposes only and it showcases vehicle makes and models that may be compatible with Smartcar and it does not guarantee that a specific vehicle will be compatible.

<Info>
  The Compatibility API is an Enterprise feature. Please [contact us](https://smartcar.com/pricing/) to upgrade your plan.
</Info>

Compatibility by region and make allows developers to query the latest version of our Compatibility Matrix based on region, engine type, make, and permission.

## Request

**Headers**

<Snippet file="header-basic-auth.mdx" />

**Query**

<ParamField query="region" type="string" required>
  One of the following regions: `US`, `CA` or `EUROPE`
</ParamField>

<ParamField query="type" type="string">
  Queries for all engine types if none are specified.

  <Expandable>
    <ResponseField name="ICE" />

    <ResponseField name="BEV" />

    <ResponseField name="PHEV" />

    <ResponseField name="HEV" />
  </Expandable>
</ParamField>

<ParamField query="make" type="string">
  A space-separated list of [makes](/api-reference/makes). This field is optional. If no make is specified, all makes will be returned.
</ParamField>

<ParamField query="scope" type="string">
  A space-separated list of [permissions](/api-reference/permissions).
  Queries for all permissions if none are specified.
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl --request GET \
    --url 'https://api.smartcar.com/v2.0/compatibility/matrix?region=US&type=BEV&make=tesla&scope=read_battery%20read_charge' \
    --header 'Authorization: Basic bXktY2xpZW50LWlkOm15LWNsaWVudC1zZWNyZXQ='
  ```

  ```javascript JavaScript theme={null}
  const response = await fetch('https://api.smartcar.com/v2.0/compatibility/matrix?region=US&type=BEV&make=tesla&scope=read_battery%20read_charge', {
    method: 'GET',
    headers: {
      'Authorization': 'Basic bXktY2xpZW50LWlkOm15LWNsaWVudC1zZWNyZXQ='
    }
  });

  const data = await response.json();
  ```

  ```python Python theme={null}
  import requests

  url = "https://api.smartcar.com/v2.0/compatibility/matrix"
  params = {
      "region": "US",
      "type": "BEV", 
      "make": "tesla",
      "scope": "read_battery read_charge"
  }
  headers = {
      "Authorization": "Basic bXktY2xpZW50LWlkOm15LWNsaWVudC1zZWNyZXQ="
  }

  response = requests.get(url, params=params, headers=headers)
  data = response.json()
  ```
</RequestExample>

## Response

<ResponseField name="make" type="array">
  An array of models supported for the given `make`.

  <Expandable title="make">
    <ResponseField name="model" type="string">
      `model` for the given `make`.
    </ResponseField>

    <ResponseField name="startYear" type="number">
      The earliest model year supported by Smartcar.
    </ResponseField>

    <ResponseField name="endYear" type="number">
      The latest model year supported by Smartcar.
    </ResponseField>

    <ResponseField name="type" type="string">
      Engine type for the given `model`.

      <Expandable title="type">
        <ResponseField name="ICE" />

        <ResponseField name="BEV" />

        <ResponseField name="PHEV" />

        <ResponseField name="HEV" />
      </Expandable>
    </ResponseField>

    <ResponseField name="endpoints" type="array">
      An array of endpoints supported for the given `model`.
    </ResponseField>

    <ResponseField name="permissions" type="array">
      An array of `permissions` supported for the given `model`.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
    {
      "NISSAN": [
        {
          "model": "LEAF",
          "startYear": 2018,
          "endYear": 2022,
          "type": "BEV",
          "endpoints": [
            "EV battery",
            "EV charging status",
            "Location",
            "Lock & unlock",
            "Odometer"
          ],
          "permissions": [
            "read_battery",
            "read_charge",
            "read_location",
            "control_security",
            "read_odometer"
          ]
        }
      ],
      "TESLA": [
        {
          "model": "3",
          "startYear": 2017,
          "endYear": 2023,
          "type": "BEV",
          "endpoints": [
            "EV battery",
            "EV charging status",
            "EV start & stop charge",
            "Location",
            "Lock & unlock",
            "Odometer",
            "Tire pressure"
          ],
          "permissions": [
            "read_battery",
            "read_charge",
            "control_charge",
            "read_location",
            "control_security",
            "read_odometer",
            "read_tires"
          ]
        }
      ]
    }
  ```
</ResponseExample>
