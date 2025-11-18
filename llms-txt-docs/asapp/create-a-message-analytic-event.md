# Source: https://docs.asapp.com/apis/autocompose/create-a-message-analytic-event.md

# Create a message analytic event

> To improve the performance of ASAPP suggestions, provide information about the actions performed by the agent while composing a message by creating `message-analytic-events`.

These analytic events indicate which AutoCompose functionality was used or not. This information along with the conversation itself is used to optimize our models, resulting in better results for the agents.

We track the following types of message analytic events:
- suggestion-1-inserted: The agent selected the first of the `suggestions` from a `Suggestion` API response.
- suggestion-2-inserted: The agent selected the second of the `suggestions` from a `Suggestion` API response.
- suggestion-3-inserted: The agent selected the third of the `suggestions` from a `Suggestion` API response.
- phrase-completion-accepted: The agent selected the `phraseCompletion` from a `Suggestion` API response.
- spellcheck-applied: A correction provided in a `SpellcheckCorrection` API response was applied automatically.
- spellcheck-undone: A correction provided in a `SpellcheckCorrection` API response was undone by clicking the undo button.
- custom-response-drawer-inserted: The agent inserted one of their custom responses from the custom response drawer.
- custom-panel-inserted: The agent inserted a response from their custom response list in the custom response panel.
- global-panel-inserted: The agent inserted a response from the global response list in the global response panel.

Some of the event types have a corresponding event object to provide details.


## OpenAPI

