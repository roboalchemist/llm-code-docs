# Source: https://docs.chatling.ai/api-reference/v2/chatbots/duplicate-chatbot.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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
