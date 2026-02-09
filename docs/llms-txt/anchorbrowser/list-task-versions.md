# Source: https://docs.anchorbrowser.io/api-reference/tasks/list-task-versions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Task Versions

> Retrieves all versions of a specific task, including draft and published versions.




## OpenAPI

````yaml openapi-mintlify.yaml get /v1/task/{taskId}/versions
openapi: 3.1.0
info:
  title: AnchorBrowser API
  version: 1.0.0
  description: APIs to manage all browser-related actions and configuration.
servers:
  - url: https://api.anchorbrowser.io
    description: API server
security: []
paths:
  /v1/task/{taskId}/versions:
    get:
      tags:
        - Tasks
      summary: List Task Versions
      description: >
        Retrieves all versions of a specific task, including draft and published
        versions.
      parameters:
        - name: taskId
          in: path
          required: true
          description: The ID of the task
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task versions retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskVersionsListResponse'
        '404':
          description: Task not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to retrieve task versions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    TaskVersionsListResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            taskId:
              type: string
              format: uuid
              description: Task identifier
            versions:
              type: array
              items:
                type: object
                properties:
                  version:
                    type: string
                    description: Version identifier
                  description:
                    type: string
                    description: Version description
                  createdAt:
                    type: string
                    format: date-time
                    description: Version creation timestamp
                  updatedAt:
                    type: string
                    format: date-time
                    description: Version last update timestamp
                required:
                  - version
                  - createdAt
                  - updatedAt
          required:
            - taskId
            - versions
    ErrorResponse:
      type: object
      properties:
        error:
          type: object
          properties:
            code:
              type: integer
            message:
              type: string
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````