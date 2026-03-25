# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/concurrency-limits-v2/bulk-increment-active-slots.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Increment Active Slots



## OpenAPI

````yaml post /v2/concurrency_limits/increment
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /v2/concurrency_limits/increment:
    post:
      tags:
        - Concurrency Limits V2
      summary: Bulk Increment Active Slots
      operationId: bulk_increment_active_slots_v2_concurrency_limits_increment_post
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
              $ref: >-
                #/components/schemas/Body_bulk_increment_active_slots_v2_concurrency_limits_increment_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/MinimalConcurrencyLimitResponse'
                title: >-
                  Response Bulk Increment Active Slots V2 Concurrency Limits
                  Increment Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_bulk_increment_active_slots_v2_concurrency_limits_increment_post:
      properties:
        slots:
          type: integer
          exclusiveMinimum: 0
          title: Slots
        names:
          items:
            type: string
          type: array
          title: Names
          min_items: 1
        mode:
          type: string
          enum:
            - concurrency
            - rate_limit
          title: Mode
          default: concurrency
        create_if_missing:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Create If Missing
          deprecated: true
      type: object
      required:
        - slots
        - names
      title: Body_bulk_increment_active_slots_v2_concurrency_limits_increment_post
    MinimalConcurrencyLimitResponse:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        name:
          type: string
          title: Name
        limit:
          type: integer
          title: Limit
      type: object
      required:
        - id
        - name
        - limit
      title: MinimalConcurrencyLimitResponse
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