# Source: https://docs.asapp.com/apis/autocompose/create-a-messagesent-analytics-event.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a MessageSent analytics event

> Create a MessageSent analytics event describing the agent's usage of AutoCompose augmentation features
while composing a message




## OpenAPI

````yaml api-specs/autocompose.yaml post /autocompose/v1/analytics/message-sent
openapi: 3.0.1
info:
  title: AutoCompose API
  description: >
    Autocompose API to suggest the next agent message.

    Suggestions are based on the conversation history, conversation metadata,
    and

    the in-progress message text the agent has already typed into the composer.
  version: 0.0.3
servers:
  - url: https://api.sandbox.asapp.com
security:
  - API-ID: []
    API-Secret: []
tags:
  - name: AutoCompose
    description: Improve agent productivity with AutoCompose API
paths:
  /autocompose/v1/analytics/message-sent:
    post:
      tags:
        - AutoCompose
      summary: Create a MessageSent analytics event
      description: >
        Create a MessageSent analytics event describing the agent's usage of
        AutoCompose augmentation features

        while composing a message
      operationId: createMessageSentEvent
      requestBody:
        description: The parameters for creating a MessageSent event
        content:
          application/json:
            schema:
              description: >-
                Analytics event describing the agent's usage of AutoCompose
                features while composing a message (we sometimes refer to these
                as augmentation features, because they augment the agent's
                work).

                Note that many of the fields are not technically required
                according to this spec. This does not mean that they can omitted
                arbitrarily. They should all be set, when they relevant for
                AutoCompose features a particular ASAPP customer is using and
                the data is available. For some use cases, some fields are not
                relevant (for example, phraseAutocompletePresentedCt is only
                relevant if phrase completions are being used). In other cases,
                the field may relevant but the data might not be avaialble (for
                example, if the request for suggestions returns too late, it
                might not be possible set initialSuggestionsId). The customer
                should try to fill in all relevant fields when they can; this
                information enables ASAPP to report on the performance of our
                features and to improve their perforamnce over time.

                When a field is omitted, it will take on a default value in the
                event data. String fields default to empty string and numeric
                fields default to 0.
              type: object
              required:
                - conversationId
                - messageId
                - augmentationType
              example:
                conversationId: 01G1167H5FFQ47SMSRYGKBW7HM
                messageId: 01BX5ZZKBKACTAV9WEVGEMMVS1
                augmentationType:
                  - AUTOSUGGEST
              properties:
                conversationId:
                  description: The ASAPP conversation id for the conversation.
                  type: string
                  example: 01G1167H5FFQ47SMSRYGKBW7HM
                messageId:
                  description: >
                    The ASAPP ID of the message that was sent. This is required
                    for every event,

                    to enable correlating the analytics event with the message
                    that was sent.
                  type: string
                  example: 01BX5ZZKBKACTAV9WEVGEMMVS1
                augmentationType:
                  description: >
                    Types of AutoCompose augmentation features used for
                    composing the

                    message. Ordering of augmentations and repeated uses of an

                    augmentation type are preserved. This is required, so that
                    the usage of

                    AutoCompose features can be measured.
                  type: array
                  items:
                    type: string
                    enum:
                      - FREEHAND
                      - AUTOSUGGEST
                      - AUTOCOMPLETE
                      - PHRASE_AUTOCOMPLETE
                      - CUSTOM_DRAWER
                      - CUSTOM_INSERT
                      - GLOBAL_INSERT
                      - FLUENCY_APPLY
                      - FLUENCY_UNDO
                  example:
                    - AUTOSUGGEST
                    - PHRASE_AUTOCOMPLETE
                    - FLUENCY_APPLY
                numEdits:
                  description: >
                    Number of keystrokes of editing the agent did after
                    selecting a full-message suggestions

                    (one of the suggestions in the suggestions array, not
                    phraseCompletion). Selecting a

                    full-message suggestion resets the counter. Accepting a
                    phrase completion by hitting tab

                    or right arrow increments the counter just like other
                    keystrokes. The idea is to have a rough

                    idea of how much editing the agent had to do after selecting
                    a full-message suggestion (in the

                    ideal case, the message was satisfactory to send as-is and
                    numEdits equals 0).
                  type: integer
                  example: 2
                selectedSuggestionText:
                  description: >
                    If the agent used a full-message suggestion to compose this
                    message,

                    this is the text of the suggestion
                  type: string
                  example: How can I help you today?
                selectedSuggestionsId:
                  description: >
                    If the agent used a full-message suggestion to compose this
                    message, this is the ID of

                    the set of suggestions that the suggestion came from. This
                    helps ASAPP assoicate the MessageSent

                    event with events emitted by AutoCompose internally. If the
                    agent did not use a full-message

                    suggestion, this field can left blank.
                  type: string
                  example: 4d2fd982640c311394008259594399a1
                selectedSuggestionIndex:
                  description: >
                    If the agent used a full-message suggestion to compose this
                    message, this is the

                    index of the selected suggestion in the set of suggestions
                    that the agent used, starting

                    from 1 for the top suggestion, 2 for the second from the
                    top, and so on. This should be

                    omitted if no suggestion was selected, but it is required if
                    the agent selected

                    a suggestion, to enable identifying which of the suggestions
                    was used.
                  type: integer
                  example: 1
                initialSuggestionsId:
                  description: >
                    The ID for the first set of suggestions the agent saw while
                    composing this message.

                    This is required for every event, if suggestions were shown
                    to the agent. If for some reason

                    suggestions were not available, it can be omitted.
                  type: string
                  example: 5e9491b203e6ecccfef964e26fb1a5d3
                timeToAction:
                  description: |
                    Number of seconds between the agent sending their previous
                    message and their first action for composing this message.
                    An agent action is when one of the following occur:
                     - Typing in the composer
                     - Selecting a suggestion
                     - Using a phrase completion
                     - Inserting a custom or global response from the library
                     - Pasting a text into the composer
                  type: number
                  example: 1.891412
                craftingTime:
                  description: |
                    Number of seconds between the agent's first action
                    and last action for composing this message.
                  type: number
                  example: 10.9472
                dwellTime:
                  description: |
                    Number of seconds between the agent's last action
                    for composing this message and the message being sent.
                  type: number
                  example: 4.132985
                phraseAutocompletePresentedCt:
                  description: |
                    Number of phrase autocomplete suggestions presented
                    to the agent.
                  type: integer
                  example: 3
                phraseAutocompleteSelectedCt:
                  description: |
                    Number of phrase autocomplete suggestions selected
                    by the agent.
                  type: integer
                  example: 1
      responses:
        '200':
          description: Successfully created a MessageSent event
          content: {}
        '400':
          description: 400 - Bad request
          content:
            application/json:
              schema:
                description: Bad request response
                type: object
                properties:
                  error:
                    example:
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
        '401':
          description: 401 - Unauthorized
          content:
            application/json:
              schema:
                description: Unauthorized response
                type: object
                properties:
                  error:
                    example:
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
        '403':
          description: 403 - Forbidden
          content:
            application/json:
              schema:
                description: Forbidden response
                type: object
                properties:
                  error:
                    example:
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
        '404':
          description: 404 - Not Found
          content:
            application/json:
              schema:
                description: Not Found response
                type: object
                properties:
                  error:
                    example:
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
        '409':
          description: 409 - Conflict
          content:
            application/json:
              schema:
                description: Conflict response
                type: object
                properties:
                  error:
                    example:
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
        '413':
          description: 413 - Request Entity Too Large
          content:
            application/json:
              schema:
                description: Request Entity Too Large response
                type: object
                properties:
                  error:
                    example:
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
        '422':
          description: 422 - Unprocessable Entity
          content:
            application/json:
              schema:
                description: Unprocessable Entity response
                type: object
                properties:
                  error:
                    example:
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
        '429':
          description: 429 - Too Many Requests
          content:
            application/json:
              schema:
                description: Too Many Requests response
                type: object
                properties:
                  error:
                    example:
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
        '503':
          description: 503 - Service Unavailable
          content:
            application/json:
              schema:
                description: Service Unavailable response
                type: object
                properties:
                  error:
                    example:
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
        default:
          description: 500 - Internal Server Error
          content:
            application/json:
              schema:
                description: Default error response
                type: object
                properties:
                  error:
                    example:
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
components:
  securitySchemes:
    API-ID:
      type: apiKey
      in: header
      name: asapp-api-id
    API-Secret:
      type: apiKey
      in: header
      name: asapp-api-secret

````