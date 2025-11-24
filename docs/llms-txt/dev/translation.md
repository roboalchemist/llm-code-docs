# Source: https://dev.writer.com/home/translation.md

# Translate text

<Warning>
  **Deprecation notice**: The [translation API endpoint](/api-reference/translation-api/translate) at `/v1/translation` is deprecated and will be removed on **December 22, 2025**.

  **Migration path**: Use the [translation tool](/home/translation-tool) in chat completions to translate text during conversations. The translation tool provides the same translation capabilities within a chat completion workflow. See the [migration guide](/api-reference/migration-guides/translation-api) for detailed instructions.
</Warning>

The [Translation API](/api-reference/translation-api/translate) translates text from one language to another. While Palmyra X models can perform translation tasks, they are not optimized for these tasks and may not perform well without correct prompting. Palmyra Translate is a dedicated model optimized for translation use cases.

<Note>
  You need an API key to access the Writer API. Get an API key by following the steps in the [API quickstart](/home/quickstart).

  We recommend setting the API key as an environment variable in a `.env` file with the name `WRITER_API_KEY`.
</Note>

## Translation endpoint

**Endpoint:** `POST /v1/translation`

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

  # Initialize the Writer client. If you don't pass the `apiKey` parameter,
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

### Request body

The request body is a JSON object with the following fields. All fields are required.

| Parameter              | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`                | string  | The model to use for the translation. Must be `palmyra-translate`.                                                                                                                                                                                                                                                                                                                          |
| `source_language_code` | string  | The ISO-639-1 language code of the original text to translate. For example, `en` for English, `zh` for Chinese, `fr` for French, `es` for Spanish. If the language has a variant, the code appends the two-digit ISO-3166 country code. For example, Mexican Spanish is `es-MX`. [See the list of supported languages and language codes](/api-reference/translation-api/language-support). |
| `target_language_code` | string  | The ISO-639-1 language code of the target language. For example, `en` for English, `zh` for Chinese, `fr` for French, `es` for Spanish. If the language has a variant, the code appends the two-digit ISO-3166 country code. For example, Mexican Spanish is `es-MX`. [See the list of supported languages and language codes](/api-reference/translation-api/language-support).            |
| `text`                 | string  | The text to translate.                                                                                                                                                                                                                                                                                                                                                                      |
| `formality`            | Boolean | If the target language supports formal or informal language, this parameter controls whether to use formal (`true`) or informal language (`false`). [See which languages support formality](/api-reference/translation-api/language-support#formality).                                                                                                                                     |
| `length_control`       | Boolean | If the target language supports length control, this parameter controls whether to control the length of the translation. [See which languages support length control](/api-reference/translation-api/language-support#length-control).                                                                                                                                                     |
| `mask_profanity`       | Boolean | If the target language supports profanity masking, this parameter controls whether to mask profane words. [See which languages support profanity masking](/api-reference/translation-api/language-support#profanity-masking).                                                                                                                                                               |

### Response format

The response is a JSON object with a `data` field that contains the translated text as a string.

```json  theme={null}
{
    "data": "Translated text"
}
```
