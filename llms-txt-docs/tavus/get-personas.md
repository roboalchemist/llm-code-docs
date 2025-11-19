# Source: https://docs.tavus.io/api-reference/personas/get-personas.md

# List Personas

> This endpoint returns a list of all Personas created by the account associated with the API Key in use.


## OpenAPI

````yaml get /v2/personas
paths:
  path: /v2/personas
  method: get
  servers:
    - url: https://tavusapi.com
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
          cookie: {}
    parameters:
      path: {}
      query:
        limit:
          schema:
            - type: integer
              description: The number of personas to return per page. Default is 10.
        page:
          schema:
            - type: integer
              description: The page number to return. Default is 1.
        persona_type:
          schema:
            - type: enum<string>
              enum:
                - user
                - system
              description: >-
                Filter the personas by type. Possible values: user, system.
                System personas are personas that have been created by Tavus.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
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
                                participant_pause_sensitivity:
                                  type: string
                                  description: >-
                                    Use this parameter to control how long of a
                                    pause you can take before the replica will
                                    respond to you. See more details
                                    [here](/sections/conversational-video-interface/persona/stt#2-participant-pause-sensitivity).
                                    The default is `medium`, but you can adjust
                                    this to `low` or `high` depending on your
                                    needs.
                                  enum:
                                    - low
                                    - medium
                                    - high
                                participant_interrupt_sensitivity:
                                  type: string
                                  description: >-
                                    Use this parameter to control how long you
                                    can speak before the replica will be
                                    interrupted by you. See more details
                                    [here](/sections/conversational-video-interface/persona/stt#3-participant-interrupt-sensitivity).
                                    The default is `medium`, but you can adjust
                                    this to `low` or `high` depending on your
                                    needs.
                                  enum:
                                    - low
                                    - medium
                                    - high
                                hotwords:
                                  type: string
                                  description: >-
                                    The hotwords that will be used for the STT
                                    engine.
                                  example: This is a hotword example
                                smart_turn_detection:
                                  type: boolean
                                  description: >
                                    Smart Turn Detection enhances the natural
                                    flow of conversation between participants
                                    and digital replicas. This intelligent
                                    system is powered by the Sparrow model,
                                    which uses lexical and semantic analysis to
                                    determine the optimal moment for the digital
                                    replica to respond. The default value is set
                                    to true.

                                     **How it works:**
                                     - Continuously evaluates the participant's speech patterns and content
                                     - Assesses the likelihood that the participant has finished speaking
                                     - Multilingual, support for 100 languages 
                                     - Works seamlessly with both speculative and non-speculative inference,                             
                                     - Continuously uses participant speech patterns and content to determine how long to wait to respond.
                                     - Works in conjunction with the `participant_pause_sensitivity` setting, which adjusts the maximum pause for when participant is clearly not done.

                                     **Key benefits:**
                                     - **Rapid response:** Triggers quick replies when the participant has definitively concluded their statement.
                                     - **Extended listening:** Allows more time when the participant is clearly in the middle of expressing a thought.

                                     Enabling Smart Turn Detection creates a more natural and engaging conversational experience, allowing the digital replica to interact more seamlessly with human participants.
                        created_at:
                          type: string
                          description: The date and time the persona was created.
                          example: ''
                        updated_at:
                          type: string
                          description: >-
                            The date and time of when the persona was last
                            updated.
              total_count:
                allOf:
                  - type: integer
                    description: The total number of personas given the filters provided.
        examples:
          example:
            value:
              data:
                - persona_id: p5317866
                  persona_name: Life Coach
                  system_prompt: >-
                    As a Life Coach, you are a dedicated professional who
                    specializes in...
                  default_replica_id: r79e1c033f
                  context: >-
                    Here are a few times that you have helped an individual make
                    a breakthrough in...
                  document_ids:
                    - d1234567890
                    - d2468101214
                  document_tags:
                    - product_info
                    - company_policies
                  layers:
                    llm:
                      model: <string>
                      base_url: your-base-url
                      api_key: your-api-key
                      tools:
                        - type: function
                          function:
                            name: get_current_weather
                            description: Get the current weather in a given location
                            parameters:
                              type: object
                              properties:
                                location:
                                  type: string
                                  description: The city and state, e.g. San Francisco, CA
                                unit:
                                  type: string
                                  enum:
                                    - celsius
                                    - fahrenheit
                              required:
                                - location
                    tts:
                      api_key: your-api-key
                      tts_engine: cartesia
                      external_voice_id: external-voice-id
                      voice_settings:
                        speed: 0.5
                        emotion:
                          - positivity:high
                          - curiosity
                      tts_emotion_control: 'false'
                      tts_model_name: sonic
                    perception:
                      perception_model: raven-0
                      ambient_awareness_queries:
                        - Is the user showing an ID card?
                        - Does the user appear distressed or uncomfortable?
                      perception_tool_prompt: >-
                        You have a tool to notify the system when an ID card is
                        detected, named `notify_if_id_shown`. You MUST use this
                        tool when a form of ID is detected.
                      perception_tools:
                        - type: function
                          function:
                            name: notify_if_id_shown
                            description: >-
                              Use this function when a drivers license or
                              passport is detected in the image with high
                              confidence. After collecting the ID, internally
                              use final_ask()
                            parameters:
                              type: object
                              properties:
                                id_type:
                                  type: string
                                  description: best guess on what type of ID it is
                              required:
                                - id_type
                    stt:
                      stt_engine: tavus-turbo
                      participant_pause_sensitivity: low
                      participant_interrupt_sensitivity: low
                      hotwords: This is a hotword example
                      smart_turn_detection: true
                  created_at: ''
                  updated_at: <string>
              total_count: 123
        description: ''
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid access token
        examples:
          example:
            value:
              message: Invalid access token
        description: UNAUTHORIZED
  deprecated: false
  type: path
components:
  schemas: {}

````