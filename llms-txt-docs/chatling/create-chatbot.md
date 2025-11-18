# Source: https://docs.chatling.ai/api-reference/v2/chatbots/create-chatbot.md

# Create chatbot

> Create a new chatbot using a template or from scratch.

## Request parameters

### Body

<ParamField body="name" type="string" required>
  The chatbot name.
</ParamField>

<ParamField body="template_id" type="integer">
  The ID of the chatbot template to use. You can get the list of available templates using the [List chatbot templates](./list-chatbot-templates) endpoint.

  Leave blank to create a chatbot from scratch.
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
