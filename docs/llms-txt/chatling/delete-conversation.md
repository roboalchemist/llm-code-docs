# Source: https://docs.chatling.ai/api-reference/v2/conversations/delete-conversation.md

# Delete conversation

> Delete a conversation.

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

<ParamField path="conversationId" type="string" required>
  The conversation ID.
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseExample>
  ```json  theme={null}
  {
      "status": "success"
  }
  ```
</ResponseExample>
