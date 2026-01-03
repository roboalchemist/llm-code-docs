# Source: https://docs.lunary.ai/docs/api/evals/list-results-for-an-evaluation.md

# List results for an evaluation



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/evals/{evalId}/results
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/evals/{evalId}/results:
    get:
      tags:
        - Evals
        - Results
      summary: List results for an evaluation
      parameters:
        - in: path
          name: evalId
          required: true
          schema:
            type: string
      responses:
        '200':
          description: List of results
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