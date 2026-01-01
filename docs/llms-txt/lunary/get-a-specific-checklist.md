# Source: https://docs.lunary.ai/docs/api/checklists/get-a-specific-checklist.md

# Get a specific checklist

> Retrieve a specific checklist by its ID.




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/checklists/{id}
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
    get:
      tags:
        - Checklists
      summary: Get a specific checklist
      description: |
        Retrieve a specific checklist by its ID.
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            format: uuid
          description: The ID of the checklist to retrieve
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Checklist'
        '404':
          description: Checklist not found
      security:
        - BearerAuth: []
components:
  schemas:
    Checklist:
      type: object
      properties:
        id:
          type: string
          format: uuid
        slug:
          type: string
        type:
          type: string
        data:
          type: object
          description: The checklist data
        projectId:
          type: string
          format: uuid
        ownerId:
          type: string
          format: uuid
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt