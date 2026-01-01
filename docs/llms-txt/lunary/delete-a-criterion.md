# Source: https://docs.lunary.ai/docs/api/evals/delete-a-criterion.md

# Delete a criterion



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi delete /v1/evals/criteria/{id}
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
    delete:
      tags:
        - Evals
        - Criteria
      summary: Delete a criterion
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Criterion deleted successfully
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