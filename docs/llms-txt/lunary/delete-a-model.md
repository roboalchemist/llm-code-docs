# Source: https://docs.lunary.ai/docs/api/models/delete-a-model.md

# Delete a model



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi delete /v1/models/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/models/{id}:
    delete:
      tags:
        - Models
      summary: Delete a model
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful deletion

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt