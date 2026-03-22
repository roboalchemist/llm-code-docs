# Source: https://docs.picaos.com/api-reference/core/available-actions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.picaos.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Available Actions

> Get a list of available actions for a given platform

## Path Parameters

<ParamField path="platform" type="string" required>
  The connector platform
</ParamField>

## Query Parameters

<ParamField query="title" type="string">
  The action title
</ParamField>

<ParamField query="key" type="string">
  The action key
</ParamField>

<ParamField query="method" type="string">
  The action method
</ParamField>

<ParamField query="limit" type="number" default="20">
  The number of actions to return
</ParamField>

<ParamField query="page" type="number" default="1">
  The page number
</ParamField>

## Response

<ResponseField name="rows" type="Action[]">
  Array of Action objects

  <Expandable title="Action properties">
    <ResponseField name="title" type="string">
      The human-readable title of the action
    </ResponseField>

    <ResponseField name="key" type="string">
      The unique identifier key for the action
    </ResponseField>

    <ResponseField name="method" type="'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE'">
      The HTTP method used for this action
    </ResponseField>

    <ResponseField name="platform" type="string">
      The platform this action belongs to
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="total" type="number">
  Total number of actions available
</ResponseField>

<ResponseField name="pages" type="number">
  Total number of pages available
</ResponseField>

<ResponseField name="page" type="number">
  Current page number
</ResponseField>

<RequestExample>
  ```bash cURL theme={null}
  curl 'https://api.picaos.com/v1/available-actions/exa' \
    -H 'x-pica-secret: YOUR_API_KEY'
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  {
      "rows": [
          {
              "title": "Get Contents",
              "key": "getContents",
              "modelName": "Content",
              "method": "POST",
              "platform": "exa"
          },
          {
              "title": "Search",
              "key": "search",
              "modelName": "Search",
              "method": "POST",
              "platform": "exa"
          },
          {
              "title": "Find Similar Links",
              "key": "findSimilarLinks",
              "modelName": "Findsimilar",
              "method": "POST",
              "platform": "exa"
          },
          {
              "title": "Get LLM Answer",
              "key": "getLlmAnswer",
              "modelName": "Answer",
              "method": "POST",
              "platform": "exa"
          }
      ],
      "total": 4,
      "pages": 1,
      "page": 1
  }
  ```
</ResponseExample>


Built with [Mintlify](https://mintlify.com).