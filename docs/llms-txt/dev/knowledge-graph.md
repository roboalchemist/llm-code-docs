# Source: https://dev.writer.com/home/knowledge-graph.md

# Create and manage a Knowledge Graph

> Integrate graph-based RAG into your agents with Knowledge Graph API. Achieve higher accuracy than traditional vector-based retrieval methods.

Knowledge Graph, our graph-based retrieval-augmented generation (RAG), achieves [higher accuracy](https://arxiv.org/abs/2405.02048) than traditional RAG approaches that use vector retrieval.

This guide will help you understand and use the [Knowledge Graph API](/api-reference/kg-api) to integrate RAG capabilities into your agents.

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

## Create a Knowledge Graph

A Knowledge Graph is a collection of files that are used to answer questions. To start working with a Knowledge Graph, create an empty Knowledge Graph that you can add files to.

**Endpoint**: `POST https://api.writer.com/v1/graphs`

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request POST https://api.writer.com/v1/graphs \
    --header "Authorization: Bearer $WRITER_API_KEY" \
    --header "Content-Type: application/json" \
    --data-raw '{
      "name": "Financial Reports",
      "description": "Knowledge Graph of 2024 financial reports"
      }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  graph_create_response = client.graphs.create(
      name="Financial Reports",
      description="Knowledge Graph of 2024 financial reports"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `api_key` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const graphCreateResponse = await client.graphs.create({
    name: "Financial Reports",
    description: "Knowledge Graph of 2024 financial reports"
  });
  ```
</CodeGroup>

### Request body

The request body is a JSON object that contains the following fields:

| Parameter     | Type   | Description                                                                                                                                             |
| ------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`        | string | The name of the Knowledge Graph.                                                                                                                        |
| `description` | string | The description of the Knowledge Graph. The description should help the model understand the purpose of the Knowledge Graph and when it should be used. |

### Response format

The response has the following structure:

| Parameter     | Type   | Description                                        |
| ------------- | ------ | -------------------------------------------------- |
| `id`          | string | The ID of the Knowledge Graph.                     |
| `created_at`  | string | The date and time the Knowledge Graph was created. |
| `name`        | string | The name of the Knowledge Graph.                   |
| `description` | string | The description of the Knowledge Graph.            |

```json  theme={null}
{
  "id": "6029b226-1ee0-4239-a1b0-cdeebfa3ad5a",
  "created_at": "2024-06-24T12:34:56Z",
  "name": "Financial Reports",
  "description": "Knowledge Graph of 2024 financial reports"
}
```

## Add a file to a Knowledge Graph

Once you've created a Knowledge Graph, you can add files to it. The files you add to a Knowledge Graph are used to answer questions and enhance the accuracy of the responses from the LLM

You must upload the file to the Writer API before adding it to a Knowledge Graph. See [Manage files](/home/files) for more information about how to upload files.

**Endpoint**: `POST /v1/graphs/{graph_id}/file`

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request POST https://api.writer.com/v1/graphs/{graph_id}/file \
  --header "Authorization: Bearer $WRITER_API_KEY" \
  --header "Content-Type: application/json" \
  --data-raw '{"file_id":"1862f090-a281-48f3-8838-26c1e78b605e"}'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  graph_file = client.graphs.add_file_to_graph(
    graph_id="{graph_id}",
    file_id="1862f090-a281-48f3-8838-26c1e78b605e",
  )
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `api_key` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const file = await client.graphs.addFileToGraph('{graph_id}', {
    file_id: '1862f090-a281-48f3-8838-26c1e78b605e',
  });
  ```
</CodeGroup>

The response will have this structure:

```json  theme={null}
{
  "id": "1862f090-a281-48f3-8838-26c1e78b605e",
  "created_at": "2024-07-01T20:41:44.159505Z",
  "name": "test.txt",
  "graph_ids": [
    "6029b226-1ee0-4239-a1b0-cdeebfa3ad5a"
  ]
}
```

### Path parameters

| Parameter  | Description                              |
| ---------- | ---------------------------------------- |
| `graph_id` | The ID of the Knowledge Graph to update. |

### Request body

The request body is a JSON object that contains the following fields:

| Parameter | Description                                       |
| --------- | ------------------------------------------------- |
| `file_id` | The ID of the file to add to the Knowledge Graph. |

You must upload the file to the Writer API before adding it to a Knowledge Graph. See [Manage files](/home/files) for more information about how to upload files.

## Remove a file from a Knowledge Graph

**Endpoint**: `DELETE /v1/graphs/{graph_id}/file/{file_id}`

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request DELETE "https://api.writer.com/v1/graphs/{graph_id}/file/{file_id}" \
  --header "Authorization: Bearer $WRITER_API_KEY"
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  client.graphs.remove_file_from_graph(
      graph_id="{graph_id}",
      file_id="{file_id}"
  )
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `api_key` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const file = await client.graphs.removeFileFromGraph('{graph_id}', '{file_id}');
  ```
</CodeGroup>

### Path parameters

| Parameter  | Description                                            |
| ---------- | ------------------------------------------------------ |
| `graph_id` | The ID of the Knowledge Graph to update.               |
| `file_id`  | The ID of the file to remove from the Knowledge Graph. |

### Response format

The response has this structure:

```json  theme={null}
{
  "id": "1862f090-a281-48f3-8838-26c1e78b605e",
  "deleted": true
}
```

## Add URLs to a Knowledge Graph

You can add URLs to a Knowledge Graph to enhance the model's knowledge with content from websites. The LLM can then query and use this information when responding to questions.

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

See more examples in [Add URLs to a Knowledge Graph](/home/web-connector-url).

## Add a Knowledge Graph to a no-code agent

After you've created a Knowledge Graph, you can add it to a [no-code agent](/home/applications) to add RAG capabilities.

You can use this endpoint to add or remove Knowledge Graphs from a no-code agent.

**Endpoint**: `PUT /v1/applications/{application_id}/graphs`

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request PUT "https://api.writer.com/v1/applications/{application_id}/graphs" \
  --header "Authorization: Bearer $WRITER_API_KEY" \
  --header "Content-Type: application/json" \
  --data-raw '{"graph_id":"6029b226-1ee0-4239-a1b0-cdeebfa3ad5a"}'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  client.applications.graphs.update(
      application_id="{application_id}",
      graph_ids=["{graph_id}"]
  )
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `api_key` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  client.applications.graphs.update('{application_id}', ['{graph_id}']);
  ```
</CodeGroup>

### Path parameters

| Parameter        | Description                            |
| ---------------- | -------------------------------------- |
| `application_id` | The ID of the no-code agent to update. |

### Request body

The request body is a JSON object that contains the following fields:

| Parameter   | Type           | Description                                                          |
| ----------- | -------------- | -------------------------------------------------------------------- |
| `graph_ids` | array\[string] | The IDs of the Knowledge Graphs to associate with the no-code agent. |

This method updates the associated Knowledge Graphs to the exact list of IDs provided in the request.

To remove a single Knowledge Graph from the no-code agent, set the `graph_ids` parameter to an array containing the IDs of all the other Knowledge Graphs associated with the no-code agent, excluding the ID of the Knowledge Graph to remove. To remove all Knowledge Graphs from the no-code agent, set this parameter to an empty array.

### Response format

The response contains the new list of IDs of the Knowledge Graphs associated with the no-code agent.

```json  theme={null}
{
  "graph_ids": [
    "6029b226-1ee0-4239-a1b0-cdeebfa3ad5a"
  ]
}
```

## Next steps

* Learn how to ask your Knowledge Graph questions in a chat completion via [tool calling](/home/kg-chat)
* Query your Knowledge Graph directly using the [question endpoint](/home/kg-query)
* Fine-tune how your Knowledge Graph searches and retrieves content using the `query_config` parameter in the [Knowledge Graph query configuration guide](/home/knowledge-graph-query-config)
