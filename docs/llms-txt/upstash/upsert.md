# Source: https://upstash.com/docs/vector/sdks/ts/commands/upsert.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/upsert.md

# Source: https://upstash.com/docs/vector/api/endpoints/upsert.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/upsert.md

# Source: https://upstash.com/docs/search/sdks/py/commands/upsert.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Upsert

## Upsert Command for Python SDK

Used to add new documents or update an existing document.

### Arguments

<ResponseField name="Documents" type="List[Document]" required>
  <Expandable defaultOpen="true">
    <ResponseField name="id" type="string | int" required>
      The unique identifier for the document.
    </ResponseField>

    <ResponseField name="content" type="dict" required>
      The main content of the document.
    </ResponseField>

    <ResponseField name="metadata" type="dict">
      Additional metadata for the document.
    </ResponseField>
  </Expandable>
</ResponseField>

<RequestExample>
  ```python  theme={"system"}
  from upstash_search import Search

  client = Search(
      url="<UPSTASH_SEARCH_REST_URL>",
      token="<UPSTASH_SEARCH_REST_TOKEN>",
  )

  index = client.index("movies")

  index.upsert(
      documents=[
          {
              "id": "movie-0",
              "content": {
                  "title": "Star Wars",
                  "overview": "Sci-fi space opera",
                  "genre": "sci-fi",
                  "category": "classic",
              },
              "metadata": {
                  "poster": "https://poster.link/starwars.jpg",
              },
          },
      ],
  )
  ```
</RequestExample>
