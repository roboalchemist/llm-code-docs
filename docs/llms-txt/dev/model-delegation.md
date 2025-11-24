# Source: https://dev.writer.com/home/model-delegation.md

# Use another LLM as a tool

With model delegation, you can use another Writer model as a tool in a [chat completion](/home/chat-completion) with Palmyra X4 and later models. The predefined LLM tool allows you to delegate specific tasks to domain-specific Writer models, such as `palmyra-fin`, `palmyra-med`, or `palmyra-creative`.

For example, in a chat application using Palmyra X5, you can delegate financial analysis tasks to the `palmyra-fin` model.

This guide helps you understand how to perform model delegation using the Writer API.

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

## Tool structure

Use the LLM tool to delegate specific tasks to another model when using the [chat endpoint](/api-reference/completion-api/chat-completion). Using [tool calling](/home/tool-calling), you can specify the Writer model you want to use for a given task. When the primary chat model calls the LLM tool based on the user's input, it signals it in the chat API response.

To use the LLM tool, add it to the `tools` array in your `chat-completion` endpoint request.

The LLM tool object has the following structure:

| Parameter              | Type     | Description                                                         |
| ---------------------- | -------- | ------------------------------------------------------------------- |
| `type`                 | `string` | The type of tool, which is `llm` for LLM tool                       |
| `function`             | `object` | An object containing the tool's description and model               |
| `function.description` | `string` | A description of what the model will be used for.                   |
| `function.model`       | `string` | The [ID of the Writer model](/home/models) to be used for this tool |

<Note>
  To help the model understand when to use the tool, follow these best practices for the `function.description` parameter:

  * Indicate that the tool is a function that invokes an LLM
  * Specify the model's purpose and capabilities
  * Describe when the tool should be used

  An example description for a tool using the `palmyra-med` model:

  > "A function that invokes the LLM identified by the given model, specialized in answering medical queries. Any user request asking for medical advice should use this tool."
</Note>

<CodeGroup>
  ```bash cURL theme={null}
  "tools": [
      {
          "type": "llm",
          "function": {
              "description": "A function that will invoke the llm identified by the given model, specialized for financial analysis and reporting. Any user request asking for financial analysis should use this tool.",
              "model": "palmyra-fin"
          }
      }  
  ]
  ```

  ```python Python theme={null}
  tools = [{
      "type": "llm",
      "function": {
          "description": "A function that will invoke the llm identified by the given model, specialized for financial analysis and reporting. Any user request asking for financial analysis should use this tool.",
          "model": "palmyra-fin"
      }
  }]
  ```

  ```js JavaScript theme={null}
  const tools = [{
      type: "llm",
      function: {
          description: "A function that will invoke the llm identified by the given model, specialized for financial analysis and reporting. Any user request asking for financial analysis should use this tool.",
          model: "palmyra-fin"
      }
  }]
  ```
</CodeGroup>

<Note>
  You can only pass one prebuilt tool in the `tools` array at a time. However, you can pass multiple [custom tools](/home/tool-calling) in the same request.

  Prebuilt tools are:

  * LLM tool
  * [Vision tool](/home/vision-tool)
  * [Knowledge Graph tool](/home/kg-chat)
  * [Translation tool](/home/translation-tool)
</Note>

### Response format

When a chat completion uses the LLM tool, the response from the LLM tool is in the `llm_data` object. The `llm_data` object contains the following fields:

| Parameter | Type   | Description                                      |
| --------- | ------ | ------------------------------------------------ |
| `prompt`  | string | The prompt used by the LLM tool.                 |
| `model`   | string | The ID of the Writer model used by the LLM tool. |

Below is an example of the full response to a chat completion request that uses the LLM tool with `palmyra-med`.

<CodeGroup>
  ```json non-streaming response [expandable] {17} theme={null}
  {
    "id": "1234",
    "object": "chat.completion",
    "choices": [
      {
        "index": 0,
        "finish_reason": "stop",
        "message": {
          "content": "The recommended daily intake of calcium for a 30-year-old woman is 1,000 mg per day.",
          "role": "assistant",
          "tool_calls": null,
          "graph_data": {
            "sources": null,
            "status": null,
            "subqueries": null
          },
          "llm_data": {
            "prompt": "What is the recommended daily intake of calcium for a 30-year-old woman?",
            "model": "palmyra-med"
          },
          "image_data": null,
          "refusal": null
        },
        "logprobs": null
      }
    ],
    "created": 1741970653,
    "model": "palmyra-x5",
    "usage": {
      "prompt_tokens": 259,
      "total_tokens": 305,
      "completion_tokens": 46,
      "prompt_token_details": null,
      "completion_tokens_details": null
    },
    "system_fingerprint": "v1",
    "service_tier": null
  }
  ```

  ```json streaming response [expandable] {16} theme={null}
  {
      "id": "1234",
      "object": "chat.completion.chunk",
      "choices": [{
          "index": 0,
          "finish_reason": None,
          "message": {
              "content": "The",
              "role": "assistant",
              "tool_calls": None,
              "graph_data": {
                  "sources": None,
                  "status": None,
                  "subqueries": None
              },
              "llm_data": {
                  "prompt": "What is the recommended daily intake of calcium for a 30-year-old woman?",
                  "model": "palmyra-med"
              },
              "image_data": None,
              "refusal": None
          },
          "logprobs": None,
      "delta": {
          "content": "The",
          "role": "assistant",
          "tool_calls": None,
          "graph_data": {
              "sources": None,
              "status": None,
              "subqueries": None
          },
          "llm_data": {
              "prompt": "What is the recommended daily intake of calcium for a 30-year-old woman?",
              "model": "palmyra-med"
          },
          "image_data": None,
          "refusal": None
      },
      "logprobs": None
      }],
      "created": 1741970696,
      "model": "palmyra-x5",
      "usage": None,
      "system_fingerprint": "v1",
      "service_tier": None
  }
  ```
</CodeGroup>

## Usage example

Here's an example of how to use the LLM tool in your application. This example specifically delegates medical questions to the `palmyra-med` model.

### Create a tools array containing an LLM tool

To use the LLM tool, create a `tools` array that specifies the Writer model you want to use.

<CodeGroup>
  ```bash cURL theme={null}
  "tools": [
      {
          "type": "llm",
          "function": {
              "description": "A function that will invoke the llm identified by the given model, specialized in answering medical queries. Any user request asking for medical advice should use this tool.",
              "model": "palmyra-med"
          }
      }
  ]
  ```

  ```python Python theme={null}
  tools = [{
      "type": "llm",
      "function": {
          "description": "A function that will invoke the llm identified by the given model, specialized in answering medical queries. Any user request asking for medical advice should use this tool.",
          "model": "palmyra-med"
      }
  }]
  ```

  ```js JavaScript theme={null}
  const tools = [{
      type: "llm",
      function: {
          description: "A function that will invoke the llm identified by the given model, specialized in answering medical queries. Any user request asking for medical advice should use this tool.",
          model: "palmyra-med"
      }
  }]
  ```
</CodeGroup>

### Send the request using chat completions

Add the tools array to the chat endpoint call along with your array of messages. Setting `tool_choice` to `auto` allows the model to choose when to use the LLM tool, based on the user's question and the description of the tool.

This example streams the response as the model generates it.

If you are unfamiliar with the chat completions endpoint or streaming vs. non-streaming responses, learn more in the [chat completion guide](/home/chat-completion).

<CodeGroup>
  ```bash cURL theme={null}
  curl --location 'https://api.writer.com/v1/chat' \
      --header 'Content-Type: application/json' \
      --header "Authorization: Bearer $WRITER_API_KEY" \
      --data '{
          "model": "palmyra-x5",
          "temperature": 0.7,
          "messages": [
              {
                  "role": "user",
                  "content": "What is the recommended daily intake of calcium for a 30-year-old woman?"
              }
          ],
          "tool_choice": "auto",
          "tools": [
              {
                  "type": "llm",
                  "function": {
                      "description": "A function that will invoke the llm identified by the given model, specialized in answering medical queries. Any user request asking for medical advice should use this tool.",
                      "model": "palmyra-med"
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

  messages = [{"role": "user", "content": "What is the recommended daily intake of calcium for a 30-year-old woman?"}]

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

  ```js JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const messages = [{role: "user", content: "What is the recommended daily intake of calcium for a 30-year-old woman?"}];

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

By following this guide, you can use specialized, fine-tuned Writer models for specific tasks within your chat applications.

## Next steps

Learn about other prebuilt tools you can use in your chat applications:

* [Analyze images](/home/vision-tool)
* [Pass questions to a Knowledge Graph](/home/kg-chat)
* [Translate text](/home/translation-tool)
