# Source: https://docs.chatling.ai/api-reference/v2/chatbots/duplicate-chatbot.md

# Duplicate chatbot

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="chatbot_id" type="string">
      The unique identifier of the duplicated chatbot.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json  theme={null}
  {
      "status": "success",
      "data": {
          "chatbot_id": "5285975738"
      }
  }
  ```
</ResponseExample>
