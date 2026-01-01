# Source: https://docs.lunary.ai/docs/api/runs/export-runs-data.md

# Export runs data

> This endpoint requires a valid private API key sent as a bearer token.




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/runs/export
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/runs/export:
    get:
      tags:
        - Runs
      summary: Export runs data
      description: |
        This endpoint requires a valid private API key sent as a bearer token.
      parameters:
        - in: query
          name: type
          required: true
          schema:
            type: string
            enum:
              - llm
              - trace
              - thread
        - in: query
          name: exportFormat
          required: true
          schema:
            type: string
            enum:
              - csv
              - jsonl
              - ojsonl
      responses:
        '200':
          description: Export successful
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
        '401':
          description: Invalid Private Key
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