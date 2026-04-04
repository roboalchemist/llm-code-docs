# Source: https://docs.asapp.com/apis/autotranscribe-media-gateway/stop-streaming.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Stop streaming

> This stops the transcription of the audio stream.

Use in conjunction with the [start-streaming](/apis/media-gateway/start-streaming-audio) endpoint to control when transcription occurs for a given call. This allow you to prevent transcription of sensitive parts of a conversation, such as entering PCI data.




## OpenAPI

````yaml api-specs/mg-autotranscribe.yaml post /mg-autotranscribe/v1/stop-streaming
openapi: 3.0.0
info:
  title: MG Autotranscribe API Router
  description: Router service for controlling MG transcription
  version: '1'
servers:
  - url: https://api.sandbox.asapp.com
security:
  - API-ID: []
    API-Secret: []
tags:
  - name: AutoTranscribe Media Gateway
    description: >-
      Operations for controlling AutoTranscribe Media Gateway transcription and
      streaming
paths:
  /mg-autotranscribe/v1/stop-streaming:
    post:
      tags:
        - AutoTranscribe Media Gateway
      summary: Stop streaming
      description: >
        This stops the transcription of the audio stream.


        Use in conjunction with the
        [start-streaming](/apis/media-gateway/start-streaming-audio) endpoint to
        control when transcription occurs for a given call. This allow you to
        prevent transcription of sensitive parts of a conversation, such as
        entering PCI data.
      operationId: stopStreaming
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                namespace:
                  description: The media gateway platform or protocol you are using.
                  type: string
                  enum:
                    - siprec
                    - twilio
                    - amazonconnect
                    - genesysaudiohook
                guid:
                  description: >-
                    The globally unique Id for the call, also sometimes called
                    Unique Call Id (UCID). Must be in decimal form.
                  type: string
              example:
                namespace: siprec
                guid: 0867617078-0032318833-2221801472-0002236962
      responses:
        '200':
          description: Router processed the request, details are in the response body
          content:
            application/json:
              schema:
                type: object
                properties:
                  autotranscribeResponse:
                    type: object
                    properties:
                      customer:
                        type: object
                        properties:
                          streamId:
                            type: string
                            example: 5ce2b755-3f38-11ed-b755-7aed4b5c38d5
                          status:
                            type: object
                            properties:
                              code:
                                type: integer
                                example: 1000
                              description:
                                type: string
                                example: OK
                          summary:
                            type: object
                            properties:
                              totalAudioBytes:
                                type: integer
                              audioDurationMs:
                                type: integer
                              streamingSeconds:
                                type: integer
                              transcripts:
                                type: integer
                            example:
                              totalAudioBytes: 1334720
                              audioDurationMs: 83420
                              streamingSeconds: 84
                              transcripts: 2
                      agent:
                        type: object
                        properties:
                          streamId:
                            type: string
                            example: 5ce2b755-3f38-11ed-b755-7aed4b5c38d5
                          status:
                            type: object
                            properties:
                              code:
                                type: integer
                                example: 1000
                              description:
                                type: string
                                example: OK
                          summary:
                            type: object
                            properties:
                              totalAudioBytes:
                                type: integer
                              audioDurationMs:
                                type: integer
                              streamingSeconds:
                                type: integer
                              transcripts:
                                type: integer
                            example:
                              totalAudioBytes: 1334720
                              audioDurationMs: 83420
                              streamingSeconds: 84
                              transcripts: 2
                  isOk:
                    type: boolean
                  errorMessage:
                    type: string
        '400':
          description: 400 - Bad request
          content:
            application/json:
              schema:
                description: Bad request response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 400-01
                      message: Bad request
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '401':
          description: 401 - Unauthorized
          content:
            application/json:
              schema:
                description: Unauthorized response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 401-01
                      message: Unauthorized
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '403':
          description: 403 - Forbidden
          content:
            application/json:
              schema:
                description: Forbidden response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 403-01
                      message: Forbidden Response
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '404':
          description: 404 - Not Found
          content:
            application/json:
              schema:
                description: Not Found response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 404-01
                      message: Not Found
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '409':
          description: 409 - Conflict
          content:
            application/json:
              schema:
                description: Conflict response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 409-01
                      message: Conflict
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '413':
          description: 413 - Request Entity Too Large
          content:
            application/json:
              schema:
                description: Request Entity Too Large response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 413-01
                      message: Request Entity Too Large
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '422':
          description: 422 - Unprocessable Entity
          content:
            application/json:
              schema:
                description: Unprocessable Entity response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 422-01
                      message: Unprocessable Entity
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '429':
          description: 429 - Too Many Requests
          content:
            application/json:
              schema:
                description: Too Many Requests response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 429-01
                      message: Too Many Requests
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        '503':
          description: 503 - Service Unavailable
          content:
            application/json:
              schema:
                description: Service Unavailable response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 503-01
                      message: Service Unavailable
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        default:
          description: 500 - Internal Server Error
          content:
            application/json:
              schema:
                description: Default error response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 500-01
                      message: Internal server error
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
components:
  securitySchemes:
    API-ID:
      type: apiKey
      in: header
      name: asapp-api-id
    API-Secret:
      type: apiKey
      in: header
      name: asapp-api-secret

````