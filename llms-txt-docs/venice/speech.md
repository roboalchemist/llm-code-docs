# Source: https://docs.venice.ai/api-reference/endpoint/audio/speech.md

# Speech API (Beta)

> Converts text to speech using various voice models and formats.

## OpenAPI

````yaml POST /audio/speech
paths:
  path: /audio/speech
  method: post
  servers:
    - url: https://api.venice.ai/api/v1
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
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
              input:
                allOf:
                  - type: string
                    minLength: 1
                    maxLength: 4096
                    description: >-
                      The text to generate audio for. The maximum length is 4096
                      characters.
                    example: Hello, this is a test of the text to speech system.
              model:
                allOf:
                  - type: string
                    enum:
                      - tts-kokoro
                    default: tts-kokoro
                    description: The model ID of a Venice TTS model.
                    example: tts-kokoro
              response_format:
                allOf:
                  - type: string
                    enum:
                      - mp3
                      - opus
                      - aac
                      - flac
                      - wav
                      - pcm
                    default: mp3
                    description: The format to audio in.
                    example: mp3
              speed:
                allOf:
                  - type: number
                    minimum: 0.25
                    maximum: 4
                    default: 1
                    description: >-
                      The speed of the generated audio. Select a value from 0.25
                      to 4.0. 1.0 is the default.
                    example: 1
              streaming:
                allOf:
                  - type: boolean
                    default: false
                    description: >-
                      Should the content stream back sentence by sentence or be
                      processed and returned as a complete audio file.
                    example: true
              voice:
                allOf:
                  - type: string
                    enum:
                      - af_alloy
                      - af_aoede
                      - af_bella
                      - af_heart
                      - af_jadzia
                      - af_jessica
                      - af_kore
                      - af_nicole
                      - af_nova
                      - af_river
                      - af_sarah
                      - af_sky
                      - am_adam
                      - am_echo
                      - am_eric
                      - am_fenrir
                      - am_liam
                      - am_michael
                      - am_onyx
                      - am_puck
                      - am_santa
                      - bf_alice
                      - bf_emma
                      - bf_lily
                      - bm_daniel
                      - bm_fable
                      - bm_george
                      - bm_lewis
                      - zf_xiaobei
                      - zf_xiaoni
                      - zf_xiaoxiao
                      - zf_xiaoyi
                      - zm_yunjian
                      - zm_yunxi
                      - zm_yunxia
                      - zm_yunyang
                      - ff_siwis
                      - hf_alpha
                      - hf_beta
                      - hm_omega
                      - hm_psi
                      - if_sara
                      - im_nicola
                      - jf_alpha
                      - jf_gongitsune
                      - jf_nezumi
                      - jf_tebukuro
                      - jm_kumo
                      - pf_dora
                      - pm_alex
                      - pm_santa
                      - ef_dora
                      - em_alex
                      - em_santa
                    default: af_sky
                    description: The voice to use when generating the audio.
                    example: af_sky
            description: Request to generate audio from text.
            refIdentifier: '#/components/schemas/CreateSpeechRequestSchema'
            requiredProperties:
              - input
            additionalProperties: false
            example:
              input: Hello, welcome to Venice Voice.
              model: tts-kokoro
              response_format: mp3
              speed: 1
              streaming: false
              voice: af_sky
        examples:
          example:
            value:
              input: Hello, welcome to Venice Voice.
              model: tts-kokoro
              response_format: mp3
              speed: 1
              streaming: false
              voice: af_sky
  response:
    '200':
      audio/aac:
        schemaArray:
          - type: file
            contentEncoding: binary
        examples:
          example: {}
        description: Audio content generated successfully
      audio/flac:
        schemaArray:
          - type: file
            contentEncoding: binary
        examples:
          example: {}
        description: Audio content generated successfully
      audio/mpeg:
        schemaArray:
          - type: file
            contentEncoding: binary
        examples:
          example: {}
        description: Audio content generated successfully
      audio/opus:
        schemaArray:
          - type: file
            contentEncoding: binary
        examples:
          example: {}
        description: Audio content generated successfully
      audio/pcm:
        schemaArray:
          - type: file
            contentEncoding: binary
        examples:
          example: {}
        description: Audio content generated successfully
      audio/wav:
        schemaArray:
          - type: file
            contentEncoding: binary
        examples:
          example: {}
        description: Audio content generated successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              details:
                allOf:
                  - type: object
                    properties: {}
                    description: Details about the incorrect input
                    example:
                      _errors: []
                      field:
                        _errors:
                          - Field is required
              error:
                allOf:
                  - type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/DetailedError'
            requiredProperties:
              - error
        examples:
          example:
            value:
              details:
                _errors: []
                field:
                  _errors:
                    - Field is required
              error: <string>
        description: Invalid request parameters
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: &ref_1
              - error
        examples:
          example:
            value:
              error: <string>
        description: Authentication failed
    '402':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Insufficient USD or Diem balance to complete request
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Unauthorized access
    '415':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Invalid request content-type
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Rate limit exceeded
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Inference processing failed
    '503':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: The model is at capacity. Please try again later.
  deprecated: false
  type: path
components:
  schemas: {}

````