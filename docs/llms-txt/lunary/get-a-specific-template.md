# Source: https://docs.lunary.ai/docs/api/templates/get-a-specific-template.md

# Get a specific template

> Get a specific prompt template and all its versions by its ID.




## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/templates/{id}
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
    get:
      tags:
        - Templates
      summary: Get a specific template
      description: |
        Get a specific prompt template and all its versions by its ID.
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Template'
              example:
                id: 123e4567-e89b-12d3-a456-426614174000
                name: Customer Support Chat
                slug: customer-support-chat
                mode: openai
                createdAt: '2023-01-01T00:00:00Z'
                projectId: 987e6543-e21b-12d3-a456-426614174000
                versions:
                  - id: abcd1234-e56f-78g9-h012-ijklmnopqrst
                    templateId: 123e4567-e89b-12d3-a456-426614174000
                    content:
                      - role: system
                        content: You are a helpful customer support agent.
                      - role: user
                        content: Hello, I have a question about my order.
                      - role: assistant
                        content: >-
                          Of course! I'd be happy to help you with your order.
                          Could you please provide me with your order number?
                    extra:
                      temperature: 0.7
                      maxTokens: 150
                    testValues:
                      orderNumber: ORD-12345
                    isDraft: false
                    notes: Updated to improve response clarity
                    createdAt: '2023-01-02T12:00:00Z'
                    version: 1
        '404':
          description: Template not found
components:
  schemas:
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt