# Source: https://docs.asapp.com/apis/generativeagent/get-call-transfer.md

# Get Call Transfer

> Get Call Transfer resource by ID.


## OpenAPI

````yaml api-specs/generativeagent.yaml get /generativeagent/v1/call-transfers/{callTransferId}
paths:
  path: /generativeagent/v1/call-transfers/{callTransferId}
  method: get
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
        callTransferId:
          schema:
            - type: string
              required: true
              description: The identifier for the call transfer.
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - description: The unique identifier for this call transfer request.
                    type: string
                    example: 0867617078-0032318833-2221801472-0002236962
              externalConversationId:
                allOf:
                  - description: >-
                      The unique identifier of the call in your call system.
                      This will be referenced in ASAPP reporting.
                    type: string
                    example: 0867617078-0032318833-2221801472-0002236962
              status:
                allOf:
                  - description: >
                      The current status of the call transfer request.

                      - `ACTIVE`: The call transfer request has been created and
                      is waiting for your system to transfer the call.

                      - `ONGOING`: The call transfer has been received by ASAPP
                      and is currently in progress. The phone number is no
                      longer assigned to the call transfer request.

                      - `COMPLETED`: The call transfer has been successfully
                      completed. The output context will be returned.

                      - `EXPIRED`: The call transfer request is no longer valid
                      (e.g., the phone number expired). 
                    type: string
                    enum:
                      - ACTIVE
                      - ONGOING
                      - COMPLETED
                      - EXPIRED
              createdAt:
                allOf:
                  - description: >-
                      Timestamp (ISO 8601) when the call transfer resource was
                      created.
                    type: string
                    example: '2024-06-01T12:34:56Z'
              callReceivedAt:
                allOf:
                  - description: >-
                      Timestamp (ISO 8601) when the call transfer was received
                      by ASAPP.
                    type: string
                    example: '2024-06-01T12:34:56Z'
              completedAt:
                allOf:
                  - description: >-
                      Timestamp (ISO 8601) when the call transfer was completed
                      by the Generative Agent.
                    type: string
                    example: '2024-06-01T12:34:56Z'
              inputContext:
                allOf:
                  - description: >-
                      The context information that was passed to the Generative
                      Agent when the call was received.
                    type: object
                    properties:
                      taskName:
                        description: >-
                          The name of the task that the [Generative Agent
                          entered](generativeagent/configuring/tasks-and-functions/enter-specific-task)
                          when the call began.
                        type: string
                      inputVariables:
                        description: >-
                          Key-value pairs of [input
                          variables](/generativeagent/configuring/tasks-and-functions/input-variables)
                          that provided context to the Generative Agent for the
                          conversation.
                        type: object
                        additionalProperties:
                          type: string
                    example:
                      taskName: welcome
                      variables:
                        email: example@gmail.com
                        name: name
              outputContext:
                allOf:
                  - description: >-
                      The context information from the Generative Agent when the
                      call ended.
                    type: object
                    properties:
                      transferType:
                        description: >
                          The type of returning transfer. Can be one of:

                          - **AGENT**: GenerativeAgent has requested to transfer
                          the call to a human agent.

                          - **SYSTEM**: A task has requested to hand the call
                          back to the originating system. Usually indicative
                          that the call was handle successfully.
                        type: string
                        enum:
                          - AGENT
                          - SYSTEM
                      currentTaskName:
                        description: >-
                          The name of the task that the Generative Agent was
                          executing when the call ended.
                        type: string
                      referenceVariables:
                        description: >-
                          Key-value pairs of reference variables that were set
                          during the conversation as returned during a [system
                          transfer](/generativeagent/configuring/tasks-and-functions/system-transfer).
                        type: object
                        additionalProperties:
                          type: string
                      transferVariables:
                        description: >-
                          Key-value pairs of transfer variables that can be used
                          when transferring to another system as returned during
                          a [system
                          transfer](/generativeagent/configuring/tasks-and-functions/system-transfer).
                        type: object
                        additionalProperties:
                          type: string
                    example:
                      currentTaskName: welcome
                      referenceVariables:
                        reference_variable_1: reference_value_1
                        reference_variable_2: reference_value_2
                      transferVariables:
                        transfer_variable_1: transfer_value_1
                        transfer_variable_2: transfer_value_2
              type:
                allOf:
                  - description: The type of call transfer method that was used.
                    type: string
                    enum:
                      - PHONE_NUMBER
                      - SIP
              phoneNumber:
                allOf:
                  - description: >-
                      Details about the assigned phone number for the transfer,
                      including the number to dial and when it expires. Only
                      available if `type` is `PHONE_NUMBER`.
                    type: object
                    properties:
                      transferNumber:
                        description: >-
                          The phone number that your IVR should dial to transfer
                          the call to ASAPP.
                        type: string
                        example: '+19995550199'
                      country:
                        description: >-
                          Country code (ISO 3166 Alpha 2) of the assigned phone
                          number.
                        type: string
                        example: US
                      expiresAt:
                        description: >-
                          Timestamp (ISO 8601) when the transfer phone number
                          will expire and become unavailable.
                        type: string
                        example: '2024-06-01T12:34:56Z'
                    required:
                      - transferNumber
                      - country
                      - expiresAt
              sip:
                allOf:
                  - description: >
                      Configuration for SIP transfers. Defines how the call will
                      be transferred back when the Generative Agent finishes the
                      conversation.


                      **Transfer Types:**

                      - `BYE`: Ends the call with a SIP BYE message. Use for
                      supervised transfers to Generative Agent.

                      - `REFER`: Sends a SIP REFER message with the return URI
                      in the Refer-To header. Use for blind transfers to another
                      system.

                      - `INVITE`: Initiates a new SIP INVITE to the return URI,
                      ASAPP will continue to transcribe the call until the call
                      is ended.
                    type: object
                    properties:
                      returnTransferType:
                        description: >
                          How the call will be transferred back when the
                          Generative Agent finishes the conversation.

                          - `BYE`: Ends the call with a SIP BYE message. Use for
                          supervised transfers to Generative Agent.

                          - `REFER`: Sends a SIP REFER message with the return
                          URI in the Refer-To header. Use for blind transfers to
                          another system.

                          - `INVITE`: Initiates a new SIP INVITE to the return
                          URI, ASAPP will continue to transcribe the call until
                          the call is ended.
                        type: string
                        enum:
                          - BYE
                          - REFER
                          - INVITE
                      returnUri:
                        description: >
                          The SIP URI to transfer the call back to when the
                          conversation ends.

                          - Used in the Refer-To header if `returnTransferType`
                          is `REFER`

                          - Used as the destination for the SIP INVITE if
                          `returnTransferType` is `INVITE`

                          - Not used if `returnTransferType` is `BYE`
                        type: string
                      returnInviteAuthentication:
                        description: >-
                          Authentication credentials for SIP INVITE transfers.
                          Required only when `returnTransferType` is `INVITE`
                          and authentication is needed.
                        type: object
                        properties:
                          username:
                            description: >-
                              Authentication username for the SIP INVITE.
                              Required if authentication is needed.
                            type: string
                            example: sip_user
                          password:
                            description: >-
                              Authentication password for the SIP INVITE.
                              Required if authentication is needed.
                            type: string
                            example: sip_password
                    example:
                      returnTransferType: REFER
                      returnUri: sip:transfer@your-company.com:5060
            description: Get Call Transfer Response
            requiredProperties:
              - id
              - externalConversationId
              - status
              - createdAt
              - type
            example:
              id: 0867617078-0032318833-2221801472-0002236962
              externalConversationId: 0867617078-0032318833-2221801472-0002236962
              status: completed
              createdAt: '2024-06-01T12:34:56Z'
              callReceivedAt: '2024-06-01T12:35:00Z'
              completedAt: '2024-06-01T12:38:56Z'
              inputContext:
                taskName: Welcome
                inputVariables:
                  email: example@gmail.com
                  name: name
              outputContext:
                transferType: SYSTEM
                currentTaskName: Welcome
                referenceVariables:
                  reference_variable_1: reference_value_1
                  reference_variable_2: reference_value_2
                transferVariables:
                  transfer_variable_1: transfer_value_1
                  transfer_variable_2: transfer_value_2
              type: PHONE_NUMBER
              phoneNumber:
                transferNumber: '+19995550199'
                country: US
                expiresAt: '2024-06-01T12:35:56Z'
        examples:
          example:
            value:
              id: 0867617078-0032318833-2221801472-0002236962
              externalConversationId: 0867617078-0032318833-2221801472-0002236962
              status: completed
              createdAt: '2024-06-01T12:34:56Z'
              callReceivedAt: '2024-06-01T12:35:00Z'
              completedAt: '2024-06-01T12:38:56Z'
              inputContext:
                taskName: Welcome
                inputVariables:
                  email: example@gmail.com
                  name: name
              outputContext:
                transferType: SYSTEM
                currentTaskName: Welcome
                referenceVariables:
                  reference_variable_1: reference_value_1
                  reference_variable_2: reference_value_2
                transferVariables:
                  transfer_variable_1: transfer_value_1
                  transfer_variable_2: transfer_value_2
              type: PHONE_NUMBER
              phoneNumber:
                transferNumber: '+19995550199'
                country: US
                expiresAt: '2024-06-01T12:35:56Z'
        description: Successful response
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