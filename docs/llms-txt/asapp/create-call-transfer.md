# Source: https://docs.asapp.com/apis/generativeagent/create-call-transfer.md

# Create Call Transfer

> Creates a new Call Transfer resource that represents an attempt to transfer a call from your IVR or CCaaS to ASAPP.

The `type` indicates the type of call transfer:
- `PHONE_NUMBER`: A temporary phone number is assigned for the transfer.
- `SIP`: Session Initiation Protocol (SIP) transfer.

You can optionally provide `inputContext` to provide context for the conversation. This is passed to GenerativeAgent.


## OpenAPI

````yaml api-specs/generativeagent.yaml post /generativeagent/v1/call-transfers
paths:
  path: /generativeagent/v1/call-transfers
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - description: >-
                      A unique identifier for this call transfer request. This
                      should be different for each transfer attempt.
                    type: string
                    example: 0867617078-0032318833-2221801472-0002236962
              externalConversationId:
                allOf:
                  - description: >
                      The unique identifier of the call in your call system.
                      Multiple call transfers using the same
                      externalConversationId will be treated as a single
                      conversation. 


                      This is the primary identifier for conversations within
                      ASAPP and is reflected in reporting.
                    type: string
                    example: 0867617078-0032318833-2221801472-0002236962
              type:
                allOf:
                  - description: >
                      The type of call transfer being made. Currently supports:

                      - `PHONE_NUMBER`: A temporary phone number is assigned for
                      the transfer.

                      - `SIP`: Session Initiation Protocol (SIP) transfer.
                    type: string
                    enum:
                      - PHONE_NUMBER
                      - SIP
              phoneNumber:
                allOf:
                  - description: >-
                      Configuration information for requesting a phone number.
                      Mandatory if `type` is `PHONE_NUMBER`.
                    type: object
                    properties:
                      country:
                        description: >-
                          Country code (ISO 3166 Alpha 2) for the phone number
                          to be assigned. Determines the country of the
                          temporary transfer number.
                        type: string
                        example: US
                    required:
                      - country
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
              inputContext:
                allOf:
                  - description: >-
                      Optional context information to pass to the Generative
                      Agent when the call is received.
                    type: object
                    properties:
                      taskName:
                        description: >-
                          The name of the task that the [Generative Agent will
                          enter](generativeagent/configuring/tasks-and-functions/enter-specific-task)
                          when the call begins.
                        type: string
                      inputVariables:
                        description: >-
                          Key-value pairs of [input
                          variables](/generativeagent/configuring/tasks-and-functions/input-variables)
                          that provide context to the Generative Agent for the
                          conversation.
                        type: object
                        additionalProperties:
                          type: string
            required: true
            description: Post Call Transfer Request
            requiredProperties:
              - id
              - externalConversationId
              - type
            example:
              id: 0867617078-0032318833-2221801472-0002236962
              externalConversationId: 0867617078-0032318833-2221801472-0002236962
              type: PHONE_NUMBER
              phoneNumber:
                country: US
              inputContext:
                taskName: Welcome
                inputVariables:
                  email: example@gmail.com
                  name: name
        examples:
          example:
            value:
              id: 0867617078-0032318833-2221801472-0002236962
              externalConversationId: 0867617078-0032318833-2221801472-0002236962
              type: PHONE_NUMBER
              phoneNumber:
                country: US
              inputContext:
                taskName: Welcome
                inputVariables:
                  email: example@gmail.com
                  name: name
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - description: >-
                      The unique identifier for this call transfer request,
                      matching the ID provided in the request.
                    type: string
                    example: 0867617078-0032318833-2221801472-0002236962
              externalConversationId:
                allOf:
                  - description: >-
                      The unique identifier of the call in your call system.
                      This will be referenced in ASAPP reporting. Usually this
                      is the same value as the call transfer ID.
                    type: string
                    example: 0867617078-0032318833-2221801472-0002236962
              status:
                allOf:
                  - description: >
                      The current status of the call transfer request. 


                      On creation, the status is `ACTIVE` and is waiting for
                      your system to transfer the call.
                    type: string
                    enum:
                      - ACTIVE
                      - ONGOING
                      - COMPLETED
                      - EXPIRED
              type:
                allOf:
                  - description: The type of call transfer method being used.
                    type: string
                    enum:
                      - PHONE_NUMBER
                      - SIP
              phoneNumber:
                allOf:
                  - description: >-
                      Details about the assigned phone number for the transfer.
                      Available only if `type` is `PHONE_NUMBER`.
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
              inputContext:
                allOf:
                  - description: >-
                      The context information that will be passed to the
                      Generative Agent when the call is received.
                    type: object
                    properties:
                      taskName:
                        description: >-
                          The name of the task that the [Generative Agent will
                          enter](generativeagent/configuring/tasks-and-functions/enter-specific-task)
                          when the call begins.
                        type: string
                      inputVariables:
                        description: >-
                          Key-value pairs of [input
                          variables](/generativeagent/configuring/tasks-and-functions/input-variables)
                          that provide context to the Generative Agent for the
                          conversation.
                        type: object
                        additionalProperties:
                          type: string
                        example:
                          email: example@gmail.com
                          name: name
            description: Post Call Transfer Response
            requiredProperties:
              - id
              - externalConversationId
              - type
            example:
              id: 0867617078-0032318833-2221801472-0002236962
              externalConversationId: 0867617078-0032318833-2221801472-0002236962
              type: PHONE_NUMBER
              phoneNumber:
                transferNumber: '+19995550199'
                country: US
                expiresAt: '2024-06-01T12:34:56Z'
              inputContext:
                taskName: Welcome
                inputVariables:
                  email: example@gmail.com
                  name: name
        examples:
          example:
            value:
              id: 0867617078-0032318833-2221801472-0002236962
              externalConversationId: 0867617078-0032318833-2221801472-0002236962
              type: PHONE_NUMBER
              phoneNumber:
                transferNumber: '+19995550199'
                country: US
                expiresAt: '2024-06-01T12:34:56Z'
              inputContext:
                taskName: Welcome
                inputVariables:
                  email: example@gmail.com
                  name: name
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