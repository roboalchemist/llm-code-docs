# Source: https://www.quo.com/docs/mdx/api-reference/calls/get-a-transcription-for-a-call.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.quo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a transcription for a call

> Retrieve a detailed transcript of a specific call identified by its unique call ID. This endpoint supports transcripts for both regular calls and calls handled by Sona. Call transcripts are only available on business and scale plans.



## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json get /v1/call-transcripts/{id}
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
  /v1/call-transcripts/{id}:
    get:
      tags:
        - Calls
      summary: Get a transcription for a call
      description: >-
        Retrieve a detailed transcript of a specific call identified by its
        unique call ID. This endpoint supports transcripts for both regular
        calls and calls handled by Sona. Call transcripts are only available on
        business and scale plans.
      operationId: getCallTranscript_v1
      parameters:
        - in: path
          name: id
          required: true
          schema:
            description: Unique identifier of the call associated with this transcript.
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
                    type: object
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
                    const: '0600400'
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
                    const: '0600401'
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
                    const: '0600403'
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
                    const: '0600404'
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
                    const: '0601500'
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