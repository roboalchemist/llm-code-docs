# Source: https://www.quo.com/docs/mdx/api-reference/calls/get-a-call-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.quo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a call by ID

> Get a call by its unique identifier.



## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json get /v1/calls/{callId}
openapi: 3.1.0
info:
  title: OpenPhone Public API
  version: 1.0.0
  description: API for connecting with OpenPhone.
  contact:
    name: OpenPhone Support
    email: support@openphone.com
    url: https://support.openphone.com/hc/en-us
  termsOfService: https://www.openphone.com/terms
servers:
  - description: Production server
    url: https://api.openphone.com
security:
  - apiKey: []
tags:
  - description: Operations related to calls
    name: Calls
  - description: >-
      Operations related to call summaries, including AI-generated summaries and
      Sona voice assistant summaries
    name: Call Summaries
  - description: >-
      Operations related to call transcripts, including AI-generated transcripts
      and Sona voice assistant transcripts
    name: Call Transcripts
  - description: Operations related to contacts
    name: Contacts
  - description: Operations related to conversations
    name: Conversations
  - description: Operations related to text messages
    name: Messages
  - description: Operations related to phone numbers
    name: Phone Numbers
  - description: Operations related to users
    name: Users
  - description: Operations related to webhooks
    name: Webhooks
paths:
  /v1/calls/{callId}:
    get:
      tags:
        - Calls
      summary: Get a call by ID
      description: Get a call by its unique identifier.
      operationId: getCallById_v1
      parameters:
        - in: path
          name: callId
          required: true
          schema:
            description: Unique identifier of the call.
            examples:
              - AC3700e624eca547eb9f749a06f2eb1
            pattern: ^AC(.*)$
            type: string
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    additionalProperties: false
                    type: object
                    properties:
                      answeredAt:
                        anyOf:
                          - description: >-
                              The timestamp when the call was answered in ISO
                              8601 format. Null if the call was not answered.
                            examples:
                              - '2022-01-01T00:00:00Z'
                            format: date-time
                            type: string
                          - type: 'null'
                      answeredBy:
                        anyOf:
                          - description: >-
                              The unique identifier of the OpenPhone user who
                              answered the incoming call. Null for outgoing
                              calls or unanswered incoming calls.
                            examples:
                              - USlHhXmRMz
                            type: string
                          - type: 'null'
                      initiatedBy:
                        anyOf:
                          - description: >-
                              The unique identifier of the OpenPhone user who
                              initiated the outgoing call. Null for incoming
                              calls.
                            examples:
                              - USlHhXmRMz
                            type: string
                          - type: 'null'
                      direction:
                        type: string
                        enum:
                          - incoming
                          - outgoing
                        description: >-
                          The direction of the call relative to the OpenPhone
                          number.
                        examples:
                          - incoming
                      status:
                        type: string
                        enum:
                          - queued
                          - initiated
                          - ringing
                          - in-progress
                          - completed
                          - busy
                          - failed
                          - no-answer
                          - canceled
                          - missed
                          - answered
                          - forwarded
                          - abandoned
                        description: The current status of the call.
                        examples:
                          - completed
                      completedAt:
                        anyOf:
                          - description: >-
                              The timestamp when the call ended, in ISO 8601
                              format. Null if the call is ongoing or was not
                              completed.
                            examples:
                              - '2022-01-01T00:00:00Z'
                            format: date-time
                            type: string
                          - type: 'null'
                      createdAt:
                        description: >-
                          The timestamp when the call record was created, in ISO
                          8601 format.
                        examples:
                          - '2022-01-01T00:00:00Z'
                        format: date-time
                        type: string
                      callRoute:
                        anyOf:
                          - description: >-
                              How the call reached the user's inbox: either by
                              direct dial to their number or routed through a
                              phone menu. Null for outbound calls.
                            examples:
                              - phone-number
                              - phone-menu
                            type: string
                          - type: 'null'
                      duration:
                        description: The total duration of the call in seconds.
                        examples:
                          - 60
                        type: integer
                      forwardedFrom:
                        anyOf:
                          - anyOf:
                              - description: >-
                                  A phone number in E.164 format, including the
                                  country code.
                                examples:
                                  - '+15555555555'
                                pattern: ^\+[1-9]\d{1,14}$
                                type: string
                              - pattern: ^US(.*)$
                                type: string
                          - type: 'null'
                      forwardedTo:
                        anyOf:
                          - anyOf:
                              - description: >-
                                  A phone number in E.164 format, including the
                                  country code.
                                examples:
                                  - '+15555555555'
                                pattern: ^\+[1-9]\d{1,14}$
                                type: string
                              - pattern: ^US(.*)$
                                type: string
                          - type: 'null'
                      aiHandled:
                        anyOf:
                          - description: >-
                              Type of AI that answered the call. Set to
                              'ai-agent' for AI responses, or null for human
                              responses.
                            examples:
                              - ai-agent
                            type: string
                          - type: 'null'
                      id:
                        description: The unique identifier of the call.
                        examples:
                          - AC123abc
                        pattern: ^AC(.*)$
                        type: string
                      phoneNumberId:
                        description: >-
                          The unique identifier of the OpenPhone number
                          associated with the call.
                        examples:
                          - PN123abc
                        pattern: ^PN(.*)$
                        type: string
                      participants:
                        maxItems: 2
                        type: array
                        items:
                          description: >-
                            A phone number in E.164 format, including the
                            country code.
                          examples:
                            - '+15555555555'
                          pattern: ^\+[1-9]\d{1,14}$
                          type: string
                      updatedAt:
                        anyOf:
                          - description: >-
                              The timestamp when the call record was last
                              updated, in ISO 8601 format. Null if never
                              updated.
                            examples:
                              - '2022-01-01T00:00:00Z'
                            format: date-time
                            type: string
                          - type: 'null'
                      userId:
                        description: >-
                          The unique identifier of the OpenPhone user account
                          associated with the call.
                        examples:
                          - US123abc
                        pattern: ^US(.*)$
                        type: string
                    required:
                      - answeredAt
                      - answeredBy
                      - initiatedBy
                      - direction
                      - status
                      - completedAt
                      - createdAt
                      - callRoute
                      - duration
                      - forwardedFrom
                      - forwardedTo
                      - aiHandled
                      - id
                      - phoneNumberId
                      - participants
                      - updatedAt
                      - userId
                required:
                  - data
        '400':
          description: Too Many Participants
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0101400'
                    type: string
                  status:
                    const: 400
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Too Many Participants
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                  description:
                    const: Too Many Participants
                    type: string
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
                  - description
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0100401'
                    type: string
                  status:
                    const: 401
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Unauthorized
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '403':
          description: Not Phone Number User
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0101403'
                    type: string
                  status:
                    const: 403
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Not Phone Number User
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                  description:
                    const: Not Phone Number User
                    type: string
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
                  - description
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0100404'
                    type: string
                  status:
                    const: 404
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Not Found
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '500':
          description: Unknown Error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0101500'
                    type: string
                  status:
                    const: 500
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Unknown
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      in: header
      name: Authorization
      type: apiKey

````