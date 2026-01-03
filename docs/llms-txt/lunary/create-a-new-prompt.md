# Source: https://docs.lunary.ai/docs/api/datasets/create-a-new-prompt.md

# Create a new prompt



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/datasets/prompts
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets/prompts:
    post:
      tags:
        - Datasets
        - Prompts
      summary: Create a new prompt
      requestBody:
        required: true
        content:
          application/json:
            schema:
              oneOf:
                - type: object
                  properties:
                    datasetId:
                      type: string
                    messages:
                      type: string
                      nullable: true
                    idealOutput:
                      type: string
                    withPromptVariation:
                      type: boolean
                      default: true
                  required:
                    - datasetId
                - type: object
                  properties:
                    datasetId:
                      type: string
                    messages:
                      type: array
                      nullable: true
                      items:
                        type: object
                        properties:
                          role:
                            type: string
                          content:
                            type: string
                        required:
                          - role
                          - content
                    idealOutput:
                      type: string
                    withPromptVariation:
                      type: boolean
                      default: true
                  required:
                    - datasetId
      responses:
        '200':
          description: Created prompt
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