# Source: https://docs.chatling.ai/api-reference/v2/contacts/list-contacts.md

# List contacts

> Get a list of all the contacts and leads saved by the chatbot.

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

### Query

<ParamField query="page" type="integer" default="1">
  The page number for pagination.
</ParamField>

<ParamField query="sort" type="string" default="date_desc">
  The sort order. Possible values:

  * `date_desc`: Sort by date in descending order.
  * `date_asc`: Sort by date in ascending order.
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="pages" type="object">
      <Expandable title="properties">
        <ResponseField name="current_page" type="integer">
          The current page number.
        </ResponseField>

        <ResponseField name="last_page" type="integer">
          The last page number.
        </ResponseField>

        <ResponseField name="per_page" type="integer">
          The number of items per page.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="contacts" type="array">
      <Expandable title="properties">
        <ResponseField name="id" type="string">
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
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success",
      "data": {
          "pages": {
              "current_page": 1,
              "last_page": 1,
              "per_page": 25
          },
          "contacts": [
              {
                  "id": "qtr89df0-112d-d197-b541-3f8674663246",
                  "name": "Mark Zuckerberg",
                  "email": "mark@meta.com",
                  "job_title": "CEO",
                  "phone": "555-555-5555",
                  "website": "https://meta.com",
                  "company": "Meta Inc.",
                  "created_at": "2024-06-08T13:38:33+00:00"
              }
          ]
      }
  }
  ```
</ResponseExample>
