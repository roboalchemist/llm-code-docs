# Source: https://docs.chatling.ai/chatbot/builder/blocks/action/delete-contact.md

# Source: https://docs.chatling.ai/api-reference/v2/contacts/delete-contact.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete contact

> Delete a contact by its ID.

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

<ParamField path="contactId" type="string" required>
  The contact ID.
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
