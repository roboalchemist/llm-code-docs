# Source: https://dev.writer.com/home/web-connector-url.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add web content to a Knowledge Graph

This guide demonstrates how to add web content to a [Knowledge Graph](/home/knowledge-graph) using web connector URLs. Adding web connector URLs to your Knowledge Graph allows you to automatically extract and index content from websites, making it available for querying in your Knowledge Graph.

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

## Overview

Adding URLs to your Knowledge Graph enables you to:

* Automatically extract content from websites
* Index web pages for Knowledge Graph queries
* Process single pages or entire sub-pages
* Monitor the status of URL processing
* Exclude specific URLs from processing

## Add URLs to a Knowledge Graph

To add web connector URLs to your Knowledge Graph, use the [PUT endpoint](/api-reference/kg-api/update-graph) to update the graph with the URLs you want to process. This endpoint allows you to add, update, or remove URLs from your Knowledge Graph.

<Warning>
  You can only add URLs to a Knowledge Graph with the `type` set to `web`. To create a Knowledge Graph with the `web` type, you must create the Knowledge Graph in [AI Studio](https://app.writer.com/ai-studio) and select "Add Website" as the way you want to add content to the Knowledge Graph. See [Setting up Knowledge Graph web connectors](https://support.writer.com/article/272-setting-up-knowledge-graph-web-connectors) for more information.

  You can see the type of a Knowledge Graph in the [Knowledge Graph details](/api-reference/kg-api/retrieve-graph) or in the [Knowledge Graph list](/api-reference/kg-api/list-graphs) endpoints.
</Warning>

<CodeGroup>
  ```bash cURL theme={null}
  # Note that this operation replaces the entire list of URLs attached to the Knowledge Graph.
  curl --location --request PUT 'https://api.writer.com/v1/graphs/{graph_id}' \
      --header 'Content-Type: application/json' \
      --header "Authorization: Bearer $WRITER_API_KEY" \
      --data '{
          "urls": [
              {
                  "url": "https://example.com/documentation",
                  "type": "sub_pages",
                  "exclude_urls": [
                      "https://example.com/documentation/admin",
                      "https://example.com/documentation/private"
                  ]
              }
          ]
      }'
  ```

  ```python python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  # Note that this operation replaces the entire list of URLs attached to the Knowledge Graph with the new list of URLs.
  client.graphs.update(
      "GRAPH_ID",
      urls=[{
          "url": "https://example.com/documentation",
          "type": "sub_pages",
          "exclude_urls": [
              "https://example.com/documentation/admin",
              "https://example.com/documentation/private"
          ]
      }]
  )

  print(client.graphs.retrieve("GRAPH_ID").urls)
  ```

  ```javascript javascript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  // Note that this operation replaces the entire list of URLs attached to the Knowledge Graph with the new list of URLs.
  const response = await client.graphs.update('GRAPH_ID', {
    urls: [{
      url: 'https://example.com/documentation',
      type: 'sub_pages',
      exclude_urls: [
        'https://example.com/documentation/admin',
        'https://example.com/documentation/private'
      ]
    }]
  });

  console.log(response.urls);
  ```
</CodeGroup>

### Request structure

<Warning>
  The `urls` array in your request **replaces** the entire existing list of URLs attached to the Knowledge Graph. To add a new URL, include both the existing URLs and the new one in your request. To remove a URL, send a request with all URLs except the one you want to remove.
</Warning>

When updating a Knowledge Graph with URLs, you need to provide a `urls` array in your request body. Each URL object has the following parameters:

| Parameter      | Type   | Description                                                                                                      |
| -------------- | ------ | ---------------------------------------------------------------------------------------------------------------- |
| `url`          | string | The URL you want to add to your Knowledge Graph                                                                  |
| `type`         | string | How you want to process the URL: either `single_page` (just this URL) or `sub_pages` (this URL and linked pages) |
| `exclude_urls` | array  | Optional. Any URLs you want to exclude from processing if `type` is `sub_pages`                                  |

### Response structure

After you update the Knowledge Graph, you see the status of each URL in the `status` object. The `status` object has the following parameters:

| Parameter    | Type   | Description                                                        |
| ------------ | ------ | ------------------------------------------------------------------ |
| `status`     | string | The current processing status: `validating`, `success`, or `error` |
| `error_type` | string | If there was an error, what type of error occurred                 |

```json  theme={null}
{
  "id": "51b058d8",
  "created_at": "2025-07-16T20:19:23.565884Z",
  "name": "Public docs",
  "description": "Public docs",
  "urls": [
    {
      "url": "https://example.com/docs",
      "status": {
        "status": "validating",
        "error_type": null
      },
      "exclude_urls": [
        "https://example.com/docs/admin",
        "https://example.com/docs/private"
      ],
      "type": "sub_pages"
    }
  ]
}
```

#### Possible error types

If URL processing fails, you may see these error types:

* `invalid_url`: The URL format is not valid
* `not_searchable`: The content cannot be accessed or processed
* `not_found`: The URL returns a 404 error
* `paywall_or_login_page`: The content requires authentication
* `unexpected_error`: An unspecified error occurred

## Usage examples

The following examples show how to add a web connector URL to a Knowledge Graph and monitor its processing status.

### Add a web connector URL

This example adds a web connector URL to a Knowledge Graph. It first retrieves the Knowledge Graph to see the current URLs and then adds a new URL to the Knowledge Graph. Note that this operation replaces the entire list of URLs attached to the Knowledge Graph, which is why it is important to retrieve the existing list of URLs first.

<CodeGroup>
  ```bash cURL theme={null}
  # 1. First, retrieve the current Knowledge Graph to see existing URLs
  curl --location 'https://api.writer.com/v1/graphs/{graph_id}' \
      --header "Authorization: Bearer $WRITER_API_KEY"

  # 2. Then, send a new request with all the URLs you want to add. In this example, there were no existing URLs, so it's adding a single URL.
  curl --location --request PUT 'https://api.writer.com/v1/graphs/{graph_id}' \
      --header 'Content-Type: application/json' \
      --header "Authorization: Bearer $WRITER_API_KEY" \
      --data '{
          "urls": [
              {
                  "url": "https://example.com/documentation",
                  "type": "sub_pages",
                  "exclude_urls": [
                      "https://example.com/documentation/admin",
                      "https://example.com/documentation/private"
                  ]
              }
          ]
      }'
  ```

  ```python Python theme={null}

  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  graph_id = "GRAPH_ID"

  graph = client.graphs.retrieve(graph_id)
  urls = graph.urls

  urls.append({
      "url": "https://example.com/documentation",
      "type": "sub_pages",
      "exclude_urls": ["https://example.com/documentation/admin", "https://example.com/documentation/private"]
  })

  client.graphs.update(graph_id, urls=urls)

  print(client.graphs.retrieve(graph_id).urls)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const graph_id = "GRAPH_ID";

  const graph = await client.graphs.retrieve(graph_id);

  const urls = graph.urls;

  urls.push({
    url: 'https://example.com/documentation',
    type: 'sub_pages',
    exclude_urls: [
      'https://example.com/documentation/admin',
      'https://example.com/documentation/private'
    ]
  });

  const response = await client.graphs.update(graph_id, { urls });

  const updatedGraph = await client.graphs.retrieve(graph_id);

  console.log(updatedGraph.urls);
  ```
</CodeGroup>

### Delete all URLs from a Knowledge Graph

To delete all URLs from a Knowledge Graph, you can send a request with an empty `urls` array.

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request PUT 'https://api.writer.com/v1/graphs/{graph_id}' \
      --header 'Content-Type: application/json' \
      --header "Authorization: Bearer $WRITER_API_KEY" \
      --data '{
          "urls": []
      }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  graph_id = "GRAPH_ID"

  client.graphs.update(graph_id, urls=[])

  print(client.graphs.retrieve(graph_id).urls)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const graph_id = "GRAPH_ID";

  const response = await client.graphs.update(graph_id, { urls: [] });

  console.log(response.urls);
  ```
</CodeGroup>

### Monitor processing status

You can check the status of your web connector URLs by retrieving the Knowledge Graph details.

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.writer.com/v1/graphs/{graph_id}' \
      --header "Authorization: Bearer $WRITER_API_KEY"
  ```

  ```python python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  graph = client.graphs.retrieve("GRAPH_ID")
  print(graph.urls)
  ```

  ```javascript javascript theme={null}
  import Writer from 'writer-sdk';

  // Initialize the Writer client. If you don't pass the `api_key` parameter, 
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  async function main() {
    const graph = await client.graphs.retrieve('GRAPH_ID');

    console.log(graph.urls);
  }

  main();
  ```
</CodeGroup>

### Query the Knowledge Graph with web content

Once the web connector URLs have been processed successfully, you can query the Knowledge Graph to access the extracted content.

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.writer.com/v1/graphs/{graph_id}/query' \
      --header 'Content-Type: application/json' \
      --header "Authorization: Bearer $WRITER_API_KEY" \
      --data '{
          "query": "What are the main features described in the documentation?",
          "subqueries": true
      }'
  ```

  ```python python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  response = client.graphs.question(
    graph_ids=["GRAPH_ID"],
    question="YOUR QUESTION"
  )

  print(f"Answer: {response.answer}")
  print(f"Sources: {response.sources}")
  ```

  ```javascript javascript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `api_key` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const response = await client.graphs.question({
    graph_ids: ["GRAPH_ID"],
    question: "YOUR QUESTION"
  });

  console.log(`Answer: ${response.answer}`);
  console.log(`Sources: ${response.sources}`);
  ```
</CodeGroup>

## Next steps

By following this guide, you can successfully add web content to your Knowledge Graphs using web connector URLs.

Next, learn about other Knowledge Graph capabilities:

* [Query a Knowledge Graph](/home/kg-query)
* [Use a Knowledge Graph in chat](/home/kg-chat)
