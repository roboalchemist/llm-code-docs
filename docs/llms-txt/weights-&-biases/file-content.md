# Source: https://docs.wandb.ai/weave/reference/service-api/files/file-content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# File Content



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /file/content
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /file/content:
    post:
      tags:
        - Files
      summary: File Content
      operationId: file_content_file_content_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FileContentReadReq'
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
        - HTTPBasic: []
components:
  schemas:
    FileContentReadReq:
      properties:
        project_id:
          type: string
          title: Project Id
        digest:
          type: string
          title: Digest
      additionalProperties: false
      type: object
      required:
        - project_id
        - digest
      title: FileContentReadReq
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
    HTTPBasic:
      type: http
      scheme: basic

````