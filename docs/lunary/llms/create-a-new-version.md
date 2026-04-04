# Source: https://docs.lunary.ai/docs/api/templates/create-a-new-version.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new version

> This endpoint allows you to push a new version of a prompt.
You can specify the content, extra parameters, test values, draft status, and notes for the new version.




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/templates/{id}/versions
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/templates/{id}/versions:
    post:
      tags:
        - Templates
        - Versions
      summary: Create a new version
      description: >
        This endpoint allows you to push a new version of a prompt.

        You can specify the content, extra parameters, test values, draft
        status, and notes for the new version.
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
          description: The ID of the template to create a new version for
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TemplateVersionInput'
            example:
              content: Hello {{name}}, welcome to {{company}}!
              extra:
                temperature: 0.7
                max_tokens: 150
              isDraft: false
              notes: Updated welcome message with company name
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TemplateVersion'
              example:
                id: '123'
                templateId: '456'
                content: Hello {{name}}, welcome to {{company}}!
                extra:
                  temperature: 0.7
                  max_tokens: 150
                isDraft: false
                notes: Updated welcome message with company name
                createdAt: '2023-06-01T12:00:00Z'
                version: 2
components:
  schemas:
    TemplateVersionInput:
      type: object
      required:
        - content
        - isDraft
      properties:
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