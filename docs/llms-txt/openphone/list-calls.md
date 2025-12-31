# Source: https://www.quo.com/docs/mdx/api-reference/calls/list-calls.md

# List calls

> Fetch a paginated list of calls associated with a specific OpenPhone number and another number.

## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json get /v1/calls
paths:
  path: /v1/calls
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
                The unique identifier of the OpenPhone number associated with
                the call.
              examples:
                - PN123abc
              example: PN123abc
        userId:
          schema:
            - type: string
              required: false
              description: >-
                The unique identifier of the OpenPhone user who either placed or
                received the call. Defaults to the workspace owner.
              examples:
                - US123abc
              example: US123abc
        participants:
          schema:
            - type: array
              items:
                allOf:
                  - minLength: 1
                    type: string
              required: true
              description: >-
                The phone numbers of participants involved in the call
                conversation, excluding your OpenPhone number. Each number
                should contain the country code and conform to the E.164 format.
                Currently limited to one-to-one (1:1) conversations only.
              examples:
                - '+15555555555'
              maxItems: 1
              example: '+15555555555'
        since:
          schema:
            - type: string
              required: false
              description: >-
                DEPRECATED, use "createdAfter" or "createdBefore" instead.
                "since" incorrectly behaves as "createdBefore" and will be
                removed in an upcoming release.
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
                Filter results to only include calls created after the specified
                date and time, in ISO 8601 format.
              examples:
                - '2022-01-01T00:00:00Z'
              format: date-time
              example: '2022-01-01T00:00:00Z'
        createdBefore:
          schema:
            - type: string
              required: false
              description: >-
                Filter results to only include calls created before the
                specified date and time, in ISO 8601 format.
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
                            The timestamp when the call record was created, in
                            ISO 8601 format.
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
                                    A phone number in E.164 format, including
                                    the country code.
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
                                    A phone number in E.164 format, including
                                    the country code.
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
                - answeredAt: '2022-01-01T00:00:00Z'
                  answeredBy: USlHhXmRMz
                  initiatedBy: USlHhXmRMz
                  direction: incoming
                  status: completed
                  completedAt: '2022-01-01T00:00:00Z'
                  createdAt: '2022-01-01T00:00:00Z'
                  callRoute: phone-number
                  duration: 60
                  forwardedFrom: '+15555555555'
                  forwardedTo: '+15555555555'
                  aiHandled: ai-agent
                  id: AC123abc
                  phoneNumberId: PN123abc
                  participants:
                    - '+15555555555'
                  updatedAt: '2022-01-01T00:00:00Z'
                  userId: US123abc
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
                  - const: '0101400'
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
                  - const: Too Many Participants
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
                  - const: Too Many Participants
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
        description: Too Many Participants
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
                  - const: '0100401'
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
                  - const: '0101403'
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
                  - const: '0100404'
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
                  - const: '0101500'
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