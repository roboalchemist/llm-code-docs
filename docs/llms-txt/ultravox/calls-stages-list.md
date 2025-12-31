# Source: https://docs.ultravox.ai/api-reference/calls/calls-stages-list.md

# List Call Stages

> Lists all stages that occurred during the specified call

Stages represent distinct segments of the conversation where different parameters (e.g. system prompt or tools) may have been used.


## OpenAPI

````yaml get /api/calls/{call_id}/stages
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/calls/{call_id}/stages:
    get:
      tags:
        - calls
      operationId: calls_stages_list
      parameters:
        - in: path
          name: call_id
          schema:
            type: string
            format: uuid
          required: true
        - name: cursor
          required: false
          in: query
          description: The pagination cursor value.
          schema:
            type: string
        - name: pageSize
          required: false
          in: query
          description: Number of results to return per page.
          schema:
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaginatedCallStageList'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    PaginatedCallStageList:
      type: object
      required:
        - results
      properties:
        next:
          type: string
          nullable: true
          format: uri
          example: http://api.example.org/accounts/?cursor=cD00ODY%3D"
        previous:
          type: string
          nullable: true
          format: uri
          example: http://api.example.org/accounts/?cursor=cj0xJnA9NDg3
        results:
          type: array
          items:
            $ref: '#/components/schemas/CallStage'
        total:
          type: integer
          example: 123
    CallStage:
      type: object
      properties:
        callId:
          type: string
          format: uuid
          readOnly: true
        callStageId:
          type: string
          format: uuid
          readOnly: true
        created:
          type: string
          format: date-time
          readOnly: true
        inactivityMessages:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.TimedMessage'
          description: >-
            Messages spoken by the agent when the user is inactive for the
            specified duration. Durations are cumulative, so a message m > 1
            with duration 30s will be spoken 30 seconds after message m-1.
        languageHint:
          type: string
          nullable: true
          description: BCP47 language code that may be used to guide speech recognition.
          maxLength: 16
        model:
          type: string
        systemPrompt:
          type: string
          nullable: true
        temperature:
          type: number
          format: double
          readOnly: true
        timeExceededMessage:
          type: string
          nullable: true
        voice:
          type: string
          nullable: true
        externalVoice:
          $ref: '#/components/schemas/ultravox.v1.ExternalVoice'
        errorCount:
          type: integer
          readOnly: true
          description: The number of errors in this call stage.
        experimentalSettings:
          readOnly: true
          nullable: true
          description: Experimental settings for this call stage.
        initialState:
          type: object
          additionalProperties: {}
          description: >-
            The initial state of the call stage which is readable/writable by
            tools.
      required:
        - callId
        - callStageId
        - created
        - errorCount
        - experimentalSettings
        - initialState
        - temperature
    ultravox.v1.TimedMessage:
      type: object
      properties:
        duration:
          pattern: ^-?(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,9})?s$
          type: string
          description: The duration after which the message should be spoken.
        message:
          type: string
          description: The message to speak.
        endBehavior:
          enum:
            - END_BEHAVIOR_UNSPECIFIED
            - END_BEHAVIOR_HANG_UP_SOFT
            - END_BEHAVIOR_HANG_UP_STRICT
          type: string
          description: The behavior to exhibit when the message is finished being spoken.
          format: enum
      description: >-
        A message the agent should say after some duration. The duration's
        meaning
         varies depending on the context.
    ultravox.v1.ExternalVoice:
      type: object
      properties:
        elevenLabs:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.ElevenLabsVoice'
          description: A voice served by ElevenLabs.
        cartesia:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CartesiaVoice'
          description: A voice served by Cartesia.
        lmnt:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.LmntVoice'
          description: A voice served by LMNT.
        google:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.GoogleVoice'
          description: |-
            A voice served by Google, using bidirectional streaming.
             (For non-streaming or output-only streaming, use generic.)
        generic:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.GenericVoice'
          description: A voice served by a generic REST-based TTS API.
      description: >-
        A voice not known to Ultravox Realtime that can nonetheless be used for
        a call.
         Such voices are significantly less validated than normal voices and you'll be
         responsible for your own TTS-related errors.
         Exactly one field must be set.
    ultravox.v1.ElevenLabsVoice:
      type: object
      properties:
        voiceId:
          type: string
          description: The ID of the voice in ElevenLabs.
        model:
          type: string
          description: The ElevenLabs model to use.
        speed:
          type: number
          description: |-
            The speaking rate. Must be between 0.7 and 1.2. Defaults to 1.
             See https://elevenlabs.io/docs/api-reference/text-to-speech/convert#request.body.voice_settings.speed
          format: float
        useSpeakerBoost:
          type: boolean
          description: >-
            See
            https://elevenlabs.io/docs/api-reference/text-to-speech/convert#request.body.voice_settings.use_speaker_boost
        style:
          type: number
          description: >-
            See
            https://elevenlabs.io/docs/api-reference/text-to-speech/convert#request.body.voice_settings.style
          format: float
        similarityBoost:
          type: number
          description: >-
            See
            https://elevenlabs.io/docs/api-reference/text-to-speech/convert#request.body.voice_settings.similarity_boost
          format: float
        stability:
          type: number
          description: >-
            See
            https://elevenlabs.io/docs/api-reference/text-to-speech/convert#request.body.voice_settings.stability
          format: float
        pronunciationDictionaries:
          type: array
          items:
            $ref: >-
              #/components/schemas/ultravox.v1.ElevenLabsVoice_PronunciationDictionaryReference
          description: >-
            See
            https://elevenlabs.io/docs/api-reference/text-to-speech/convert#request.body.pronunciation_dictionary_locators
        optimizeStreamingLatency:
          type: integer
          description: >-
            See
            https://elevenlabs.io/docs/api-reference/text-to-speech/convert#request.query.optimize_streaming_latency.optimize_streaming_latency
          format: int32
        maxSampleRate:
          type: integer
          description: >-
            The maximum sample rate Ultravox will try to use. ElevenLabs limits
            your allowed sample rate
             based on your tier. See https://elevenlabs.io/pricing#pricing-table (and click "Show API details")
          format: int32
      description: Specification for a voice served by ElevenLabs.
    ultravox.v1.CartesiaVoice:
      type: object
      properties:
        voiceId:
          type: string
          description: The ID of the voice in Cartesia.
        model:
          type: string
          description: The Cartesia model to use.
        speed:
          type: number
          description: >-
            (Deprecated) The speaking rate. Must be between -1 and 1. Defaults
            to 0.
          format: float
        emotion:
          type: string
          description: (Deprecated) Use generation_config.emotion instead.
        emotions:
          type: array
          items:
            type: string
          description: (Deprecated) Use generation_config.emotion instead.
        generationConfig:
          allOf:
            - $ref: >-
                #/components/schemas/ultravox.v1.CartesiaVoice_CartesiaGenerationConfig
          description: Configure the various attributes of the generated speech.
      description: >-
        Specification for a voice served by Cartesia. See
        https://docs.cartesia.ai/api-reference/tts/websocket
    ultravox.v1.LmntVoice:
      type: object
      properties:
        voiceId:
          type: string
          description: The ID of the voice in LMNT.
        model:
          type: string
          description: The LMNT model to use.
        speed:
          type: number
          description: |-
            The speaking rate. Must be between 0.25 and 2. Defaults to 1.
             See https://docs.lmnt.com/api-reference/speech/synthesize-speech-bytes#body-speed
          format: float
        conversational:
          type: boolean
          description: >-
            See
            https://docs.lmnt.com/api-reference/speech/synthesize-speech-bytes#body-conversational
      description: Specification for a voice served by LMNT.
    ultravox.v1.GoogleVoice:
      type: object
      properties:
        voiceId:
          type: string
          description: The ID (name) of the voice in Google, e.g. "en-US-Chirp3-HD-Charon".
        speakingRate:
          type: number
          description: |-
            The speaking rate. Must be between 0.25 and 2. Defaults to 1.
             See https://cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingAudioConfig
          format: float
      description: |-
        Specification for a voice served by Google.
         This implementation uses bidirectional streaming, so voices prior to Chirp3 are not supported.
    ultravox.v1.GenericVoice:
      type: object
      properties:
        url:
          type: string
          description: The endpoint to which requests are sent.
        headers:
          type: object
          additionalProperties:
            type: string
          description: Headers to include in the request.
        body:
          type: object
          description: >-
            The request body to send. Some field should include a placeholder
            for text
             represented as {text}. The placeholder will be replaced with the text to synthesize.
        responseSampleRate:
          type: integer
          description: The sample rate of the audio returned by the API.
          format: int32
        responseWordsPerMinute:
          type: integer
          description: >-
            An estimate of the speaking rate of the returned audio in words per
            minute. This is
             used for transcript timing while audio is streamed in the response. (Once the response
             is complete, Ultravox Realtime uses the real audio duration to adjust the timing.)
             Defaults to 150 and is unused for non-streaming responses.
          format: int32
        responseMimeType:
          type: string
          description: >-
            The real mime type of the content returned by the API. If unset, the
            Content-Type response header
             will be used. This is useful for APIs whose response bodies don't strictly adhere to what the
             API claims via header. For example, if your API claims to return audio/wav but omits the WAV
             header (thus really returning raw PCM), set this to audio/l16. Similarly, if your API claims to
             return JSON but actually streams JSON Lines, set this to application/jsonl.
        jsonAudioFieldPath:
          type: string
          description: >-
            For JSON responses, the path to the field containing base64-encoded
            audio data. The data must
             be PCM audio, optionally with a WAV header.
        jsonByteEncoding:
          enum:
            - JSON_BYTE_ENCODING_UNSPECIFIED
            - JSON_BYTE_ENCODING_BASE64
            - JSON_BYTE_ENCODING_HEX
          type: string
          description: >-
            For JSON responses, how audio bytes are encoded into the
            json_audio_field_path string.
             Defaults to base64. Also supports hex.
          format: enum
      description: >-
        Specification for a voice served by some generic REST-based TTS API. The
        API must
         accept an application/json POST request (as defined below) and return either WAV
         audio, raw PCM audio, or application/json with a base64 encoded audio data field
         that itself corresponds to WAV or raw PCM audio.
         Note that this simple API implies a lack of either input streaming or audio timing
         information, so more specific voice types are preferable when available.
    ultravox.v1.ElevenLabsVoice_PronunciationDictionaryReference:
      type: object
      properties:
        dictionaryId:
          type: string
          description: The dictionary's ID.
        versionId:
          type: string
          description: The dictionary's version.
      description: A reference to a pronunciation dictionary within ElevenLabs.
    ultravox.v1.CartesiaVoice_CartesiaGenerationConfig:
      type: object
      properties:
        volume:
          type: number
          description: >-
            Adjust the volume of the generated speech between 0.5x and 2.0x the
            original volume (default is 1.0x). Valid values are between [0.5,
            2.0] inclusive.
          format: float
        speed:
          type: number
          description: >-
            Adjust the speed of the generated speech between 0.6x and 2.0x the
            original speed (default is 1.0x). Valid values are between [0.6,
            1.5] inclusive.
          format: float
        emotion:
          type: string
          description: >-
            The primary emotions are neutral, calm, angry, content, sad, scared.
            For more options, see Prompting Sonic-3.
      description: Cartesia generation configuration for Sonic-3 and later models.
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt