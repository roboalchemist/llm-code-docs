# Source: https://www.quo.com/docs/mdx/api-reference/calls/get-recordings-for-a-call.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.quo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get recordings for a call

> Retrieve a list of recordings associated with a specific call. The results are sorted chronologically, with the oldest recording segment appearing first in the list.



## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json get /v1/call-recordings/{callId}
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
  /v1/call-recordings/{callId}:
    get:
      tags:
        - Calls
      summary: Get recordings for a call
      description: >-
        Retrieve a list of recordings associated with a specific call. The
        results are sorted chronologically, with the oldest recording segment
        appearing first in the list.
      operationId: getCallRecordings_v1
      parameters:
        - in: path
          name: callId
          required: true
          schema:
            description: >-
              The unique identifier of the call for which recordings are being
              retrieved.
            examples:
              - AC3700e624eca547eb9f749a06f
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
                    type: array
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
                required:
                  - data
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0900400'
                    type: string
                  status:
                    const: 400
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Bad Request
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
                    const: '0900401'
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
          description: Forbidden
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0900403'
                    type: string
                  status:
                    const: 403
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Forbidden
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
                    const: '0900404'
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
                    const: '0901500'
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