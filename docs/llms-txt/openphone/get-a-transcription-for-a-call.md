# Source: https://www.quo.com/docs/mdx/api-reference/calls/get-a-transcription-for-a-call.md

# Get a transcription for a call

> Retrieve a detailed transcript of a specific call identified by its unique call ID. This endpoint supports transcripts for both regular calls and calls handled by Sona. Call transcripts are only available on business and scale plans.

## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json get /v1/call-transcripts/{id}
paths:
  path: /v1/call-transcripts/{id}
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: Unique identifier of the call associated with this transcript.
              examples:
                - AC3700e624eca547eb9f749a06f2eb1
              example: AC3700e624eca547eb9f749a06f2eb1
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
              data:
                allOf:
                  - type: object
                    properties:
                      callId:
                        description: >-
                          The unique identifier of the call to which this
                          transcript belongs.
                        examples:
                          - ACea724hac8c30465bcbcff0b76e4c1c7b
                        type: string
                      createdAt:
                        description: >-
                          The timestamp when the transcription was created, in
                          ISO 8601 format.
                        examples:
                          - '2022-01-01T00:00:00Z'
                        format: date-time
                        type: string
                      dialogue:
                        anyOf:
                          - type: array
                            items:
                              type: object
                              properties:
                                content:
                                  description: >-
                                    The transcribed text of a specific dialogue
                                    segment.
                                  examples:
                                    - Hello, world!
                                  type: string
                                start:
                                  description: >-
                                    The start time of the dialogue segment in
                                    seconds, relative to the beginning of the
                                    call.
                                  examples:
                                    - 5.123456
                                  type: number
                                end:
                                  description: >-
                                    The end time of the dialogue segment in
                                    seconds, relative to the beginning of the
                                    call.
                                  examples:
                                    - 10.123456
                                  type: number
                                identifier:
                                  anyOf:
                                    - description: >-
                                        The phone number of the participant who
                                        spoke during this dialogue segment.
                                      examples:
                                        - '+19876543210'
                                      type: string
                                    - type: 'null'
                                userId:
                                  anyOf:
                                    - description: >-
                                        The unique identifier of the OpenPhone
                                        user who spoke during this dialogue
                                        segment. Null for external participants
                                        or if user identification is not
                                        available.
                                      examples:
                                        - US123abc
                                      pattern: ^US(.*)$
                                      type: string
                                    - type: 'null'
                              required:
                                - content
                                - start
                                - end
                                - identifier
                                - userId
                          - type: 'null'
                      duration:
                        description: The total duration of the transcribed call in seconds.
                        examples:
                          - 100
                        type: number
                      status:
                        type: string
                        enum:
                          - absent
                          - in-progress
                          - completed
                          - failed
                        description: The status of the call transcription.
                        examples:
                          - completed
                    required:
                      - callId
                      - createdAt
                      - dialogue
                      - duration
                      - status
            requiredProperties:
              - data
        examples:
          example:
            value:
              data:
                callId: ACea724hac8c30465bcbcff0b76e4c1c7b
                createdAt: '2022-01-01T00:00:00Z'
                dialogue:
                  - content: Hello, world!
                    start: 5.123456
                    end: 10.123456
                    identifier: '+19876543210'
                    userId: US123abc
                duration: 100
                status: completed
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
                  - const: '0600400'
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
                  - const: '0600401'
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
                  - const: '0600403'
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
                  - const: Forbidden
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
        description: Forbidden
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
                  - const: '0600404'
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
                  - const: '0601500'
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