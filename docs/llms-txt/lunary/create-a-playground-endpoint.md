# Source: https://docs.lunary.ai/docs/api/playground-endpoints/create-a-playground-endpoint.md

# Create a playground endpoint

> Create a new playground endpoint



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/playground-endpoints
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
    post:
      tags:
        - Playground Endpoints
      summary: Create a playground endpoint
      description: Create a new playground endpoint
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: fc986c1b-3ac3-43f2-9eea-591c65a3532e
      responses:
        '201':
          description: Endpoint created successfully
          content:
            application/json:
              schema:
                $ref: de2e1fa8-21f2-491c-ba89-61f1f6d017c0

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt