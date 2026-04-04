# Source: https://docs.tavus.io/api-reference/objectives/delete-objectives.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Objective

> This endpoint deletes a single objective by its unique identifier.




## OpenAPI

````yaml delete /v2/objectives/{objectives_id}
openapi: 3.0.3
info:
  title: Tavus Developer API Collection
  version: 1.0.0
  contact: {}
servers:
  - url: https://tavusapi.com
security:
  - apiKey: []
tags:
  - name: Videos
  - name: Replicas
  - name: Conversations
  - name: Personas
  - name: Replacements
  - name: Transcriptions
  - name: Documents
paths:
  /v2/objectives/{objectives_id}:
    parameters:
      - name: objectives_id
        in: path
        required: true
        description: The unique identifier of the objective.
        schema:
          type: string
          example: o12345
    delete:
      tags:
        - Objectives
      summary: Delete Objective
      description: |
        This endpoint deletes a single objective by its unique identifier.
      operationId: deleteObjective
      responses:
        '204':
          description: NO CONTENT - Objective deleted successfully
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message.
                    example: Invalid objectives_id
        '401':
          description: UNAUTHORIZED
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: The error message.
                    example: Invalid access token
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message.
                    example: Objective not found
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````