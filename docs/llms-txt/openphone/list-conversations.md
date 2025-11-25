# Source: https://www.quo.com/docs/mdx/api-reference/conversations/list-conversations.md

# List Conversations

> Fetch a paginated list of conversations of OpenPhone conversations. Can be filtered by user and/or phone numbers. Defaults to all conversations in the OpenPhone organization. Results are returned in descending order based on the most recent conversation.

## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json get /v1/conversations
paths:
  path: /v1/conversations
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
        phoneNumber:
          schema:
            - type: string
              required: false
              description: >-
                DEPRECATED, use `phoneNumbers` instead. If both `phoneNumber`
                and `phoneNumbers` are provided, `phoneNumbers` will be used.
                Filters results to only include conversations with the specified
                OpenPhone phone number. Can be either your OpenPhone phone
                number ID or the full phone number in E.164 format.

                A phone number in E.164 format, including the country code.
              deprecated: true
              examples:
                - '+15555555555'
              example: '+15555555555'
            - type: string
              required: false
              description: >-
                DEPRECATED, use `phoneNumbers` instead. If both `phoneNumber`
                and `phoneNumbers` are provided, `phoneNumbers` will be used.
                Filters results to only include conversations with the specified
                OpenPhone phone number. Can be either your OpenPhone phone
                number ID or the full phone number in E.164 format.
              deprecated: true
              examples:
                - '+15555555555'
                - PN123abc
              example: '+15555555555'
        phoneNumbers:
          schema:
            - type: array
              items:
                allOf:
                  - anyOf:
                      - description: >-
                          A phone number in E.164 format, including the country
                          code.
                        examples:
                          - '+15555555555'
                        pattern: ^\+[1-9]\d{1,14}$
                        type: string
                      - pattern: ^PN(.*)$
                        type: string
              required: false
              description: >-
                Filters results to only include conversations with the specified
                OpenPhone phone numbers. Each item can be either an OpenPhone
                phone number ID or a full phone number in E.164 format.
              examples:
                - - '+15555555555'
                  - PN123abc
              maxItems: 100
              minItems: 1
              example:
                '0': '+15555555555'
                '1': PN123abc
        userId:
          schema:
            - type: string
              required: false
              description: >-
                The unique identifier of the user the making the request. Used
                to filter results to only include the user's conversations.
              examples:
                - US123abc
              example: US123abc
        createdAfter:
          schema:
            - type: string
              required: false
              description: >-
                Filter results to only include conversations created after the
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
                Filter results to only include conversations created before the
                specified date and time, in ISO_8601 format.
              examples:
                - '2022-01-01T00:00:00Z'
              format: date-time
              example: '2022-01-01T00:00:00Z'
        excludeInactive:
          schema:
            - type: boolean
              required: false
              description: Exclude inactive conversations from the results.
              examples:
                - true
              example: true
        updatedAfter:
          schema:
            - type: string
              required: false
              description: >-
                Filter results to only include conversations updated after the
                specified date and time, in ISO_8601 format.
              examples:
                - '2022-01-01T00:00:00Z'
              format: date-time
              example: '2022-01-01T00:00:00Z'
        updatedBefore:
          schema:
            - type: string
              required: false
              description: >-
                Filter results to only include conversations updated before the
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
                        assignedTo:
                          anyOf:
                            - type: string
                            - type: 'null'
                        createdAt:
                          anyOf:
                            - format: date-time
                              type: string
                            - type: 'null'
                        deletedAt:
                          anyOf:
                            - format: date-time
                              type: string
                            - type: 'null'
                        id:
                          pattern: ^CN(.*)$
                          type: string
                        lastActivityAt:
                          anyOf:
                            - format: date-time
                              type: string
                            - type: 'null'
                        lastActivityId:
                          anyOf:
                            - pattern: ^AC(.*)$
                              type: string
                            - type: 'null'
                        mutedUntil:
                          anyOf:
                            - format: date-time
                              type: string
                            - type: 'null'
                        name:
                          anyOf:
                            - type: string
                            - type: 'null'
                        participants:
                          type: array
                          items:
                            description: >-
                              A phone number in E.164 format, including the
                              country code.
                            examples:
                              - '+15555555555'
                            pattern: ^\+[1-9]\d{1,14}$
                            type: string
                        phoneNumberId:
                          pattern: ^PN(.*)$
                          type: string
                        snoozedUntil:
                          anyOf:
                            - format: date-time
                              type: string
                            - type: 'null'
                        updatedAt:
                          anyOf:
                            - format: date-time
                              type: string
                            - type: 'null'
                      required:
                        - assignedTo
                        - createdAt
                        - deletedAt
                        - id
                        - lastActivityAt
                        - lastActivityId
                        - mutedUntil
                        - name
                        - participants
                        - phoneNumberId
                        - snoozedUntil
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
                - assignedTo: <string>
                  createdAt: '2023-11-07T05:31:56Z'
                  deletedAt: '2023-11-07T05:31:56Z'
                  id: <string>
                  lastActivityAt: '2023-11-07T05:31:56Z'
                  lastActivityId: <string>
                  mutedUntil: '2023-11-07T05:31:56Z'
                  name: <string>
                  participants:
                    - '+15555555555'
                  phoneNumberId: <string>
                  snoozedUntil: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
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
                  - const: '1000400'
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
                  - const: Bad Request
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
        description: Bad Request
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
                  - const: '1000401'
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
                  - const: '1001403'
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
                  - const: '1000404'
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
                  - const: '1001500'
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