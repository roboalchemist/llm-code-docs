# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/concurrency-limits/decrement-concurrency-limits-v1.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Decrement Concurrency Limits V1

> Decrement concurrency limits for the given tags.

Finds and revokes the lease for V2 limits or decrements V1 active slots.
Returns the list of limits that were decremented.



## OpenAPI

````yaml post /concurrency_limits/decrement
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /concurrency_limits/decrement:
    post:
      tags:
        - Concurrency Limits
      summary: Decrement Concurrency Limits V1
      description: |-
        Decrement concurrency limits for the given tags.

        Finds and revokes the lease for V2 limits or decrements V1 active slots.
        Returns the list of limits that were decremented.
      operationId: decrement_concurrency_limits_v1_concurrency_limits_decrement_post
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
                #/components/schemas/Body_decrement_concurrency_limits_v1_concurrency_limits_decrement_post
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
                  Response Decrement Concurrency Limits V1 Concurrency Limits
                  Decrement Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_decrement_concurrency_limits_v1_concurrency_limits_decrement_post:
      properties:
        names:
          items:
            type: string
          type: array
          title: Names
          description: The tags to release a slot for
        task_run_id:
          type: string
          format: uuid
          title: Task Run Id
          description: The ID of the task run releasing the slot
      type: object
      required:
        - names
        - task_run_id
      title: Body_decrement_concurrency_limits_v1_concurrency_limits_decrement_post
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