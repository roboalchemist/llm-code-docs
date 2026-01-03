# Source: https://docs.lunary.ai/docs/api/views/update-a-view.md

# Update a view

> Updates an existing view with the provided details.



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi patch /v1/views/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/views/{id}:
    patch:
      tags:
        - Views
      summary: Update a view
      description: Updates an existing view with the provided details.
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ViewUpdateInput'
            example:
              name: Updated LLM View
              data:
                - AND
                - id: models
                  params:
                    models:
                      - gpt-4
                      - gpt-3.5-turbo
              icon: user
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/View'
              example:
                id: 1234abcd
                name: Updated LLM View
                data:
                  - AND
                  - id: models
                    params:
                      models:
                        - gpt-4
                        - gpt-3.5-turbo
                columns: []
                icon: user
                type: llm
                projectId: project123
                ownerId: user456
                updatedAt: '2023-04-02T10:15:00Z'
components:
  schemas:
    ViewUpdateInput:
      type: object
      properties:
        name:
          type: string
          example: Updated LLM View
        data:
          type: array
          items:
            oneOf:
              - type: string
              - type: object
                properties:
                  id:
                    type: string
                  params:
                    type: object
          example:
            - AND
            - id: models
              params:
                models:
                  - gpt-4
                  - gpt-3.5-turbo
        columns:
          type: object
          example:
            id: ID
            content: Content
            date: Date
            user: User
        icon:
          type: string
          example: user
    View:
      type: object
      properties:
        id:
          type: string
          example: 1234abcd
        name:
          type: string
          example: LLM Conversations
        data:
          type: array
          items:
            oneOf:
              - type: string
              - type: object
                properties:
                  id:
                    type: string
                  params:
                    type: object
          example:
            - AND
            - id: models
              params:
                models:
                  - gpt-4
        columns:
          type: object
        icon:
          type: string
          example: chat
        type:
          type: string
          enum:
            - llm
            - thread
            - trace
          example: llm
        projectId:
          type: string
          example: project123
        ownerId:
          type: string
          example: user456
        updatedAt:
          type: string
          format: date-time
          example: '2023-04-01T12:00:00Z'

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt