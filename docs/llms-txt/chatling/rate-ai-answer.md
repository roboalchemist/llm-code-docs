# Source: https://docs.chatling.ai/api-reference/v2/conversations/rate-ai-answer.md

# Rate AI answer

Use this endpoint to rate an AI answer as helpful or not helpful. You can only rate AI answers generated using the Knowledge Base.

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

<ParamField path="conversationId" type="string" required>
  The conversation ID.
</ParamField>

<ParamField path="messageId" type="string" required>
  The message ID.
</ParamField>

### Body

<ParamField body="rating" type="string" required>
  * `0`: Remove rating
  * `1`: Helpful
  * `-1`: Not helpful
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success",
      "data": null
  }
  ```
</ResponseExample>
