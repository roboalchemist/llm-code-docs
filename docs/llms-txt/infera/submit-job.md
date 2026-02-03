# Source: https://docs.infera.org/api-reference/endpoint/submit-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Submit Job



## OpenAPI

````yaml post /submit_job
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.infera.org/
    description: Infera production servers
security: []
paths:
  /submit_job:
    post:
      summary: Submit Job
      operationId: submit_job_submit_job_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/JobRequest'
        required: true
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
    JobRequest:
      properties:
        model:
          type: string
          title: Model
        messages:
          items:
            $ref: '#/components/schemas/InputMessage'
          type: array
          title: Messages
        max_output:
          type: integer
          title: Max Output
        temperature:
          type: number
          title: Temperature
      type: object
      required:
        - model
        - messages
        - max_output
        - temperature
      title: JobRequest
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    InputMessage:
      properties:
        role:
          type: string
          title: Role
        content:
          type: string
          title: Content
      type: object
      required:
        - role
        - content
      title: InputMessage
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