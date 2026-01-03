# Source: https://docs.together.ai/reference/get-files-id.md

# List File

> List the metadata for a single uploaded data file.



## OpenAPI

````yaml GET /files/{id}
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /files/{id}:
    get:
      tags:
        - Files
      summary: List file
      description: List the metadata for a single uploaded data file.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: File retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileResponse'
components:
  schemas:
    FileResponse:
      type: object
      required:
        - id
        - object
        - created_at
        - filename
        - bytes
        - purpose
        - FileType
        - Processed
        - LineCount
      properties:
        id:
          type: string
        object:
          type: string
          example: file
        created_at:
          type: integer
          example: 1715021438
        filename:
          type: string
          example: my_file.jsonl
        bytes:
          type: integer
          example: 2664
        purpose:
          $ref: '#/components/schemas/FilePurpose'
        Processed:
          type: boolean
        FileType:
          $ref: '#/components/schemas/FileType'
        LineCount:
          type: integer
    FilePurpose:
      type: string
      description: The purpose of the file
      example: fine-tune
      enum:
        - fine-tune
        - eval
        - eval-sample
        - eval-output
        - eval-summary
        - batch-generated
        - batch-api
    FileType:
      type: string
      description: The type of the file
      default: jsonl
      example: jsonl
      enum:
        - csv
        - jsonl
        - parquet
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt