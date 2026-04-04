# Source: https://docs.asapp.com/apis/generativeagent/get-call-transfer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Call Transfer

> Get Call Transfer resource by ID.




## OpenAPI

````yaml api-specs/generativeagent.yaml get /generativeagent/v1/call-transfers/{callTransferId}
openapi: 3.0.1
info:
  title: GenerativeAgent API
  description: >
    GenerativeAgent API allows customers to interact with a chat / voice
    automation bot leveraging LLMs by sending messages and receiving responses
    asynchronously through webhooks
  contact:
    email: api-info@asapp.com
  license:
    name: ASAPP Software License
    url: https://api.asapp.com/LICENSE
  version: '0.1'
servers:
  - url: https://api.sandbox.asapp.com
security:
  - API-ID: []
    API-Secret: []
tags:
  - name: GenerativeAgent
    description: >-
      Operations to send messages and trigger GenerativeAgent to respond or
      query the current state
paths:
  /generativeagent/v1/call-transfers/{callTransferId}:
    get:
      tags:
        - GenerativeAgent
      summary: Get Call Transfer
      description: |
        Get Call Transfer resource by ID.
      operationId: getCallTransfer
      parameters:
        - name: callTransferId
          description: The identifier for the call transfer.
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                description: Get Call Transfer Response
                type: object
                properties:
                  id:
                    description: The unique identifier for this call transfer request.
                    type: string
                    example: 0867617078-0032318833-2221801472-0002236962
                  externalConversationId:
                    description: >-
                      The unique identifier of the call in your call system.
                      This will be referenced in ASAPP reporting.
                    type: string
                    example: 0867617078-0032318833-2221801472-0002236962
                  status:
                    description: >
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
                    description: >-
                      Timestamp (ISO 8601) when the call transfer resource was
                      created.
                    type: string
                    example: '2024-06-01T12:34:56Z'
                  callReceivedAt:
                    description: >-
                      Timestamp (ISO 8601) when the call transfer was received
                      by ASAPP.
                    type: string
                    example: '2024-06-01T12:34:56Z'
                  completedAt:
                    description: >-
                      Timestamp (ISO 8601) when the call transfer was completed
                      by the Generative Agent.
                    type: string
                    example: '2024-06-01T12:34:56Z'
                  inputContext:
                    description: >-
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
                    description: >-
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
                    description: The type of call transfer method that was used.
                    type: string
                    enum:
                      - PHONE_NUMBER
                      - SIP
                  phoneNumber:
                    description: >-
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
                    description: >
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
                required:
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