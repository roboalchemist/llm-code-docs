# Source: https://www.quo.com/docs/mdx/api-reference/messages/send-a-text-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.quo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send a text message

> Send a text message from your OpenPhone number to a recipient.



## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json post /v1/messages
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
  /v1/messages:
    post:
      tags:
        - Messages
      summary: Send a text message
      description: Send a text message from your OpenPhone number to a recipient.
      operationId: sendMessage_v1
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                content:
                  minLength: 1
                  maxLength: 1600
                  pattern: .*\S.*
                  description: The text content of the message to be sent.
                  type: string
                phoneNumberId:
                  description: >-
                    DEPRECATED, use "from" instead. OpenPhone phone number ID to
                    send a message from
                  examples:
                    - OP1232abc
                  deprecated: true
                  pattern: ^PN(.*)$
                  type: string
                from:
                  anyOf:
                    - pattern: ^PN(.*)$
                      type: string
                    - description: >-
                        A phone number in E.164 format, including the country
                        code.
                      examples:
                        - '+15555555555'
                      pattern: ^\+[1-9]\d{1,14}$
                      type: string
                to:
                  minItems: 1
                  maxItems: 1
                  type: array
                  items:
                    description: >-
                      A phone number in E.164 format, including the country
                      code.
                    examples:
                      - '+15555555555'
                    pattern: ^\+[1-9]\d{1,14}$
                    type: string
                userId:
                  description: >-
                    The unique identifier of the OpenPhone user sending the
                    message. If not provided, defaults to the phone number
                    owner.
                  examples:
                    - US123abc
                  pattern: ^US(.*)$
                  type: string
                setInboxStatus:
                  type: string
                  enum:
                    - done
                  description: >-
                    Used to set the status of the related OpenPhone inbox
                    conversation. The default behavior without setting this
                    parameter will be for the message sent to show up as an open
                    conversation in the user's inbox. Setting the parameter to
                    `'done'` would move the conversation to the Done inbox view.
                  examples:
                    - done
              required:
                - content
                - from
                - to
      responses:
        '202':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      id:
                        description: The unique identifier of the message.
                        examples:
                          - AC123abc
                        pattern: ^AC(.*)$
                        type: string
                      to:
                        type: array
                        items:
                          description: >-
                            A phone number in E.164 format, including the
                            country code.
                          examples:
                            - '+15555555555'
                          pattern: ^\+[1-9]\d{1,14}$
                          type: string
                      from:
                        description: >-
                          A phone number in E.164 format, including the country
                          code.
                        examples:
                          - '+15555555555'
                        pattern: ^\+[1-9]\d{1,14}$
                        type: string
                      text:
                        description: The content of the message.
                        examples:
                          - Hello, world!
                        type: string
                      phoneNumberId:
                        anyOf:
                          - description: >-
                              The unique identifier of the OpenPhone phone
                              number that the message was sent from.
                            examples:
                              - PN123abc
                            pattern: ^PN(.*)$
                            type: string
                          - type: 'null'
                      direction:
                        type: string
                        enum:
                          - incoming
                          - outgoing
                        description: >-
                          The direction of the message relative to the OpenPhone
                          number.
                        examples:
                          - incoming
                      userId:
                        description: >-
                          The unique identifier of the user who sent the
                          message. Null for incoming messages.
                        examples:
                          - US123abc
                        pattern: ^US(.*)$
                        type: string
                      status:
                        type: string
                        enum:
                          - queued
                          - sent
                          - delivered
                          - undelivered
                        description: The status of the message.
                        examples:
                          - sent
                      createdAt:
                        description: >-
                          The timestamp when the message was created at, in ISO
                          8601 format
                        examples:
                          - '2022-01-01T00:00:00Z'
                        format: date-time
                        type: string
                      updatedAt:
                        description: >-
                          The timestamp when the message status was last
                          updated, in ISO 8601 format.
                        examples:
                          - '2022-01-01T00:00:00Z'
                        format: date-time
                        type: string
                    required:
                      - id
                      - to
                      - from
                      - text
                      - phoneNumberId
                      - direction
                      - userId
                      - status
                      - createdAt
                      - updatedAt
                required:
                  - data
        '400':
          description: A2P Registration Not Approved
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0206400'
                    type: string
                  status:
                    const: 400
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: A2P Registration Not Approved
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
                    const: A2P Registration Not Approved
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
                    const: '0200401'
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
        '402':
          description: Not Enough Credits
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0200402'
                    type: string
                  status:
                    const: 402
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Not Enough Credits
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
                    const: >-
                      The organization does not have enough prepaid credits to
                      send the message
                    type: string
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
                  - description
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
                    const: '0202403'
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
                    const: '0200404'
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
                    const: '0201500'
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