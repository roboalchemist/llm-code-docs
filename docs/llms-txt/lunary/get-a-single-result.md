# Source: https://docs.lunary.ai/docs/api/evals/get-a-single-result.md

# Get a single result



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/evals/results/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/evals/results/{id}:
    get:
      tags:
        - Evals
        - Results
      summary: Get a single result
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Result details
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