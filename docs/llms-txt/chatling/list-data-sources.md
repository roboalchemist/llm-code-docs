# Source: https://docs.chatling.ai/api-reference/v2/knowledge-base/list-data-sources.md

# List data sources

> Get a list of the data sources added to the knowledge base.

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

<ParamField query="type" type="string">
  Filter by the type of the data source. Possible values are `link`, `text`, `faq`, `document`, and `zoho`.

  Leave blank to get all types of data sources.
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

    <ResponseField name="sources" type="array">
      <Expandable title="properties">
        <ResponseField name="id" type="string">
          The unique identifier of the data source.
        </ResponseField>

        <ResponseField name="type" type="string">
          The type of the data source.
        </ResponseField>

        <ResponseField name="status" type="string">
          The processing status of the data source. Possible values are `pending`, `processing`, `processed`, `error`.
        </ResponseField>

        <ResponseField name="characters" type="integer">
          The number of characters used by the data source.
        </ResponseField>

        <ResponseField name="resync_queued" type="boolean">
          Whether the data source is queued for resync.
        </ResponseField>

        <ResponseField name="data" type="object">
          Additional data based on the type of the data source.
        </ResponseField>

        <ResponseField name="created_at" type="string">
          The date and time when the data source was created.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      {
      "status": "success",
      "data": {
          "pages": {
              "current_page": 1,
              "last_page": 3,
              "per_page": 25
          },
          "sources": [
              {
                  "id": "321e979b-a174-89fc-25de-f0b31dbd659f",
                  "type": "link",
                  "status": "processed",
                  "characters": 6232,
                  "resync_queued": false,
                  "data": {
                      "url": "https://chatling.ai",
                      "page_title": "No-Code AI Chatbot for Your Website | Chatling"
                  },
                  "created_at": "2024-06-15T12:23:41"
              },
          ]
      }
  }
  ```
</ResponseExample>
