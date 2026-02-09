# Source: https://docs.lunary.ai/docs/api/templates/create-a-new-template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new template

> Creates a new template with the provided details.
The template includes a slug, mode, content, and additional configuration options.




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/templates
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/templates:
    post:
      tags:
        - Templates
      summary: Create a new template
      description: >
        Creates a new template with the provided details.

        The template includes a slug, mode, content, and additional
        configuration options.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TemplateInput'
            example:
              slug: greeting-template
              mode: openai
              content:
                - role: system
                  content: You are a friendly AI assistant.
                - role: user
                  content: Hello, how are you?
              extra:
                temperature: 0.7
                max_tokens: 150
              isDraft: false
              notes: Initial greeting template
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Template'
              example:
                id: 123e4567-e89b-12d3-a456-426614174000
                slug: greeting-template
                mode: openai
                createdAt: '2023-06-01T12:00:00Z'
                versions:
                  - id: 789e0123-e45b-67d8-a901-234567890000
                    content:
                      - role: system
                        content: You are a friendly AI assistant.
                      - role: user
                        content: Hello, how are you?
                    extra:
                      temperature: 0.7
                      max_tokens: 150
                    isDraft: false
                    notes: Initial greeting template
                    createdAt: '2023-06-01T12:00:00Z'
                    version: 1
components:
  schemas:
    TemplateInput:
      type: object
      required:
        - slug
        - mode
        - content
      properties:
        slug:
          type: string
        mode:
          type: string
          enum:
            - text
            - openai
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