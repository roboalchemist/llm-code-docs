# Source: https://docs.chatling.ai/api-reference/v2/usage/email-credits.md

# Email Credits

> Get the email credits usage for the project.

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="used" type="integer">
      The number of email credits used.
    </ResponseField>

    <ResponseField name="max" type="integer">
      The maximum number of email credits allowed for the project.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success",
      "data": {
          "used": 125,
          "max": 1500
      }
  }
  ```
</ResponseExample>
