# Source: https://docs.chatling.ai/api-reference/v2/usage/user-seats.md

# User Seats

> Get the user seats usage for the project.

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="used" type="integer">
      The number of seats used.
    </ResponseField>

    <ResponseField name="max" type="integer">
      The maximum number of seats allowed for the project.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success",
      "data": {
          "used": 3,
          "max": 10
      }
  }
  ```
</ResponseExample>
