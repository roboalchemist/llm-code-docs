# Source: https://docs.infera.org/api-reference/endpoint/get-completion-time.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Completion Time



## OpenAPI

````yaml get /get_completion_time/{job_id}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.infera.org/
    description: Infera production servers
security: []
paths:
  /get_completion_time/{job_id}:
    get:
      summary: Get Completion Time
      operationId: get_completion_time_get_completion_time__job_id__get
      parameters:
        - name: job_id
          in: path
          required: true
          schema:
            type: string
            format: uuid4
            title: Job Id
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
      security:
        - APIKeyHeader: []
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
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: api_key

````