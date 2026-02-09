# Source: https://docs.lunary.ai/docs/api/checklists/list-all-checklists.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List all checklists

> Retrieve all checklists for the current project.
Optionally filter by type. Returns checklists ordered by most recently updated.




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/checklists
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/checklists:
    get:
      tags:
        - Checklists
      summary: List all checklists
      description: >
        Retrieve all checklists for the current project.

        Optionally filter by type. Returns checklists ordered by most recently
        updated.
      parameters:
        - in: query
          name: type
          required: false
          schema:
            type: string
          description: The type of checklists to retrieve (optional)
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Checklist'
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