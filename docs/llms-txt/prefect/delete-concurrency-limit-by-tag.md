# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/concurrency-limits/delete-concurrency-limit-by-tag.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Concurrency Limit By Tag



## OpenAPI

````yaml delete /concurrency_limits/tag/{tag}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /concurrency_limits/tag/{tag}:
    delete:
      tags:
        - Concurrency Limits
      summary: Delete Concurrency Limit By Tag
      operationId: delete_concurrency_limit_by_tag_concurrency_limits_tag__tag__delete
      parameters:
        - name: tag
          in: path
          required: true
          schema:
            type: string
            description: The tag name
            title: Tag
          description: The tag name
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
              schema: {}
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