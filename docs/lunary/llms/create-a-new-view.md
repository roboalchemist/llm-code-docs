# Source: https://docs.lunary.ai/docs/api/views/create-a-new-view.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new view

> Creates a new dashboard view with the provided details.



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/views
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/views:
    post:
      tags:
        - Views
      summary: Create a new view
      description: Creates a new dashboard view with the provided details.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ViewInput'
            example:
              name: New LLM View
              data:
                - AND
                - id: models
                  params:
                    models:
                      - gpt-4
              icon: chart
              type: llm
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/View'
              example:
                id: 5678efgh
                name: New LLM View
                data:
                  - AND
                  - id: models
                    params:
                      models:
                        - gpt-4
                columns: []
                icon: chart
                type: llm
                projectId: project123
                ownerId: user456
                updatedAt: '2023-04-01T14:30:00Z'
components:
  schemas:
    ViewInput:
      type: object
      required:
        - name
        - data
        - type
      properties:
        name:
          type: string
          example: New LLM View
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
          example:
            id: ID
            content: Content
            date: Date
        icon:
          type: string
          example: chart
        type:
          type: string
          enum:
            - llm
            - thread
            - trace
          example: llm
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