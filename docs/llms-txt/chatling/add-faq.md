# Source: https://docs.chatling.ai/api-reference/v2/knowledge-base/add-faq.md

# Add FAQ

> Add new FAQ data sources to the knowledge base.

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

### Body

<ParamField body="faqs" type="array" required>
  Array of FAQs to add to the knowledge base.

  <Expandable title="properties">
    <ParamField body="q" type="string" required>
      The question of the FAQ.
    </ParamField>

    <ParamField body="a" type="string" required>
      The answer of the FAQ.
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="faqs_added" type="integer">
      The number of FAQs that were added successfully.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success",
      "data": {
          "faqs_added": 45
      }
  }
  ```
</ResponseExample>
