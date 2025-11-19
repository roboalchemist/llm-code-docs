# Source: https://docs.tavus.io/api-reference/personas/create-persona.md

> This endpoint creates and customizes a digital replica's behavior and capabilities for Conversational Video Interface (CVI).

**Core Components:**
- Replica - Choice of audio/visual appearance
- Context - Customizable contextual information, for use by LLM
- System Prompt - Customizable system prompt, for use by LLM
- Layers
  - Perception - Multimodal vision and understanding settings (Raven)
  - STT - Transcription and turn taking settings (Sparrow)
  - Conversational Flow - Turn-taking, interruption handling, and active listening settings
  - LLM - Language model settings
  - TTS - Text-to-Speech settings


# Create Persona

## OpenAPI

````yaml post /v2/personas
paths:
  path: /v2/personas
  method: post
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              persona_name:
                allOf:
                  - type: string
                    description: A name for the persona.
                    example: Life Coach
              system_prompt:
                allOf:
                  - type: string
                    description: >-
                      This is the system prompt that will be used by the llm.
                      **Each request must have a `system_prompt` value unless
                      you're using echo mode**.
                    example: >-
                      As a Life Coach, you are a dedicated professional who
                      specializes in...
              pipeline_mode:
                allOf:
                  - type: string
                    description: >-
                      The pipeline mode to use for the persona. Possible values:
                      `full`, `echo`. `full` will provide the default end-to-end
                      experience. `echo` will turn off most steps, and allow the
                      replica to sync video with audio passed in through Echo
                      events, which it will speak out.
                    enum:
                      - full
                      - echo
              context:
                allOf:
                  - type: string
                    description: This is the context that will be used by the llm.
                    example: >-
                      Here are a few times that you have helped an individual
                      make a breakthrough in...
              default_replica_id:
                allOf:
                  - type: string
                    description: >-
                      The default replica_id associated with this persona if one
                      exists. When creating a conversation, a persona_id with a
                      default_replica_id associated can we used to create a
                      conversation without specifying a replica_id.
                    example: rfe12d8b9597
              document_ids:
                allOf:
                  - type: array
                    description: >-
                      Array of document IDs that the persona will have access
                      to. These documents will be available to the persona in
                      all their conversations. The `document_ids` are returned
                      in the response of the [Get
                      Document](/api-reference/documents/get-document) and the
                      [Create
                      Document](/api-reference/documents/create-document)
                      endpoints.
                    items:
                      type: string
                    example:
                      - d1234567890
                      - d2468101214
              document_tags:
                allOf:
                  - type: array
                    description: >-
                      Array of document tags that the persona will have access
                      to. Documents matching these tags will be available to the
                      persona in all their conversations. The tags are passed in
                      the `document_tags` parameter of the [Create
                      Document](/api-reference/documents/create-document)
                      endpoint. As soon as one document has the tag, you will be
                      able to pass the tags in this parameter..
                    items:
                      type: string
                    example:
                      - product_info
                      - company_policies
              layers:
                allOf:
                  - type: object
                    properties:
                      perception:
                        type: object
                        properties:
                          perception_model:
                            type: string
                            description: >-
                              The perception model to use. Options include
                              `raven-0` for advanced multimodal perception or
                              `basic` for simpler vision capabilities, and `off`
                              to disable all perception.
                            enum:
                              - raven-0
                              - basic
                              - 'off'
                            example: raven-0
                          ambient_awareness_queries:
                            type: array
                            description: >-
                              Custom queries that Raven will continuously
                              monitor for in the visual stream. These provide
                              ambient context without requiring explicit
                              prompting.
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
                              A prompt that details how and when to use the
                              tools that are passed to the perception layer.
                              This helps the replica understand the context of
                              the perception tools and grounds it.
                            example: >-
                              You have a tool to notify the system when an ID
                              card is detected, named `notify_if_id_shown`. You
                              MUST use this tool when a form of ID is detected.
                          perception_tools:
                            type: array
                            description: >-
                              Tools that can be triggered based on visual
                              context, enabling automated actions in response to
                              visual cues.
                            items:
                              type: object
                              properties:
                                name:
                                  type: string
                                  description: The name of the tool to be called.
                                description:
                                  type: string
                                  description: >-
                                    A description of what the tool does and when
                                    it should be called.
                            example:
                              - type: function
                                function:
                                  name: notify_if_id_shown
                                  description: >-
                                    Use this function when a drivers license or
                                    passport is detected in the image with high
                                    confidence. After collecting the ID,
                                    internally use final_ask()
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
                          participant_pause_sensitivity:
                            type: string
                            description: >-
                              Use this parameter to control how long of a pause
                              you can take before the replica will respond to
                              you. See more details
                              [here](/sections/conversational-video-interface/persona/stt#2-participant-pause-sensitivity).
                              The default is `medium`, but you can adjust this
                              to `low` or `high` depending on your needs.
                            enum:
                              - high
                              - medium
                              - low
                              - verylow
                              - superlow
                            example: high
                          participant_interrupt_sensitivity:
                            type: string
                            description: >-
                              Use this parameter to control how long you can
                              speak before the replica will be interrupted by
                              you. See more details
                              [here](/sections/conversational-video-interface/persona/stt#3-participant-interrupt-sensitivity).
                              The default is `medium`, but you can adjust this
                              to `low` or `high` depending on your needs.
                            enum:
                              - high
                              - medium
                              - low
                              - verylow
                              - superlow
                            example: high
                          hotwords:
                            type: string
                            description: >
                              The hotwords parameter lets you provide example
                              phrases that guide the STT model to prioritize
                              certain words or phrases—especially names,
                              technical terms, or uncommon language. For
                              instance, including "Roey is the name of the
                              person you're speaking with" helps the model
                              transcribe "Roey" correctly instead of "Rowie."
                            example: >-
                              Roey is the name of the person you're speaking
                              with.
                          smart_turn_detection:
                            type: boolean
                            example: true
                            description: >
                              Smart Turn Detection enhances the natural flow of
                              conversation between participants and digital
                              replicas. This intelligent system is powered by
                              the Sparrow model, which uses lexical and semantic
                              analysis to determine the optimal moment for the
                              digital replica to respond. The default value is
                              set to true.


                              **How it works:**

                              - Continuously evaluates the participant's speech
                              patterns and content

                              - Assesses the likelihood that the participant has
                              finished speaking

                              - Multilingual 

                              - Works seamlessly with both speculative and
                              non-speculative
                              inference,                             

                              - Continuously uses participant speech patterns
                              and content to determine how long to wait to
                              respond.

                              - Works in conjunction with the
                              `participant_pause_sensitivity` setting, which
                              adjusts the maximum pause for when participant is
                              clearly not done.


                              **Key benefits:**

                              - **Rapid response:** Triggers quick replies when
                              the participant has definitively concluded their
                              statement.

                              - **Extended listening:** Allows more time when
                              the participant is clearly in the middle of
                              expressing a thought.


                              Enabling Smart Turn Detection creates a more
                              natural and engaging conversational experience,
                              allowing the digital replica to interact more
                              seamlessly with human participants.
                      conversational_flow:
                        type: object
                        description: >-
                          Controls conversational flow dynamics for the replica.
                          When not explicitly provided, all fields default to
                          None (turned off). If any parameter is provided,
                          sensible defaults are applied to all other parameters.
                          See more details
                          [here](/sections/conversational-video-interface/persona/conversational-flow).
                        properties:
                          turn_detection_model:
                            type: string
                            description: >-
                              The model used for turn detection. Options include
                              `sparrow-0` for standard turn detection,
                              `sparrow-1` (recommended) for advanced turn
                              detection that is faster, more accurate, and more
                              natural, and `time-based` for simple timeout-based
                              detection. Default is `sparrow-0` when any
                              conversational flow parameter is provided.
                            enum:
                              - sparrow-0
                              - sparrow-1
                              - time-based
                            example: sparrow-1
                          turn_taking_patience:
                            type: string
                            description: >-
                              Controls how eagerly and quickly the replica
                              claims conversational turns. Affects both response
                              latency and likelihood of interrupting during
                              natural pauses. `low` = eager and quick to
                              respond, may interrupt pauses; `medium` (default)
                              = balanced; `high` = patient, waits for clear turn
                              completion.
                            enum:
                              - low
                              - medium
                              - high
                            example: medium
                          turn_commitment:
                            type: string
                            description: >-
                              Controls how aggressively the replica will barge
                              in and take its turn at the start of speaking.
                              This affects the replica's willingness to start
                              talking even when the user may still be speaking.
                              `low` = less aggressive barge-in, waits for user
                              to finish; `medium` (default) = balanced barge-in
                              behavior; `high` = more aggressive barge-in,
                              starts speaking more readily.
                            enum:
                              - low
                              - medium
                              - high
                            example: medium
                          replica_interruptibility:
                            type: string
                            description: >-
                              Controls how sensitive the replica is to user
                              speech while the replica is talking. Determines
                              whether the replica stops to listen or keeps
                              speaking. `low` = keeps talking, less
                              interruptible; `medium` (default) = balanced;
                              `high` = stops easily, more interruptible.
                            enum:
                              - low
                              - medium
                              - high
                            example: medium
                          active_listening:
                            type: string
                            description: >-
                              Controls the frequency of backchannel responses
                              (e.g., 'yeah', 'mhmm') while the user is speaking.
                              `off` (default) = no backchannels; `low` =
                              infrequent; `medium` = moderate; `high` = frequent
                              backchannels. Note: This feature is currently in
                              English-only beta.
                            enum:
                              - 'off'
                              - low
                              - medium
                              - high
                            example: 'off'
                      llm:
                        type: object
                        properties:
                          model:
                            type: string
                            description: >
                              "The model name that will be used by the LLM. To
                              use Tavus' LLMs, you may select from the following
                              models:

                              - `tavus-llama-4` (Recommended)

                              - `tavus-gpt-4o`

                              - `tavus-gpt-4o-mini`


                              If you would like to use your own
                              OpenAI-compatible LLM, you may provide a `model`,
                              `base_url`, and `api_key`."
                                #### Context Window Limit

                                * All Tavus-hosted models have a **limit of 32,000 tokens**.
                                * Contexts over **25,000 tokens** will experience noticeable performance degradation (slower response times).

                                > **Tip**: 1 token ≈ 4 characters, therefore 32,000 tokens ≈ 128,000 characters (including spaces and punctuation).
                          base_url:
                            type: string
                            description: The base url for your OpenAI compatible endpoint.
                            example: your-base-url
                          api_key:
                            type: string
                            description: The API key for the OpenAI compatible endpoint.
                            example: your-api-key
                          speculative_inference:
                            type: boolean
                            description: >-
                              When set to `true`, the LLM begins processing
                              speech transcriptions before user input ends,
                              improving responsiveness.
                            example: true
                          tools:
                            type: array
                            description: >-
                              Optional tools to provide to your custom LLM -
                              click
                              [here](/sections/conversational-video-interface/persona/llm-tool)
                              for more details.
                            example:
                              - type: function
                                function:
                                  name: get_current_weather
                                  description: Get the current weather in a given location
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
                            description: Optional headers to provide to your custom LLM
                            example:
                              Authorization: Bearer your-api-key
                          extra_body:
                            type: object
                            description: Optional extra body to provide to your custom LLM
                            example:
                              temperature: 0.5
                      tts:
                        type: object
                        properties:
                          api_key:
                            type: string
                            description: >-
                              The API key for the chosen TTS provider. Only
                              required when using private voices.
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
                              The voice ID used for the TTS engine when you want
                              to customize your replica's voice. Choose from
                              Cartesia's stock voices by referring to their
                              [Voice
                              Catalog](https://docs.cartesia.ai/api-reference/voices/list),
                              or if you want more options you can consider
                              [ElevenLabs](https://elevenlabs.io/docs/api-reference/voices/get-all).
                            example: external-voice-id
                          voice_settings:
                            type: object
                            description: >
                              Optional voice settings to customize TTS behavior.
                              Settings vary by provider.


                              **Cartesia (Sonic-1 only):**

                              - `speed`: Range -1.0 to 1.0 (negative = slower,
                              positive = faster)

                              - `emotion`: Array of emotion tags in format
                              "emotion:level" (e.g., "positivity:high")
                                - Emotions: anger, positivity, surprise, sadness, curiosity
                                - Levels: low, medium, high
                              - [Cartesia
                              Documentation](https://docs.cartesia.ai/2024-11-13/build-with-cartesia/capability-guides/control-speed-and-emotion)


                              **ElevenLabs:**

                              - `speed`: Range 0.7 to 1.2 (0.7 = slowest, 1.2 =
                              fastest)

                              - `stability`: Range 0.0 to 1.0 (0.0 = variable,
                              1.0 = stable)

                              - `similarity_boost`: Range 0.0 to 1.0 (0.0 =
                              creative, 1.0 = original)

                              - `style`: Range 0.0 to 1.0 (0.0 = neutral, 1.0 =
                              exaggerated)

                              - `use_speaker_boost`: Boolean (enhances speaker
                              similarity)

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
                              If true, the TTS engine will be able to control
                              the emotion of the voice. Only available for
                              Cartesia TTS.
                            example: 'false'
                          tts_model_name:
                            type: string
                            description: >-
                              The model name that will be used by the TTS
                              engine. Please double check this with the TTS
                              provider you are using to ensure valid model
                              names.
                            example: sonic
        examples:
          Required Parameters Only:
            value:
              pipeline_mode: full
              system_prompt: >-
                As a Life Coach, you are a dedicated professional who
                specializes in...
          Full Customizations:
            value:
              persona_name: Life Coach
              system_prompt: >-
                As a Life Coach, you are a dedicated professional who
                specializes in...
              pipeline_mode: full
              context: >-
                Here are a few times that you have helped an individual make a
                breakthrough in...
              default_replica_id: rfe12d8b9597
              layers:
                llm:
                  model: tavus-gpt-4o
                  speculative_inference: true
                  tools:
                    - type: function
                      function:
                        name: life_coach_insight
                        description: >-
                          Offer personalized life coaching advice or guidance
                          based on a user's challenge or goal.
                        parameters:
                          type: object
                          properties:
                            topic:
                              type: string
                              description: >-
                                The area of life or goal the user wants to
                                improve (e.g. career, relationships, confidence)
                            urgency_level:
                              type: string
                              enum:
                                - low
                                - medium
                                - high
                          required:
                            - topic
                tts:
                  tts_engine: cartesia
                  voice_settings:
                    speed: normal
                    emotion:
                      - positivity:high
                      - curiosity
                  tts_emotion_control: true
                  tts_model_name: sonic
                perception:
                  perception_model: raven-0
                  ambient_awareness_queries:
                    - Is the user showing an ID card?
                    - Does the user appear distressed or uncomfortable?
                  perception_tool_prompt: >-
                    You have a tool to notify the system when an ID card is
                    detected, named `notify_if_id_shown`. You MUST use this tool
                    when a form of ID is detected.
                  perception_tools:
                    - type: function
                      function:
                        name: notify_if_id_shown
                        description: >-
                          Use this function when a drivers license or passport
                          is detected in the image with high confidence. After
                          collecting the ID, internally use final_ask()
                        parameters:
                          type: object
                          properties:
                            id_type:
                              type: string
                              description: best guess on what type of ID it is
                          required:
                            - id_type
                stt:
                  stt_engine: tavus-advanced
                  participant_pause_sensitivity: high
                  participant_interrupt_sensitivity: high
                  smart_turn_detection: true
                conversational_flow:
                  turn_detection_model: sparrow-1
                  turn_taking_patience: medium
                  turn_commitment: medium
                  replica_interruptibility: high
                  active_listening: low
                document_ids:
                  - d1234567890
                  - d2468101214
                document_tags:
                  - product_info
                  - company_policies
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              persona_id:
                allOf:
                  - type: string
                    description: A unique identifier for the persona.
                    example: p5317866
              persona_name:
                allOf:
                  - type: string
                    description: The name of the persona.
                    example: Life Coach
              created_at:
                allOf:
                  - type: string
                    description: The date and time the persona was created.
        examples:
          example:
            value:
              persona_id: p5317866
              persona_name: Life Coach
              created_at: <string>
        description: ''
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid replica_uuid
        examples:
          example:
            value:
              error: Invalid replica_uuid
        description: Bad Request
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