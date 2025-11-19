# Source: https://dev.writer.com/home/kg-chat.md

# Use a Knowledge Graph in a chat

> Query Knowledge Graphs during chat completions with tool calling. Reference multiple graphs and configure query parameters for accurate responses.

This guide demonstrates how to send questions to a [Knowledge Graph](/home/knowledge-graph) during a [chat completion](/home/chat-completion). Knowledge Graph chat is a predefined tool you can use to reference a Knowledge Graph when users chat with a Palmyra LLM.

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

## Tool structure

Knowledge Graph chat is a predefined tool supported by Palmyra X4 and later models, to be used with tool calling in the [chat endpoint](/api-reference/completion-api/chat-completion). To use Knowledge Graph chat, add the following object to the `tools` array when calling the chat endpoint:

| Parameter               | Type    | Description                                                                                                                                                                                                                     |
| ----------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                  | string  | The type of tool. Must be `graph` for Knowledge Graph chat.                                                                                                                                                                     |
| `function`              | object  | An object containing the `graph_ids`, `description`, `subqueries`, and `query_config` parameters                                                                                                                                |
| `function.graph_ids`    | array   | An array of strings containing the graph IDs you wish to reference                                                                                                                                                              |
| `function.description`  | string  | A description of the graphs you are referencing. This helps the model understand when to use the Knowledge Graph tool in the chat. If there are multiple graphs, include a description for each, referencing the graph by name. |
| `function.subqueries`   | Boolean | A Boolean indicating whether to include the subqueries used by Palmyra in the response.                                                                                                                                         |
| `function.query_config` | object  | Configuration options for Knowledge Graph queries. See the [Query configuration parameters](#query-configuration-parameters) below.                                                                                             |

### Query configuration parameters

| Parameter            | Type    | Range              | Default | Description                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------- | ------- | ------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `max_subquestions`   | integer | 1-10               | 6       | Maximum number of sub-questions to generate when processing complex queries.                                                                                                                                                                                                                                                                                                     |
| `search_weight`      | integer | 0-100              | 50      | Controls the balance between keyword and semantic search in ranking results.                                                                                                                                                                                                                                                                                                     |
| `grounding_level`    | number  | 0.0-1.0            | 0.0     | Controls how closely responses must match to source material.                                                                                                                                                                                                                                                                                                                    |
| `max_snippets`       | integer | 5-25 (recommended) | 30      | Maximum number of text snippets to retrieve from the Knowledge Graph for context. Works in concert with `search_weight` to control best matches vs broader coverage. **Note**: While technically supports 1-60, values below 5 may return no results due to RAG implementation. Recommended range is 5-25. Due to RAG system behavior, you may see more snippets than requested. |
| `max_tokens`         | integer | 100-8000           | 4000    | Maximum number of tokens the model can generate in the response.                                                                                                                                                                                                                                                                                                                 |
| `keyword_threshold`  | number  | 0.0-1.0            | 0.7     | Threshold for keyword-based matching when searching Knowledge Graph content.                                                                                                                                                                                                                                                                                                     |
| `semantic_threshold` | number  | 0.0-1.0            | 0.7     | Threshold for semantic similarity matching when searching Knowledge Graph content. Set higher for stricter relevance, lower for broader range.                                                                                                                                                                                                                                   |
| `inline_citations`   | Boolean | true/false         | false   | Whether to include inline citations within the response text.                                                                                                                                                                                                                                                                                                                    |

For detailed explanations and usage examples, see the [Knowledge Graph query configuration guide](/home/knowledge-graph-query-config).

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.writer.com/v1/chat' \
      --header 'Content-Type: application/json' \
      --header "Authorization: Bearer $WRITER_API_KEY" \
      --data '{
          "model": "palmyra-x5",
          "messages": [
              {
                  "role": "user",
                  "content": "Which of our products contain both food coloring and chocolate?"
              }
          ],
          "tool_choice": "auto",
          "tools": [
              {
                  "type": "graph",
                  "function": {
                      "description": "Knowledge Graph containing information about Acme Inc. food products",
                      "graph_ids": [
                          "<GRAPH_ID>"
                      ],
                      "subqueries": true
                  }
              }
          ],
          "stream": true
      }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  tools = [{
      "type": "graph",
      "function": {
          "description": "Description of the graph(s)",
          "graph_ids": [
              "<GRAPH_ID>"
          ],
          "subqueries": True
      }
  }]

  messages = [{"role": "user", "content": "Which of our products contain both food coloring and chocolate?"}]

  response = client.chat.chat(
      model="palmyra-x5", 
      messages=messages, 
      tools=tools,  # The tools array defined earlier.
      tool_choice="auto",
      stream=True
  )

  for chunk in response:
      if chunk.choices[0].delta.content is not None:
          print(chunk.choices[0].delta.content, end="", flush=True)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const tools = [{
      type: "graph",
      function: {
          description: "Description of the graph(s)",
          graph_ids: [
              "<GRAPH_ID>"
          ],
          subqueries: true
      }
  }]

  let messages = [{role: "user", content: "Which of our products contain both food coloring and chocolate?"}]

  const response = await client.chat.chat({
      model: "palmyra-x5",
      messages: messages,
      tools: tools, // The tools array defined earlier.
      tool_choice: "auto",
      stream: true
  });

  for await (const chunk of response) {
      if (chunk.choices[0].delta.content) {
          process.stdout.write(chunk.choices[0].delta.content);
      }
  }
  ```
</CodeGroup>

<Note>
  You can only pass one prebuilt tool in the `tools` array at a time. However, you can pass multiple [custom tools](/home/tool-calling) in the same request.

  Prebuilt tools are:

  * Knowledge Graph tool
  * [LLM tool](/home/model-delegation)
  * [Translation tool](/home/translation-tool)
  * [Vision tool](/home/vision-tool)
</Note>

### Response format

When a chat completion uses the Knowledge Graph tool, the response from the Knowledge Graph tool is in the `graph_data` object. That object contains the following fields:

| Parameter            | Type   | Description                                                                                                |
| -------------------- | ------ | ---------------------------------------------------------------------------------------------------------- |
| `sources`            | array  | An array of objects containing the source file IDs and snippets that helped the model answer the question. |
| `sources.file_id`    | string | The ID of the source file.                                                                                 |
| `sources.snippet`    | string | A snippet from the source file that helped the model answer the question.                                  |
| `status`             | string | The status of the query.                                                                                   |
| `subqueries`         | array  | An array of objects containing the subqueries used by Palmyra in the response.                             |
| `subqueries.query`   | string | The query used by Palmyra to answer the question.                                                          |
| `subqueries.answer`  | string | The answer to the question.                                                                                |
| `subqueries.sources` | array  | An array of objects containing the source file IDs and snippets that helped the model answer the question. |

The full response has the following structure.

The subqueries and sources shown are abbreviated for readability. If the `subqueries` parameter is `false`, or if the model doesn't need subqueries to answer the question, this array is be empty.

<CodeGroup>
  ```json streaming response [expandable] {12} theme={null}
  {
      "id": "1234",
      "object": "chat.completion.chunk",
      "choices": [
          {
              "index": 0,
              "finish_reason": "stop",
              "delta": {
                  "content": "None of our products contain both chocolate and food coloring. The products containing chocolate are different from those containing food coloring.",
                  "role": "assistant",
                  "tool_calls": null,
                  "graph_data": {
                      "sources": [
                          {
                              "file_id": "1234",
                              "snippet": "with cocoa for an extra touch of chocolate…"
                          },
                          {
                              "file_id": "5678",
                              "snippet": "Sugar, corn syrup, artificial flavors, food coloring…"
                          }
                      ],
                      "status": "finished",
                      "subqueries": [
                          {
                              "query": "Which of our products contain food coloring?",
                              "answer": "The products that contain food coloring are...",
                              "sources": [
                                  {
                                      "file_id": "1234",
                                      "snippet": "Sugar, citric acid, artificial flavors…"
                                  },
                                  {
                                      "file_id": "5678",
                                      "snippet": "Coffee, coconut milk, ice"
                                  }
                              ]
                          },
                          {
                              "query": "Which of our products contain chocolate?",
                              "answer": "Several products contain chocolate. These include…",
                              "sources": [
                                  {
                                      "file_id": "1234",
                                      "snippet": "with cocoa for an extra touch of chocolate…"
                                  }
                              ]
                          }
                      ]
                  }
              },
          }
      ]
      // Other fields omitted for brevity    
  }
  ```

  ```json non-streaming response [expandable] {12} theme={null}
  {
      "id": "1234",
      "object": "chat.completion",
      "choices": [
          {
              "index": 0,
              "finish_reason": "stop",
              "message": {
                  "content": "None of our products contain both chocolate and food coloring. The products containing chocolate are different from those containing food coloring.",
                  "role": "assistant",
                  "tool_calls": null,
                  "graph_data": {
                      "sources": [
                          {
                              "file_id": "1234",
                              "snippet": "with cocoa for an extra touch of chocolate…"
                          },
                          {
                              "file_id": "5678",
                              "snippet": "Sugar, corn syrup, artificial flavors, food coloring…"
                          }
                      ],
                      "status": "finished",
                      "subqueries": [
                          {
                              "query": "Which of our products contain food coloring?",
                              "answer": "The products that contain food coloring are...",
                              "sources": [
                                  {
                                      "file_id": "1234",
                                      "snippet": "Sugar, citric acid, artificial flavors…"
                                  },
                                  {
                                      "file_id": "5678",
                                      "snippet": "Coffee, coconut milk, ice"
                                  }
                              ]
                          },
                          {
                              "query": "Which of our products contain chocolate?",
                              "answer": "Several products contain chocolate. These include…",
                              "sources": [
                                  {
                                      "file_id": "1234",
                                      "snippet": "with cocoa for an extra touch of chocolate…"
                                  }
                              ]
                          }
                      ]
                  }
              },
          }
      ]
      // Other fields omitted for brevity    
  }
  ```
</CodeGroup>

## Usage example

The following example uses a hypothetical product information Knowledge Graph to answer a question about which food products contain both food coloring and chocolate.

### Create the tools array

First, define the `tools` array with the `type` set to `graph`. The `function` object contains the `graph_ids`, `description`, and `subqueries` parameters.

In this example, the subqueries are included in the response. Subqueries can be useful for debugging or for providing additional context to the user about how the model arrived at the answer.

<CodeGroup>
  ```bash cURL theme={null}
  "tools": [
      {
          "type": "graph",
          "function": {
              "description": "Knowledge Graph containing information about Acme Inc. food products",
              "graph_ids": [
                  "<GRAPH_ID>"
              ],
              "subqueries": true
          }
      }
  ]
  ```

  ```python Python theme={null}
  tools = [{
      "type": "graph",
      "function": {
          "description": "Knowledge Graph containing information about Acme Inc. food products",
          "graph_ids": [
              "<GRAPH_ID>"
          ],
          "subqueries": True
      }
  }]
  ```

  ```javascript JavaScript theme={null}
  const tools = [{
      type: "graph",
      function: {
          description: "Knowledge Graph containing information about Acme Inc. food products",
          graph_ids: [
              "<GRAPH_ID>"
          ],
          subqueries: true
      }
  }]
  ```
</CodeGroup>

### Send the request

Add the tools array to the chat endpoint call along with your array of messages. Setting `tool_choice` to `auto` allows the model to choose when to use the Knowledge Graph tool, based on the user's question and the description of the tool.

This example streams the response in real-time as the model generates it.

If you are unfamiliar with the chat completions endpoint or streaming vs. non-streaming responses, learn more in the [chat completion guide](/home/chat-completion).

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.writer.com/v1/chat' \
      --header 'Content-Type: application/json' \
      --header "Authorization: Bearer $WRITER_API_KEY" \
      --data '{
          "model": "palmyra-x5",
          "messages": [
              {
                  "role": "user",
                  "content": "Which of our products contain both food coloring and chocolate?"
              }
          ],
          "tool_choice": "auto",
          "tools": [
              {
                  "type": "graph",
                  "function": {
                      "description": "Knowledge Graph containing information about Acme Inc. food products",
                      "graph_ids": [
                          "<GRAPH_ID>"
                      ],
                      "subqueries": true
                  }
              }
          ],
          "stream": true
      }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  tools = [{
      "type": "graph",
      "function": {
          "description": "Knowledge Graph containing information about Acme Inc. food products",
          "graph_ids": [
              "<GRAPH_ID>"
          ],
          "subqueries": True
      }
  }]

  messages = [{"role": "user", "content": "Which of our products contain both food coloring and chocolate?"}]

  response = client.chat.chat(
      model="palmyra-x5", 
      messages=messages, 
      tools=tools,  # The tools array defined earlier.
      tool_choice="auto",
      stream=True
  )

  for chunk in response:
      if chunk.choices[0].delta.content is not None:
          print(chunk.choices[0].delta.content, end="", flush=True)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const tools = [{
      type: "graph",
      function: {
          description: "Knowledge Graph containing information about Acme Inc. food products",
          graph_ids: [
              "<GRAPH_ID>"
          ],
          subqueries: true
      }
  }]

  let messages = [{role: "user", content: "Which of our products contain both food coloring and chocolate?"}]

  const response = await client.chat.chat({
      model: "palmyra-x5", 
      messages: messages, 
      tools: tools, // The tools array defined earlier.
      tool_choice: "auto",
      stream: true 
  });

  for await (const chunk of response) {
      if (chunk.choices[0].delta.content) {
          process.stdout.write(chunk.choices[0].delta.content);
      }
  }
  ```
</CodeGroup>

### Display Knowledge Graph subqueries and sources

You may want to display the `sources` or `subqueries` in your UI to assist your user in understanding how the model derived the answer to the question. The following example shows how to display the subqueries as well as the status of the query from the Knowledge Graph.

<CodeGroup>
  ```python Python theme={null}
  from writerai import Writer

  # Initialize the client.
  client = Writer()

  tools = [{
      "type": "graph",
      "function": {
          "description": "Knowledge Graph containing information about Acme Inc. food products",
          "graph_ids": [
              "<GRAPH_ID>"
          ],
          "subqueries": True
      }
  }]

  messages = [{"role": "user", "content": "Which of our products contain both food coloring and chocolate?"}]

  response = client.chat.chat(
      model="palmyra-x5",
      messages=messages,
      tools=tools,
      tool_choice="auto",
      stream=True
  )

  for chunk in response:
      if chunk.choices[0].delta.content is not None:
          print(chunk.choices[0].delta.content, end="", flush=True)

      if chunk.choices[0].delta.graph_data is not None:
          if chunk.choices[0].delta.graph_data.status is not None:
              print(f"Query status: {chunk.choices[0].delta.graph_data.status}")
          if chunk.choices[0].delta.graph_data.subqueries:
              print(f"Subquery: {chunk.choices[0].delta.graph_data.subqueries[0].query}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the client.
  const client = new Writer();

  const tools = [{
      type: "graph",
      function: {
          description: "Knowledge Graph containing information about Acme Inc. food products",
          graph_ids: [
              "<GRAPH_ID>"
          ],
          subqueries: true
      }
  }]

  let messages = [{role: "user", content: "Which of our products contain both food coloring and chocolate?"}]

  const response = await client.chat.chat({
      model: "palmyra-x5", 
      messages: messages, 
      tools: tools, // The tools array defined earlier.
      tool_choice: "auto",
      stream: true 
  });

  for await (const chunk of response) {
      if (chunk.choices[0].delta.content) {
          console.log(chunk.choices[0].delta.content);
      }

      if (chunk.choices[0].delta.graph_data) {
          if (chunk.choices[0].delta.graph_data.status) {
              console.log(`Query status: ${chunk.choices[0].delta.graph_data.status}`);
          }
          if (chunk.choices[0].delta.graph_data.subqueries && 
              chunk.choices[0].delta.graph_data.subqueries.length > 0 &&
              chunk.choices[0].delta.graph_data.subqueries[0].query) {
              console.log(`Subquery: ${chunk.choices[0].delta.graph_data.subqueries[0].query}`);
          }
      }
  }
  ```
</CodeGroup>

### Customize query behavior

You can fine-tune how your Knowledge Graph searches and retrieves content using the `query_config` parameter. Learn about all available configuration options in the [Knowledge Graph query configuration guide](/home/knowledge-graph-query-config).

## Next steps

By following this guide, you can reference Knowledge Graphs in your users' chats in your application.

Next, learn about other prebuilt tools you can use in your chat applications:

* [Analyze images](/home/vision-tool)
* [Pass questions to a domain-specific LLM](/home/model-delegation)
* [Translate text](/home/translation-tool)
