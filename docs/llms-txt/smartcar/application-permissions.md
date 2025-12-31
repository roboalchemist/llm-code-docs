# Source: https://smartcar.com/docs/api-reference/application-permissions.md

# Permissions

> Returns a list of the permissions that have been granted to your application in relation to this vehicle.

## Request

<ParamField path="id" type="string" required>
  The vehicle id.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/application-permissions.mdx" />
</RequestExample>

## Response

<ResponseField name="permissions" type="[permissions]">
  An array of [permissions](/api-reference/permissions).
</ResponseField>

<ResponseField name="paging" type="object">
  Metadata about the current list of elements.

  <Expandable>
    <ResponseField name="count" type="integer">
      The total number of elements for the entire query (not just the given page).
    </ResponseField>

    <ResponseField name="offset" type="integer">
      The current start index of the returned list of elements.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
      "paging": {
          "count": 25,
          "offset": 10
      },
      "permissions": [
          "read_vehicle_info"
      ]
  } 
  ```
</ResponseExample>
