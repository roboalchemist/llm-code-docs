# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/concurrency-limits-v2/create-concurrency-limit-v2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Concurrency Limit V2

> Create a task run concurrency limit.

For more information, see https://docs.prefect.io/v3/how-to-guides/workflows/global-concurrency-limits.



## OpenAPI

````yaml post /v2/concurrency_limits/
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /v2/concurrency_limits/:
    post:
      tags:
        - Concurrency Limits V2
      summary: Create Concurrency Limit V2
      description: >-
        Create a task run concurrency limit.


        For more information, see
        https://docs.prefect.io/v3/how-to-guides/workflows/global-concurrency-limits.
      operationId: create_concurrency_limit_v2_v2_concurrency_limits__post
      parameters:
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ConcurrencyLimitV2Create'
      responses:
        '201':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConcurrencyLimitV2'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    ConcurrencyLimitV2Create:
      properties:
        active:
          type: boolean
          title: Active
          description: Whether the concurrency limit is active.
          default: true
        name:
          type: string
          pattern: ^[^/%&><]+$
          title: Name
          description: The name of the concurrency limit.
        limit:
          type: integer
          minimum: 0
          title: Limit
          description: The concurrency limit.
        active_slots:
          type: integer
          minimum: 0
          title: Active Slots
          description: The number of active slots.
          default: 0
        denied_slots:
          type: integer
          minimum: 0
          title: Denied Slots
          description: The number of denied slots.
          default: 0
        slot_decay_per_second:
          type: number
          minimum: 0
          title: Slot Decay Per Second
          description: The decay rate for active slots when used as a rate limit.
          default: 0
      additionalProperties: false
      type: object
      required:
        - name
        - limit
      title: ConcurrencyLimitV2Create
      description: Data used by the Prefect REST API to create a v2 concurrency limit.
    ConcurrencyLimitV2:
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
          description: Whether the concurrency limit is active.
          default: true
        name:
          type: string
          pattern: ^[^/%&><]+$
          title: Name
          description: The name of the concurrency limit.
        limit:
          type: integer
          title: Limit
          description: The concurrency limit.
        active_slots:
          type: integer
          title: Active Slots
          description: The number of active slots.
          default: 0
        denied_slots:
          type: integer
          title: Denied Slots
          description: The number of denied slots.
          default: 0
        slot_decay_per_second:
          type: number
          title: Slot Decay Per Second
          description: The decay rate for active slots when used as a rate limit.
          default: 0
        avg_slot_occupancy_seconds:
          type: number
          title: Avg Slot Occupancy Seconds
          description: The average amount of time a slot is occupied.
          default: 2
      type: object
      required:
        - name
        - limit
        - id
        - created
        - updated
      title: ConcurrencyLimitV2
      description: An ORM representation of a v2 concurrency limit.
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