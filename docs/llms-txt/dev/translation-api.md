# Source: https://dev.writer.com/api-reference/migration-guides/translation-api.md

# Migrate from translation API to translation tool

This guide shows you how to migrate from the deprecated [Translation API endpoint](/api-reference/translation-api/translate) to the [translation tool](/home/translation-tool) in chat completions. After completing these steps, you can translate text using the translation tool, which provides the same capabilities within a chat completion workflow.

## Compare the APIs

The Translation API and the translation tool both provide text translation, but the translation tool integrates translation into conversational workflows and changes how you specify translation requests and configurations. The table below compares the two approaches.

| Aspect                | Translation API                                                                                                               | Translation tool                                                                                                                                                                                                                                                                        |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Endpoint**          | `/v1/translation`                                                                                                             | `/v1/chat` with the prebuilt [translation tool](/home/translation-tool) specification                                                                                                                                                                                                   |
| **Request structure** | Pass translation parameters such as `text`, `source_language_code`, `target_language_code`, etc. directly in the request body | Provide the text to translate as part of the conversation `messages` array and include the [translation tool](/home/translation-tool) in the `tools` array. Specify additional settings (such as languages or preferences) in the tool configuration, not as direct request parameters. |
| **Response format**   | Translation in the `data` field                                                                                               | Answer in `choices[0].message.content`; structured details in the `translation_data` field                                                                                                                                                                                              |
| **Parameter control** | Explicit API parameters for each option                                                                                       | Most translation details (languages, formality, etc.) specified in the prompt or tool configuration rather than as top-level request fields                                                                                                                                             |

## Migrate your code

The tabs below show a request using the translation API and the same request using the translation tool.

