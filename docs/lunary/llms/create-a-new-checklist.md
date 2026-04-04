# Source: https://docs.lunary.ai/docs/api/checklists/create-a-new-checklist.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new checklist

> Creates a new checklist with the provided slug, type, and data.




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/checklists
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
    post:
      tags:
        - Checklists
      summary: Create a new checklist
      description: |
        Creates a new checklist with the provided slug, type, and data.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChecklistInput'
            example:
              slug: pre-deployment-checklist
              type: deployment
              data:
                items:
                  - name: Run tests
                    completed: false
                  - name: Update documentation
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
      security:
        - BearerAuth: []
components:
  schemas:
    ChecklistInput:
      type: object
      required:
        - slug
        - type
        - data
      properties:
        slug:
          type: string
          description: Unique identifier for the checklist within the project
        type:
          type: string
          description: The type of checklist
        data:
          type: array
          description: The checklist data
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