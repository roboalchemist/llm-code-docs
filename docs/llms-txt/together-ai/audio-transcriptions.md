# Source: https://docs.together.ai/reference/audio-transcriptions.md

# Create an Audio Transcription

> Transcribes audio into text



## OpenAPI

````yaml POST /audio/transcriptions
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
  /audio/transcriptions:
    post:
      tags:
        - Audio
      summary: Create audio transcription request
      description: Transcribes audio into text
      operationId: audio-transcriptions
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/AudioTranscriptionRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AudioTranscriptionResponse'
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
    AudioTranscriptionRequest:
      type: object
      required:
        - file
      properties:
        file:
          oneOf:
            - $ref: '#/components/schemas/AudioFileBinary'
            - $ref: '#/components/schemas/AudioFileUrl'
          description: >-
            Audio file upload or public HTTP/HTTPS URL. Supported formats .wav,
            .mp3, .m4a, .webm, .flac.
        model:
          type: string
          description: Model to use for transcription
          default: openai/whisper-large-v3
          enum:
            - openai/whisper-large-v3
        language:
          type: string
          description: >-
            Optional ISO 639-1 language code. If `auto` is provided, language is
            auto-detected.
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
        diarize:
          type: boolean
          description: >
            Whether to enable speaker diarization. When enabled, you will get
            the speaker id for each word in the transcription. In the response,
            in the words array, you will get the speaker id for each word. In
            addition, we also return the speaker_segments array which contains
            the speaker id for each speaker segment along with the start and end
            time of the segment along with all the words in the segment. <br>
            <br> For eg - ... "speaker_segments": [
              "speaker_id": "SPEAKER_00",
              "start": 0,
              "end": 30.02,
              "words": [
                {
                  "id": 0,
                  "word": "Tijana",
                  "start": 0,
                  "end": 11.475,
                  "speaker_id": "SPEAKER_00"
                },
                ...
          default: false
        min_speakers:
          type: integer
          description: >-
            Minimum number of speakers expected in the audio. Used to improve
            diarization accuracy when the approximate number of speakers is
            known.
        max_speakers:
          type: integer
          description: >-
            Maximum number of speakers expected in the audio. Used to improve
            diarization accuracy when the approximate number of speakers is
            known.
    AudioTranscriptionResponse:
      oneOf:
        - $ref: '#/components/schemas/AudioTranscriptionJsonResponse'
        - $ref: '#/components/schemas/AudioTranscriptionVerboseJsonResponse'
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
    AudioFileBinary:
      type: string
      format: binary
      description: Audio file to transcribe
    AudioFileUrl:
      type: string
      format: uri
      description: Public HTTPS URL to audio file
    AudioTranscriptionJsonResponse:
      type: object
      required:
        - text
      properties:
        text:
          type: string
          description: The transcribed text
          example: Hello, world!
    AudioTranscriptionVerboseJsonResponse:
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
          example: transcribe
        language:
          type: string
          description: The language of the audio
          example: english
        duration:
          type: number
          format: float
          description: The duration of the audio in seconds
          example: 3.5
        text:
          type: string
          description: The transcribed text
          example: Hello, world!
        segments:
          type: array
          items:
            $ref: '#/components/schemas/AudioTranscriptionSegment'
          description: Array of transcription segments
        words:
          type: array
          items:
            $ref: '#/components/schemas/AudioTranscriptionWord'
          description: >-
            Array of transcription words (only when timestamp_granularities
            includes 'word')
        speaker_segments:
          type: array
          items:
            $ref: '#/components/schemas/AudioTranscriptionSpeakerSegment'
          description: >-
            Array of transcription speaker segments (only when diarize is
            enabled)
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
    AudioTranscriptionSpeakerSegment:
      type: object
      required:
        - speaker_id
        - start
        - end
        - words
        - text
        - id
      properties:
        speaker_id:
          type: string
          description: The speaker identifier
          example: SPEAKER_00
        start:
          type: number
          format: float
          description: Start time of the speaker segment in seconds
          example: 0
        end:
          type: number
          format: float
          description: End time of the speaker segment in seconds
          example: 30.02
        words:
          type: array
          items:
            $ref: '#/components/schemas/AudioTranscriptionWord'
          description: Array of words spoken by this speaker in this segment
        text:
          type: string
          description: The full text spoken by this speaker in this segment
          example: Hello, how are you doing today?
        id:
          type: integer
          description: Unique identifier for the speaker segment
          example: 1
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt