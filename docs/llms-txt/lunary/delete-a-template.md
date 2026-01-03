# Source: https://docs.lunary.ai/docs/api/templates/delete-a-template.md

# Delete a template



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi delete /v1/templates/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/templates/{id}:
    delete:
      tags:
        - Templates
      summary: Delete a template
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '204':
          description: Successful deletion

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt