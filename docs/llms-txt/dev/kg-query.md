# Source: https://dev.writer.com/home/kg-query.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ask questions to Knowledge Graphs

The Knowledge Graph [question endpoint](/api-reference/kg-api/question) allows you to ask questions directly to one or more Knowledge Graphs. This provides a direct way to query your Knowledge Graphs without needing to use chat completions. You can also enable subqueries to break down complex questions into smaller subqueries and provide answers for each one.

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

## Question endpoint

**Endpoint:** `POST /v1/graphs/question`

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request POST https://api.writer.com/v1/graphs/question \
    --header "Authorization: Bearer $WRITER_API_KEY" \
    --header "Content-Type: application/json" \
    --data-raw '{
      "graph_ids": ["<GRAPH_ID>"],
      "question": "<QUESTION>"
    }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  response = client.graphs.question(
    graph_ids=["<GRAPH_ID>"],
    question="<QUESTION>"
  )

  print(f"Answer: {response.answer}")
  print(f"Sources: {response.sources}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `api_key` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const response = await client.graphs.question({
    graph_ids: ["<GRAPH_ID>"],
    question: "<QUESTION>"
  });

  console.log(`Answer: ${response.answer}`);
  console.log(`Sources: ${response.sources}`);
  ```
</CodeGroup>

### Request body

<Tip>
  To find the ID of your Knowledge Graph, you can:

  * Call the [Knowledge Graph list endpoint](/api-reference/kg-api/list-graphs) to get the list of all your Knowledge Graphs with their IDs
  * Find the ID in the URL of the Knowledge Graph page in [AI Studio](https://app.writer.com/aistudio)
</Tip>

The request body is a JSON object with the following fields:

| Parameter      | Type           | Required | Description                                                                                                                                                                                                                            |
| -------------- | -------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `graph_ids`    | array\[string] | Yes      | The unique identifiers of the Knowledge Graphs to query. You can specify multiple Knowledge Graph IDs to search across multiple graphs.                                                                                                |
| `question`     | string         | Yes      | The question to answer using the Knowledge Graph.                                                                                                                                                                                      |
| `subqueries`   | Boolean        | No       | Specify whether to include subqueries. Defaults to `false`.                                                                                                                                                                            |
| `stream`       | Boolean        | No       | Determines whether to stream the response. If `true`, the output is sent as it is generated, which can be useful for real-time applications. Defaults to `false`. See how to [handle streaming responses](#stream-the-response) below. |
| `query_config` | object         | No       | Configuration options for Knowledge Graph queries. See [Query configuration parameters](#query-configuration-parameters) below for detailed parameter descriptions.                                                                    |

### Query configuration parameters

| Parameter            | Type    | Range              | Default | Description                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------- | ------- | ------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `max_subquestions`   | integer | 1-10               | 6       | Maximum number of sub-questions to generate when processing complex queries.                                                                                                                                                                                                                                                                                                     |
| `search_weight`      | integer | 0-100              | 50      | Controls the balance between keyword and semantic search in ranking results.                                                                                                                                                                                                                                                                                                     |
| `grounding_level`    | number  | 0.0-1.0            | 0.0     | Controls how closely responses must match to source material. Set lower for grounded outputs, higher for creativity.                                                                                                                                                                                                                                                             |
| `max_snippets`       | integer | 5-25 (recommended) | 30      | Maximum number of text snippets to retrieve from the Knowledge Graph for context. Works in concert with `search_weight` to control best matches vs broader coverage. **Note**: While technically supports 1-60, values below 5 may return no results due to RAG implementation. Recommended range is 5-25. Due to RAG system behavior, you may see more snippets than requested. |
| `max_tokens`         | integer | 100-8000           | 4000    | Maximum number of tokens the model can generate in the response.                                                                                                                                                                                                                                                                                                                 |
| `keyword_threshold`  | number  | 0.0-1.0            | 0.7     | Threshold for keyword-based matching when searching Knowledge Graph content.                                                                                                                                                                                                                                                                                                     |
| `semantic_threshold` | number  | 0.0-1.0            | 0.7     | Threshold for semantic similarity matching when searching Knowledge Graph content. Set higher for stricter relevance, lower for broader range.                                                                                                                                                                                                                                   |
| `inline_citations`   | Boolean | true/false         | false   | Whether to include inline citations within the response text.                                                                                                                                                                                                                                                                                                                    |

For detailed explanations and usage examples, see the [Knowledge Graph query configuration guide](/home/knowledge-graph-query-config).

### Response format

The response is a JSON object with the following fields:

| Parameter              | Type   | Description                                                                                                 |
| ---------------------- | ------ | ----------------------------------------------------------------------------------------------------------- |
| `question`             | string | The question you asked.                                                                                     |
| `answer`               | string | The answer to the question based on the Knowledge Graph content.                                            |
| `sources`              | array  | An array of source objects that contain the file information and text snippets used to generate the answer. |
| `sources[].file_id`    | string | If the source is a file, this is the unique identifier of the file that contains the source information.    |
| `sources[].snippet`    | string | If the source is a file, this is a snippet of text from the source file used to answer the question.        |
| `subqueries`           | array  | An array of subquery objects. Only included if `subqueries` is `true`.                                      |
| `subqueries[].query`   | string | The subquery the model generated to answer the question.                                                    |
| `subqueries[].answer`  | string | The answer to the subquery.                                                                                 |
| `subqueries[].sources` | array  | An array of source objects for the subquery.                                                                |

<Tabs>
  <Tab title="Non-streaming response">
    ```json  theme={null}
    {
      "question": "What was our company's revenue growth in Q4 2023?",
      "answer": "The company achieved 23% year-over-year revenue growth in Q4 2023, reaching $142 million in total revenue.",
      "sources": [
        {
          "file_id": "1234",
          "snippet": "In the fourth quarter of 2023, we saw strong performance with revenue reaching $142 million, representing a 23% increase compared to Q4 2022."
        }
      ]
    }
    ```
  </Tab>

  <Tab title="Streaming response">
    ```json  theme={null}
    data: {
        "question": "What was our company's revenue growth in Q4 2023?",
        "answer": "The",
        "sources": [],
        "subqueries": null,
        "references": null
    }
    ```
  </Tab>
</Tabs>

## Examples

### Query multiple knowledge graphs

You can query multiple Knowledge Graphs at once by providing multiple graph IDs in the `graph_ids` array.

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request POST https://api.writer.com/v1/graphs/question \
    --header "Authorization: Bearer $WRITER_API_KEY" \
    --header "Content-Type: application/json" \
    --data-raw '{
      "graph_ids": [
        "<GRAPH_ID_1>",
        "<GRAPH_ID_2>"
      ],
      "question": "What are the key findings from our research documents?"
    }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  client = Writer()

  response = client.graphs.question(
    graph_ids=[
      "<GRAPH_ID_1>",
      "<GRAPH_ID_2>"
    ],
    question="What are the key findings from our research documents?"
  )

  print(f"Answer: {response.answer}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  const client = new Writer();

  const response = await client.graphs.question({
    graph_ids: [
      "<GRAPH_ID_1>",
      "<GRAPH_ID_2>"
    ],
    question: "What are the key findings from our research documents?"
  });

  console.log(`Answer: ${response.answer}`);
  ```
</CodeGroup>

### Enable subqueries

When you enable subqueries, the model breaks down complex questions into smaller subqueries and provides answers for each one from the Knowledge Graphs.

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request POST https://api.writer.com/v1/graphs/question \
    --header "Authorization: Bearer $WRITER_API_KEY" \
    --header "Content-Type: application/json" \
    --data-raw '{
      "graph_ids": ["<GRAPH_ID>"],
      "question": "What are the main products and their market performance?",
      "subqueries": true
    }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  client = Writer()

  response = client.graphs.question(
    graph_ids=["<GRAPH_ID>"],
    question="What are the main products and their market performance?",
    subqueries=True
  )

  print(f"Main answer: {response.answer}")
  for subquery in response.subqueries:
      print(f"Subquery: {subquery.query}")
      print(f"Answer: {subquery.answer}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  const client = new Writer();

  const response = await client.graphs.question({
    graph_ids: ["<GRAPH_ID>"],
    question: "What are the main products and their market performance?",
    subqueries: true
  });

  console.log(`Main answer: ${response.answer}`);
  response.subqueries.forEach(subquery => {
      console.log(`Subquery: ${subquery.query}`);
      console.log(`Answer: ${subquery.answer}`);
  });
  ```
</CodeGroup>

### Stream the response

You can stream the response from the Knowledge Graphs by setting the `stream` parameter to `true`. This is useful for real-time applications that need to see the response as it is generated.

<CodeGroup>
  ```bash cURL theme={null}
  curl --location --request POST https://api.writer.com/v1/graphs/question \
    --header "Authorization: Bearer $WRITER_API_KEY" \
    --header "Content-Type: application/json" \
    --data-raw '{
      "graph_ids": ["<GRAPH_ID>"],
      "question": "<QUESTION>",
      "stream": true
    }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  client = Writer()

  response = client.graphs.question(
    graph_ids=["<GRAPH_ID>"],
    question="<QUESTION>",
    stream=True
  )

  for chunk in response:
      print(chunk.answer, end="", flush=True)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  const client = new Writer();

  const response = await client.graphs.question({
    graph_ids: ["<GRAPH_ID>"],
    question: "<QUESTION>",
    stream: true
  });

  for await (const chunk of response) {
      process.stdout.write(chunk.answer);
  }
  ```
</CodeGroup>

## Next steps

* Learn how to [create and manage Knowledge Graphs](/home/knowledge-graph)
* Use Knowledge Graphs in chat completions with [tool calling](/home/kg-chat)
* Explore [Knowledge Graph API reference](/api-reference/kg-api)
