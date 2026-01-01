# Source: https://docs.lunary.ai/docs/api/evals/list-evaluations.md

# List evaluations



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/evals
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
    get:
      tags:
        - Evals
      summary: List evaluations
      responses:
        '200':
          description: List of evaluations
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