# Source: https://docs.together.ai/reference/delete-fine-tunes-id.md

# Delete A Fine-tuning Event

> Delete a fine-tuning job.



## OpenAPI

````yaml DELETE /fine-tunes/{id}
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
  /fine-tunes/{id}:
    delete:
      tags:
        - Fine-tuning
      summary: Delete a fine-tune job
      description: Delete a fine-tuning job.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
        - name: force
          in: query
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: Fine-tune job deleted successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FinetuneDeleteResponse'
        '404':
          description: Fine-tune job not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
components:
  schemas:
    FinetuneDeleteResponse:
      type: object
      properties:
        message:
          type: string
          description: Message indicating the result of the deletion
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