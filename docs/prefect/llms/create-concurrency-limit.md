# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/concurrency-limits/create-concurrency-limit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Concurrency Limit

> Create a task run concurrency limit.

For more information, see https://docs.prefect.io/v3/concepts/tag-based-concurrency-limits.



## OpenAPI

````yaml post /concurrency_limits/
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /concurrency_limits/:
    post:
      tags:
        - Concurrency Limits
      summary: Create Concurrency Limit
      description: >-
        Create a task run concurrency limit.


        For more information, see
        https://docs.prefect.io/v3/concepts/tag-based-concurrency-limits.
      operationId: create_concurrency_limit_concurrency_limits__post
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
              $ref: '#/components/schemas/ConcurrencyLimitCreate'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConcurrencyLimit'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    ConcurrencyLimitCreate:
      properties:
        tag:
          type: string
          title: Tag
          description: A tag the concurrency limit is applied to.
        concurrency_limit:
          type: integer
          title: Concurrency Limit
          description: The concurrency limit.
      additionalProperties: false
      type: object
      required:
        - tag
        - concurrency_limit
      title: ConcurrencyLimitCreate
      description: Data used by the Prefect REST API to create a concurrency limit.
    ConcurrencyLimit:
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
        tag:
          type: string
          title: Tag
          description: A tag the concurrency limit is applied to.
        concurrency_limit:
          type: integer
          title: Concurrency Limit
          description: The concurrency limit.
        active_slots:
          items:
            type: string
            format: uuid
          type: array
          title: Active Slots
          description: A list of active run ids using a concurrency slot
      type: object
      required:
        - tag
        - concurrency_limit
        - id
        - created
        - updated
      title: ConcurrencyLimit
      description: An ORM representation of a concurrency limit.
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