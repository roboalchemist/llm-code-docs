# Source: https://docs.together.ai/reference/audio-speech.md

# Create Audio Generation Request

> Generate audio from input text



## OpenAPI

````yaml POST /audio/speech
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
  /audio/speech:
    post:
      tags:
        - Audio
      summary: Create audio generation request
      description: Generate audio from input text
      operationId: audio-speech
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AudioSpeechRequest'
      responses:
        '200':
          description: OK
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
            audio/wav:
              schema:
                type: string
                format: binary
            audio/mpeg:
              schema:
                type: string
                format: binary
            text/event-stream:
              schema:
                $ref: '#/components/schemas/AudioSpeechStreamResponse'
        '400':
          description: BadRequest
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
    AudioSpeechRequest:
      type: object
      required:
        - model
        - input
        - voice
      properties:
        model:
          description: >
            The name of the model to query.<br> <br> [See all of Together AI's
            chat
            models](https://docs.together.ai/docs/serverless-models#audio-models)
            The current supported tts models are: - cartesia/sonic -
            hexgrad/Kokoro-82M - canopylabs/orpheus-3b-0.1-ft
          example: canopylabs/orpheus-3b-0.1-ft
          anyOf:
            - type: string
              enum:
                - cartesia/sonic
                - hexgrad/Kokoro-82M
                - canopylabs/orpheus-3b-0.1-ft
            - type: string
        input:
          type: string
          description: Input text to generate the audio for
        voice:
          description: >
            The voice to use for generating the audio. The voices supported are
            different for each model. For eg - for canopylabs/orpheus-3b-0.1-ft,
            one of the voices supported is tara, for hexgrad/Kokoro-82M, one of
            the voices supported is af_alloy and for cartesia/sonic, one of the
            voices supported is "friendly sidekick". <br> <br> You can view the
            voices supported for each model using the /v1/voices endpoint
            sending the model name as the query parameter. [View all supported
            voices
            here](https://docs.together.ai/docs/text-to-speech#voices-available).
          type: string
        response_format:
          type: string
          description: >-
            The format of audio output. Supported formats are mp3, wav, raw if
            streaming is false. If streaming is true, the only supported format
            is raw.
          default: wav
          enum:
            - mp3
            - wav
            - raw
        language:
          type: string
          description: Language of input text.
          default: en
          enum:
            - en
            - de
            - fr
            - es
            - hi
            - it
            - ja
            - ko
            - nl
            - pl
            - pt
            - ru
            - sv
            - tr
            - zh
        response_encoding:
          type: string
          description: Audio encoding of response
          default: pcm_f32le
          enum:
            - pcm_f32le
            - pcm_s16le
            - pcm_mulaw
            - pcm_alaw
        sample_rate:
          type: integer
          default: 44100
          description: >-
            Sampling rate to use for the output audio. The default sampling rate
            for canopylabs/orpheus-3b-0.1-ft and hexgrad/Kokoro-82M is 24000 and
            for cartesia/sonic is 44100.
        stream:
          type: boolean
          default: false
          description: >-
            If true, output is streamed for several characters at a time instead
            of waiting for the full response. The stream terminates with `data:
            [DONE]`. If false, return the encoded audio as octet stream
    AudioSpeechStreamResponse:
      oneOf:
        - $ref: '#/components/schemas/AudioSpeechStreamEvent'
        - $ref: '#/components/schemas/StreamSentinel'
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
    AudioSpeechStreamEvent:
      type: object
      required:
        - data
      properties:
        data:
          $ref: '#/components/schemas/AudioSpeechStreamChunk'
    StreamSentinel:
      type: object
      required:
        - data
      properties:
        data:
          title: stream_signal
          type: string
          enum:
            - '[DONE]'
    AudioSpeechStreamChunk:
      type: object
      required:
        - object
        - model
        - b64
      properties:
        object:
          type: string
          enum:
            - audio.tts.chunk
        model:
          type: string
          example: cartesia/sonic
        b64:
          type: string
          description: base64 encoded audio stream
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt