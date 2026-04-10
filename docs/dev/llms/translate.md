# Source: https://dev.writer.com/api-reference/translation-api/translate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Translate text

> Translate text from one language to another.

<Warning>
  **Deprecation notice**: The [translation API endpoint](/api-reference/translation-api/translate) at `/v1/translation` is deprecated and will be removed on **December 22, 2025**.

  **Migration path**: Use the [translation tool](/home/translation-tool) in chat completions to translate text during conversations. The translation tool provides the same translation capabilities within a chat completion workflow. See the [migration guide](/api-reference/migration-guides/translation-api) for detailed instructions.
</Warning>

The Translation API allows you to translate text from one language to another. See [Language support](/api-reference/translation-api/language-support) for a list of supported languages.


## OpenAPI

````yaml post /v1/translation
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/translation:
    post:
      tags:
        - Translation
      summary: Translate text
      description: Translate text from one language to another.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/translation_request'
            example:
              model: palmyra-translate
              source_language_code: en
              target_language_code: es
              text: Hello, world!
              formality: true
              length_control: true
              mask_profanity: true
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              example:
                data: ¡Hola, mundo!
              schema:
                $ref: '#/components/schemas/translation_response'
      security:
        - bearerAuth: []
components:
  schemas:
    translation_request:
      title: Translation Request
      required:
        - model
        - source_language_code
        - target_language_code
        - text
        - formality
        - length_control
        - mask_profanity
      type: object
      properties:
        model:
          type: string
          description: The model to use for translation.
          enum:
            - palmyra-translate
        source_language_code:
          type: string
          description: >-
            The
            [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
            language code of the original text to translate. For example, `en`
            for English, `zh` for Chinese, `fr` for French, `es` for Spanish. If
            the language has a variant, the code appends the two-digit [ISO-3166
            country
            code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
            For example, Mexican Spanish is `es-MX`. See the [list of supported
            languages and language
            codes](https://dev.writer.com/api-reference/translation-api/language-support).
        target_language_code:
          type: string
          description: >-
            The
            [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
            language code of the target language for the translation. For
            example, `en` for English, `zh` for Chinese, `fr` for French, `es`
            for Spanish. If the language has a variant, the code appends the
            two-digit [ISO-3166 country
            code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
            For example, Mexican Spanish is `es-MX`. See the [list of supported
            languages and language
            codes](https://dev.writer.com/api-reference/translation-api/language-support).
        text:
          type: string
          description: The text to translate. Maximum of 100,000 words.
        formality:
          type: boolean
          description: >-
            Whether to use formal or informal language in the translation. See
            the [list of languages that support
            formality](https://dev.writer.com/api-reference/translation-api/language-support#formality).
            If the language does not support formality, this parameter is
            ignored.
        length_control:
          type: boolean
          description: >-
            Whether to control the length of the translated text. See the [list
            of languages that support length
            control](https://dev.writer.com/api-reference/translation-api/language-support#length-control).
            If the language does not support length control, this parameter is
            ignored.
        mask_profanity:
          type: boolean
          description: >-
            Whether to mask profane words in the translated text. See the [list
            of languages that do not support profanity
            masking](https://dev.writer.com/api-reference/translation-api/language-support#profanity-masking).
            If the language does not support profanity masking, this parameter
            is ignored.
    translation_response:
      title: Translation Response
      required:
        - data
      type: object
      properties:
        data:
          type: string
          description: The result of the translation.
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        Bearer authentication header of the form `Bearer <token>`, where
        `<token>` is your [Writer API
        key](https://dev.writer.com/api-reference/api-keys).

````