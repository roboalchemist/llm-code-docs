# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/concurrency-limits-v2/read-concurrency-limit-v2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Concurrency Limit V2



## OpenAPI

````yaml get /v2/concurrency_limits/{id_or_name}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /v2/concurrency_limits/{id_or_name}:
    get:
      tags:
        - Concurrency Limits V2
      summary: Read Concurrency Limit V2
      operationId: read_concurrency_limit_v2_v2_concurrency_limits__id_or_name__get
      parameters:
        - name: id_or_name
          in: path
          required: true
          schema:
            anyOf:
              - type: string
                format: uuid
              - type: string
            description: The ID or name of the concurrency limit
            title: Id Or Name
          description: The ID or name of the concurrency limit
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GlobalConcurrencyLimitResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    GlobalConcurrencyLimitResponse:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        created:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Created
        updated:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Updated
        active:
          type: boolean
          title: Active
          description: Whether the global concurrency limit is active.
          default: true
        name:
          type: string
          title: Name
          description: The name of the global concurrency limit.
        limit:
          type: integer
          title: Limit
          description: The concurrency limit.
        active_slots:
          type: integer
          title: Active Slots
          description: The number of active slots.
        slot_decay_per_second:
          type: number
          title: Slot Decay Per Second
          description: The decay rate for active slots when used as a rate limit.
          default: 2
      type: object
      required:
        - name
        - limit
        - active_slots
        - id
        - created
        - updated
      title: GlobalConcurrencyLimitResponse
      description: A response object for global concurrency limits.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````

Built with [Mintlify](https://mintlify.com).