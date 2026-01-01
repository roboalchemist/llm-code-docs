# Source: https://docs.lunary.ai/docs/api/datasets/get-prompt-by-id.md

# Get prompt by ID



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/datasets/prompts/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets/prompts/{id}:
    get:
      tags:
        - Datasets
        - Prompts
      summary: Get prompt by ID
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Prompt details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetPrompt'
      security:
        - BearerAuth: []
components:
  schemas:
    DatasetPrompt:
      type: object
      properties:
        id:
          type: string
        datasetId:
          type: string
        messages:
          oneOf:
            - type: array
              items:
                type: object
                properties:
                  role:
                    type: string
                  content:
                    type: string
            - type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt