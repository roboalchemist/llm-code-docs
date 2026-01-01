# Source: https://docs.lunary.ai/docs/api/datasets/create-a-new-dataset.md

# Create a new dataset



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/datasets
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets:
    post:
      tags:
        - Datasets
      summary: Create a new dataset
      requestBody:
        required: true
        content:
          application/json:
            schema:
              oneOf:
                - type: object
                  properties:
                    slug:
                      type: string
                    format:
                      type: string
                      enum:
                        - text
                    prompt:
                      type: string
                      nullable: true
                    withPromptVariation:
                      type: boolean
                      default: true
                  required:
                    - slug
                    - format
                - type: object
                  properties:
                    slug:
                      type: string
                    format:
                      type: string
                      enum:
                        - chat
                    prompt:
                      oneOf:
                        - type: array
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
                        - type: string
                      nullable: true
                    withPromptVariation:
                      type: boolean
                      default: true
                  required:
                    - slug
                    - format
      responses:
        '200':
          description: Created dataset
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Dataset'
      security:
        - BearerAuth: []
components:
  schemas:
    Dataset:
      type: object
      properties:
        id:
          type: string
        slug:
          type: string
        format:
          type: string
          enum:
            - text
            - chat
        ownerId:
          type: string
        projectId:
          type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt