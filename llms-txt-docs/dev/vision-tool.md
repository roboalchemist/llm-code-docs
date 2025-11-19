# Source: https://dev.writer.com/home/vision-tool.md

# Analyze images in a chat

The Vision tool for chat completions allows you to analyze images during a chat completion. You can perform actions such as extracting text, interpreting charts and graphs, performing image-based compliance checks, and more.

The Writer API also has a [`vision` endpoint](/api-reference/vision-api/analyze-images) that you can use to analyze images outside of a chat completion. See the [vision API guide](/home/analyze-images) for more information.

This guide explains how to use the Vision tool in a chat completion and provides an example of how to use it.

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

## Tool structure

The Vision tool allows you to analyze an image during a [chat with an LLM](/home/chat-completion).

To use the Vision tool, add it to the `tools` array in your `chat-completion` endpoint request.

The Vision tool object has the following structure:

| Parameter                    | Type     | Description                                                                                                                                                                                                                                                       |
| ---------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                       | `string` | The type of tool, which is `vision` for the Vision tool                                                                                                                                                                                                           |
| `function`                   | `object` | An object containing the tool's description and model                                                                                                                                                                                                             |
| `function.model`             | `string` | `palmyra-vision`                                                                                                                                                                                                                                                  |
| `function.variables`         | `array`  | An array of objects, one for each image to pass to Palmyra Vision                                                                                                                                                                                                 |
| `function.variables.name`    | `string` | The name of the image to pass to Palmyra Vision. You must use this name when referencing the image in the message you provide to the chat completion endpoint. Reference the image as `{{name}}`, where `name` is the name you provided in the `variables` array. |
| `function.variables.file_id` | `string` | The ID of the uploaded image. The maximum allowed file size is 7 MB. You must upload the image to Writer before using it with the Vision tool. Learn more in [Manage Files](/home/files).                                                                         |

The message you provide to the chat completion endpoint must reference each image you include in the `function.variables` array, by name. For example, if you include an image named `new_product` in the `function.variables` array, you must reference it in the message as `{{new_product}}`, with double curly braces around the name. Your message to the chat completion endpoint might look like this: "Provide a two-sentence summary of the product within the image `{{new_product}}`."

<CodeGroup>
  ```bash cURL theme={null}
  "tools": [
      {
          "type": "vision",
          "function": {
              "model": "palmyra-vision",
              "variables": [
                  {
                      "name": "new_product",
                      "file_id": "1234567890"
                  }
              ]
          }
      }  
  ]
  ```

  ```python Python theme={null}
  tools = [{
      "type": "vision",
      "function": {
          "model": "palmyra-vision",
          "variables": [
              {
                  "name": "new_product",
                  "file_id": "1234567890"
              }
          ]
      }
  }]
  ```

  ```js JavaScript theme={null}
  const tools = [{
      type: "vision",
      function: {
          model: "palmyra-vision",
          variables: [
              {
                  name: "new_product",
                  file_id: "1234567890"
              }
          ]
      }
  }]
  ```
</CodeGroup>

<Note>
  You can only pass one prebuilt tool in the `tools` array at a time. However, you can pass multiple [custom tools](/home/tool-calling) in the same request.

  Prebuilt tools are:

  * Vision tool
  * [Knowledge Graph tool](/home/kg-chat)
  * [Translation tool](/home/translation-tool)
  * [LLM tool](/home/model-delegation)
</Note>

### Response format

For non-streaming responses, the response from the Vision tool is in the `choices[0].message.content` field. For streaming responses, the response is in the `choices[0].delta.content` field.

See the [chat completion endpoint](/api-reference/completion-api/chat-completion#response-id) for more information on the response fields.

<CodeGroup>
  ```json non-streaming response theme={null}
  {
    "id": "1234",
    "object": "chat.completion",
    "choices": [
      {
        "index": 0,
        "finish_reason": "tool_calls",
        "message": {
          "content": "The image shows...",
          "role": "assistant",
          "tool_calls": null,
          "graph_data": {
            "sources": null,
            "status": null,
            "subqueries": null
          },
          "llm_data": null,
          "image_data": null,
          "refusal": null
        },
        "logprobs": null
      }
    ],
    "created": 1743740333,
    "model": "palmyra-x5",
    "usage": {
      "prompt_tokens": 223,
      "total_tokens": 254,
      "completion_tokens": 31,
      "prompt_token_details": null,
      "completion_tokens_details": null
    },
    "system_fingerprint": "v1",
    "service_tier": null
  }
  ```

  ```json streaming response theme={null}
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
              "llm_data": {},
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
          "llm_data": {},
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

This example uses `palmyra-vision` to interpret a graph during a chat completion.

### Upload an image to Writer

Before you can use the Vision tool, you must upload the image to Writer.

The following code samples demonstrate how to upload an image and print the File ID. You need the File ID to pass to the Vision endpoint.

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST 'https://api.writer.com/v1/files' \
    -H 'Content-Type: image/jpeg' \
    -H 'Content-Disposition: attachment; filename=graph.jpg' \
    -H "Authorization: Bearer $WRITER_API_KEY" \
    --data-binary "@path/to/file/graph.jpg"
  ```

  ```python Python theme={null}
  from pathlib import Path
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  file_ = client.files.upload(
    content=Path("path/to/file/graph.jpg"),
    content_disposition="attachment; filename=graph.jpg",
    content_type="image/jpeg"
  )

  print(file_.id)
  ```

  ```javascript JavaScript theme={null}
  import fs from 'fs';
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `api_key` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const file = await client.files.upload({
    content: fs.createReadStream("path/to/file/graph.jpg"),
    "Content-Disposition": "attachment; filename=graph.jpg",
    "Content-Type": "image/jpeg"
  });

  console.log(file.id)
  ```
</CodeGroup>

Learn more about [uploading and managing files](/home/files).

### Create a tools array containing a Vision tool

To use the Vision tool, create a `tools` array that specifies the Writer model you want to use.

<CodeGroup>
  ```bash cURL theme={null}
  "tools": [
      {
          "type": "vision",
          "function": {
              "model": "palmyra-vision",
              "variables": [
                  {
                      "name": "graph",
                      "file_id": "1234567890"
                  }
              ]
          }
      }
  ]
  ```

  ```python Python theme={null}
  tools = [{
      "type": "vision",
      "function": {
          "model": "palmyra-vision",
          "variables": [
              {
                  "name": "graph",
                  "file_id": "1234567890"
              }
          ]
      }
  }]
  ```

  ```js JavaScript theme={null}
  const tools = [{
      type: "vision",
      function: {
          model: "palmyra-vision",
          variables: [
              {
                  name: "graph",
                  file_id: "1234567890"
              }
          ]
      }
  }]
  ```
</CodeGroup>

### Send the request using chat completions

Add the tools array to the chat endpoint call along with your array of messages. Setting `tool_choice` to `auto` allows the model to choose when to use the Vision tool, based on the message provided in the `messages` array.

This example streams the response in real time, rather than waiting for the entire response to be generated.

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
                  "content": "Summarize the main trends and findings in the graph {{graph}}."
              }
          ],
          "tool_choice": "auto",
          "tools": [
              {
                  "type": "vision",
                  "function": {
                      "model": "palmyra-vision",
                      "variables": [
                          {
                              "name": "graph",
                              "file_id": "1234567890"
                          }
                      ]
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

  messages = [{"role": "user", "content": "Summarize the main trends and findings in the graph {{graph}}."}]

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

  const messages = [{role: "user", content: "Summarize the main trends and findings in the graph {{graph}}."}];

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

By following this guide, you can use the Vision tool to have the `palmyra-vision` model interpret an image during a chat completion.

## Next steps

Learn about additional capabilities of the Writer API, such as [analyzing unstructured medical documents](/home/medical-comprehend) and [web search](/home/web-search).
