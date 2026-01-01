# Source: https://docs.lunary.ai/docs/api/checklists/delete-a-checklist.md

# Delete a checklist

> Delete a specific checklist by its ID.




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi delete /v1/checklists/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/checklists/{id}:
    delete:
      tags:
        - Checklists
      summary: Delete a checklist
      description: |
        Delete a specific checklist by its ID.
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            format: uuid
          description: The ID of the checklist to delete
      responses:
        '200':
          description: Successful deletion
        '404':
          description: Checklist not found
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