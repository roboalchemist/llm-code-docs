# Source: https://docs.together.ai/reference/list-evaluation-models.md

# List Evaluation Models



## OpenAPI

````yaml GET /evaluation/model-list
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
  /evaluation/model-list:
    get:
      tags:
        - evaluation
      summary: Get model list
      operationId: getModelList
      parameters:
        - name: model_source
          in: query
          required: false
          schema:
            type: string
            default: all
      responses:
        '200':
          description: Model list retrieved successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  model_list:
                    type: array
                    items:
                      type: string
                      description: The name of the model
        '400':
          description: Invalid request format
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '500':
          description: Error retrieving model list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
components:
  schemas:
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