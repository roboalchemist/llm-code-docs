# Source: https://docs.chatling.ai/chatbot/builder/blocks/hubspot/retrieve-contact.md

# Source: https://docs.chatling.ai/api-reference/v2/contacts/retrieve-contact.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve contact

> Retrieve a contact by its ID.

## Request parameters

### Path

<ParamField path="contactId" type="string" required>
  The contact ID.
</ParamField>

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="id" type="integer">
      The unique identifier of the contact.
    </ResponseField>

    <ResponseField name="name" type="string">
      The name of the contact.
    </ResponseField>

    <ResponseField name="email" type="string">
      The email address of the contact.
    </ResponseField>

    <ResponseField name="job_title" type="string">
      The job title of the contact.
    </ResponseField>

    <ResponseField name="phone" type="string">
      The phone number of the contact.
    </ResponseField>

    <ResponseField name="website" type="string">
      The website URL of the contact.
    </ResponseField>

    <ResponseField name="company" type="string">
      The company name of the contact.
    </ResponseField>

    <ResponseField name="created_at" type="string">
      The date and time when the contact was created.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json  theme={null}
  {
      "status": "success",
      "data": {
          "id": "qtr89df0-112d-d197-b541-3f8674663246",
          "name": "Mark Zuckerberg",
          "email": "mark@meta.com",
          "job_title": "CEO",
          "phone": "555-555-5555",
          "website": "https://meta.com",
          "company": "Meta Inc.",
          "created_at": "2024-06-08T13:38:33+00:00"
      }
  }
  ```
</ResponseExample>
