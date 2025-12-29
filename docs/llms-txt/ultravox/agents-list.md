# Source: https://docs.ultravox.ai/api-reference/agents/agents-list.md

# List Agents

> Returns details for all agents



## OpenAPI

````yaml get /api/agents
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/agents:
    get:
      tags:
        - agents
      operationId: agents_list
      parameters:
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
        - in: query
          name: search
          schema:
            type: string
            minLength: 1
          description: The search string used to filter results
        - name: sort
          required: false
          in: query
          description: Which field to use when ordering the results.
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaginatedAgentList'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    PaginatedAgentList:
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
            $ref: '#/components/schemas/Agent'
        total:
          type: integer
          example: 123
    Agent:
      type: object
      properties:
        agentId:
          type: string
          format: uuid
          readOnly: true
        publishedRevisionId:
          type: string
          format: uuid
          readOnly: true
          nullable: true
        name:
          type: string
          maxLength: 64
        created:
          type: string
          format: date-time
          readOnly: true
        callTemplate:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CallTemplate'
          nullable: true
        statistics:
          allOf:
            - $ref: '#/components/schemas/AgentStatistics'
          readOnly: true
      required:
        - agentId
        - created
        - publishedRevisionId
        - statistics
    ultravox.v1.CallTemplate:
      type: object
      properties:
        name:
          type: string
          description: The name of the call template.
        created:
          type: string
          description: When the call template was created.
          format: date-time
        updated:
          type: string
          description: When the call template was last modified.
          format: date-time
        medium:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CallMedium'
          description: The medium used for calls by default.
        initialOutputMedium:
          enum:
            - MESSAGE_MEDIUM_UNSPECIFIED
            - MESSAGE_MEDIUM_VOICE
            - MESSAGE_MEDIUM_TEXT
          type: string
          description: The medium initially used for calls by default. Defaults to voice.
          format: enum
        joinTimeout:
          pattern: ^-?(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,9})?s$
          type: string
          description: A default timeout for joining calls. Defaults to 30 seconds.
        maxDuration:
          pattern: ^-?(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,9})?s$
          type: string
          description: The default maximum duration of calls. Defaults to 1 hour.
        vadSettings:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.VadSettings'
          description: The default voice activity detection settings for calls.
        recordingEnabled:
          type: boolean
          description: Whether calls are recorded by default.
        firstSpeakerSettings:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.FirstSpeakerSettings'
          description: >-
            The default settings for the initial message to get a conversation
            started for calls.
             Defaults to `agent: {}` which means the agent will start the conversation with an
             (interruptible) greeting generated based on the system prompt and any initial messages.
        systemPrompt:
          type: string
          description: |-
            The system prompt used for generations.
             If multiple stages are defined for the call, this will be used only for stages without their own systemPrompt.
        temperature:
          type: number
          description: |-
            The model temperature, between 0 and 1. Defaults to 0.
             If multiple stages are defined for the call, this will be used only for stages without their own temperature.
          format: float
        model:
          type: string
          description: |-
            The model used for generations. Currently defaults to ultravox-v0.6.
             If multiple stages are defined for the call, this will be used only for stages without their own model.
        voice:
          type: string
          description: |-
            The name or ID of the voice the agent should use for calls.
             If multiple stages are defined for the call, this will be used only for stages without their own voice (or external_voice).
        externalVoice:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.ExternalVoice'
          description: >-
            A voice not known to Ultravox Realtime that can nonetheless be used
            for calls with this agent.
             Your account must have an API key set for the provider of the voice.
             Either this or `voice` may be set, but not both.
        languageHint:
          type: string
          description: >-
            A BCP47 language code that may be used to guide speech recognition
            and synthesis.
             If multiple stages are defined for the call, this will be used only for stages without their own languageHint.
        timeExceededMessage:
          type: string
          description: >-
            What the agent should say immediately before hanging up if the
            call's time limit is reached.
             If multiple stages are defined for the call, this will be used only for stages without their own timeExceededMessage.
        inactivityMessages:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.TimedMessage'
          description: >-
            Messages spoken by the agent when the user is inactive for the
            specified duration.
             Durations are cumulative, so a message m > 1 with duration 30s will be spoken 30 seconds after message m-1.
             If multiple stages are defined for the call, this will be used only for stages without their own inactivityMessages.
        selectedTools:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.SelectedTool'
          description: |-
            The tools available to the agent for this call.
             The following fields are treated as templates when converting to a CallTool.
               * description
               * static_parameters.value
               * http.auth_headers.value
               * http.auth_query_params.value
             If multiple stages are defined for the call, this will be used only for stages without their own selectedTools.
        dataConnection:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.DataConnectionConfig'
          description: Data connection configuration for calls created with this agent.
        contextSchema:
          type: object
          description: >-
            JSON schema for the variables used in string templates. If unset, a
            default schema will
             be created from the variables used in the string templates.
             Call creation requests must provide context adhering to this schema.
             The follow fields are treated as templates:
               * system_prompt
               * language_hint
               * time_exceeded_message
               * inactivity_messages.message
               * selected_tools.description
               * selected_tools.static_parameters.value
               * selected_tools.http.auth_headers.value
               * selected_tools.http.auth_query_params.value
             If multiple stages are defined for the call, each must define its own context schema (or use the generated one).
      description: >-
        A CallTemplate that can be used to create Ultravox calls with shared
        properties.
    AgentStatistics:
      type: object
      properties:
        calls:
          type: integer
          readOnly: true
          default: 0
      required:
        - calls
    ultravox.v1.CallMedium:
      type: object
      properties:
        webRtc:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CallMedium_WebRtcMedium'
          description: |-
            The call will use WebRTC with the Ultravox client SDK.
             This is the default.
        twilio:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CallMedium_TwilioMedium'
          description: |-
            The call will use Twilio's "Media Streams" protocol.
             Once you have a join URL from starting a call, include it in your
             TwiML like so:
             <Connect><Stream url=${your-join-url} /></Connect>
             This works for both inbound and outbound calls.
        serverWebSocket:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CallMedium_WebSocketMedium'
          description: >-
            The call will use a plain websocket connection. This is unlikely to
            yield an acceptable user
             experience if used from a browser or mobile client, but may be suitable for a
             server-to-server connection. This option provides a simple way to connect your own server to
             an Ultravox inference instance.
        telnyx:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CallMedium_TelnyxMedium'
          description: |-
            The call will use Telnyx's media streaming protocol.
             Once you have a join URL from starting a call, include it in your
             TexML like so:
             <Connect><Stream url=${your-join-url} bidirectionalMode="rtp" /></Connect>
             This works for both inbound and outbound calls.
        plivo:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CallMedium_PlivoMedium'
          description: |-
            The call will use Plivo's AudioStreams protocol.
             Once you have a join URL from starting a call, include it in your
             Plivo XML like so:
             <Stream keepCallAlive="true" bidirectional="true" contentType="audio/x-l16;rate=16000">${your-join-url}</Stream>
             This works for both inbound and outbound calls.
        exotel:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CallMedium_ExotelMedium'
          description: |-
            The call will use Exotel's "Voicebot" protocol.
             Once you have a join URL from starting a call, provide it to Exotel as the wss target URL
             for your Voicebot (either directly or more likely dynamically from your own server).
        sip:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CallMedium_SipMedium'
          description: >-
            The call will be connected using Session Initiation Protocol (SIP).
            Note that SIP incurs
             additional charges and must be enabled for your account.
      description: >-
        Details about a call's protocol. By default, calls occur over WebRTC
        using
         the Ultravox client SDK. Setting a different call medium will prepare the
         server for a call using a different protocol.
         At most one call medium may be set.
    ultravox.v1.VadSettings:
      type: object
      properties:
        turnEndpointDelay:
          pattern: ^-?(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,9})?s$
          type: string
          description: >-
            The minimum amount of time the agent will wait to respond after the
            user seems to be done
             speaking. Increasing this value will make the agent less eager to respond, which may increase
             perceived response latency but will also make the agent less likely to jump in before the user
             is really done speaking.

             Built-in VAD currently operates on 32ms frames, so only multiples of 32ms are meaningful.
             (Anything from 1ms to 31ms will produce the same result.)

             Defaults to "0.384s" (384ms) as a starting point, but there's nothing special about this value
             aside from it corresponding to 12 VAD frames.
        minimumTurnDuration:
          pattern: ^-?(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,9})?s$
          type: string
          description: >-
            The minimum duration of user speech required to be considered a user
            turn.
             Increasing this value will cause the agent to ignore short user audio. This may be useful in
             particularly noisy environments, but it comes at the cost of possibly ignoring very short
             user responses such as "yes" or "no".

             Defaults to "0s" meaning the agent considers all user audio inputs (that make it through
             built-in noise cancellation).
        minimumInterruptionDuration:
          pattern: ^-?(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,9})?s$
          type: string
          description: >-
            The minimum duration of user speech required to interrupt the agent.
            This works the same way
             as minimumTurnDuration, but allows for a higher threshold for interrupting the agent. (This
             value will be ignored if it is less than minimumTurnDuration.)

             Defaults to "0.09s" (90ms) as a starting point, but there's nothing special about this value.
        frameActivationThreshold:
          type: number
          description: >-
            The threshold for the VAD to consider a frame as speech. This is a
            value between 0.1 and 1.

             Miniumum value is 0.1, which is the default value.
          format: float
      description: Call-level VAD settings.
    ultravox.v1.FirstSpeakerSettings:
      type: object
      properties:
        user:
          allOf:
            - $ref: >-
                #/components/schemas/ultravox.v1.FirstSpeakerSettings_UserGreeting
          description: If set, the user should speak first.
        agent:
          allOf:
            - $ref: >-
                #/components/schemas/ultravox.v1.FirstSpeakerSettings_AgentGreeting
          description: If set, the agent should speak first.
      description: |-
        Settings for the initial message to get a conversation started.
         Exactly one of user or agent should be set. The default is agent
         (unless firstSpeaker is also set, in which case the default will
         match that).
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
    ultravox.v1.SelectedTool:
      type: object
      properties:
        toolId:
          type: string
          description: The ID of an existing base tool.
        toolName:
          type: string
          description: >-
            The name of an existing base tool. The name must uniquely identify
            the tool.
        temporaryTool:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.BaseToolDefinition'
          description: >-
            A temporary tool definition, available only for this call (and
            subsequent
             calls created using priorCallId without overriding selected tools). Exactly one
             implementation (http or client) should be set. See the 'Base Tool Definition'
             schema for more details.
        nameOverride:
          type: string
          description: >-
            An override for the model_tool_name. This is primarily useful when
            using
             multiple instances of the same durable tool (presumably with different
             parameter overrides.) The set of tools used within a call must have a unique
             set of model names and every name must match this pattern: ^[a-zA-Z0-9_-]{1,64}$.
        descriptionOverride:
          type: string
          description: >-
            An override for the tool's description, as presented to the model.
            This is primarily
             useful when using a built-in tool whose description you want to tweak to better fit
             the rest of your prompt.
        authTokens:
          type: object
          additionalProperties:
            type: string
          description: Auth tokens used to satisfy the tool's security requirements.
        parameterOverrides:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/google.protobuf.Value'
          description: >-
            Static values to use in place of dynamic parameters. Any parameter
            included
             here will be hidden from the model and the static value will be used instead.
             Some tools may require certain parameters to be overridden, but any parameter
             can be overridden regardless of whether it is required to be.
        transitionId:
          type: string
          description: >-
            For internal use. Relates this tool to a stage transition definition
            within a call template for attribution.
      description: >-
        A tool selected for a particular call. Exactly one of tool_id,
        tool_name, or
         temporary_tool should be set.
    ultravox.v1.DataConnectionConfig:
      type: object
      properties:
        websocketUrl:
          type: string
          description: >-
            The websocket URL to which the session will connect to stream data
            messages.
        audioConfig:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.DataConnectionAudioConfig'
          description: >-
            Audio configuration for the data connection. If not set, no audio
            will be sent.
        dataMessages:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.EnabledDataMessages'
          description: Controls which data messages are enabled for the data connection.
      description: >-
        Data connection enables an auxiliary websocket for streaming data
        messages.
    ultravox.v1.CallMedium_WebRtcMedium:
      type: object
      properties:
        dataMessages:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.EnabledDataMessages'
          description: Controls which data messages are enabled for the call.
      description: Details for a WebRTC call.
    ultravox.v1.CallMedium_TwilioMedium:
      type: object
      properties:
        outgoing:
          allOf:
            - $ref: >-
                #/components/schemas/ultravox.v1.TwilioMedium_OutgoingRequestParams
          description: >-
            If set, Ultravox will directly create a call with Twilio. Twilio
            must be configured
             for the requesting account.
      description: Details for a Twilio call.
    ultravox.v1.CallMedium_WebSocketMedium:
      type: object
      properties:
        inputSampleRate:
          type: integer
          description: The sample rate for input (user) audio. Required.
          format: int32
        outputSampleRate:
          type: integer
          description: >-
            The desired sample rate for output (agent) audio. If unset, defaults
            to the input_sample_rate.
          format: int32
        clientBufferSizeMs:
          type: integer
          description: >-
            The size of the client-side audio buffer in milliseconds. Smaller
            buffers allow for faster
             interruptions but may cause audio underflow if network latency fluctuates too greatly. For
             the best of both worlds, set this to some large value (e.g. 30000) and implement support for
             playback_clear_buffer messages. Defaults to 60.
          format: int32
        dataMessages:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.EnabledDataMessages'
          description: Controls which data messages are enabled for the call.
      description: Details for a WebSocket call.
    ultravox.v1.CallMedium_TelnyxMedium:
      type: object
      properties:
        outgoing:
          allOf:
            - $ref: >-
                #/components/schemas/ultravox.v1.TelnyxMedium_OutgoingRequestParams
          description: >-
            If set, Ultravox will directly create a call with Telnyx. Telnyx
            must be configured
             for the requesting account.
      description: Details for a Telnyx call.
    ultravox.v1.CallMedium_PlivoMedium:
      type: object
      properties:
        outgoing:
          allOf:
            - $ref: >-
                #/components/schemas/ultravox.v1.PlivoMedium_OutgoingRequestParams
          description: >-
            If set, Ultravox will directly create a call with Plivo. Plivo must
            be configured
             for the requesting account.
      description: Details for a Plivo call.
    ultravox.v1.CallMedium_ExotelMedium:
      type: object
      properties: {}
      description: Details for a Exotel call.
    ultravox.v1.CallMedium_SipMedium:
      type: object
      properties:
        incoming:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.SipMedium_SipIncoming'
          description: Details for an incoming SIP call.
        outgoing:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.SipMedium_SipOutgoing'
          description: >-
            Details for an outgoing SIP call. Ultravox will initiate this call
            (and there will be no joinUrl).
      description: Details for a SIP call. Exactly one of incoming or outgoing must be set.
    ultravox.v1.FirstSpeakerSettings_UserGreeting:
      type: object
      properties:
        fallback:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.FallbackAgentGreeting'
          description: >-
            If set, the agent will start the conversation itself if the user
            doesn't start
             speaking within the given delay.
      description: Additional properties for when the user speaks first.
    ultravox.v1.FirstSpeakerSettings_AgentGreeting:
      type: object
      properties:
        uninterruptible:
          type: boolean
          description: >-
            Whether the user should be prevented from interrupting the agent's
            first message.
             Defaults to false (meaning the agent is interruptible as usual).
        text:
          type: string
          description: A specific greeting the agent should say.
        prompt:
          type: string
          description: A prompt for the agent to generate a greeting.
        delay:
          pattern: ^-?(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,9})?s$
          type: string
          description: >-
            If set, the agent will wait this long before starting its greeting.
            This may be useful
             for ensuring the user is ready.
      description: Additional properties for when the agent speaks first.
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
    ultravox.v1.BaseToolDefinition:
      type: object
      properties:
        modelToolName:
          type: string
          description: >-
            The name of the tool, as presented to the model. Must match
            ^[a-zA-Z0-9_-]{1,64}$.
        description:
          type: string
          description: The description of the tool.
        dynamicParameters:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.DynamicParameter'
          description: The parameters that the tool accepts.
        staticParameters:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.StaticParameter'
          description: The static parameters added when the tool is invoked.
        automaticParameters:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.AutomaticParameter'
          description: >-
            Additional parameters that are automatically set by the system when
            the tool is invoked.
        requirements:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.ToolRequirements'
          description: >-
            Requirements that must be fulfilled when creating a call for the
            tool to be used.
        timeout:
          pattern: ^-?(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,9})?s$
          type: string
          description: >-
            The maximum amount of time the tool is allowed for execution. The
            conversation is frozen
             while tools run, so prefer sticking to the default unless you're comfortable with that
             consequence. If your tool is too slow for the default and can't be made faster, still try to
             keep this timeout as low as possible.
        precomputable:
          type: boolean
          description: >-
            The tool is guaranteed to be non-mutating, repeatable, and free of
            side-effects. Such tools
             can safely be executed speculatively, reducing their effective latency. However, the fact they
             were called may not be reflected in the call history if their result ends up unused.
        http:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.BaseHttpToolDetails'
          description: Details for an HTTP tool.
        client:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.BaseClientToolDetails'
          description: >-
            Details for a client-implemented tool. Only body parameters are
            allowed
             for client tools.
        dataConnection:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.BaseDataConnectionToolDetails'
          description: >-
            Details for a tool implemented via a data connection websocket. Only
            body
             parameters are allowed for data connection tools.
        defaultReaction:
          enum:
            - AGENT_REACTION_UNSPECIFIED
            - AGENT_REACTION_SPEAKS
            - AGENT_REACTION_LISTENS
            - AGENT_REACTION_SPEAKS_ONCE
          type: string
          description: >-
            Indicates the default for how the agent should proceed after the
            tool is invoked.
             Can be overridden by the tool implementation via the X-Ultravox-Agent-Reaction
             header.
          format: enum
        staticResponse:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.StaticToolResponse'
          description: >-
            Static response to a tool. When this is used, this response will be
            returned
             without waiting for the tool's response.
      description: >-
        The base definition of a tool that can be used during a call. Exactly
        one
         implementation (http or client) should be set.
    google.protobuf.Value:
      description: >-
        Represents a dynamically typed value which can be either null, a number,
        a string, a boolean, a recursive struct value, or a list of values.
    ultravox.v1.DataConnectionAudioConfig:
      type: object
      properties:
        sampleRate:
          type: integer
          description: >-
            The sample rate of the audio stream. If not set, will default to
            16000.
          format: int32
        channelMode:
          enum:
            - CHANNEL_MODE_UNSPECIFIED
            - CHANNEL_MODE_MIXED
            - CHANNEL_MODE_SEPARATED
          type: string
          description: >-
            The audio channel mode to use. CHANNEL_MODE_MIXED will combine user
            and agent audio
             into a single mono output while CHANNEL_MODE_SEPARATED will result in stereo audio
             where user and agent are separated. The latter is the default.
          format: enum
      description: Configuration for audio in data connections
    ultravox.v1.EnabledDataMessages:
      type: object
      properties:
        pong:
          type: boolean
          description: 'Responds to a ping message. (Default: enabled)'
        state:
          type: boolean
          description: 'Indicates that the agent state has changed. (Default: enabled)'
        transcript:
          type: boolean
          description: >-
            Provides transcripts of the user and agent speech. (Default:
            enabled)
        clientToolInvocation:
          type: boolean
          description: 'Requests a client-implemented tool invocation. (Default: enabled)'
        dataConnectionToolInvocation:
          type: boolean
          description: >-
            Requests a data-connection-implemented tool invocation. (Default:
            enabled for data connections, disabled otherwise)
        playbackClearBuffer:
          type: boolean
          description: >-
            Requests the client-side audio buffer to be cleared. (Default:
            enabled for websocket connections, disabled otherwise)
        callStarted:
          type: boolean
          description: >-
            Provides information about the call when it starts. (Default:
            enabled)
        debug:
          type: boolean
          description: 'Communicates debug information. (Default: disabled)'
        callEvent:
          type: boolean
          description: 'Indicates that a call event has been recorded. (Default: disabled)'
        toolUsed:
          type: boolean
          description: 'Indicates that a tool was used. (Default: disabled)'
        userStartedSpeaking:
          type: boolean
          description: >-
            Indicates that the user has started speaking (according to simple
            VAD). (Default: disabled)
        userStoppedSpeaking:
          type: boolean
          description: >-
            Indicates that the user has stopped speaking (according to simple
            VAD). (Default: disabled)
      description: Whether certain data messages are enabled for a connection.
    ultravox.v1.TwilioMedium_OutgoingRequestParams:
      type: object
      properties:
        to:
          type: string
          description: >-
            The phone number, in E.164 format (e.g. +14155552671), (or sip
            address) to call.
        from:
          type: string
          description: >-
            The phone number or client identifier to use as the caller id. If
            `to` is a phone
             number, `from` must be a phone number owned by your Twilio account.
        additionalParams:
          type: object
          description: >-
            Additional parameters to include in the Twilio call creation
            request.
             See https://www.twilio.com/docs/voice/api/call-resource#request-body-parameters
      description: Parameters for a Twilio call creation request.
    ultravox.v1.TelnyxMedium_OutgoingRequestParams:
      type: object
      properties:
        to:
          type: string
          description: The phone number to call in E.164 format (e.g. +14155552671).
        from:
          type: string
          description: The phone number initiating the call.
        additionalParams:
          type: object
          description: >-
            Additional parameters to include in the Telnyx call creation
            request.
             See https://developers.telnyx.com/api/call-scripting/initiate-texml-call
      description: Parameters for a Telnyx call creation request.
    ultravox.v1.PlivoMedium_OutgoingRequestParams:
      type: object
      properties:
        to:
          type: string
          description: >-
            The phone number(s) or sip URI(s) to call, separated by `<` if
            multiple.
        from:
          type: string
          description: >-
            The phone number initiating the call, in E.164 format (e.g.
            +14155552671).
        additionalParams:
          type: object
          description: |-
            Additional parameters to include in the Plivo call creation request.
             See https://www.plivo.com/docs/voice/api/call/make-a-call
      description: Parameters for a Plivo call creation request.
    ultravox.v1.SipMedium_SipIncoming:
      type: object
      properties: {}
      description: Details for an incoming SIP call.
    ultravox.v1.SipMedium_SipOutgoing:
      type: object
      properties:
        to:
          type: string
          description: The SIP URI to connect to. (Phone numbers are not allowed.)
        from:
          type: string
          description: >-
            The SIP URI to connect from. This is the "from" field in the SIP
            INVITE.
        username:
          type: string
          description: The SIP username to use for authentication.
        password:
          type: string
          description: The password for the specified username.
      description: Details for an outgoing SIP call.
    ultravox.v1.FallbackAgentGreeting:
      type: object
      properties:
        delay:
          pattern: ^-?(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,9})?s$
          type: string
          description: >-
            How long the agent should wait before starting the conversation
            itself.
        text:
          type: string
          description: A specific greeting the agent should say.
        prompt:
          type: string
          description: A prompt for the agent to generate a greeting.
      description: >-
        A fallback for the case when the user is expected to speak first but
        doesn't.
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
    ultravox.v1.DynamicParameter:
      type: object
      properties:
        name:
          type: string
          description: The name of the parameter.
        location:
          enum:
            - PARAMETER_LOCATION_UNSPECIFIED
            - PARAMETER_LOCATION_QUERY
            - PARAMETER_LOCATION_PATH
            - PARAMETER_LOCATION_HEADER
            - PARAMETER_LOCATION_BODY
          type: string
          description: Where the parameter is used.
          format: enum
        schema:
          type: object
          description: |-
            The JsonSchema definition of the parameter. This typically
             includes things like type, description, enum values, format,
             other restrictions, etc.
        required:
          type: boolean
          description: Whether the parameter is required.
      description: A dynamic parameter the tool accepts that may be set by the model.
    ultravox.v1.StaticParameter:
      type: object
      properties:
        name:
          type: string
          description: The name of the parameter.
        location:
          enum:
            - PARAMETER_LOCATION_UNSPECIFIED
            - PARAMETER_LOCATION_QUERY
            - PARAMETER_LOCATION_PATH
            - PARAMETER_LOCATION_HEADER
            - PARAMETER_LOCATION_BODY
          type: string
          description: Where the parameter is used.
          format: enum
        value:
          allOf:
            - $ref: '#/components/schemas/google.protobuf.Value'
          description: The value of the parameter.
      description: >-
        A static parameter that is unconditionally added when the tool is
        invoked. This
         parameter is not exposed to or set by the model.
    ultravox.v1.AutomaticParameter:
      type: object
      properties:
        name:
          type: string
          description: The name of the parameter.
        location:
          enum:
            - PARAMETER_LOCATION_UNSPECIFIED
            - PARAMETER_LOCATION_QUERY
            - PARAMETER_LOCATION_PATH
            - PARAMETER_LOCATION_HEADER
            - PARAMETER_LOCATION_BODY
          type: string
          description: Where the parameter is used.
          format: enum
        knownValue:
          enum:
            - KNOWN_PARAM_UNSPECIFIED
            - KNOWN_PARAM_CALL_ID
            - KNOWN_PARAM_CONVERSATION_HISTORY
            - KNOWN_PARAM_OUTPUT_SAMPLE_RATE
            - KNOWN_PARAM_CALL_STATE
            - KNOWN_PARAM_CALL_STAGE_ID
          type: string
          description: The value to set for the parameter.
          format: enum
      description: A parameter that is automatically set by the system.
    ultravox.v1.ToolRequirements:
      type: object
      properties:
        httpSecurityOptions:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.SecurityOptions'
          description: Security requirements for an HTTP tool.
        requiredParameterOverrides:
          type: array
          items:
            type: string
          description: >-
            Dynamic parameters that must be overridden with an explicit (static)
            value.
      description: >-
        The requirements for using a tool, which must be satisfied when creating
        a call with the tool.
    ultravox.v1.BaseHttpToolDetails:
      type: object
      properties:
        baseUrlPattern:
          type: string
          description: >-
            The base URL pattern for the tool, possibly with placeholders for
            path parameters.
        httpMethod:
          type: string
          description: The HTTP method for the tool.
      description: Details for invoking a tool via HTTP.
    ultravox.v1.BaseClientToolDetails:
      type: object
      properties: {}
      description: Details for invoking a tool expected to be implemented by the client.
    ultravox.v1.BaseDataConnectionToolDetails:
      type: object
      properties: {}
      description: Details for invoking a tool via a data connection.
    ultravox.v1.StaticToolResponse:
      type: object
      properties:
        responseText:
          type: string
          description: The predefined text response to be returned immediately
      description: >-
        A predefined, static response for a tool. When a tool has a static
        response, it
         can be returned immediately, without waiting for full tool execution.
    ultravox.v1.SecurityOptions:
      type: object
      properties:
        options:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.SecurityRequirements'
          description: >-
            The options for security. Only one must be met. The first one that
            can be
             satisfied will be used in general. The single exception to this rule is
             that we always prefer a non-empty set of requirements over an empty set
             unless no non-empty set can be satisfied.
      description: The different options for satisfying a tool's security requirements.
    ultravox.v1.SecurityRequirements:
      type: object
      properties:
        requirements:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ultravox.v1.SecurityRequirement'
          description: Requirements keyed by name.
        ultravoxCallTokenRequirement:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.UltravoxCallTokenRequirement'
          description: >-
            An additional special security requirement that can be automatically
            fulfilled
             during call creation. If a tool has this requirement set, a token identifying
             the call and relevant scopes will be created during call creation and set as
             an X-Ultravox-Call-Token header when the tool is invoked.
             Such tokens are only verifiable by the Ultravox service and primarily exist
             for built-in tools (though it's possible for third-party tools that wrap a
             built-in tool to make use of them as well).
      description: The security requirements for a request. All requirements must be met.
    ultravox.v1.SecurityRequirement:
      type: object
      properties:
        queryApiKey:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.QueryApiKeyRequirement'
          description: An API key must be added to the query string.
        headerApiKey:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.HeaderApiKeyRequirement'
          description: An API key must be added to a custom header.
        httpAuth:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.HttpAuthRequirement'
          description: The HTTP authentication header must be added.
      description: >-
        A single security requirement that must be met for a tool to be
        available. Exactly one
         of query_api_key, header_api_key, or http_auth should be set.
    ultravox.v1.UltravoxCallTokenRequirement:
      type: object
      properties:
        scopes:
          type: array
          items:
            type: string
          description: The scopes that must be present in the token.
      description: >-
        A security requirement that will automatically be fulfilled during call
        creation.
         The generated token will be set as an X-Ultravox-Call-Token header when the tool
         is invoked. The token is only verifiable by the Ultravox service and should not be
         used for authentication by any other service.
         The token will also be invalid as soon as the call is completed.
    ultravox.v1.QueryApiKeyRequirement:
      type: object
      properties:
        name:
          type: string
          description: The name of the query parameter.
      description: >-
        A security requirement that will cause an API key to be added to the
        query string.
    ultravox.v1.HeaderApiKeyRequirement:
      type: object
      properties:
        name:
          type: string
          description: The name of the header.
      description: >-
        A security requirement that will cause an API key to be added to the
        header.
    ultravox.v1.HttpAuthRequirement:
      type: object
      properties:
        scheme:
          type: string
          description: The scheme of the HTTP authentication, e.g. "Bearer".
      description: >-
        A security requirement that will cause an HTTP authentication header to
        be added.
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt