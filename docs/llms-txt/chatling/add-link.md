# Source: https://docs.chatling.ai/api-reference/v2/knowledge-base/add-link.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Add link

> Add new link data sources to the knowledge base.

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

### Body

<ParamField body="links" type="string[]" required>
  Array of webpage links to add to the knowledge base.
</ParamField>

<ParamField body="exclude_classes" type="string[]">
  Exclude sections of webpages based on their HTML class names.
</ParamField>

<ParamField body="exclude_ids" type="string[]">
  Exclude sections of webpages based on their HTML IDs.
</ParamField>

<ParamField body="exclude_header" type="boolean">
  Exclude `header` tags.
</ParamField>

<ParamField body="exclude_footer" type="boolean">
  Exclude `footer` tags.
</ParamField>

<ParamField body="exclude_nav" type="boolean">
  Exclude `nav` tags.
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="links_added" type="integer">
      The number of links that were added successfully.
    </ResponseField>

    <ResponseField name="duplicate_links_removed" type="array">
      An array of duplicate links that were removed.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success",
      "data": {
          "links_added": 105,
          "duplicate_links_removed": []
      }
  }
  ```
</ResponseExample>
