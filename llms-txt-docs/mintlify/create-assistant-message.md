# Source: https://mintlify.com/docs/api/assistant/create-assistant-message.md

# Assistant message

> Generates a response message from the assistant for the specified domain.

## OpenAPI

````yaml POST /assistant/{domain}/message
paths:
  path: /assistant/{domain}/message
  method: post
  servers:
    - url: https://api-dsc.mintlify.com/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                The Authorization header expects a Bearer token. See the
                [Assistant API Key
                documentation](/docs/api-reference/introduction#assistant-api-key)
                for details on how to get your API key.
          cookie: {}
    parameters:
      path:
        domain:
          schema:
            - type: string
              required: true
              description: >-
                The domain identifier from your `domain.mintlify.app` URL. Can
                be found at the end of your dashboard URL. For example,
                `dashboard.mintlify.com/organization/domain` has a domain
                identifier of `domain`.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              fp:
                allOf:
                  - type: string
                    description: >-
                      Browser fingerprint or arbitrary string identifier. There
                      may be future functionality which allows you to get the
                      messages for a given fingerprint
              threadId:
                allOf:
                  - default: null
                    type: string
                    description: >-
                      An optional identifier used to maintain conversation
                      continuity across multiple messages. When provided, it
                      allows the system to associate follow-up messages with the
                      same conversation thread. The threadId is returned in the
                      response as event.threadId when event.type === 'finish'.
              messages:
                allOf:
                  - type: array
                    default:
                      - id: foobar
                        role: user
                        content: how do i get started
                        parts:
                          - type: text
                            text: How do I get started
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: Unique identifier for the message
                        role:
                          type: string
                          enum:
                            - system
                            - assistant
                            - data
                            - user
                          description: The role of the message sender
                        createdAt:
                          type: string
                          format: date-time
                          description: Timestamp when the message was created
                        content:
                          type: string
                          description: The content of the message
                        annotations:
                          type: array
                          items: {}
                          description: Optional array of annotations for the message
                        parts:
                          type: array
                          items:
                            oneOf:
                              - type: object
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - text
                                  text:
                                    type: string
                                required:
                                  - type
                                  - text
                              - type: object
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - reasoning
                                  reasoning:
                                    type: string
                                  details:
                                    type: array
                                    items:
                                      oneOf:
                                        - type: object
                                          properties:
                                            type:
                                              type: string
                                              enum:
                                                - text
                                            text:
                                              type: string
                                            signature:
                                              type: string
                                          required:
                                            - type
                                            - text
                                        - type: object
                                          properties:
                                            type:
                                              type: string
                                              enum:
                                                - redacted
                                            data:
                                              type: string
                                          required:
                                            - type
                                            - data
                                required:
                                  - type
                                  - reasoning
                                  - details
                              - type: object
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - step-start
                                required:
                                  - type
                              - type: object
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - source
                                  source:
                                    type: object
                                    properties:
                                      sourceType:
                                        type: string
                                        enum:
                                          - url
                                      id:
                                        type: string
                                      url:
                                        type: string
                                      title:
                                        type: string
                                    required:
                                      - sourceType
                                      - id
                                      - url
                                required:
                                  - type
                                  - source
                              - type: object
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - tool-invocation
                                  toolInvocation:
                                    oneOf:
                                      - type: object
                                        properties:
                                          state:
                                            type: string
                                            enum:
                                              - partial-call
                                          step:
                                            type: number
                                          toolCallId:
                                            type: string
                                          toolName:
                                            type: string
                                          args: {}
                                        required:
                                          - state
                                          - toolCallId
                                          - toolName
                                          - args
                                      - type: object
                                        properties:
                                          state:
                                            type: string
                                            enum:
                                              - call
                                          step:
                                            type: number
                                          toolCallId:
                                            type: string
                                          toolName:
                                            type: string
                                          args: {}
                                        required:
                                          - state
                                          - toolCallId
                                          - toolName
                                          - args
                                      - type: object
                                        properties:
                                          state:
                                            type: string
                                            enum:
                                              - result
                                          step:
                                            type: number
                                          toolCallId:
                                            type: string
                                          toolName:
                                            type: string
                                          args: {}
                                          result: {}
                                        required:
                                          - state
                                          - toolCallId
                                          - toolName
                                          - args
                                          - result
                                required:
                                  - type
                                  - toolInvocation
                          description: >-
                            Array of message parts with different types
                            including text, reasoning, sources, and tool
                            invocations
                        experimental_attachments:
                          type: array
                          items:
                            type: object
                            properties:
                              name:
                                type: string
                              contentType:
                                type: string
                              url:
                                type: string
                            required:
                              - url
                          description: >-
                            Optional array of experimental attachments for the
                            message
                      required:
                        - id
                        - role
                        - content
                        - parts
                    description: >-
                      Array of messages in the conversation. On the frontend,
                      you will likely want to use the handleSubmit function from
                      the @ai-sdk package's useChat hook to append user messages
                      and handle streaming responses, rather than manually
                      defining the objects in this array as they have so many
                      parameters.
              retrievalPageSize:
                allOf:
                  - type: number
                    default: 5
                    description: Number of retrieval results to return
              filter:
                allOf:
                  - type: object
                    default: null
                    properties:
                      version:
                        type: string
                        description: Optional version filter
                      language:
                        type: string
                        description: Optional language filter
                    description: Optional filter criteria for the search
            required: true
            requiredProperties:
              - fp
              - messages
        examples:
          example:
            value:
              fp: <string>
              threadId: null
              messages:
                - id: foobar
                  role: user
                  content: how do i get started
                  parts:
                    - type: text
                      text: How do I get started
              retrievalPageSize: 5
              filter: null
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            description: >-
              Response object that streams formatted data stream parts with the
              specified status, headers, and content. This matches what is
              expected from the AI SDK as documented at
              [ai-sdk.dev/docs/ai-sdk-ui/streaming-data](https://ai-sdk.dev/docs/ai-sdk-ui/streaming-data).
              Instead of writing your own parser, it is recommended to use the
              [useChat hook from ai-sdk as documented
              here](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat#usechat).
        examples:
          example:
            value: {}
        description: Message generated successfully
  deprecated: false
  type: path
  xMcp:
    enabled: true
components:
  schemas: {}

````