# Source: https://www.quo.com/docs/mdx/api-reference/messages/send-a-text-message.md

# Send a text message

> Send a text message from your OpenPhone number to a recipient.

## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json post /v1/messages
paths:
  path: /v1/messages
  method: post
  servers:
    - url: https://api.openphone.com
      description: Production server
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            Authorization:
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
              content:
                allOf:
                  - minLength: 1
                    maxLength: 1600
                    pattern: .*\S.*
                    description: The text content of the message to be sent.
                    type: string
              phoneNumberId:
                allOf:
                  - description: >-
                      DEPRECATED, use "from" instead. OpenPhone phone number ID
                      to send a message from
                    examples:
                      - OP1232abc
                    deprecated: true
                    pattern: ^PN(.*)$
                    type: string
              from:
                allOf:
                  - anyOf:
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
                allOf:
                  - minItems: 1
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
                allOf:
                  - description: >-
                      The unique identifier of the OpenPhone user sending the
                      message. If not provided, defaults to the phone number
                      owner.
                    examples:
                      - US123abc
                    pattern: ^US(.*)$
                    type: string
              setInboxStatus:
                allOf:
                  - type: string
                    enum:
                      - done
                    description: >-
                      Used to set the status of the related OpenPhone inbox
                      conversation. The default behavior without setting this
                      parameter will be for the message sent to show up as an
                      open conversation in the user's inbox. Setting the
                      parameter to `'done'` would move the conversation to the
                      Done inbox view.
                    examples:
                      - done
            required: true
            requiredProperties:
              - content
              - from
              - to
        examples:
          example:
            value:
              content: <string>
              phoneNumberId: OP1232abc
              from: <string>
              to:
                - '+15555555555'
              userId: US123abc
              setInboxStatus: done
  response:
    '202':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
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
            requiredProperties:
              - data
        examples:
          example:
            value:
              data:
                id: AC123abc
                to:
                  - '+15555555555'
                from: '+15555555555'
                text: Hello, world!
                phoneNumberId: PN123abc
                direction: incoming
                userId: US123abc
                status: sent
                createdAt: '2022-01-01T00:00:00Z'
                updatedAt: '2022-01-01T00:00:00Z'
        description: Success
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0206400'
                    type: string
              status:
                allOf:
                  - const: 400
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: A2P Registration Not Approved
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
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
                allOf:
                  - const: A2P Registration Not Approved
                    type: string
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
              - description
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
              description: <string>
        description: A2P Registration Not Approved
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0200401'
                    type: string
              status:
                allOf:
                  - const: 401
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Unauthorized
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
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
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
        description: Unauthorized
    '402':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0200402'
                    type: string
              status:
                allOf:
                  - const: 402
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Not Enough Credits
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
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
                allOf:
                  - const: >-
                      The organization does not have enough prepaid credits to
                      send the message
                    type: string
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
              - description
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
              description: <string>
        description: Not Enough Credits
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0202403'
                    type: string
              status:
                allOf:
                  - const: 403
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Not Phone Number User
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
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
                allOf:
                  - const: Not Phone Number User
                    type: string
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
              - description
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
              description: <string>
        description: Not Phone Number User
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0200404'
                    type: string
              status:
                allOf:
                  - const: 404
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Not Found
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
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
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
        description: Not Found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0201500'
                    type: string
              status:
                allOf:
                  - const: 500
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Unknown
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
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
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
        description: Unknown Error
  deprecated: false
  type: path
components:
  schemas: {}

````