# Source: https://docs.chatling.ai/api-reference/v2/chatbots/list-chatbots.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List chatbots

> Get a list of all the chatbots in the project.

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

    <ResponseField name="chatbots" type="array">
      <Expandable title="properties">
        <ResponseField name="id" type="string">
          The unique identifier of the chatbot.
        </ResponseField>

        <ResponseField name="name" type="string">
          The name of the chatbot.
        </ResponseField>

        <ResponseField name="version" type="string">
          The version of the chatbot.
        </ResponseField>

        <ResponseField name="visibility" type="string">
          The visibility of the chatbot. Can be `public` or `private`.
        </ResponseField>

        <ResponseField name="created_at" type="string">
          The date the chatbot was created.
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
          "chatbots": [
              {
                  "id": "8917794239",
                  "name": "My first chatbot",
                  "version": "2.0",
                  "visibility": "public",
                  "created_at": "2024-06-05T12:13:35:00+00:00"
              }
          ]
      }
  }
  ```
</ResponseExample>
