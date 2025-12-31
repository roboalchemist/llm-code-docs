# Source: https://docs.chatling.ai/api-reference/v2/chatbots/update-chatbot-settings.md

# Update chatbot settings

> Update the settings of a chatbot.

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

### Body

<ParamField body="name" type="string">
  The chatbot name.
</ParamField>

<ParamField body="visibility" type="string">
  The visibility of the chatbot. Possible values are `public` and `private`.
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="id" type="integer">
      The unique identifier of the chatbot.
    </ResponseField>

    <ResponseField name="name" type="string">
      The name of the chatbot.
    </ResponseField>

    <ResponseField name="version" type="string">
      The version of the chatbot.
    </ResponseField>

    <ResponseField name="visibility" type="string">
      The visibility of the chatbot.
    </ResponseField>

    <ResponseField name="created_at" type="string">
      The date and time when the chatbot was created.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json  theme={null}
  {
      "status": "success",
      "data": {
          "id": "9761342719",
          "name": "My chatbot",
          "version": "2.0",
          "visibility": "public",
          "created_at": "2024-06-17T12:00:00+00:00"
      }
  }
  ```
</ResponseExample>
