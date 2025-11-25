# Source: https://www.quo.com/docs/mdx/api-reference/calls/get-recordings-for-a-call.md

# Get recordings for a call

> Retrieve a list of recordings associated with a specific call. The results are sorted chronologically, with the oldest recording segment appearing first in the list.

## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json get /v1/call-recordings/{callId}
paths:
  path: /v1/call-recordings/{callId}
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
        callId:
          schema:
            - type: string
              required: true
              description: >-
                The unique identifier of the call for which recordings are being
                retrieved.
              examples:
                - AC3700e624eca547eb9f749a06f
              example: AC3700e624eca547eb9f749a06f
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
                  - type: array
                    items:
                      additionalProperties: false
                      type: object
                      properties:
                        duration:
                          anyOf:
                            - description: >-
                                The length of the call recording in seconds.
                                Null if the recording is not completed or the
                                duration is unknown.
                              examples:
                                - 60
                              type: integer
                            - type: 'null'
                        id:
                          description: The unique identifier of the call recording.
                          examples:
                            - CRwRVK2qBq
                          type: string
                        startTime:
                          anyOf:
                            - description: >-
                                The timestamp when the recording began, in ISO
                                8601 format. Null if the recording hasn't
                                started or the start time is unknown.
                              examples:
                                - '2022-01-01T00:00:00Z'
                              format: date-time
                              type: string
                            - type: 'null'
                        status:
                          anyOf:
                            - type: string
                              enum:
                                - absent
                                - completed
                                - deleted
                                - failed
                                - in-progress
                                - paused
                                - processing
                                - stopped
                                - stopping
                              description: The current status of the call recording.
                              examples:
                                - completed
                            - type: 'null'
                        type:
                          anyOf:
                            - description: >-
                                The file type of the call recording. Null if the
                                type is not specified or is unknown.
                              examples:
                                - audio/mpeg
                              type: string
                            - type: 'null'
                        url:
                          anyOf:
                            - description: >-
                                The URL where the call recording can be accessed
                                or downloaded. Null if the URL is not available
                                or the recording is not accessible.
                              examples:
                                - >-
                                  https://examplestorage.com/a643d4d3e1484fcc8b721627284eda5e.mp3
                              format: uri-reference
                              type: string
                            - type: 'null'
                      required:
                        - duration
                        - id
                        - startTime
                        - status
                        - type
                        - url
            requiredProperties:
              - data
        examples:
          example:
            value:
              data:
                - duration: 60
                  id: CRwRVK2qBq
                  startTime: '2022-01-01T00:00:00Z'
                  status: completed
                  type: audio/mpeg
                  url: >-
                    https://examplestorage.com/a643d4d3e1484fcc8b721627284eda5e.mp3
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
                  - const: '0900400'
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
                  - const: '0900401'
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
                  - const: '0900403'
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
                  - const: '0900404'
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
                  - const: '0901500'
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