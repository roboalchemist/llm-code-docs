# Source: https://docs.lunary.ai/docs/api/templates/update-a-template-version.md

# Update a template version



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi patch /v1/template-versions/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/template-versions/{id}:
    patch:
      tags:
        - Templates
      summary: Update a template version
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
          description: ID of the template version
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TemplateVersionUpdateInput'
      responses:
        '200':
          description: Updated template version
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TemplateVersion'
        '401':
          description: Unauthorized access
components:
  schemas:
    TemplateVersionUpdateInput:
      type: object
      properties:
        content:
          oneOf:
            - type: array
            - type: string
        extra:
          type: object
        testValues:
          type: object
        isDraft:
          type: boolean
        notes:
          type: string
    TemplateVersion:
      type: object
      properties:
        id:
          type: string
        templateId:
          type: string
        content:
          type: array
          items:
            type: object
            properties:
              role:
                type: string
              content:
                type: string
        extra:
          type: object
        testValues:
          type: object
        isDraft:
          type: boolean
        notes:
          type: string
        createdAt:
          type: string
          format: date-time
        version:
          type: number

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt