# Source: https://docs.lunary.ai/docs/api/datasets/delete-a-prompt-variation.md

# Delete a prompt variation



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi delete /v1/datasets/variations/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets/variations/{id}:
    delete:
      tags:
        - Datasets
        - Prompts
        - Variations
      summary: Delete a prompt variation
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Prompt variation deleted successfully
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