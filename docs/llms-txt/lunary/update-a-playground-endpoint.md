# Source: https://docs.lunary.ai/docs/api/playground-endpoints/update-a-playground-endpoint.md

# Update a playground endpoint

> Update an existing playground endpoint



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi put /v1/playground-endpoints/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/playground-endpoints/{id}:
    put:
      tags:
        - Playground Endpoints
      summary: Update a playground endpoint
      description: Update an existing playground endpoint
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: c60bcce1-007d-42a9-a781-400e0c45ac07
      responses:
        '200':
          description: Endpoint updated successfully
          content:
            application/json:
              schema:
                $ref: de2e1fa8-21f2-491c-ba89-61f1f6d017c0
        '404':
          description: Endpoint not found

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt