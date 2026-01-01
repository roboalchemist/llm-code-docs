# Source: https://docs.together.ai/reference/get-files-id-content.md

# Get File Contents

> Get the contents of a single uploaded data file.



## OpenAPI

````yaml GET /files/{id}/content
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
  /files/{id}/content:
    get:
      tags:
        - Files
      summary: Get file contents
      description: Get the contents of a single uploaded data file.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: File content retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileObject'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
components:
  schemas:
    FileObject:
      type: object
      properties:
        object:
          type: string
        id:
          type: string
        filename:
          type: string
        size:
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