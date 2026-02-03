# Source: https://docs.infera.org/api-reference/endpoint/update-result.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Result



## OpenAPI

````yaml post /worker/update_result
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.infera.org/
    description: Infera production servers
security: []
paths:
  /worker/update_result:
    post:
      summary: Update Result
      operationId: update_result_worker_update_result_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/JobResult'
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
components:
  schemas:
    JobResult:
      properties:
        job_id:
          type: string
          title: Job Id
        api_key:
          type: string
          title: Api Key
        model_name:
          type: string
          title: Model Name
        result:
          type: object
          title: Result
        status:
          type: string
          title: Status
      type: object
      required:
        - job_id
        - api_key
        - model_name
        - result
        - status
      title: JobResult
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

````