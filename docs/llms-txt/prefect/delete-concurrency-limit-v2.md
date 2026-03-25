# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/concurrency-limits-v2/delete-concurrency-limit-v2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Concurrency Limit V2



## OpenAPI

````yaml delete /v2/concurrency_limits/{id_or_name}
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
    delete:
      tags:
        - Concurrency Limits V2
      summary: Delete Concurrency Limit V2
      operationId: delete_concurrency_limit_v2_v2_concurrency_limits__id_or_name__delete
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