# Source: https://docs.ultravox.ai/api-reference/voices/voices-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Voices

> Retrieves all available voices



## OpenAPI

````yaml get /api/voices
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/voices:
    get:
      tags:
        - voices
      description: List all voices in your account.
      operationId: voices_list
      parameters:
        - in: query
          name: billingStyle
          schema:
            enum:
              - VOICE_BILLING_STYLE_INCLUDED
              - VOICE_BILLING_STYLE_EXTERNAL
            type: string
            minLength: 1
          description: >-
            The billing style used to filter results.


            * `VOICE_BILLING_STYLE_INCLUDED` - Voices with no additional charges
            beyond the cost of the call

            * `VOICE_BILLING_STYLE_EXTERNAL` - Voices with costs billed directly
            by the TTS provider
        - name: cursor
          required: false
          in: query
          description: The pagination cursor value.
          schema:
            type: string
        - in: query
          name: ownership
          schema:
            enum:
              - private
              - public
            type: string
            minLength: 1
          description: |-
            The ownership used to filter results.

            * `private` - Only private voices
            * `public` - Only public voices
        - name: pageSize
          required: false
          in: query
          description: Number of results to return per page.
          schema:
            type: integer
        - in: query
          name: primaryLanguage
          schema:
            type: string
            minLength: 1
          description: >-
            The desired primary language for voice results using BCP47. Voices
            with different regions/scripts/variants but the same language tag
            may also be included but will be further down the results. If not
            provided, all languages are included.
        - in: query
          name: provider
          schema:
            type: array
            items:
              enum:
                - lmnt
                - cartesia
                - google
                - respeecher
                - eleven_labs
                - inworld
              type: string
              description: |-
                * `lmnt` - LMNT
                * `cartesia` - Cartesia
                * `google` - Google
                * `respeecher` - Respeecher
                * `eleven_labs` - Eleven Labs
                * `inworld` - Inworld
          description: The providers used to filter results.
        - in: query
          name: search
          schema:
            type: string
            minLength: 1
          description: The search string used to filter results.
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaginatedVoiceList'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    PaginatedVoiceList:
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
            $ref: '#/components/schemas/Voice'
        total:
          type: integer
          example: 123
    Voice:
      type: object
      properties:
        voiceId:
          type: string
          format: uuid
          readOnly: true
        name:
          type: string
          maxLength: 40
        description:
          type: string
          nullable: true
          maxLength: 240
        primaryLanguage:
          type: string
          nullable: true
          description: >-
            BCP47 language code for the primary language supported by this
            voice.
          maxLength: 10
        languageLabel:
          type: string
          nullable: true
          readOnly: true
          description: >-
            Human-readable language label with flag emoji and English name
            (e.g., '🇺🇸 English (United States)').
        previewUrl:
          format: uri
          type: string
          readOnly: true
        ownership:
          allOf:
            - $ref: '#/components/schemas/OwnershipEnum'
          readOnly: true
        billingStyle:
          allOf:
            - $ref: '#/components/schemas/BillingStyleEnum'
          readOnly: true
          description: >-
            How billing works for this voice.

            VOICE_BILLING_STYLE_INCLUDED - The cost of this voice is included in
            the call cost. There are no additional charges for it.

            VOICE_BILLING_STYLE_EXTERNAL - This voice requires an API key for
            its provider, who will bill for usage separately.
        provider:
          type: string
          readOnly: true
          nullable: true
        definition:
          $ref: '#/components/schemas/ultravox.v1.ExternalVoice'
      required:
        - billingStyle
        - definition
        - languageLabel
        - name
        - ownership
        - previewUrl
        - provider
        - voiceId
    OwnershipEnum:
      enum:
        - public
        - private
      type: string
    BillingStyleEnum:
      enum:
        - VOICE_BILLING_STYLE_INCLUDED
        - VOICE_BILLING_STYLE_EXTERNAL
      type: string
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
        inworld:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.InworldVoice'
          description: |-
            A voice served by Inworld, using bidirectional streaming.
             (For non-streaming or output-only streaming, use generic.)
        respeecher:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.RespeecherVoice'
          description: A voice served by Respeecher, using bidirectional streaming.
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
    ultravox.v1.InworldVoice:
      type: object
      properties:
        voiceId:
          type: string
          description: The ID of the voice in Inworld.
        modelId:
          type: string
          description: >-
            The ID of the model to use for generations, e.g.
            "inworld-tts-1-max".
             See https://docs.inworld.ai/docs/tts/tts-models
        speakingRate:
          type: number
          description: |-
            The speaking rate. Must be between 0.5 and 1.5. Defaults to 1.
             See https://docs.inworld.ai/api-reference/ttsAPI/texttospeech/synthesize-speech-stream#body-audio-config-speaking-rate
          format: float
        temperature:
          type: number
          description: >-
            How much randomness to use when sampling audio tokens. Must be
            between 0.0 and 2.0.
             See https://docs.inworld.ai/api-reference/ttsAPI/texttospeech/synthesize-speech-stream#body-temperature
          format: float
        applyTextNormalization:
          type: boolean
          description: >-
            Whether or not to apply text normalization. This should typically
            only be disabled if the
             agent is instructed to normalize text directly.
             See https://docs.inworld.ai/api-reference/ttsAPI/texttospeech/synthesize-speech-stream#body-apply-text-normalization.
      description: Specification for a voice served by Inworld.
    ultravox.v1.RespeecherVoice:
      type: object
      properties:
        voiceId:
          type: string
          description: The ID of the voice in Respeecher.
        seed:
          type: integer
          description: Random seed for reproducible generation.
          format: int32
        temperature:
          type: number
          description: >-
            Controls randomness of the output. Higher values produce more varied
            speech.
             If set, must be greater than or equal to 0.0.
          format: float
        topK:
          type: integer
          description: |-
            Limits sampling to the top K most likely tokens.
             If set, must be exactly -1 or greater than 0.
          format: int32
        topP:
          type: number
          description: >-
            Limits sampling to tokens with cumulative probability up to this
            value.
             If set, must be greater than 0 and less than or equal to 1.0.
          format: float
        minP:
          type: number
          description: |-
            Minimum probability threshold for token sampling.
             If set, must be between 0.0 and 1.0, inclusive.
          format: float
        presencePenalty:
          type: number
          description: |-
            Penalty for tokens already present in the context.
             If set, must be between 0 and 2, inclusive.
          format: float
        repetitionPenalty:
          type: number
          description: |-
            Penalty for repeating tokens.
             If set, must be between 1 and 2, inclusive.
          format: float
        frequencyPenalty:
          type: number
          description: |-
            Penalty based on token frequency.
             If set, must be between 0 and 2, inclusive.
          format: float
      description: |-
        Specification for a voice served by Respeecher.
         See https://space.respeecher.com/docs/api/tts/sampling-params-guide
         for parameter guidance.
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
        pronunciationDictId:
          type: string
          description: |-
            The ID of a pronunciation dictionary to use for the generation.
             Pronunciation dictionaries are supported by sonic-3 models and newer.
             See https://docs.cartesia.ai/build-with-cartesia/capability-guides/specify-custom-pronunciations
      description: Cartesia generation configuration for Sonic-3 and later models.
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````