# Source: https://docs.infera.org/api-reference/endpoint/chat-completions.md

# Chat Completions

## OpenAPI

````yaml post /chat/completions
paths:
  path: /chat/completions
  method: post
  servers:
    - url: https://api.infera.org/
      description: Infera production servers
  request:
    security:
      - title: APIKeyHeader
        parameters:
          query: {}
          header:
            api_key:
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
              model:
                allOf:
                  - type: string
                    title: Model
              messages:
                allOf:
                  - items:
                      $ref: '#/components/schemas/InputMessage'
                    type: array
                    title: Messages
              max_tokens:
                allOf:
                  - type: integer
                    title: Max Tokens
              temperature:
                allOf:
                  - type: number
                    title: Temperature
              request_timeout_time:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Request Timeout Time
                    default: 240
            required: true
            title: ChatCompletionsRequest
            refIdentifier: '#/components/schemas/ChatCompletionsRequest'
            requiredProperties:
              - model
              - messages
              - max_tokens
              - temperature
        examples:
          example:
            value:
              model: <string>
              messages:
                - role: <string>
                  content: <string>
              max_tokens: 123
              temperature: 123
              request_timeout_time: 123
  response:
    '200':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
    InputMessage:
      properties:
        role:
          type: string
          title: Role
        content:
          type: string
          title: Content
      type: object
      required:
        - role
        - content
      title: InputMessage
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````