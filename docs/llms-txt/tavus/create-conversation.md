# Source: https://docs.tavus.io/api-reference/conversations/create-conversation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

> This endpoint starts a real-time video conversation with your AI replica, powered by a persona that allows it to see, hear, and respond like a human.


**Core Components:**
- Replica - Choice of audio/visual appearance 
- Persona - Define the replica's behavior and capabilities


The response includes a `conversation_url` that you can use to join the call or embed it on your website. [Learn how to embed it here](/sections/integrations/embedding-cvi).

If you provide a `callback_url`, you’ll receive webhooks with updates about the conversation status. [Learn more about Callback here](/sections/webhooks-and-callbacks).


# Create Conversation

<Accordion title="Required Parameters" icon="lightbulb">
  Required parameters vary depending on the use case:

  **Full Pipeline Conversation:**

  * `persona_id`
  * `replica_id`

  **Audio-Only Conversation:**

  * `persona_id`
  * `replica_id`
  * `audio_only`

  <Warning>
    - `replica_id` is **required** if the persona does **not** have a default replica.
    - `replica_id` is **optional** if the persona **does** have a default replica.
    - If both a default replica and `replica_id` are provided, the supplied `replica_id` will **override** the default.
  </Warning>
</Accordion>


## OpenAPI

````yaml post /v2/conversations
openapi: 3.0.3
info:
  title: Tavus Developer API Collection
  version: 1.0.0
  contact: {}
servers:
  - url: https://tavusapi.com
security:
  - apiKey: []
tags:
  - name: Videos
  - name: Replicas
  - name: Conversations
  - name: Personas
  - name: Replacements
  - name: Transcriptions
  - name: Documents
