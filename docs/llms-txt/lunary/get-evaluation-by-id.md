# Source: https://docs.lunary.ai/docs/api/evals/get-evaluation-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get evaluation by ID



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/evals/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/evals/{id}:
    get:
      tags:
        - Evals
      summary: Get evaluation by ID
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Evaluation details
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````