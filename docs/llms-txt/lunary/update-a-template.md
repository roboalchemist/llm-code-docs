# Source: https://docs.lunary.ai/docs/api/templates/update-a-template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a template

> This endpoint allows you to update the slug and mode of an existing template.
The mode can be either "text" or "openai" (array of chat messages).




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi patch /v1/templates/{id}
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
    patch:
      tags:
        - Templates
      summary: Update a template
      description: >
        This endpoint allows you to update the slug and mode of an existing
        template.

        The mode can be either "text" or "openai" (array of chat messages).
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
          description: The ID of the template to update
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TemplateUpdateInput'
            example:
              slug: updated-customer-support-chat
              mode: openai
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Template'
              example:
                id: 123e4567-e89b-12d3-a456-426614174000
                slug: updated-customer-support-chat
                mode: openai
                projectId: 456e7890-e12b-34d5-a678-426614174111
                createdAt: '2023-01-01T00:00:00Z'
                versions:
                  - id: 789e0123-e45b-67d8-a901-426614174222
                    templateId: 123e4567-e89b-12d3-a456-426614174000
                    content:
                      - role: system
                        content: You are a helpful customer support agent.
                      - role: user
                        content: I have a question about my order.
                    extra:
                      temperature: 0.7
                      max_tokens: 150
                    testValues:
                      orderNumber: ORD-12345
                    isDraft: false
                    notes: Updated version for improved customer support
                    createdAt: '2023-01-02T12:00:00Z'
                    version: 1
        '400':
          description: Invalid input
        '404':
          description: Template not found
components:
  schemas:
    TemplateUpdateInput:
      type: object
      properties:
        slug:
          type: string
        mode:
          type: string
          enum:
            - text
            - openai
    Template:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        slug:
          type: string
        mode:
          type: string
          enum:
            - text
            - openai
        createdAt:
          type: string
          format: date-time
        group:
          type: string
        projectId:
          type: string
        versions:
          type: array
          items:
            $ref: '#/components/schemas/TemplateVersion'
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