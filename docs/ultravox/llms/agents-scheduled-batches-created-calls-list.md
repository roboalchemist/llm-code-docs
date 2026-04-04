# Source: https://docs.ultravox.ai/api-reference/agents/agents-scheduled-batches-created-calls-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Scheduled Call Batch Created Calls

> Returns details for all created calls in a scheduled call batch



## OpenAPI

````yaml get /api/agents/{agent_id}/scheduled_batches/{batch_id}/created_calls
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/agents/{agent_id}/scheduled_batches/{batch_id}/created_calls:
    get:
      tags:
        - agents
      operationId: agents_scheduled_batches_created_calls_list
      parameters:
        - in: path
          name: agent_id
          schema:
            type: string
            format: uuid
          required: true
        - in: path
          name: batch_id
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
                $ref: '#/components/schemas/PaginatedCallList'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    PaginatedCallList:
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
            $ref: '#/components/schemas/Call'
        total:
          type: integer
          example: 123
    Call:
      type: object
      properties:
        callId:
          type: string
          format: uuid
          readOnly: true
        clientVersion:
          type: string
          readOnly: true
          nullable: true
          description: The version of the client that joined this call.
        created:
          type: string
          format: date-time
          readOnly: true
        joined:
          type: string
          format: date-time
          readOnly: true
          nullable: true
        ended:
          type: string
          format: date-time
          readOnly: true
          nullable: true
        endReason:
          readOnly: true
          nullable: true
          description: |-
            The reason the call ended.

            * `unjoined` - Client never joined
            * `hangup` - Client hung up
            * `agent_hangup` - Agent hung up
            * `timeout` - Call timed out
            * `connection_error` - Connection error
            * `system_error` - System error
          oneOf:
            - $ref: '#/components/schemas/EndReasonEnum'
            - $ref: '#/components/schemas/NullEnum'
        billedDuration:
          type: string
          readOnly: true
          nullable: true
        billedSideInputTokens:
          type: integer
          readOnly: true
          nullable: true
        billedSideOutputTokens:
          type: integer
          readOnly: true
          nullable: true
        billingStatus:
          allOf:
            - $ref: '#/components/schemas/BillingStatusEnum'
          readOnly: true
        firstSpeaker:
          allOf:
            - $ref: '#/components/schemas/FirstSpeakerEnum'
          deprecated: true
          readOnly: true
          description: >-
            Who was supposed to talk first when the call started. Typically set
            to FIRST_SPEAKER_USER for outgoing calls and left as the default
            (FIRST_SPEAKER_AGENT) otherwise.
        firstSpeakerSettings:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.FirstSpeakerSettings'
          description: Settings for the initial message to get the call started.
        inactivityMessages:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.TimedMessage'
          description: >-
            Messages spoken by the agent when the user is inactive for the
            specified duration. Durations are cumulative, so a message m > 1
            with duration 30s will be spoken 30 seconds after message m-1.
        initialOutputMedium:
          allOf:
            - $ref: '#/components/schemas/InitialOutputMediumEnum'
          readOnly: true
          description: >-
            The medium used initially by the agent. May later be changed by the
            client.
        joinTimeout:
          type: string
          default: 30s
        joinUrl:
          type: string
          readOnly: true
          nullable: true
        languageHint:
          type: string
          nullable: true
          description: BCP47 language code that may be used to guide speech recognition.
          maxLength: 16
        maxDuration:
          type: string
          default: 3600s
        medium:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CallMedium'
          nullable: true
        model:
          type: string
          default: ultravox-v0.7
        recordingEnabled:
          type: boolean
          default: false
        systemPrompt:
          type: string
          nullable: true
        temperature:
          type: number
          format: double
          maximum: 1
          minimum: 0
          default: 0
        timeExceededMessage:
          type: string
          nullable: true
        voice:
          type: string
          nullable: true
        externalVoice:
          $ref: '#/components/schemas/ultravox.v1.ExternalVoice'
        voiceOverrides:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.ExternalVoice'
          description: Overrides for the selected voice.
        transcriptOptional:
          type: boolean
          default: true
          description: Indicates whether a transcript is optional for the call.
          deprecated: true
        vadSettings:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.VadSettings'
          nullable: true
          description: VAD settings for the call.
        shortSummary:
          type: string
          readOnly: true
          nullable: true
          description: A short summary of the call.
        summary:
          type: string
          readOnly: true
          nullable: true
          description: A summary of the call.
        agent:
          allOf:
            - $ref: '#/components/schemas/AgentBasic'
          readOnly: true
          description: The agent used for this call.
        agentId:
          type: string
          nullable: true
          readOnly: true
          description: The ID of the agent used for this call.
        experimentalSettings:
          description: Experimental settings for the call.
        metadata:
          type: object
          additionalProperties:
            type: string
          description: >-
            Optional metadata key-value pairs to associate with the call. All
            values must be strings.
        initialState:
          type: object
          additionalProperties: {}
          description: The initial state of the call which is readable/writable by tools.
        requestContext: {}
        dataConnectionConfig:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.DataConnectionConfig'
          description: >-
            Settings for exchanging data messages with an additional
            participant.
        callbacks:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.Callbacks'
          description: Callbacks configuration for the call.
        sipDetails:
          allOf:
            - $ref: '#/components/schemas/CallSipDetails'
          readOnly: true
          nullable: true
          description: SIP details for the call, if applicable.
      required:
        - agent
        - agentId
        - billedDuration
        - billedSideInputTokens
        - billedSideOutputTokens
        - billingStatus
        - callId
        - clientVersion
        - created
        - endReason
        - ended
        - experimentalSettings
        - firstSpeaker
        - firstSpeakerSettings
        - initialOutputMedium
        - initialState
        - joinUrl
        - joined
        - metadata
        - requestContext
        - shortSummary
        - sipDetails
        - summary
    EndReasonEnum:
      enum:
        - unjoined
        - hangup
        - agent_hangup
        - timeout
        - connection_error
        - system_error
      type: string
      description: |-
        * `unjoined` - Client never joined
        * `hangup` - Client hung up
        * `agent_hangup` - Agent hung up
        * `timeout` - Call timed out
        * `connection_error` - Connection error
        * `system_error` - System error
    NullEnum:
      enum:
        - null
    BillingStatusEnum:
      enum:
        - BILLING_STATUS_PENDING
        - BILLING_STATUS_FREE_CONSOLE
        - BILLING_STATUS_FREE_ZERO_EFFECTIVE_DURATION
        - BILLING_STATUS_FREE_MINUTES
        - BILLING_STATUS_FREE_SYSTEM_ERROR
        - BILLING_STATUS_FREE_OTHER
        - BILLING_STATUS_BILLED
        - BILLING_STATUS_REFUNDED
        - BILLING_STATUS_UNSPECIFIED
      type: string
      description: >-
        * BILLING_STATUS_PENDING* - The call hasn't been billed yet, but will be
        in the future. This is the case for ongoing calls for example. (Note:
        Calls created before May 28, 2025 may have this status even if they were
        billed.)

        * BILLING_STATUS_FREE_CONSOLE* - The call was free because it was
        initiated on https://app.ultravox.ai.

        * BILLING_STATUS_FREE_ZERO_EFFECTIVE_DURATION* - The call was free
        because its effective duration was zero. (Note: There may still be a
        non-zero sip bill in this case.)

        * BILLING_STATUS_FREE_MINUTES* - The call was unbilled but counted
        against the account's free minutes. (Note: There may still be a non-zero
        sip bill in this case.)

        * BILLING_STATUS_FREE_SYSTEM_ERROR* - The call was free because it ended
        due to a system error.

        * BILLING_STATUS_FREE_OTHER* - The call is in an undocumented free
        billing state.

        * BILLING_STATUS_BILLED* - The call was billed. See billedDuration for
        the billed duration.

        * BILLING_STATUS_REFUNDED* - The call was billed but was later refunded.

        * BILLING_STATUS_UNSPECIFIED* - The call is in an unexpected billing
        state. Please contact support.
    FirstSpeakerEnum:
      enum:
        - FIRST_SPEAKER_AGENT
        - FIRST_SPEAKER_USER
      type: string
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
    InitialOutputMediumEnum:
      enum:
        - MESSAGE_MEDIUM_VOICE
        - MESSAGE_MEDIUM_TEXT
      type: string
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
    AgentBasic:
      type: object
      properties:
        agentId:
          type: string
          format: uuid
          readOnly: true
        name:
          type: string
          readOnly: true
      required:
        - agentId
        - name
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
    ultravox.v1.Callbacks:
      type: object
      properties:
        joined:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.Callback'
          description: Callback invoked when the call is joined.
        ended:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.Callback'
          description: Callback invoked when the call has ended.
        billed:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.Callback'
          description: Callback invoked when the call is billed.
      description: Configuration for call lifecycle callbacks.
    CallSipDetails:
      type: object
      properties:
        billedDuration:
          type: string
          readOnly: true
          nullable: true
        terminationReason:
          nullable: true
          readOnly: true
          oneOf:
            - $ref: '#/components/schemas/TerminationReasonEnum'
            - $ref: '#/components/schemas/NullEnum'
      required:
        - billedDuration
        - terminationReason
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
    ultravox.v1.Callback:
      type: object
      properties:
        url:
          type: string
          description: The URL to invoke.
        secrets:
          type: array
          items:
            type: string
          description: Secrets to use to signing the callback request.
      description: A lifecycle callback configuration.
    TerminationReasonEnum:
      enum:
        - SIP_TERMINATION_NORMAL
        - SIP_TERMINATION_INVALID_NUMBER
        - SIP_TERMINATION_TIMEOUT
        - SIP_TERMINATION_DESTINATION_UNAVAILABLE
        - SIP_TERMINATION_BUSY
        - SIP_TERMINATION_CANCELED
        - SIP_TERMINATION_REJECTED
        - SIP_TERMINATION_UNKNOWN
      type: string
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