# Source: https://docs.chatling.ai/api-reference/v2/usage/ai-credits.md

# Source: https://docs.chatling.ai/ai/ai-credits.md

# Source: https://docs.chatling.ai/api-reference/v2/usage/ai-credits.md

# AI Credits

> Get the AI credits usage for the project.

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="used" type="integer">
      The number of AI credits used.
    </ResponseField>

    <ResponseField name="max" type="integer">
      The maximum number of AI credits allowed for the project.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success",
      "data": {
          "used": 55,
          "max": 3000
      }
  }
  ```
</ResponseExample>
