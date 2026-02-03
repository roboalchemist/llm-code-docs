# Source: https://docs.asapp.com/apis/generativeagent/create-call-transfer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Call Transfer

> Creates a new Call Transfer resource that represents an attempt to transfer a call from your IVR or CCaaS to ASAPP.

The `type` indicates the type of call transfer:
- `PHONE_NUMBER`: A temporary phone number is assigned for the transfer.
- `SIP`: Session Initiation Protocol (SIP) transfer.

You can optionally provide `inputContext` to provide context for the conversation. This is passed to GenerativeAgent.




## OpenAPI

````yaml api-specs/generativeagent.yaml post /generativeagent/v1/call-transfers
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
  /generativeagent/v1/call-transfers:
    post:
      tags:
        - GenerativeAgent
      summary: Create Call Transfer
      description: >
        Creates a new Call Transfer resource that represents an attempt to
        transfer a call from your IVR or CCaaS to ASAPP.


        The `type` indicates the type of call transfer:

        - `PHONE_NUMBER`: A temporary phone number is assigned for the transfer.

        - `SIP`: Session Initiation Protocol (SIP) transfer.


        You can optionally provide `inputContext` to provide context for the
        conversation. This is passed to GenerativeAgent.
      operationId: createCallTransfer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              description: Post Call Transfer Request
              type: object
              properties:
                id:
                  description: >-
                    A unique identifier for this call transfer request. This
                    should be different for each transfer attempt.
                  type: string
                  example: 0867617078-0032318833-2221801472-0002236962
                externalConversationId:
                  description: >
                    The unique identifier of the call in your call system.
                    Multiple call transfers using the same
                    externalConversationId will be treated as a single
                    conversation. 


                    This is the primary identifier for conversations within
                    ASAPP and is reflected in reporting.
                  type: string
                  example: 0867617078-0032318833-2221801472-0002236962
                type:
                  description: >
                    The type of call transfer being made. Currently supports:

                    - `PHONE_NUMBER`: A temporary phone number is assigned for
                    the transfer.

                    - `SIP`: Session Initiation Protocol (SIP) transfer.
                  type: string
                  enum:
                    - PHONE_NUMBER
                    - SIP
                phoneNumber:
                  description: >-
                    Configuration information for requesting a phone number.
                    Mandatory if `type` is `PHONE_NUMBER`.
                  type: object
                  properties:
                    country:
                      description: >-
                        Country code (ISO 3166 Alpha 2) for the phone number to
                        be assigned. Determines the country of the temporary
                        transfer number.
                      type: string
                      example: US
                  required:
                    - country
                sip:
                  description: >
                    Configuration for SIP transfers. Defines how the call will
                    be transferred back when the Generative Agent finishes the
                    conversation.


                    **Transfer Types:**

                    - `BYE`: Ends the call with a SIP BYE message. Use for
                    supervised transfers to Generative Agent.

                    - `REFER`: Sends a SIP REFER message with the return URI in
                    the Refer-To header. Use for blind transfers to another
                    system.

                    - `INVITE`: Initiates a new SIP INVITE to the return URI,
                    ASAPP will continue to transcribe the call until the call is
                    ended.
                  type: object
                  properties:
                    returnTransferType:
                      description: >
                        How the call will be transferred back when the
                        Generative Agent finishes the conversation.

                        - `BYE`: Ends the call with a SIP BYE message. Use for
                        supervised transfers to Generative Agent.

                        - `REFER`: Sends a SIP REFER message with the return URI
                        in the Refer-To header. Use for blind transfers to
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

                        - Used in the Refer-To header if `returnTransferType` is
                        `REFER`

                        - Used as the destination for the SIP INVITE if
                        `returnTransferType` is `INVITE`

                        - Not used if `returnTransferType` is `BYE`
                      type: string
                    returnInviteAuthentication:
                      description: >-
                        Authentication credentials for SIP INVITE transfers.
                        Required only when `returnTransferType` is `INVITE` and
                        authentication is needed.
                      type: object
                      properties:
                        username:
                          description: >-
                            Authentication username for the SIP INVITE. Required
                            if authentication is needed.
                          type: string
                          example: sip_user
                        password:
                          description: >-
                            Authentication password for the SIP INVITE. Required
                            if authentication is needed.
                          type: string
                          example: sip_password
                  example:
                    returnTransferType: REFER
                    returnUri: sip:transfer@your-company.com:5060
                inputContext:
                  description: >-
                    Optional context information to pass to the Generative Agent
                    when the call is received.
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
              required:
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
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                description: Post Call Transfer Response
                type: object
                properties:
                  id:
                    description: >-
                      The unique identifier for this call transfer request,
                      matching the ID provided in the request.
                    type: string
                    example: 0867617078-0032318833-2221801472-0002236962
                  externalConversationId:
                    description: >-
                      The unique identifier of the call in your call system.
                      This will be referenced in ASAPP reporting. Usually this
                      is the same value as the call transfer ID.
                    type: string
                    example: 0867617078-0032318833-2221801472-0002236962
                  status:
                    description: >
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
                    description: The type of call transfer method being used.
                    type: string
                    enum:
                      - PHONE_NUMBER
                      - SIP
                  phoneNumber:
                    description: >-
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
                  inputContext:
                    description: >-
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
                required:
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