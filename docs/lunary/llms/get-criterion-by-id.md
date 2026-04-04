# Source: https://docs.lunary.ai/docs/api/evals/get-criterion-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get criterion by ID



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/evals/criteria/{id}
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
    get:
      tags:
        - Evals
        - Criteria
      summary: Get criterion by ID
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Criterion details
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````