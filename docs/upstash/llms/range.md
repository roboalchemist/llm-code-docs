# Source: https://upstash.com/docs/vector/sdks/ts/commands/range.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/range.md

# Source: https://upstash.com/docs/vector/api/endpoints/range.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/range.md

# Source: https://upstash.com/docs/search/sdks/py/commands/range.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Range

## Range Command for Python SDK

The range method is used to retrieve documents in chunks with pagination.

### Arguments

<ResponseField name="Payload" type="dict" required>
  <Expandable defaultOpen="true">
    <ResponseField name="cursor" type="string" required>
      The cursor to the last retrieved document. Should be set to `""` in the initial range request.
    </ResponseField>

    <ResponseField name="limit" type="int" required>
      The number of maximum documents wanted in the response of range. (page size)
    </ResponseField>
  </Expandable>
</ResponseField>

### Response

<ResponseField name="Response" type="dict" required>
  <Expandable defaultOpen="true">
    <ResponseField name="Documents" type="List[Document]" required>
      This field is `null` if no document with the specified ID is found.

      <Expandable defaultOpen="true">
        <ResponseField name="id" type="string | number" required>
          The ID of the resulting document.
        </ResponseField>

        <ResponseField name="content" type="Record<string, unknown>">
          The main content of the document.
        </ResponseField>

        <ResponseField name="metadata" type="Record<string, unknown>">
          Additional metadata for the document.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="next_cursor" type="string">
      The cursor for the next page of documents.
    </ResponseField>
  </Expandable>
</ResponseField>

<RequestExample>
  ```python  theme={"system"}
  range_documents = index.range(cursor="", limit=1)
  print(range_documents.documents)

  range_documents = index.range(
      cursor=range_documents.next_cursor,
      limit=3
  )
  print(range_documents.documents)
  ```
</RequestExample>
