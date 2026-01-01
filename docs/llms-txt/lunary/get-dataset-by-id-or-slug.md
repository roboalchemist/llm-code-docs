# Source: https://docs.lunary.ai/docs/api/datasets/get-dataset-by-id-or-slug.md

# Get dataset by ID or slug



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/datasets/{identifier}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets/{identifier}:
    get:
      tags:
        - Datasets
      summary: Get dataset by ID or slug
      parameters:
        - in: path
          name: identifier
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Dataset details
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