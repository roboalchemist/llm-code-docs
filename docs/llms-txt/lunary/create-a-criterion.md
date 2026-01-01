# Source: https://docs.lunary.ai/docs/api/evals/create-a-criterion.md

# Create a criterion



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/evals/criteria
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/evals/criteria:
    post:
      tags:
        - Evals
        - Criteria
      summary: Create a criterion
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                evalId:
                  type: string
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
              required:
                - evalId
                - name
                - metric
      responses:
        '200':
          description: Created criterion
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