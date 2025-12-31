# Source: https://docs.asapp.com/apis/autotranscribe-media-gateway/start-streaming.md

# Start streaming

> This starts the transcription of the audio stream.

Use in conjunction with the [stop-streaming](/apis/media-gateway/stop-streaming-audio) endpoint to control when transcription occurs for a given call. This allow you to prevent transcription of sensitive parts of a conversation, such as entering PCI data.


## OpenAPI

````yaml api-specs/mg-autotranscribe.yaml post /mg-autotranscribe/v1/start-streaming
paths:
  path: /mg-autotranscribe/v1/start-streaming
  method: post
  servers:
    - url: https://api.sandbox.asapp.com
  request:
    security:
      - title: API ID & API Secret
        parameters:
          query: {}
          header:
            asapp-api-id:
              type: apiKey
            asapp-api-secret:
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
              namespace:
                allOf:
                  - description: The media gateway platform or protocol you are using.
                    type: string
                    enum:
                      - siprec
                      - twilio
                      - amazonconnect
                      - genesysaudiohook
              guid:
                allOf:
                  - description: >-
                      The globally unique Id for the call, also sometimes called
                      Unique Call Id (UCID). Must be in decimal form.
                    type: string
              autotranscribeParams:
                allOf:
                  - type: object
                    properties:
                      language:
                        description: IETF language tag
                        type: string
                        default: en-US
                      detailedToken:
                        description: >
                          Determines whether AutoTranscribe outputs word-level
                          details like word content, timestamp and word type
                        type: boolean
                        default: false
                      audioRecordingAllowed:
                        description: >
                          Determines whether ASAPP may record and store the
                          audio for this conversation for the purposes of model
                          training
                        type: boolean
                        default: false
                      redactionOutput:
                        description: >
                          Determines whether the transcription output is
                          redacted.


                          If detailedToken is true, requests with value
                          "redacted" or "redacted_and_unredacted" will be
                          rejected.


                          If no redaction rules configured by the client for
                          "redacted" or "redacted_and_unredacted", the request
                          will be rejected.
                        type: string
                        default: redacted
                        enum:
                          - redacted
                          - unredacted
                          - redacted_and_unredacted
                    example:
                      language: en-US
                      detailedToken: false
                      audioRecordingAllowed: false
                      redactionOutput: redacted
              siprecParams:
                allOf:
                  - type: object
                    properties:
                      mediaLineOrder:
                        description: >
                          Defines the mapping of media lines (m-lines) in SDP of
                          SIPREC protocol.

                          - `CUSTOMER_FIRST` will map top audio m-line to
                          customer side of conversation (usual for inbound calls
                          to call center, default)

                          - `AGENT_FIRST` will map top audio m-line to agent
                          side of the conversation (usual for outbound calls
                          from call center)
                        type: string
                        default: CUSTOMER_FIRST
                        enum:
                          - CUSTOMER_FIRST
                          - AGENT_FIRST
              twilioParams:
                allOf:
                  - type: object
                    properties:
                      trackMap:
                        type: object
                        properties:
                          inbound:
                            type: string
                            description: The inbound twilio track
                            default: customer
                            enum:
                              - customer
                              - agent
                          outbound:
                            type: string
                            description: The outbound twilio track
                            default: agent
                            enum:
                              - customer
                              - agent
                    example:
                      trackMap:
                        inbound: customer
                        outbound: agent
              amazonConnectParams:
                allOf:
                  - type: object
                    properties:
                      streamArn:
                        type: string
                        description: Amazon stream arn
                      startSelectorType:
                        type: string
                        description: >-
                          Identifies the fragment on the Kinesis video stream
                          where you want to start getting the data from
                        enum:
                          - NOW
                          - FRAGMENT_NUMBER
                      afterFragmentNumber:
                        type: string
                        description: >-
                          Amazon fragment number from where you want to start
                          returning the fragments - mandatory if
                          startSelectorType is FRAGMENT_NUMBER
                    example:
                      streamArn: >-
                        arn:aws:kinesisvideo:us-east-1:000000000000:stream/streamtest-connect-asappconnect-contact-1117e864-690f-4e1e-9dcf-6fbfcc288e41/1654194145007
                      startSelectorType: FRAGMENT_NUMBER
                      afterFragmentNumber: '91343852333181476958523476930058290730435475343'
              customerId:
                allOf:
                  - description: >-
                      Id of the customer on the call. Usually taken from Call
                      Center CTI information.
                    type: string
              agentId:
                allOf:
                  - description: >-
                      The Id of the agent on the call. Usually taken from Call
                      Center CTI information.
                    type: string
            required: true
            requiredProperties:
              - namespace
              - guid
              - customerId
              - agentId
            example:
              namespace: siprec
              guid: 0867617078-0032318833-2221801472-0002236962
              customerId: customerId
              agentId: agentId
              autotranscribeParams:
                language: en-US
              siprecParams:
                mediaLineOrder: CUSTOMER_FIRST
        examples:
          example:
            value:
              namespace: siprec
              guid: 0867617078-0032318833-2221801472-0002236962
              customerId: customerId
              agentId: agentId
              autotranscribeParams:
                language: en-US
              siprecParams:
                mediaLineOrder: CUSTOMER_FIRST
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              autotranscribeResponse:
                allOf:
                  - type: object
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
              isOk:
                allOf:
                  - type: boolean
              errorMessage:
                allOf:
                  - type: string
            example:
              isOk: true
              autotranscribeResponse:
                customer:
                  streamId: 5ce2b755-3f38-11ed-b755-7aed4b5c38d5
                  status:
                    code: 1000
                    description: OK
                agent:
                  streamId: cf31116-3f38-11ed-9116-7a0a36c763f1
                  status:
                    code: 1000
                    description: OK
        examples:
          example:
            value:
              isOk: true
              autotranscribeResponse:
                customer:
                  streamId: 5ce2b755-3f38-11ed-b755-7aed4b5c38d5
                  status:
                    code: 1000
                    description: OK
                agent:
                  streamId: cf31116-3f38-11ed-9116-7a0a36c763f1
                  status:
                    code: 1000
                    description: OK
        description: Router processed the request, details are in the response body
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Bad request response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 400-01
                message: Bad request
        description: 400 - Bad request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Unauthorized response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 401-01
                message: Unauthorized
        description: 401 - Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Forbidden response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 403-01
                message: Forbidden Response
        description: 403 - Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Not Found response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 404-01
                message: Not Found
        description: 404 - Not Found
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Conflict response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 409-01
                message: Conflict
        description: 409 - Conflict
    '413':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Request Entity Too Large response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 413-01
                message: Request Entity Too Large
        description: 413 - Request Entity Too Large
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Unprocessable Entity response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 422-01
                message: Unprocessable Entity
        description: 422 - Unprocessable Entity
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Too Many Requests response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 429-01
                message: Too Many Requests
        description: 429 - Too Many Requests
    '503':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Service Unavailable response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 503-01
                message: Service Unavailable
        description: 503 - Service Unavailable
    default:
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
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
            description: Default error response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 500-01
                message: Internal server error
        description: 500 - Internal Server Error
  deprecated: false
  type: path
components:
  schemas: {}

````