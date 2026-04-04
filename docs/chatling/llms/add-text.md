# Source: https://docs.chatling.ai/api-reference/v2/knowledge-base/add-text.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Add text

> Add new text data sources to the knowledge base.

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

### Body

<ParamField body="texts" type="string[]" required>
  Array of texts to add to the knowledge base.
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="texts_added" type="integer">
      The number of texts that were added successfully.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success",
      "data": {
          "texts_added": 45
      }
  }
  ```
</ResponseExample>
