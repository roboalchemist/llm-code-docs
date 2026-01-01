# Source: https://docs.lunary.ai/docs/api/evals/run-the-evaluation.md

# Run the evaluation



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/evals/{id}/run
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/evals/{id}/run:
    post:
      tags:
        - Evals
      summary: Run the evaluation
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '204':
          description: No Content
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