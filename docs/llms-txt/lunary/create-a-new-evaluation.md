# Source: https://docs.lunary.ai/docs/api/evals/create-a-new-evaluation.md

# Create a new evaluation



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/evals
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/evals:
    post:
      tags:
        - Evals
      summary: Create a new evaluation
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                datasetId:
                  type: string
                description:
                  type: string
              required:
                - name
                - datasetId
      responses:
        '200':
          description: Created evaluation
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