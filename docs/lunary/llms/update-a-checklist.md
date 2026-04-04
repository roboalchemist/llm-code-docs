# Source: https://docs.lunary.ai/docs/api/checklists/update-a-checklist.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a checklist

> Update an existing checklist's slug and/or data.




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi patch /v1/checklists/{id}
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
    patch:
      tags:
        - Checklists
      summary: Update a checklist
      description: |
        Update an existing checklist's slug and/or data.
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
            format: uuid
          description: The ID of the checklist to update
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChecklistUpdateInput'
            example:
              slug: updated-checklist-slug
              data:
                items:
                  - name: Run tests
                    completed: true
                  - name: Update documentation
                    completed: true
                  - name: Deploy to production
                    completed: false
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Checklist'
        '400':
          description: Invalid input
        '404':
          description: Checklist not found
      security:
        - BearerAuth: []
components:
  schemas:
    ChecklistUpdateInput:
      type: object
      properties:
        slug:
          type: string
          description: Updated slug for the checklist
        data:
          type: object
          description: Updated checklist data
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