````yaml api-specs/autocompose.yaml post /autocompose/v1/conversations/{conversationId}/message-analytic-events
paths:
  path: /autocompose/v1/conversations/{conversationId}/message-analytic-events
  method: post
  servers:
    - url: https://api.sandbox.asapp.com
  request:
    security:
      - title: API ID & API Secret
        parameters:
          query: {}
          header:
            asapp-api-id:
              type: apiKey
            asapp-api-secret:
              type: apiKey
          cookie: {}
    parameters:
      path:
        conversationId:
          schema:
            - type: string
              required: true
              description: The identifier for a conversation.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    example: suggestion-1-inserted
                    enum:
                      - suggestion-1-inserted
                      - suggestion-2-inserted
                      - suggestion-3-inserted
                      - phrase-completion-accepted
                      - spellcheck-applied
                      - spellcheck-undone
                      - custom-response-drawer-inserted
                      - custom-panel-inserted
                      - global-panel-inserted
                    description: |
                      The type of message analytic event.
              suggestionsId:
                allOf:
                  - description: >
                      For suggestion-1-inserted, suggestion-2-inserted,
                      suggestion-3-inserted, phrase-completion-accepted,

                      this is the `id` from the Suggestions API response that
                      the agent

                      interacted with. This allows ASAPP to connect the event
                      with additional information (e.g., the

                      text of the suggestion that was inserted).


                      For spellcheck-undone, custom-response-drawer-inserted,
                      custom-panel-inserted, and global-panel-inserted, this is
                      the

                      `id` of the most recent Suggestions API response in this
                      conversation.


                      In all of these cases, providing the Suggestions `id`
                      allows ASAPP to associate the event with the message the
                      agent

                      is composing. During the normal flow of using the
                      AutoCompose API, the Suggestions API will always have been
                      called

                      at least once since the previous agent message by the time
                      a message analytic event occurs, and each time the

                      Suggestions API is called, ASAPP records the ID of the
                      previous

                      agent message. Thus, the Suggestions `id` in the analytic
                      event links back to the previous agent message. This
                      permits

                      the analytic event to later be linked to the new message
                      the agent is composing, even though the event occurs
                      before

                      the message is sent.
                    type: string
                    example: 4d2fd982640c311394008259594399a1
              spellcheckApplied:
                allOf:
                  - type: object
                    description: |
                      The details about the spellcheck applied analytic event
                    nullable: true
                    properties:
                      correctionId:
                        description: The ID of the spellcheck correction API response
                        type: string
                        example: 75bc8912c66842594375bc8912c66842
                    required:
                      - correctionId
              spellcheckUndone:
                allOf:
                  - type: object
                    description: |
                      The details about the spellcheck undone analytic event
                    nullable: true
                    properties:
                      correctionId:
                        description: The ID of the spellcheck correction API response
                        type: string
                        example: 75bc8912c66842594375bc8912c66842
                    required:
                      - correctionId
              customResponseDrawerInserted:
                allOf:
                  - type: object
                    description: >-
                      The details about the custom response drawer inserted
                      analytic event
                    nullable: true
                    properties:
                      query:
                        description: >
                          The query the agent typed to search in the custom
                          response drawer
                        type: string
                        example: Hi
                      text:
                        description: >
                          The text of the custom response the agent inserted
                          from the custom response drawer
                        type: string
                        example: Hi, I'm Alice. How can I help you today?
                    required:
                      - query
                      - text
              customPanelInserted:
                allOf:
                  - type: object
                    description: The details about the custom panel inserted analytic event
                    nullable: true
                    properties:
                      text:
                        description: >
                          The text of the custom response the agent inserted
                          using the custom response panel
                        type: string
                        example: Hi, I'm Alice. How can I help you today?
                    required:
                      - text
              globalPanelInserted:
                allOf:
                  - type: object
                    description: The details about the global panel inserted analytic event
                    nullable: true
                    properties:
                      text:
                        description: >
                          The text of the custom response the agent inserted
                          using the global response panel
                        type: string
                        example: How can I help you today?
                    required:
                      - text
            description: >
              Analytics event reporting actions the agent performed while
              composing a message.
            requiredProperties:
              - type
              - suggestionsId
            example:
              type: suggestion-1-inserted
              suggestionsId: 4d2fd982640c311394008259594399a1
        examples:
          Create a suggestion-inserted event.:
            value:
              type: suggestion-1-inserted
              suggestionsId: 4d2fd982640c311394008259594399a1
          Create a spellcheck-applied event.:
            value:
              type: spellcheck-applied
              suggestionsId: 4d2fd982640c311394008259594399a1
              spellcheckApplied:
                correctionId: 75bc8912c66842594375bc8912c66842
          Create a spellcheck-undone event.:
            value:
              type: spellcheck-undone
              suggestionsId: 4d2fd982640c311394008259594399a1
              spellcheckUndone:
                correctionId: 75bc8912c66842594375bc8912c66842
          Create a custom-response-drawer-inserted event.:
            value:
              type: custom-response-drawer-inserted
              suggestionsId: 4d2fd982640c311394008259594399a1
              customResponseDrawerInserted:
                query: Hi
                text: Hi, I'm Alice. How can I help you today?
          Create a custom-panel-inserted event.:
            value:
              type: custom-panel-inserted
              suggestionsId: 4d2fd982640c311394008259594399a1
              customPanelInserted:
                text: Hi, I'm Alice. How can I help you today?
          Create a global-panel-inserted event.:
            value:
              type: global-panel-inserted
              suggestionsId: 4d2fd982640c311394008259594399a1
              globalPanelInserted:
                text: How can I help you today?
        description: The parameters for reporting the analytic event
  response:
    '200': {}
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 400-01
                      message: Bad request
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Bad request response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 400-01
                message: Bad request
        description: 400 - Bad request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 401-01
                      message: Unauthorized
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Unauthorized response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 401-01
                message: Unauthorized
        description: 401 - Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 403-01
                      message: Forbidden Response
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Forbidden response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 403-01
                message: Forbidden Response
        description: 403 - Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 404-01
                      message: Not Found
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Not Found response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 404-01
                message: Not Found
        description: 404 - Not Found
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 409-01
                      message: Conflict
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Conflict response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 409-01
                message: Conflict
        description: 409 - Conflict
    '413':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 413-01
                      message: Request Entity Too Large
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Request Entity Too Large response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 413-01
                message: Request Entity Too Large
        description: 413 - Request Entity Too Large
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 422-01
                      message: Unprocessable Entity
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Unprocessable Entity response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 422-01
                message: Unprocessable Entity
        description: 422 - Unprocessable Entity
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 429-01
                      message: Too Many Requests
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Too Many Requests response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 429-01
                message: Too Many Requests
        description: 429 - Too Many Requests
    '503':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 503-01
                      message: Service Unavailable
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Service Unavailable response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 503-01
                message: Service Unavailable
        description: 503 - Service Unavailable
    default:
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 500-01
                      message: Internal server error
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Default error response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 500-01
                message: Internal server error
        description: 500 - Internal Server Error
  deprecated: false
  type: path
components:
  schemas: {}

````