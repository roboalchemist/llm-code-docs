# Source: https://dev.writer.com/api-reference/translation-api/translate.md

# Translate text

> Translate text from one language to another.

## OpenAPI

````yaml post /v1/translation
paths:
  path: /v1/translation
  method: post
  servers:
    - url: https://api.writer.com
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication header of the form `Bearer <token>`, where
                `<token>` is your [Writer API
                key](https://dev.writer.com/api-reference/api-keys).
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              model:
                allOf:
                  - type: string
                    description: The model to use for translation.
                    enum:
                      - palmyra-translate
              source_language_code:
                allOf:
                  - type: string
                    description: >-
                      The
                      [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
                      language code of the original text to translate. For
                      example, `en` for English, `zh` for Chinese, `fr` for
                      French, `es` for Spanish. If the language has a variant,
                      the code appends the two-digit [ISO-3166 country
                      code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
                      For example, Mexican Spanish is `es-MX`. See the [list of
                      supported languages and language
                      codes](https://dev.writer.com/api-reference/translation-api/language-support).
              target_language_code:
                allOf:
                  - type: string
                    description: >-
                      The
                      [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
                      language code of the target language for the translation.
                      For example, `en` for English, `zh` for Chinese, `fr` for
                      French, `es` for Spanish. If the language has a variant,
                      the code appends the two-digit [ISO-3166 country
                      code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
                      For example, Mexican Spanish is `es-MX`. See the [list of
                      supported languages and language
                      codes](https://dev.writer.com/api-reference/translation-api/language-support).
              text:
                allOf:
                  - type: string
                    description: The text to translate. Maximum of 100,000 words.
              formality:
                allOf:
                  - type: boolean
                    description: >-
                      Whether to use formal or informal language in the
                      translation. See the [list of languages that support
                      formality](https://dev.writer.com/api-reference/translation-api/language-support#formality).
                      If the language does not support formality, this parameter
                      is ignored.
              length_control:
                allOf:
                  - type: boolean
                    description: >-
                      Whether to control the length of the translated text. See
                      the [list of languages that support length
                      control](https://dev.writer.com/api-reference/translation-api/language-support#length-control).
                      If the language does not support length control, this
                      parameter is ignored.
              mask_profanity:
                allOf:
                  - type: boolean
                    description: >-
                      Whether to mask profane words in the translated text. See
                      the [list of languages that do not support profanity
                      masking](https://dev.writer.com/api-reference/translation-api/language-support#profanity-masking).
                      If the language does not support profanity masking, this
                      parameter is ignored.
            required: true
            title: Translation Request
            refIdentifier: '#/components/schemas/translation_request'
            requiredProperties:
              - model
              - source_language_code
              - target_language_code
              - text
              - formality
              - length_control
              - mask_profanity
        examples:
          example:
            value:
              model: palmyra-translate
              source_language_code: en
              target_language_code: es
              text: Hello, world!
              formality: true
              length_control: true
              mask_profanity: true
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request POST https://api.writer.com/v1/translation \
           --header "Authorization: Bearer <token>" \
           --header "Content-Type: application/json" \
          --data-raw
          '{"model":"string","source_language_code":"string","target_language_code":"string","text":"string","formality":false,"length_control":false,"mask_profanity":false}'
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const translationResponse = await client.translation.translate({
              formality: true,
              length_control: true,
              mask_profanity: true,
              model: 'palmyra-translate',
              source_language_code: 'en',
              target_language_code: 'es',
              text: 'Hello, world!',
            });

            console.log(translationResponse.data);
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              api_key=os.environ.get("WRITER_API_KEY"),  # This is the default and can be omitted
          )
          translation_response = client.translation.translate(
              formality=True,
              length_control=True,
              mask_profanity=True,
              model="palmyra-translate",
              source_language_code="en",
              target_language_code="es",
              text="Hello, world!",
          )
          print(translation_response.data)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: string
                    description: The result of the translation.
            title: Translation Response
            refIdentifier: '#/components/schemas/translation_response'
            requiredProperties:
              - data
        examples:
          example:
            value:
              data: ¡Hola, mundo!
        description: Successful response
  deprecated: false
  type: path
components:
  schemas: {}

````