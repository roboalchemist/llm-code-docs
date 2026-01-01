# Source: https://docs.lunary.ai/docs/api/evals/update-a-criterion.md

# Update a criterion



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi patch /v1/evals/criteria/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/evals/criteria/{id}:
    patch:
      tags:
        - Evals
        - Criteria
      summary: Update a criterion
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
                name:
                  type: string
                metric:
                  type: string
                threshold:
                  type: number
                  nullable: true
                weighting:
                  type: number
                parameters:
                  type: object
      responses:
        '200':
          description: Updated criterion
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt