# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/concurrency-limits/increment-concurrency-limits-v1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Increment Concurrency Limits V1

> Increment concurrency limits for the given tags.

During migration, this handles both V1 and V2 limits to support mixed states.
Post-migration, it only uses V2 with lease-based concurrency.



## OpenAPI

````yaml post /concurrency_limits/increment
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /concurrency_limits/increment:
    post:
      tags:
        - Concurrency Limits
      summary: Increment Concurrency Limits V1
      description: >-
        Increment concurrency limits for the given tags.


        During migration, this handles both V1 and V2 limits to support mixed
        states.

        Post-migration, it only uses V2 with lease-based concurrency.
      operationId: increment_concurrency_limits_v1_concurrency_limits_increment_post
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
                #/components/schemas/Body_increment_concurrency_limits_v1_concurrency_limits_increment_post
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
                  Response Increment Concurrency Limits V1 Concurrency Limits
                  Increment Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_increment_concurrency_limits_v1_concurrency_limits_increment_post:
      properties:
        names:
          items:
            type: string
          type: array
          title: Names
          description: The tags to acquire a slot for
        task_run_id:
          type: string
          format: uuid
          title: Task Run Id
          description: The ID of the task run acquiring the slot
      type: object
      required:
        - names
        - task_run_id
      title: Body_increment_concurrency_limits_v1_concurrency_limits_increment_post
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