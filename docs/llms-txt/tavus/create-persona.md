# Source: https://docs.tavus.io/api-reference/personas/create-persona.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

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

<Note>
  For detailed guides on each layer of the Conversational Video Interface, click <a href="/sections/conversational-video-interface/persona/overview#cvi-layer" target="_blank">here</a>.
</Note>

<Warning>
  When using full pipeline mode, the `system_prompt` field is required.
</Warning>


## OpenAPI

````yaml post /v2/personas
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
  /v2/personas:
    post:
      tags:
        - Personas
      summary: Create Persona
      description: >
        This endpoint creates a new persona that can be used by replicas in
        conversations. 


        With a persona, you are able to craft the personalities of your replica
        across conversations.

        <Warning>

        When using full pipeline mode, the `system_prompt` field is required.

        </Warning>


        #### LLM

        With the `llm` layer, you can leverage your own OpenAI compatible LLM or
        you can use one a Tavus provided model.

        - **tavus-gpt-4o:** The smartest option for complex interactions.

        - **tavus-gpt-4o-mini:** A hybrid model that balances performance and
        intelligence.

        - **tavus-gpt-oss:** The **default** choice if no LLM layer is
        provided. 


        [Get Started with Your Own
        LLM](/sections/conversational-video-interface/custom-llm-onboarding)


        #### TTS

        With Tavus' default TTS engine, you get the faster
        utterance-to-utterance speed, but you can always bring your own if you
        have voices already trained with:

        - **Cartesia**

        - **Elevenlabs**


        [Get Started with Your Own
        TTS](/sections/conversational-video-interface/custom-tts-onboarding)
      operationId: createPersona
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                persona_name:
                  type: string
                  description: A name for the persona.
                  example: Life Coach
                system_prompt:
                  type: string
                  description: >-
                    This is the system prompt that will be used by the llm.
                    **Each request must have a `system_prompt` value unless
                    you're using echo mode**.
                  example: >-
                    As a Life Coach, you are a dedicated professional who
                    specializes in...
                pipeline_mode:
                  type: string
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
                  type: string
                  description: This is the context that will be used by the llm.
                  example: >-
                    Here are a few times that you have helped an individual make
                    a breakthrough in...
                default_replica_id:
                  type: string
                  description: >-
                    The default replica_id associated with this persona if one
                    exists. When creating a conversation, a persona_id with a
                    default_replica_id associated can we used to create a
                    conversation without specifying a replica_id.
                  example: rfe12d8b9597
                document_ids:
                  type: array
                  description: >-
                    Array of document IDs that the persona will have access to.
                    These documents will be available to the persona in all
                    their conversations. The `document_ids` are returned in the
                    response of the [Get
                    Document](/api-reference/documents/get-document) and the
                    [Create Document](/api-reference/documents/create-document)
                    endpoints.
                  items:
                    type: string
                  example:
                    - d1234567890
                    - d2468101214
                document_tags:
                  type: array
                  description: >-
                    Array of document tags that the persona will have access to.
                    Documents matching these tags will be available to the
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
                  type: object
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
                            Custom queries that Raven will continuously monitor
                            for in the visual stream. These provide ambient
                            context without requiring explicit prompting.
                          items:
                            type: string
                          example:
                            - Is the user showing an ID card?
                            - Does the user appear distressed or uncomfortable?
                        perception_tool_prompt:
                          type: string
                          description: >-
                            A prompt that details how and when to use the tools
                            that are passed to the perception layer. This helps
                            the replica understand the context of the perception
                            tools and grounds it.
                          example: >-
                            You have a tool to notify the system when an ID card
                            is detected, named `notify_if_id_shown`. You MUST
                            use this tool when a form of ID is detected.
                        perception_tools:
                          type: array
                          description: >-
                            Tools that can be triggered based on visual context,
                            enabling automated actions in response to visual
                            cues.
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
                      description: >
                        **Note**: Turn-taking is now configured on the
                        [Conversational Flow
                        layer](/sections/conversational-video-interface/persona/conversational-flow).
                      properties:
                        hotwords:
                          type: string
                          description: >
                            The hotwords parameter lets you provide example
                            phrases that guide the STT model to prioritize
                            certain words or phrases—especially names, technical
                            terms, or uncommon language. For instance, including
                            "Roey is the name of the person you're speaking
                            with" helps the model transcribe "Roey" correctly
                            instead of "Rowie."
                          example: Roey is the name of the person you're speaking with.
                    conversational_flow:
                      type: object
                      description: >-
                        Controls conversational flow dynamics for the replica.
                        When not explicitly provided, all fields default to None
                        (turned off). If any parameter is provided, sensible
                        defaults are applied to all other parameters. See more
                        details
                        [here](/sections/conversational-video-interface/persona/conversational-flow).
                      properties:
                        turn_detection_model:
                          type: string
                          description: >-
                            The model used for turn detection. Options include
                            `sparrow-1` (recommended) for advanced turn
                            detection that is faster, more accurate, and more
                            natural, `sparrow-0` (legacy) for standard turn
                            detection, and `time-based` for simple timeout-based
                            detection. Default is `sparrow-1` when any
                            conversational flow parameter is provided.
                          enum:
                            - sparrow-1
                            - sparrow-0
                            - time-based
                          example: sparrow-1
                        turn_taking_patience:
                          type: string
                          description: >-
                            Controls how eagerly and quickly the replica claims
                            conversational turns. Affects both response latency
                            and likelihood of interrupting during natural
                            pauses. `low` = eager and quick to respond, may
                            interrupt pauses; `medium` (default) = balanced;
                            `high` = patient, waits for clear turn completion.
                          enum:
                            - low
                            - medium
                            - high
                          example: medium
                        replica_interruptibility:
                          type: string
                          description: >-
                            Controls how sensitive the replica is to user speech
                            while the replica is talking. Determines whether the
                            replica stops to listen or keeps speaking. `low` =
                            keeps talking, less interruptible; `medium`
                            (default) = balanced; `high` = stops easily, more
                            interruptible.
                          enum:
                            - low
                            - medium
                            - high
                          example: medium
                    llm:
                      type: object
                      properties:
                        model:
                          type: string
                          description: >
                            "The model name that will be used by the LLM. To use
                            Tavus' LLMs, you may select from the following
                            models:

                            - `tavus-gpt-oss` (Recommended)

                            - `tavus-gpt-4o`

                            - `tavus-gpt-4o-mini`


                            If you would like to use your own OpenAI-compatible
                            LLM, you may provide a `model`, `base_url`, and
                            `api_key`."
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
                            When set to `true`, the LLM begins processing speech
                            transcriptions before user input ends, improving
                            responsiveness.
                          example: true
                        tools:
                          type: array
                          description: >-
                            Optional tools to provide to your custom LLM - click
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
                          description: >
                            Optional parameters to customize the LLM request. 


                            For Tavus-hosted models, you can pass `temperature`
                            and `top_p`:

                            - `temperature`: Controls randomness in the model's
                            output. Range typically 0.0 to 2.0. Lower values
                            make output more deterministic and focused, higher
                            values make it more creative and varied.

                            - `top_p`: Controls diversity via nucleus sampling.
                            Range 0.0 to 1.0. Lower values make output more
                            focused on high-probability tokens, higher values
                            allow more diverse token selection.


                            For custom LLMs, you can pass any parameters that
                            your LLM provider supports (e.g., `temperature`,
                            `top_p`, `frequency_penalty`, etc.).
                          example:
                            temperature: 0.7
                            top_p: 0.9
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
                            Cartesia's stock voices by referring to their [Voice
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

                            - `stability`: Range 0.0 to 1.0 (0.0 = variable, 1.0
                            = stable)

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
                            If true, the TTS engine will be able to control the
                            emotion of the voice. Only available for Cartesia
                            TTS.
                          example: 'false'
                        tts_model_name:
                          type: string
                          description: >-
                            The model name that will be used by the TTS engine.
                            Please double check this with the TTS provider you
                            are using to ensure valid model names.
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
                    Here are a few times that you have helped an individual make
                    a breakthrough in...
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
                              Offer personalized life coaching advice or
                              guidance based on a user's challenge or goal.
                            parameters:
                              type: object
                              properties:
                                topic:
                                  type: string
                                  description: >-
                                    The area of life or goal the user wants to
                                    improve (e.g. career, relationships,
                                    confidence)
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
                      stt_engine: tavus-advanced
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  persona_id:
                    type: string
                    description: A unique identifier for the persona.
                    example: p5317866
                  persona_name:
                    type: string
                    description: The name of the persona.
                    example: Life Coach
                  created_at:
                    type: string
                    description: The date and time the persona was created.
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
                    example: Invalid replica_uuid
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