paths:
  /v2/conversations:
    post:
      tags:
        - Conversations
      summary: Create Conversation
      description: >
        With the Tavus Conversational Video Interface (CVI) you are able to
        create a `conversation` with a replica in real time.


        ### Conversations

        A `conversation` is a video call with a replica. 


        After creating a `conversation`, a `conversation_url` will be returned
        in the response. The `conversation_url` can be used to join the
        conversation directly or can be embedded in a website. To embed the
        `conversation_url` in a website, you can find [instructions
        here](https://www.daily.co/products/prebuilt-video-call-app/quickstart/).


        Once a conversation is created, the replica will automatically join the
        call and will start participating.


        By providing a `callback_url`, you can receive webhooks with updates
        regarding the conversation state.


        <a href="/sections/conversational-video-interface/recording-rooms"
        target="_blank">Learn about recording conversations here</a>.

        <Warning>

        - **If your persona does not have a default replica**, the `replica_id`
        is required.

        - **If your persona has a default replica**, the `replica_id` is not
        required.

        - **If your persona has a default replica and you define `replica_id`**,
        it will override the persona's default replica.

        </Warning>
      operationId: createConversation
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                replica_id:
                  type: string
                  description: >-
                    The unique identifier for the replica that will join the
                    conversation. **Each request must have a valid `replica_id`
                    value that's either directly passed in or as part of a
                    persona**.
                  example: rfe12d8b9597
                persona_id:
                  type: string
                  description: >
                    The unique identifier for the persona that the replica will
                    use in the conversation.


                    - **If your Persona does not have a valid `replica_id`, you
                    must define the `replica_id` field.**

                    - **If your Persona already has a valid `replica_id` and you
                    provide one in the request, the `replica_id` provided in the
                    request will be used instead of the one defined in your
                    persona**.
                  example: p9a95912
                audio_only:
                  type: boolean
                  description: >-
                    Specifies whether the interaction should be voice-only.
                    **This field is required if you want to create an audio-only
                    conversation**.
                  example: 'false'
                callback_url:
                  type: string
                  description: >-
                    A url that will receive webhooks with updates regarding the
                    conversation state.
                  example: https://yourwebsite.com/webhook
                conversation_name:
                  type: string
                  description: A name for the conversation.
                  example: Improve Sales Technique
                conversational_context:
                  type: string
                  description: >-
                    Optional context that will be appended to any context
                    provided in the persona, if one is provided.
                  example: >-
                    I want to improve my sales techniques. Help me practice
                    handling common objections from clients and closing deals
                    more effectively.
                custom_greeting:
                  type: string
                  description: >-
                    An optional custom greeting that the replica will give once
                    a participant joines the conversation.
                  example: Hey there!
                memory_stores:
                  type: array
                  items:
                    type: string
                  description: >-
                    The memory stores to use for the conversation. The persona
                    will have access to the existing memories in the store and
                    will add newly made memories to the store as well. In most
                    use cases, you will only need to pass in a single memory
                    store.
                  example:
                    - anna
                document_ids:
                  type: array
                  items:
                    type: string
                  description: >-
                    The ids of the documents that the persona will be able to
                    access during the conversation. The `document_ids` are
                    returned during the document creation process in the
                    response of the [Get
                    Document](/api-reference/documents/get-document) and the
                    [Create Document](/api-reference/documents/create-document)
                    endpoints.
                  example:
                    - doc_1234567890
                document_retrieval_strategy:
                  type: string
                  description: >-
                    The strategy to use for document retrieval. Possible values:
                    `speed`, `quality`, `balanced`. Default is `balanced`.
                  example: balanced
                document_tags:
                  type: array
                  items:
                    type: string
                  description: >-
                    The tags of the documents that the replica will be able to
                    access during the conversation. The tags are passed in the
                    `document_tags` parameter of the [Create
                    Document](/api-reference/documents/create-document)
                    endpoint. The document tags do not have to be created
                    explicitly, it is enough to pass in the tags during the
                    document creation process.
                  example:
                    - sales
                    - marketing
                test_mode:
                  type: boolean
                  description: >-
                    If true, the conversation will be created but the replica
                    will not join the call. This can be used for testing the
                    conversation creation process without incurring any costs.
                    Additionally, the conversation will be created with a status
                    `ended` so it does not affect concurrency limits.
                  example: false
                require_auth:
                  type: boolean
                  description: >-
                    If true, creates a private room requiring authentication. A
                    `meeting_token` will be returned in the response that must
                    be used to join the conversation. Without a valid token,
                    users will see 'You are not allowed to join this meeting.'
                  example: false
                max_participants:
                  type: integer
                  minimum: 2
                  description: >-
                    Maximum number of participants allowed in the conversation
                    room. Must be at least 2 (the replica counts as one
                    participant).
                  example: 2
                properties:
                  type: object
                  description: >-
                    Optional properties that can be used to customize the
                    conversation.
                  properties:
                    max_call_duration:
                      type: integer
                      description: >-
                        The maximum duration of the call in seconds. The default
                        max_call_duration is 3600 seconds (1 hour). Once the
                        time limit specified by this parameter has been reached,
                        the conversation will automatically shut down.
                      example: 3600
                    participant_left_timeout:
                      type: integer
                      description: >-
                        The duration in seconds after which the call will be
                        automatically shut down once the last participant
                        leaves.
                      example: 60
                    participant_absent_timeout:
                      type: integer
                      description: >-
                        Starting from conversation creation, the duration in
                        seconds after which the call will be automatically shut
                        down if no participant joins the call. Default is 300
                        seconds (5 minutes).
                      example: 300
                    enable_recording:
                      type: boolean
                      description: >-
                        If true, the user will be able to record the
                        conversation. You can find more instructions on
                        recording
                        [here](/sections/conversational-video-interface/quickstart/conversation-recordings#conversation-recordings).
                      example: true
                    enable_closed_captions:
                      type: boolean
                      description: >-
                        If true, the user will be able to display closed
                        captions (subtitles) during the conversation. You can
                        find more instructions on displaying closed captions if
                        you are using your custom DailyJS components
                        [here](https://docs.daily.co/reference/daily-js/events/transcription-events#transcription-message).
                        You need to have an [event
                        listener](https://docs.daily.co/reference/daily-js/events)
                        on Daily that listens for app-messages.
                      example: true
                    apply_greenscreen:
                      type: boolean
                      description: >-
                        If true, the background will be replaced with a
                        greenscreen (RGB values: [0, 255, 155]). You can use
                        WebGL on the frontend to make the greenscreen
                        transparent or change its color.
                      example: true
                    language:
                      type: string
                      description: >-
                        The language of the conversation. Please provide the
                        FULL language name, not the two letter code, or specify
                        `multilingual` for automatic language detection. When
                        set to `multilingual`, CVI will use ASR language
                        detection to identify the user's spoken language and
                        respond accordingly. If you are using your own TTS
                        voice, please ensure it supports the language you
                        provide. If you are using a stock replica or default
                        persona, please note that only Elevenlabs and Cartesia
                        supported languages are available. You can find a full
                        list of supported languages for Cartesia
                        [here](https://docs.cartesia.ai/2024-11-13/build-with-cartesia/models#language-support),
                        and for ElevenLabs
                        [here](https://elevenlabs.io/languages).
                      example: multilingual
                    recording_s3_bucket_name:
                      type: string
                      description: >-
                        The name of the S3 bucket where the recording will be
                        stored.
                      example: conversation-recordings
                    recording_s3_bucket_region:
                      type: string
                      description: >-
                        The region of the S3 bucket where the recording will be
                        stored.
                      example: us-east-1
                    aws_assume_role_arn:
                      type: string
                      description: >-
                        The ARN of the role that will be assumed to access the
                        S3 bucket.
                      example: ''
            examples:
              Required Parameters Only:
                value:
                  replica_id: rfe12d8b9597
                  persona_id: pdced222244b
              Full Customizations:
                value:
                  replica_id: rfe12d8b9597
                  persona_id: pdced222244b
                  callback_url: https://yourwebsite.com/webhook
                  conversation_name: Improve Sales Technique
                  conversational_context: >-
                    I want to improve my sales techniques. Help me practice
                    handling common objections from clients and closing deals
                    more effectively.
                  properties:
                    max_call_duration: 1800
                    participant_left_timeout: 60
                    participant_absent_timeout: 120
                    language: multilingual
                    enable_closed_captions: true
                    apply_greenscreen: true
              Audio Only:
                value:
                  replica_id: rfe12d8b9597
                  persona_id: pdced222244b
                  audio_only: true
              Private Room:
                value:
                  replica_id: rfe12d8b9597
                  persona_id: pdced222244b
                  require_auth: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  conversation_id:
                    type: string
                    description: A unique identifier for the conversation.
                    example: c123456
                  conversation_name:
                    type: string
                    description: The name of the conversation.
                    example: A Meeting with Hassaan
                  conversation_url:
                    type: string
                    description: >-
                      A direct link to join the conversation. This link can be
                      used to join the conversation directly or can be embedded
                      in a website.
                    example: https://tavus.daily.co/c123456
                  status:
                    type: string
                    description: >-
                      The status of the conversation. Possible values: `active`,
                      `ended`.
                    example: active
                  callback_url:
                    type: string
                    description: >-
                      The url that will receive webhooks with updates of the
                      conversation state.
                    example: sample.com/callback
                  created_at:
                    type: string
                    description: The date and time the conversation was created.
                    example: <string>
                  meeting_token:
                    type: string
                    description: >-
                      A short-lived JWT token required to join the conversation.
                      Only returned when `require_auth` is true. Append as
                      `?t=TOKEN` to the conversation URL or pass to Daily SDK's
                      join() method.
                    example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message.
                    example: >-
                      There was an error creating the conversation, please reach
                      out to support at support@tavus.io!
        '401':
          description: UNAUTHORIZED
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: The error message.
                    example: Invalid access token
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````