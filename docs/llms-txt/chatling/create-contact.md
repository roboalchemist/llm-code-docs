# Source: https://docs.chatling.ai/chatbot/builder/blocks/hubspot/create-contact.md

# Source: https://docs.chatling.ai/chatbot/builder/blocks/action/create-contact.md

# Source: https://docs.chatling.ai/api-reference/v2/contacts/create-contact.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create contact

> Create a new contact for the chatbot.

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

### Body

<ParamField body="properties" type="object">
  At least one of the following properties is required.

  <Expandable title="properties">
    <ParamField body="first_name" type="string" placeholder="John" />

    <ParamField body="last_name" type="string" placeholder="Doe" />

    <ParamField body="email" type="string" placeholder="john.doe@example.com" />

    <ParamField body="phone" type="string" placeholder="1234567890" />

    <ParamField body="job_title" type="string" placeholder="Software Engineer" />

    <ParamField body="company_name" type="string" placeholder="Acme Inc" />

    <ParamField body="website_url" type="string" placeholder="https://acme.com" />

    <ParamField body="industry" type="string" placeholder="Technology" />

    <ParamField body="address" type="string" placeholder="123 Main St" />

    <ParamField body="city" type="string" placeholder="New York" />

    <ParamField body="state" type="string" placeholder="NY" />

    <ParamField body="postal_code" type="string" placeholder="10001" />

    <ParamField body="country" type="string" placeholder="USA" />
  </Expandable>
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="id" type="string">
      The unique identifier of the contact.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success",
      "data": {
          "id": "qtr89df0-112d-d197-b541-3f8674663246"
      }
  }
  ```
</ResponseExample>
