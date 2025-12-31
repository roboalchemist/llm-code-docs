# Source: https://docs.chatling.ai/api-reference/v2/chatbots/list-chatbot-templates.md

# List chatbot templates

> Get a list of all the available chatbot templates. Can be used to create a new chatbot.

## Request parameters

### Query

<ParamField query="page" type="integer" default="1">
  The page number for pagination.
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

    <ResponseField name="templates" type="array">
      <Expandable title="properties">
        <ResponseField name="id" type="integer">
          The unique identifier of the template.
        </ResponseField>

        <ResponseField name="name" type="string">
          The name of the template.
        </ResponseField>

        <ResponseField name="description" type="string">
          The description of the template.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json  theme={null}
  {
      "status": "success",
      "data": {
          "pages": {
              "current_page": 1,
              "last_page": 1,
              "per_page": 25
          },
          "templates": [
              {
                  "id": 1,
                  "name": "AI Chatbot",
                  "description": "Uses AI to automatically respond to customers by leveraging your data, such as your website content, documents, and more."
              },
              {
                  "id": 2,
                  "name": "Basic Lead Generation",
                  "description": "Engage with prospective leads and capture their contact information."
              }
          ]
      }
  }
  ```
</ResponseExample>
