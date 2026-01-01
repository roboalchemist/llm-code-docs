# Source: https://docs.together.ai/reference/upload-file.md

# Upload a file

> Upload a file with specified purpose, file name, and file type.



## OpenAPI

````yaml POST /files/upload
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
  /files/upload:
    post:
      tags:
        - Files
      summary: Upload a file
      description: Upload a file with specified purpose, file name, and file type.
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              required:
                - purpose
                - file_name
                - file
              properties:
                purpose:
                  $ref: '#/components/schemas/FilePurpose'
                file_name:
                  type: string
                  description: The name of the file being uploaded
                  example: dataset.csv
                file_type:
                  $ref: '#/components/schemas/FileType'
                file:
                  type: string
                  format: binary
                  description: The content of the file being uploaded
      responses:
        '200':
          description: File uploaded successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
components:
  schemas:
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
    ErrorData:
      type: object
      required:
        - error
      properties:
        error:
          type: object
          properties:
            message:
              type: string
              nullable: false
            type:
              type: string
              nullable: false
            param:
              type: string
              nullable: true
              default: null
            code:
              type: string
              nullable: true
              default: null
          required:
            - type
            - message
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt