# Source: https://docs.lunary.ai/docs/api/playground-endpoints/list-all-playground-endpoints.md

# List all playground endpoints

> Get all playground endpoints for the current project



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/playground-endpoints
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/playground-endpoints:
    get:
      tags:
        - Playground Endpoints
      summary: List all playground endpoints
      description: Get all playground endpoints for the current project
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items: dd22a2be-a870-4bd5-97c6-8d704192e21f

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt