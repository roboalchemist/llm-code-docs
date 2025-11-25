# Source: https://smartcar.com/docs/api-reference/user-vehicles.md

# User Vehicles

> Returns a paged list of all vehicles connected to the application for the current authorized `user`.

<Note>
  This endpoint is under a different path while we complete the transition to v3.0. You can safely continue using this endpoint, but please be aware that it may be deprecated in the future.
</Note>

## Request

**Query**

<ParamField query="limit" type="integer" default="10">
  The number of vehicles to return per page. `Max: 50`
</ParamField>

<ParamField query="offset" type="integer">
  The index to start the `vehicles` list at.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/all-vehicles.mdx" />
</RequestExample>

## Response

<ResponseField name="paging" type="Object">
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

<ResponseField name="vehicles" type="[string]">
  An array of vehicle IDs.
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
      "paging": {
          "count": 25,
          "offset": 10
      },
      "vehicles": [
          "36ab27d0-fd9d-4455-823a-ce30af709ffc"
      ]
  }
  ```
</ResponseExample>
