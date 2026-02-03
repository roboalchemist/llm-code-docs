# Source: https://docs.chatling.ai/api-reference/v2/usage/knowledge-base.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Knowledge Base

> Get the knowledge base usage for the project.

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="used" type="integer">
      Total number of characters used in the knowledge base.
    </ResponseField>

    <ResponseField name="max" type="integer">
      The maximum number of characters allowed for the project.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success",
      "data": {
          "used": 1500000,
          "max": 20000000
      }
  }
  ```
</ResponseExample>
