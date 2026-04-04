# Source: https://docs.together.ai/reference/audio-translations.md

# Create an Audio Translation

> Translates audio into English



## OpenAPI

````yaml POST /audio/translations
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /audio/translations:
    post:
      tags:
        - Audio
      summary: Create audio translation request
      description: Translates audio into English
      operationId: audio-translations
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/AudioTranslationRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AudioTranslationResponse'
        '400':
          description: BadRequest
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '429':
          description: RateLimit
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
components:
  schemas:
    AudioTranslationRequest:
      type: object
      required:
        - file
      properties:
        file:
          oneOf:
            - type: string
              format: binary
              description: Audio file to translate
            - type: string
              format: uri
              description: Public HTTP/HTTPS URL to audio file
          description: >-
            Audio file upload or public HTTP/HTTPS URL. Supported formats .wav,
            .mp3, .m4a, .webm, .flac.
        model:
          type: string
          description: Model to use for translation
          default: openai/whisper-large-v3
          enum:
            - openai/whisper-large-v3
        language:
          type: string
          description: >-
            Target output language. Optional ISO 639-1 language code. If
            omitted, language is set to English.
          default: en
          example: en
        prompt:
          type: string
          description: Optional text to bias decoding.
        response_format:
          type: string
          description: The format of the response
          default: json
          enum:
            - json
            - verbose_json
        temperature:
          type: number
          format: float
          description: Sampling temperature between 0.0 and 1.0
          default: 0
          minimum: 0
          maximum: 1
        timestamp_granularities:
          oneOf:
            - type: string
              enum:
                - segment
                - word
            - type: array
              items:
                type: string
                enum:
                  - segment
                  - word
              uniqueItems: true
              minItems: 1
              maxItems: 2
          description: >-
            Controls level of timestamp detail in verbose_json. Only used when
            response_format is verbose_json. Can be a single granularity or an
            array to get multiple levels.
          default: segment
          example:
            - word
            - segment
    AudioTranslationResponse:
      oneOf:
        - $ref: '#/components/schemas/AudioTranslationJsonResponse'
        - $ref: '#/components/schemas/AudioTranslationVerboseJsonResponse'
    ErrorData:
      type: object
      required:
        - error
      properties:
        error:
          type: object
          properties:
            message:
              type: string
              nullable: false
            type:
              type: string
              nullable: false
            param:
              type: string
              nullable: true
              default: null
            code:
              type: string
              nullable: true
              default: null
          required:
            - type
            - message
    AudioTranslationJsonResponse:
      type: object
      required:
        - text
      properties:
        text:
          type: string
          description: The translated text
          example: Hello, world!
    AudioTranslationVerboseJsonResponse:
      type: object
      required:
        - task
        - language
        - duration
        - text
        - segments
      properties:
        task:
          type: string
          description: The task performed
          enum:
            - transcribe
            - translate
          example: translate
        language:
          type: string
          description: The target language of the translation
          example: english
        duration:
          type: number
          format: float
          description: The duration of the audio in seconds
          example: 3.5
        text:
          type: string
          description: The translated text
          example: Hello, world!
        segments:
          type: array
          items:
            $ref: '#/components/schemas/AudioTranscriptionSegment'
          description: Array of translation segments
        words:
          type: array
          items:
            $ref: '#/components/schemas/AudioTranscriptionWord'
          description: >-
            Array of translation words (only when timestamp_granularities
            includes 'word')
    AudioTranscriptionSegment:
      type: object
      required:
        - id
        - start
        - end
        - text
      properties:
        id:
          type: integer
          description: Unique identifier for the segment
          example: 0
        start:
          type: number
          format: float
          description: Start time of the segment in seconds
          example: 0
        end:
          type: number
          format: float
          description: End time of the segment in seconds
          example: 3.5
        text:
          type: string
          description: The text content of the segment
          example: Hello, world!
    AudioTranscriptionWord:
      type: object
      required:
        - word
        - start
        - end
      properties:
        word:
          type: string
          description: The word
          example: Hello
        start:
          type: number
          format: float
          description: Start time of the word in seconds
          example: 0
        end:
          type: number
          format: float
          description: End time of the word in seconds
          example: 0.5
        speaker_id:
          type: string
          description: The speaker id for the word (only when diarize is enabled)
          example: SPEAKER_00
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt