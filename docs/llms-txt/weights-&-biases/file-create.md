# Source: https://docs.wandb.ai/weave/reference/service-api/files/file-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# File Create



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /file/create
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /file/create:
    post:
      tags:
        - Files
      summary: File Create
      operationId: file_create_file_create_post
      requestBody:
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Body_file_create_file_create_post'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileCreateRes'
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
    Body_file_create_file_create_post:
      properties:
        project_id:
          type: string
          title: Project Id
        file:
          type: string
          format: binary
          title: File
      type: object
      required:
        - project_id
        - file
      title: Body_file_create_file_create_post
    FileCreateRes:
      properties:
        digest:
          type: string
          title: Digest
      type: object
      required:
        - digest
      title: FileCreateRes
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