# Source: https://docs.lunary.ai/docs/api/datasets/get-prompt-variation-by-id.md

# Get prompt variation by ID



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/datasets/variations/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets/variations/{id}:
    get:
      tags:
        - Datasets
        - Prompts
        - Variations
      summary: Get prompt variation by ID
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Prompt variation details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetPromptVariation'
      security:
        - BearerAuth: []
components:
  schemas:
    DatasetPromptVariation:
      type: object
      properties:
        id:
          type: string
        promptId:
          type: string
        variables:
          type: object
        idealOutput:
          type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt