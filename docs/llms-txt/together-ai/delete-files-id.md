# Source: https://docs.together.ai/reference/delete-files-id.md

# Delete A File

> Delete a previously uploaded data file.



## OpenAPI

````yaml DELETE /files/{id}
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
    delete:
      tags:
        - Files
      summary: Delete a file
      description: Delete a previously uploaded data file.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: File deleted successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileDeleteResponse'
components:
  schemas:
    FileDeleteResponse:
      type: object
      properties:
        id:
          type: string
        deleted:
          type: boolean
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt