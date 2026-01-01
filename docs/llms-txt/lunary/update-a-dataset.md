# Source: https://docs.lunary.ai/docs/api/datasets/update-a-dataset.md

# Update a dataset



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi patch /v1/datasets/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets/{id}:
    patch:
      tags:
        - Datasets
      summary: Update a dataset
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                slug:
                  type: string
      responses:
        '200':
          description: Updated dataset
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