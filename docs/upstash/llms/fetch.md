# Source: https://upstash.com/docs/vector/sdks/ts/commands/fetch.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/fetch.md

# Source: https://upstash.com/docs/vector/sdks/php/commands/fetch.md

# Source: https://upstash.com/docs/vector/api/endpoints/fetch.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/fetch.md

# Source: https://upstash.com/docs/search/sdks/py/commands/fetch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Fetch

## Fetch Command for Python SDK

Used to retrieve documents by their IDs.

### Arguments

<ResponseField name="FetchPayload" type="object" required>
  <Expandable defaultOpen="true">
    <ResponseField name="ids" type="string[]">
      The IDs of the documents you want to fetch.
    </ResponseField>

    <ResponseField name="prefix" type="string">
      An ID prefix to match document IDs.
    </ResponseField>
  </Expandable>
</ResponseField>

### Response

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

<RequestExample>
  ```python By ID theme={"system"}
  documents = index.fetch(ids=["movie-0", "movie-1"])
  print(documents)
  ```

  ```python ID Prefix theme={"system"}
  documents = index.fetch(prefix=["movie-"])
  print(documents)
  ```
</RequestExample>
