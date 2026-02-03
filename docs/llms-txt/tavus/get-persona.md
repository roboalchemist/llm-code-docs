# Source: https://docs.tavus.io/api-reference/personas/get-persona.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Persona

> This endpoint returns a single persona by its unique identifier.




## OpenAPI

````yaml get /v2/personas/{persona_id}
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
  /v2/personas/{persona_id}:
    parameters:
      - name: persona_id
        in: path
        required: true
        description: The unique identifier of the persona.
        schema:
          type: string
          example: pf3073f2dcc1
    get:
      tags:
        - Personas
      summary: Get Persona
      description: |
        This endpoint returns a single persona by its unique identifier.
      operationId: getPersona
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        persona_id:
                          type: string
                          description: A unique identifier for the persona.
                          example: p5317866
                        persona_name:
                          type: string
                          description: A name for the persona.
                          example: Life Coach
                        system_prompt:
                          type: string
                          description: The system prompt that will be used by the llm.
                          example: >-
                            As a Life Coach, you are a dedicated professional
                            who specializes in...
                        default_replica_id:
                          type: string
                          example: r79e1c033f
                          description: >-
                            The default replica_id associated with this persona
                            if one exists.
                        context:
                          type: string
                          description: The context that will be used by the llm.
                          example: >-
                            Here are a few times that you have helped an
                            individual make a breakthrough in...
                        document_ids:
                          type: array
                          description: >-
                            Array of document IDs that the persona has access
                            to. These documents will be available to the persona
                            in all their conversations. The document_ids are
                            returned in the response of the [Get
                            Document](/api-reference/documents/get-document) and
                            the [Create
                            Document](/api-reference/documents/create-document)
                            endpoints.
                          items:
                            type: string
                          example:
                            - d1234567890
                            - d2468101214
                        document_tags:
                          type: array
                          description: >-
                            Array of document tags that the persona has access
                            to. Documents matching these tags will be available
                            to the persona in all their conversations.
                          items:
                            type: string
                          example:
                            - product_info
                            - company_policies
                        layers:
                          type: object
                          properties:
                            llm:
                              type: object
                              properties:
                                model:
                                  type: string
                                  description: The model name that will be used by the llm.
                                base_url:
                                  type: string
                                  description: >-
                                    The base URL for the OpenAI compatible
                                    endpoint if you are using your own llm.
                                  example: your-base-url
                                api_key:
                                  type: string
                                  description: >-
                                    The API key for the OpenAI compatible
                                    endpoint if you are using your own llm.
                                  example: your-api-key
                                tools:
                                  type: array
                                  description: Optional tools to provide to your custom LLM
                                  example:
                                    - type: function
                                      function:
                                        name: get_current_weather
                                        description: >-
                                          Get the current weather in a given
                                          location
                                        parameters:
                                          type: object
                                          properties:
                                            location:
                                              type: string
                                              description: >-
                                                The city and state, e.g. San Francisco,
                                                CA
                                            unit:
                                              type: string
                                              enum:
                                                - celsius
                                                - fahrenheit
                                          required:
                                            - location
                                headers:
                                  type: object
                                  description: >-
                                    Optional headers to provide to your custom
                                    LLM
                                  example:
                                    Authorization: Bearer your-api-key
                                extra_body:
                                  type: object
                                  description: >
                                    Optional parameters to customize the LLM
                                    request. 


                                    For Tavus-hosted models, you can pass
                                    `temperature` and `top_p`:

                                    - `temperature`: Controls randomness in the
                                    model's output. Range typically 0.0 to 2.0.
                                    Lower values make output more deterministic
                                    and focused, higher values make it more
                                    creative and varied.

                                    - `top_p`: Controls diversity via nucleus
                                    sampling. Range 0.0 to 1.0. Lower values
                                    make output more focused on high-probability
                                    tokens, higher values allow more diverse
                                    token selection.


                                    For custom LLMs, you can pass any parameters
                                    that your LLM provider supports (e.g.,
                                    `temperature`, `top_p`, `frequency_penalty`,
                                    etc.).
                                  example:
                                    temperature: 0.7
                                    top_p: 0.9
                            tts:
                              type: object
                              properties:
                                api_key:
                                  type: string
                                  description: >-
                                    The API key for the chosen TTS provider.
                                    Only required when using private voices.
                                  example: your-api-key
                                tts_engine:
                                  type: string
                                  description: The TTS engine that will be used.
                                  enum:
                                    - cartesia
                                    - elevenlabs
                                external_voice_id:
                                  type: string
                                  description: >-
                                    The voice ID used for the TTS engine when
                                    you want to customize your replica's voice.
                                    Choose from Cartesia's stock voices by
                                    referring to their [Voice
                                    Catalog](https://docs.cartesia.ai/api-reference/voices/list),
                                    or if you want more options you can consider
                                    [ElevenLabs](https://elevenlabs.io/docs/api-reference/voices/get-all).
                                  example: external-voice-id
                                voice_settings:
                                  type: object
                                  description: >
                                    Optional voice settings to customize TTS
                                    behavior. Settings vary by provider.


                                    **Cartesia (Sonic-1 only):**

                                    - `speed`: Range -1.0 to 1.0 (negative =
                                    slower, positive = faster)

                                    - `emotion`: Array of emotion tags in format
                                    "emotion:level" (e.g., "positivity:high")
                                      - Emotions: anger, positivity, surprise, sadness, curiosity
                                      - Levels: low, medium, high
                                    - [Cartesia
                                    Documentation](https://docs.cartesia.ai/2024-11-13/build-with-cartesia/capability-guides/control-speed-and-emotion)


                                    **ElevenLabs:**

                                    - `speed`: Range 0.0 to 1.0 (0.0 = slowest,
                                    1.0 = fastest)

                                    - `stability`: Range 0.0 to 1.0 (0.0 =
                                    variable, 1.0 = stable)

                                    - `similarity_boost`: Range 0.0 to 1.0 (0.0
                                    = creative, 1.0 = original)

                                    - `style`: Range 0.0 to 1.0 (0.0 = neutral,
                                    1.0 = exaggerated)

                                    - `use_speaker_boost`: Boolean (enhances
                                    speaker similarity)

                                    - [ElevenLabs
                                    Documentation](https://elevenlabs.io/docs/api-reference/voices/settings/get)
                                  example:
                                    speed: 0.5
                                    emotion:
                                      - positivity:high
                                      - curiosity
                                tts_emotion_control:
                                  type: boolean
                                  description: >-
                                    If true, the TTS engine will be able to
                                    control the emotion of the voice. Only
                                    available for Cartesia TTS.
                                  example: 'false'
                                tts_model_name:
                                  type: string
                                  description: >-
                                    The model name that will be used by the TTS
                                    engine. Please double check this with the
                                    TTS provider you are using to ensure valid
                                    model names.
                                  example: sonic
                            perception:
                              type: object
                              properties:
                                perception_model:
                                  type: string
                                  description: >-
                                    The perception model to use. Options include
                                    `raven-0` for advanced multimodal perception
                                    or `basic` for simpler vision capabilities,
                                    and `off` to disable all perception.
                                  enum:
                                    - raven-0
                                    - basic
                                    - 'off'
                                  example: raven-0
                                ambient_awareness_queries:
                                  type: array
                                  description: >-
                                    Custom queries that Raven will continuously
                                    monitor for in the visual stream. These
                                    provide ambient context without requiring
                                    explicit prompting.
                                  items:
                                    type: string
                                  example:
                                    - Is the user showing an ID card?
                                    - >-
                                      Does the user appear distressed or
                                      uncomfortable?
                                perception_tool_prompt:
                                  type: string
                                  description: >-
                                    A prompt that details how and when to use
                                    the tools that are passed to the perception
                                    layer. This helps the replica understand the
                                    context of the perception tools and grounds
                                    it.
                                  example: >-
                                    You have a tool to notify the system when an
                                    ID card is detected, named
                                    `notify_if_id_shown`. You MUST use this tool
                                    when a form of ID is detected.
                                perception_tools:
                                  type: array
                                  description: >-
                                    Tools that can be triggered based on visual
                                    context, enabling automated actions in
                                    response to visual cues.
                                  items:
                                    type: object
                                    properties:
                                      name:
                                        type: string
                                        description: The name of the tool to be called.
                                      description:
                                        type: string
                                        description: >-
                                          A description of what the tool does and
                                          when it should be called.
                                  example:
                                    - type: function
                                      function:
                                        name: notify_if_id_shown
                                        description: >-
                                          Use this function when a drivers license
                                          or passport is detected in the image
                                          with high confidence. After collecting
                                          the ID, internally use final_ask()
                                        parameters:
                                          type: object
                                          properties:
                                            id_type:
                                              type: string
                                              description: best guess on what type of ID it is
                                          required:
                                            - id_type
                            stt:
                              type: object
                              description: >
                                **Note**: Turn-taking is now configured on the
                                [Conversational Flow
                                layer](/sections/conversational-video-interface/persona/conversational-flow).
                              properties:
                                stt_engine:
                                  type: string
                                  description: >-
                                    The STT engine that will be used.
                                    `tavus-turbo` is our lowest-latency model,
                                    but `tavus-advanced` provides higher
                                    transcription accuracy. Please note that
                                    non-English languages will default to
                                    `tavus-advanced` if not specified.
                                  enum:
                                    - tavus-turbo
                                    - tavus-advanced
                                hotwords:
                                  type: string
                                  description: >-
                                    The hotwords that will be used for the STT
                                    engine.
                                  example: This is a hotword example
                        created_at:
                          type: string
                          description: The date and time the persona was created.
                          example: ''
                        updated_at:
                          type: string
                          description: >-
                            The date and time of when the persona was last
                            updated.
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
                    example: Invalid persona_id
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
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````