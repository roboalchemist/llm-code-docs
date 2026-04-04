# Source: https://docs.anchorbrowser.io/api-reference/tasks/get-task-metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Task Metadata

> Retrieves task metadata without the code content. Useful for getting task information
without downloading the full task code.




## OpenAPI

````yaml openapi-mintlify.yaml get /v1/task/{taskId}
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
  /v1/task/{taskId}:
    get:
      tags:
        - Tasks
      summary: Get Task Metadata
      description: >
        Retrieves task metadata without the code content. Useful for getting
        task information

        without downloading the full task code.
      parameters:
        - name: taskId
          in: path
          required: true
          description: The ID of the task to retrieve
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Task metadata retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskMetadataResponse'
        '404':
          description: Task not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to retrieve task
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    TaskMetadataResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/TaskMetadata'
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
    TaskMetadata:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the task
        name:
          type: string
          pattern: ^[a-zA-Z0-9_-]+$
          minLength: 1
          maxLength: 255
          description: Task name
        teamId:
          type: string
          format: uuid
          description: Team identifier that owns this task
        description:
          type: string
          maxLength: 1000
          description: Optional description of the task
        latest:
          type: string
          description: Latest version identifier
        deleted:
          type: boolean
          description: Whether the task is soft deleted
        createdAt:
          type: string
          format: date-time
          description: Task creation timestamp
        updatedAt:
          type: string
          format: date-time
          description: Task last update timestamp
      required:
        - id
        - name
        - teamId
        - latest
        - deleted
        - createdAt
        - updatedAt
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````