<Tabs>
  <Tab title="Before: Translation API">
    The Translation API accepts text and translation parameters directly in the request body:

    <CodeGroup>
      ```bash cURL theme={null}
      curl --request POST \
        --url https://api.writer.com/v1/translation \
        --header "Authorization: Bearer $WRITER_API_KEY" \
        --header 'Content-Type: application/json' \
        --data '{
        "model": "palmyra-translate",
        "source_language_code": "en",
        "target_language_code": "es",
        "text": "Hello, world!",
        "formality": true,
        "length_control": true,
        "mask_profanity": true
      }'
      ```

      ```python Python theme={null}
      from writerai import Writer

      # Initialize the Writer client. If you don't pass the `api_key` parameter,
      # the client looks for the `WRITER_API_KEY` environment variable.
      client = Writer()

      response = client.translation.translate(
        model="palmyra-translate",
        source_language_code="en",
        target_language_code="es",
        text="Hello, world!",
        formality=True,
        length_control=True,
        mask_profanity=True
      )

      print(response.data)
      ```

      ```javascript JavaScript theme={null}
      import { Writer } from "writer-sdk";

      // Initialize the Writer client. If you don't pass the `apiKey` parameter,
      // the client looks for the `WRITER_API_KEY` environment variable.
      const client = new Writer();

      const response = await client.translation.translate({
        model: "palmyra-translate",
        source_language_code: "en",
        target_language_code: "es",
        text: "Hello, world!",
        formality: true,
        length_control: true,
        mask_profanity: true
      });

      console.log(response.data);
      ```
    </CodeGroup>

    **Response:**

    ```json  theme={null}
    {
      "data": "¡Hola, mundo!"
    }
    ```
  </Tab>

  <Tab title="After: Translation tool">
    The translation tool uses the chat completions endpoint with a translation tool specification. The model handles the translation request based on your message and the tool configuration:

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
                "formality": true,
                "length_control": true,
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

      tools = [{
        "type": "translation",
        "function": {
          "model": "palmyra-translate",
          "formality": True,
          "length_control": True,
          "mask_profanity": True
        }
      }]

      response = client.chat.chat(
        model="palmyra-x5", 
        messages=messages, 
        tools=tools,
        tool_choice="auto"
      )

      print(response.choices[0].message.content)
      ```

      ```javascript JavaScript theme={null}
      import { Writer } from "writer-sdk";

      // Initialize the Writer client. If you don't pass the `apiKey` parameter,
      // the client looks for the `WRITER_API_KEY` environment variable.
      const client = new Writer();

      const messages = [{role: "user", content: "Translate the following message to Spanish: 'Hello, world!'"}];

      const tools = [{
        type: "translation",
        function: {
          model: "palmyra-translate",
          formality: true,
          length_control: true,
          mask_profanity: true
        }
      }];

      const response = await client.chat.chat({
        model: "palmyra-x5", 
        messages: messages, 
        tools: tools,
        tool_choice: "auto"
      });

      console.log(response.choices[0].message.content);
      ```
    </CodeGroup>

    **Response:**

    ```json  theme={null}
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
            "translation_data": {
              "source_text": "Hello, world!",
              "source_language_code": "en",
              "target_language_code": "es"
            }
          }
        }
      ]
    }
    ```
  </Tab>
</Tabs>

## Map your parameters

The following table shows how Translation API parameters map to the translation tool:

| Translation API        | Translation tool                               |
| ---------------------- | ---------------------------------------------- |
| `text`                 | Include in the message `content` field         |
| `source_language_code` | `tools[0].function.source_language` (optional) |
| `target_language_code` | `tools[0].function.target_language` (optional) |
| `formality`            | `tools[0].function.formality`                  |
| `length_control`       | `tools[0].function.length_control`             |
| `mask_profanity`       | `tools[0].function.mask_profanity`             |

<Note>
  With the translation tool, the `source_language` and `target_language` parameters are optional. If you don't provide them, the model automatically detects the source language and determines the target language from your message.

  To specify languages explicitly, include them in your message prompt (for example, "Translate to Spanish") or use the optional `source_language` and `target_language` parameters in the tool configuration.
</Note>

## Access translation metadata

The translation tool response includes additional metadata in the `translation_data` field. The metadata includes the source text, source language, and target language:

<CodeGroup>
  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client. If you don't pass the `api_key` parameter,
  # the client looks for the `WRITER_API_KEY` environment variable.
  client = Writer()

  messages = [{"role": "user", "content": "Translate the following message to Spanish: 'Hello, world!'"}]

  tools = [{
    "type": "translation",
    "function": {
      "model": "palmyra-translate",
      "formality": True,
      "length_control": True,
      "mask_profanity": True
    }
  }]

  response = client.chat.chat(
    model="palmyra-x5", 
    messages=messages, 
    tools=tools,
    tool_choice="auto"
  )

  # Get translated text
  translated_text = response.choices[0].message.content

  # Get translation metadata
  translation_metadata = response.choices[0].message.translation_data
  source_lang = translation_metadata.source_language_code
  target_lang = translation_metadata.target_language_code
  source_text = translation_metadata.source_text

  print(f"Translated '{source_text}' from {source_lang} to {target_lang}: {translated_text}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from "writer-sdk";

  // Initialize the Writer client. If you don't pass the `apiKey` parameter,
  // the client looks for the `WRITER_API_KEY` environment variable.
  const client = new Writer();

  const messages = [{role: "user", content: "Translate the following message to Spanish: 'Hello, world!'"}];

  const tools = [{
    type: "translation",
    function: {
      model: "palmyra-translate",
      formality: true,
      length_control: true,
      mask_profanity: true
    }
  }];
  const response = await client.chat.chat({
    model: "palmyra-x5", 
    messages: messages, 
    tools: tools,
    tool_choice: "auto"
  });

  // Get translated text
  const translatedText = response.choices[0].message.content;

  // Get translation metadata
  const translationMetadata = response.choices[0].message.translation_data;
  const sourceLang = translationMetadata.source_language_code;
  const targetLang = translationMetadata.target_language_code;
  const sourceText = translationMetadata.source_text;

  console.log(`Translated '${sourceText}' from ${sourceLang} to ${targetLang}: ${translatedText}`);
  ```
</CodeGroup>

## Explore related features

Learn more about the translation tool and related features:

* [Translation tool guide](/home/translation-tool)
* [Language support](/api-reference/translation-api/language-support)
* [Chat completion guide](/home/chat-completion)
* [Other prebuilt tools](/home/tool-calling)
