# Source: https://docs.lunary.ai/docs/api/datasets/create-a-new-prompt-variation.md

# Create a new prompt variation



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/datasets/variations
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets/variations:
    post:
      tags:
        - Datasets
        - Prompts
        - Variations
      summary: Create a new prompt variation
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                promptId:
                  type: string
                variables:
                  type: object
                idealOutput:
                  type: string
      responses:
        '200':
          description: Created prompt variation
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