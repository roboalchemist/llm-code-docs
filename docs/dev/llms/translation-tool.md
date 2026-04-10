# Source: https://dev.writer.com/home/translation-tool.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Translate text in a chat

The translation tool for chat completions allows you to translate text during a conversation.

While Palmyra X models can perform translation tasks, they are not optimized for these tasks and may not perform well without correct prompting. Palmyra Translate is a dedicated model optimized for translation use cases.

This guide explains how to use the translation tool in a chat completion and provides an example of how to use it.

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

## Tool structure

The translation tool allows you to translate text during a [chat completion](/home/chat-completion).

To use the translation tool, add it to the `tools` array in your `chat-completion` endpoint request.

The translation tool object has the following structure:

| Parameter                  | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                     | `string`  | The type of tool, which is `translation` for the translation tool                                                                                                                                                                                                                                                                                                                                                     |
| `function`                 | `object`  | An object containing the tool's description and model                                                                                                                                                                                                                                                                                                                                                                 |
| `function.model`           | `string`  | `palmyra-translate`                                                                                                                                                                                                                                                                                                                                                                                                   |
| `function.formality`       | `boolean` | Whether the translation should be formal or informal, [if the target language supports it](/api-reference/translation-api/language-support#formality).                                                                                                                                                                                                                                                                |
| `function.length_control`  | `boolean` | Whether to control the length of the translation, [if the target language supports it](/api-reference/translation-api/language-support#length-control).                                                                                                                                                                                                                                                               |
| `function.mask_profanity`  | `boolean` | Whether to mask profanity in the translation, [if the target language supports it](/api-reference/translation-api/language-support#profanity-masking).                                                                                                                                                                                                                                                                |
| `function.source_language` | `string`  | (Optional) The [language code](/api-reference/translation-api/language-support#language-codes) of the text you want to translate. If you don't provide a source language, the model automatically detects the language of the text you want to translate. If your message contains a different language than this value, this value overrides the language detection.                                                 |
| `function.target_language` | `string`  | (Optional) The [language code](/api-reference/translation-api/language-support#language-codes) you want to translate the text to. If you don't provide a target language, the model automatically selects the most appropriate language based on the message you provide to the chat completion endpoint. If your message contains a different language than this value, this value overrides the language selection. |

<CodeGroup>
  ```bash cURL theme={null}
  "tools": [
      {
          "type": "translation",
          "function": {
              "model": "palmyra-translate",
              "formality": false,
              "length_control": false,
              "mask_profanity": true
          }
      }  
  ]
  ```

  ```python Python theme={null}
  tools = [{
      "type": "translation",
      "function": {
          "model": "palmyra-translate",
          "formality": False,
          "length_control": False,
          "mask_profanity": True
      }
  }]
  ```

  ```js JavaScript theme={null}
  const tools = [{
      type: "translation",
      function: {
          model: "palmyra-translate",
          formality: false,
          length_control: false,
          mask_profanity: true
      }
  }]
  ```
</CodeGroup>

<Note>
  You can only pass one prebuilt tool in the `tools` array at a time. However, you can pass multiple [custom tools](/home/tool-calling) in the same request.

  Prebuilt tools are:

  * Translation tool
  * [Knowledge Graph tool](/home/kg-chat)
  * [LLM tool](/home/model-delegation)
  * [Vision tool](/home/vision-tool)
</Note>

### Response format

For non-streaming responses, the translated text is in the `choices[0].message.content` field. For streaming responses, the translated text is in the `choices[0].delta.content` field.

The response also contains a `translation_data` field that contains the following information:

| Parameter              | Type     | Description                                                         |
| ---------------------- | -------- | ------------------------------------------------------------------- |
| `source_language_code` | `string` | The language code of the text you provided to the translation tool. |
| `target_language_code` | `string` | The language code of the translated text.                           |
| `source_text`          | `string` | The text the translation tool translated.                           |

<Warning>
  You can use the translation tool with streaming chat responses, but the translation tool call is not streamed. The response comes back in the `choices[0].delta.content` field once the full translation is complete.

  If you are unfamiliar with the chat completions endpoint or streaming vs. non-streaming responses, learn more in the [chat completion guide](/home/chat-completion).
</Warning>

See the [chat completion endpoint](/api-reference/completion-api/chat-completion#response-id) for more information on the response fields.

<CodeGroup>
  ```json non-streaming response {9,19-23} theme={null}
  {
    "id": "63ae5c5d",
    "object": "chat.completion",
    "choices": [
      {
        "index": 0,
        "finish_reason": "tool_calls",
        "message": {
          "content": "¡Hola, mundo!",
          "role": "assistant",
          "tool_calls": null,
          "graph_data": {
            "sources": null,
            "status": null,
            "subqueries": null
          },
          "llm_data": null,
          "image_data": null,
          "translation_data": {
            "source_text": "Hello, world!",
            "source_language_code": "en",
            "target_language_code": "es"
          },
          "refusal": null
        },
        "logprobs": null
      }
    ],
    "created": 1745956341,
    "model": "palmyra-x5",
    "usage": {
      "prompt_tokens": 2909,
      "total_tokens": 2945,
      "completion_tokens": 36,
      "prompt_token_details": null,
      "completion_tokens_details": null
    },
    "system_fingerprint": "v1",
    "service_tier": null
  }
  ```

  ```json streaming response {26,36-40} theme={null}
  {
      "id": "8cbef9eb",
      "object": "chat.completion.chunk",
      "choices": [{
          "index": 0,
          "finish_reason": "tool_calls",
          "message": {
              "content": "¡Hola, mundo!",
              "role": "assistant",
              "tool_calls": null,
              "graph_data": {
                  "sources": null,
                  "status": null,
                  "subqueries": null
              },
              "llm_data": null,
              "image_data": null,
              "translation_data": {
                  "source_text": "Hello, world!",
                  "source_language_code": "en",
                  "target_language_code": "es"
              },
              "refusal": null
          },
          "delta": {
              "content": "¡Hola, mundo!",
              "role": "assistant",
              "tool_calls": null,
              "graph_data": {
                  "sources": null,
                  "status": null,
                  "subqueries": null
              },
              "llm_data": null,
              "image_data": null,
              "translation_data": {
                  "source_text": "Hello, world!",
                  "source_language_code": "en",
                  "target_language_code": "es"
              },
              "refusal": null
          },
          "logprobs": null
      }],
      "created": 1745956498,
      "model": "palmyra-x5",
      "usage": null,
      "system_fingerprint": "v1",
      "service_tier": null
  }
  ```
</CodeGroup>

## Usage example

This example uses `palmyra-translate` to translate a message during a chat completion.

### Create a tools array containing a translation tool

First, create a `tools` array that specifies the translation tool you want to use.

<CodeGroup>
  ```bash cURL theme={null}
  "tools": [
      {
          "type": "translation",
          "function": {
              "model": "palmyra-translate",
              "formality": false,
              "length_control": false,
              "mask_profanity": true
          }
      }
  ]
  ```

  ```python Python theme={null}
  tools = [{
      "type": "translation",
      "function": {
          "model": "palmyra-translate",
          "formality": False,
          "length_control": False,
          "mask_profanity": True
      }
  }]
  ```

  ```js JavaScript theme={null}
  const tools = [{
      type: "translation",
      function: {
          model: "palmyra-translate",
          formality: false,
          length_control: false,
          mask_profanity: true
          ]
      }
  }]
  ```
</CodeGroup>

### Send the request using chat completions

Add the tools array to the chat endpoint call along with your array of messages. Setting `tool_choice` to `auto` allows the model to choose when to use the translation tool, based on the message provided in the `messages` array.

The response contains the translated text in the `choices[0].message.content` field.

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
                  "content": "Translate the following message to Spanish: Hello, world!"
              }
          ],
          "tool_choice": "auto",
          "tools": [
              {
                  "type": "translation",
                  "function": {
                      "model": "palmyra-translate",
                      "formality": false,
                      "length_control": false,
                      "mask_profanity": true
                      }
                  }
          ]
      }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  messages = [{"role": "user", "content": "Translate the following message to Spanish: 'Hello, world!'"}]

  response = client.chat.chat(
      model="palmyra-x5", 
      messages=messages, 
      tools=tools,  # The tools array defined earlier.
      tool_choice="auto"
  )

  print(response.choices[0].message.content)
  ```

  ```js JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const messages = [{role: "user", content: "Translate the following message to Spanish: 'Hello, world!'"}];

  const response = await client.chat.chat({
      model: "palmyra-x5", 
      messages: messages, 
      tools: tools, // The tools array defined earlier.
      tool_choice: "auto"
  });

  console.log(response.choices[0].message.content);
  ```
</CodeGroup>

If you want to verify the translation data in the response, you can print the `translation_data` field to see the source text, source language code, and target language code that the translation tool used.

<CodeGroup>
  ```python Python theme={null}
  print(response.choices[0].message.translation_data)
  ```

  ```js JavaScript theme={null}
  console.log(response.choices[0].message.translation_data);
  ```
</CodeGroup>

By following this guide, you can use the translation tool to have the `palmyra-translate` model translate a message during a chat completion.

## Next steps

Learn about additional capabilities of the Writer API, such as [analyzing images](/home/analyze-images) and [web search](/home/web-search).
