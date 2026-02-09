# Source: https://docs.ultravox.ai/api-reference/agents/agents-scheduled-batches-patch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Scheduled Call Batch

> Updates a scheduled call batch

Allows partial modifications to the scheduled call batch.


## OpenAPI

````yaml patch /api/agents/{agent_id}/scheduled_batches/{batch_id}
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/agents/{agent_id}/scheduled_batches/{batch_id}:
    patch:
      tags:
        - agents
      operationId: agents_scheduled_batches_partial_update
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
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedScheduledCallBatch'
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ScheduledCallBatch'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    PatchedScheduledCallBatch:
      type: object
      properties:
        batchId:
          type: string
          format: uuid
          readOnly: true
        created:
          type: string
          format: date-time
          readOnly: true
        windowStart:
          type: string
          format: date-time
          nullable: true
          description: The start of the time window during which calls can be made.
        windowEnd:
          type: string
          format: date-time
          nullable: true
          description: The end of the time window during which calls can be made.
        webhookUrl:
          type: string
          format: uri
          nullable: true
          description: >-
            The URL to which a request will be made (synchronously) when a call
            in the batch is created, excluding those with an outgoing medium.
            Required if any call has a non-outgoing medium and not allowed
            otherwise.
          maxLength: 200
        webhookSecret:
          type: string
          nullable: true
          description: >-
            The signing secret for requests made to the webhookUrl. This is used
            to verify that the request came from Ultravox. If unset, an
            appropriate secret will be chosen for you (but you'll still need to
            make your endpoint aware of it to verify requests).
          maxLength: 120
        paused:
          type: boolean
        totalCount:
          type: integer
          readOnly: true
          description: The total number of calls in this batch.
        completedCount:
          type: integer
          readOnly: true
          description: >-
            The number of calls in this batch that have been completed (created
            or error).
        endedAt:
          type: string
          format: date-time
          readOnly: true
          nullable: true
        calls:
          type: array
          items:
            $ref: '#/components/schemas/ScheduledCall'
          writeOnly: true
          minItems: 1
    ScheduledCallBatch:
      type: object
      properties:
        batchId:
          type: string
          format: uuid
          readOnly: true
        created:
          type: string
          format: date-time
          readOnly: true
        windowStart:
          type: string
          format: date-time
          nullable: true
          description: The start of the time window during which calls can be made.
        windowEnd:
          type: string
          format: date-time
          nullable: true
          description: The end of the time window during which calls can be made.
        webhookUrl:
          type: string
          format: uri
          nullable: true
          description: >-
            The URL to which a request will be made (synchronously) when a call
            in the batch is created, excluding those with an outgoing medium.
            Required if any call has a non-outgoing medium and not allowed
            otherwise.
          maxLength: 200
        webhookSecret:
          type: string
          nullable: true
          description: >-
            The signing secret for requests made to the webhookUrl. This is used
            to verify that the request came from Ultravox. If unset, an
            appropriate secret will be chosen for you (but you'll still need to
            make your endpoint aware of it to verify requests).
          maxLength: 120
        paused:
          type: boolean
        totalCount:
          type: integer
          readOnly: true
          description: The total number of calls in this batch.
        completedCount:
          type: integer
          readOnly: true
          description: >-
            The number of calls in this batch that have been completed (created
            or error).
        endedAt:
          type: string
          format: date-time
          readOnly: true
          nullable: true
        calls:
          type: array
          items:
            $ref: '#/components/schemas/ScheduledCall'
          writeOnly: true
          minItems: 1
      required:
        - batchId
        - calls
        - completedCount
        - created
        - endedAt
        - totalCount
    ScheduledCall:
      type: object
      properties:
        status:
          allOf:
            - $ref: '#/components/schemas/ScheduledCallStatusEnum'
          readOnly: true
        batchId:
          type: string
          format: uuid
          readOnly: true
        callId:
          type: string
          format: uuid
          readOnly: true
          nullable: true
        error:
          type: string
          readOnly: true
          nullable: true
        medium:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CallMedium'
          nullable: true
          description: >-
            The call medium to use for the call. In particular, allows for
            specifying per-call recipients for outgoing media.
        metadata:
          nullable: true
          description: >-
            Optional metadata key-value pairs to associate with the call. All
            values must be strings.
        templateContext:
          nullable: true
          description: The context used to render the agent's template.
        experimentalSettings:
          nullable: true
      required:
        - batchId
        - callId
        - error
        - status
    ScheduledCallStatusEnum:
      enum:
        - FUTURE
        - PENDING
        - SUCCESS
        - EXPIRED
        - ERROR
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
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````