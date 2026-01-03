# Source: https://docs.lunary.ai/docs/api/playground-endpoints/delete-a-playground-endpoint.md

# Delete a playground endpoint

> Delete a playground endpoint



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi delete /v1/playground-endpoints/{id}
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
    delete:
      tags:
        - Playground Endpoints
      summary: Delete a playground endpoint
      description: Delete a playground endpoint
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '204':
          description: Endpoint deleted successfully
        '404':
          description: Endpoint not found

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt