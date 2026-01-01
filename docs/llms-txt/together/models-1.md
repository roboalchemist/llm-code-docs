# Source: https://docs.together.ai/reference/models-1.md

# List All Models

> Lists all of Together's open-source models



## OpenAPI

````yaml GET /models
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
  /models:
    get:
      tags:
        - Models
      summary: List all models
      description: Lists all of Together's open-source models
      operationId: models
      parameters:
        - name: dedicated
          in: query
          description: Filter models to only return dedicated models
          schema:
            type: boolean
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelInfoList'
        '400':
          description: BadRequest
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
        '404':
          description: NotFound
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '429':
          description: RateLimit
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '504':
          description: Timeout
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
      deprecated: false
components:
  schemas:
    ModelInfoList:
      type: array
      items:
        $ref: '#/components/schemas/ModelInfo'
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
    ModelInfo:
      type: object
      required:
        - id
        - object
        - created
        - type
      properties:
        id:
          type: string
          example: Austism/chronos-hermes-13b
        object:
          type: string
          example: model
        created:
          type: integer
          example: 1692896905
        type:
          enum:
            - chat
            - language
            - code
            - image
            - embedding
            - moderation
            - rerank
          example: chat
        display_name:
          type: string
          example: Chronos Hermes (13B)
        organization:
          type: string
          example: Austism
        link:
          type: string
        license:
          type: string
          example: other
        context_length:
          type: integer
          example: 2048
        pricing:
          $ref: '#/components/schemas/Pricing'
    Pricing:
      type: object
      required:
        - hourly
        - input
        - output
        - base
        - finetune
      properties:
        hourly:
          type: number
          example: 0
        input:
          type: number
          example: 0.3
        output:
          type: number
          example: 0.3
        base:
          type: number
          example: 0
        finetune:
          type: number
          example: 0
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt