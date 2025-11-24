# Source: https://docs.galileo.ai/api-reference/protect-notification.md

# Protect notification

> When a Protect execution completes with the status specified in the configuration, the webhook specified is
triggered with this payload.

## OpenAPI

````yaml https://api.acme.rungalileo.io/public/v1/openapi.json webhook protect-notification
paths:
  path: protect-notification
  method: post
  servers:
    - url: https://api.acme.rungalileo.io
      description: Galileo Public APIs - acme
  request:
    security: []
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
              status:
                allOf:
                  - $ref: '#/components/schemas/ExecutionStatus'
                    description: Status of the request after processing the rules.
                    default: not_triggered
              text:
                allOf:
                  - type: string
                    title: Text
                    description: Text from the request after processing the rules.
              trace_metadata:
                allOf:
                  - $ref: '#/components/schemas/TraceMetadata'
            required: true
            title: Response
            refIdentifier: '#/components/schemas/Response'
            requiredProperties:
              - text
              - trace_metadata
        examples:
          example:
            value:
              status: not_triggered
              text: <string>
              trace_metadata:
                id: <string>
                received_at: 123
                response_at: 123
                execution_time: -1
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
  type: webhook
components:
  schemas:
    ExecutionStatus:
      type: string
      enum:
        - triggered
        - failed
        - error
        - timeout
        - paused
        - not_triggered
        - skipped
      title: ExecutionStatus
      description: Status of the execution.
    TraceMetadata:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: Unique identifier for the request.
        received_at:
          type: integer
          title: Received At
          description: Time the request was received by the server in nanoseconds.
        response_at:
          type: integer
          title: Response At
          description: Time the response was sent by the server in nanoseconds.
        execution_time:
          type: number
          title: Execution Time
          description: Execution time for the request (in seconds).
          default: -1
      type: object
      title: TraceMetadata
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