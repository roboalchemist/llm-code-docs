# Source: https://docs.lunary.ai/docs/api/views/get-a-specific-view.md

# Get a specific view

> Retrieves details of a specific view by its ID.



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/views/{id}
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
    get:
      tags:
        - Views
      summary: Get a specific view
      description: Retrieves details of a specific view by its ID.
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
                $ref: '#/components/schemas/View'
              example:
                id: 1234abcd
                name: LLM Conversations
                data:
                  - AND
                  - id: models
                    params:
                      models:
                        - gpt-4
                columns:
                  id: ID
                  content: Content
                icon: chat
                type: llm
                projectId: project123
                ownerId: user456
                updatedAt: '2023-04-01T12:00:00Z'
        '404':
          description: View not found
components:
  schemas:
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