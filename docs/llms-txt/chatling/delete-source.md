# Source: https://docs.chatling.ai/api-reference/v2/knowledge-base/delete-source.md

# Delete data source

> Delete a data source from the knowledge base.

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

<ParamField path="dataSourceId" type="string" required>
  The data source ID.
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success"
  }
  ```
</ResponseExample>
