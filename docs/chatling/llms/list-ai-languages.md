# Source: https://docs.chatling.ai/api-reference/v2/ai-kb/list-ai-languages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List AI languages

> Get a list of all the supported AI languages.

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

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

    <ResponseField name="languages" type="array">
      <Expandable title="properties">
        <ResponseField name="id" type="integer">
          The unique identifier of the language.
        </ResponseField>

        <ResponseField name="name" type="string">
          The name of the language.
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
              "last_page": 6,
              "per_page": 15
          },
          "languages": [
              {
                  "id": 1,
                  "name": "Auto"
              },
              {
                  "id": 2,
                  "name": "English"
              },
              {
                  "id": 3,
                  "name": "Albanian"
              },
              {
                  "id": 4,
                  "name": "Arabic"
              },
              {
                  "id": 5,
                  "name": "Armenian"
              },
              {
                  "id": 7,
                  "name": "Azerbaijani"
              },
              {
                  "id": 9,
                  "name": "Basque"
              },
              {
                  "id": 10,
                  "name": "Belarusian"
              },
              {
                  "id": 11,
                  "name": "Bengali"
              },
              {
                  "id": 12,
                  "name": "Bhojpuri"
              },
              {
                  "id": 13,
                  "name": "Bosnian"
              },
              {
                  "id": 15,
                  "name": "Bulgarian"
              },
              {
                  "id": 17,
                  "name": "Catalan"
              },
              {
                  "id": 19,
                  "name": "Chinese (Simplified)"
              },
              {
                  "id": 20,
                  "name": "Croatian"
              }
          ]
      }
  }
  ```
</ResponseExample>
