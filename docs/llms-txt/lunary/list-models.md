# Source: https://docs.lunary.ai/docs/api/models/list-models.md

# List models



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/models
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/models:
    get:
      tags:
        - Models
      summary: List models
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Model'
components:
  schemas:
    Model:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        pattern:
          type: string
        unit:
          type: string
          enum:
            - TOKENS
            - CHARACTERS
            - MILLISECONDS
        inputCost:
          type: number
        outputCost:
          type: number
        tokenizer:
          type: string
        startDate:
          type: string
          format: date-time
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt