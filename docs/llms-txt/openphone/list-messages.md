# Source: https://www.quo.com/docs/mdx/api-reference/messages/list-messages.md

# List messages

> Retrieve a chronological list of messages exchanged between your OpenPhone number and specified participants, with support for filtering and pagination. 

## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json get /v1/messages
paths:
  path: /v1/messages
  method: get
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
      query:
        phoneNumberId:
          schema:
            - type: string
              required: true
              description: >-
                The unique identifier of the OpenPhone number used to send or
                receive the messages. PhoneNumberID can be retrieved via the Get
                Phone Numbers endpoint.
              examples:
                - OP123abc
              example: OP123abc
        userId:
          schema:
            - type: string
              required: false
              description: The unique identifier of the user the message was sent from.
              examples:
                - US123abc
              example: US123abc
        participants:
          schema:
            - type: array
              items:
                allOf:
                  - description: >-
                      A phone number in E.164 format, including the country
                      code.
                    examples:
                      - '+15555555555'
                    pattern: ^\+[1-9]\d{1,14}$
                    type: string
              required: true
              description: >-
                Array of phone numbers involved in the conversation, excluding
                your OpenPhone number, in E.164 format.
              examples:
                - '+15555555555'
              example: '+15555555555'
        since:
          schema:
            - type: string
              required: false
              description: >-
                DEPRECATED, use "createdAfter" or "createdBefore" instead.
                "since" currently behaves as "createdBefore" and will be removed
                in an upcoming release.
              deprecated: true
              examples:
                - '2022-01-01T00:00:00Z'
              format: date-time
              example: '2022-01-01T00:00:00Z'
        createdAfter:
          schema:
            - type: string
              required: false
              description: >-
                Filter results to only include messages created after the
                specified date and time, in ISO_8601 format.
              examples:
                - '2022-01-01T00:00:00Z'
              format: date-time
              example: '2022-01-01T00:00:00Z'
        createdBefore:
          schema:
            - type: string
              required: false
              description: >-
                Filter results to only include messages created before the
                specified date and time, in ISO_8601 format.
              examples:
                - '2022-01-01T00:00:00Z'
              format: date-time
              example: '2022-01-01T00:00:00Z'
        maxResults:
          schema:
            - type: integer
              required: true
              description: Maximum number of results to return per page.
              maximum: 100
              minimum: 1
              default: 10
        pageToken:
          schema:
            - type: string
              required: false
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    items:
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
                            A phone number in E.164 format, including the
                            country code.
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
                            The direction of the message relative to the
                            OpenPhone number.
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
                            The timestamp when the message was created at, in
                            ISO 8601 format
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
              totalItems:
                allOf:
                  - description: >-
                      Total number of items available. ⚠️ Note: `totalItems` is
                      not accurately returning the total number of items that
                      can be paginated. We are working on fixing this issue.
                    type: integer
              nextPageToken:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
            requiredProperties:
              - data
              - totalItems
              - nextPageToken
        examples:
          example:
            value:
              data:
                - id: AC123abc
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
              totalItems: 123
              nextPageToken: <string>
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