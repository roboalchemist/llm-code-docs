# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/concurrency-limits-v2/update-concurrency-limit-v2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Concurrency Limit V2



## OpenAPI

````yaml patch /v2/concurrency_limits/{id_or_name}
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
    patch:
      tags:
        - Concurrency Limits V2
      summary: Update Concurrency Limit V2
      operationId: update_concurrency_limit_v2_v2_concurrency_limits__id_or_name__patch
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ConcurrencyLimitV2Update'
      responses:
        '204':
          description: Successful Response
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    ConcurrencyLimitV2Update:
      properties:
        active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Active
        name:
          anyOf:
            - type: string
              pattern: ^[^/%&><]+$
            - type: 'null'
          title: Name
        limit:
          anyOf:
            - type: integer
              minimum: 0
            - type: 'null'
          title: Limit
        active_slots:
          anyOf:
            - type: integer
              minimum: 0
            - type: 'null'
          title: Active Slots
        denied_slots:
          anyOf:
            - type: integer
              minimum: 0
            - type: 'null'
          title: Denied Slots
        slot_decay_per_second:
          anyOf:
            - type: number
              minimum: 0
            - type: 'null'
          title: Slot Decay Per Second
      additionalProperties: false
      type: object
      title: ConcurrencyLimitV2Update
      description: Data used by the Prefect REST API to update a v2 concurrency limit.
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