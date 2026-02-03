# Source: https://docs.anchorbrowser.io/api-reference/tasks/delete-task-version.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Task Version

> Soft deletes a specific version of a task. The version will no longer be accessible
but the data is preserved for potential recovery.




## OpenAPI

````yaml openapi-mintlify.yaml delete /v1/task/{taskId}/{taskVersion}
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
  /v1/task/{taskId}/{taskVersion}:
    delete:
      tags:
        - Tasks
      summary: Delete Task Version
      description: >
        Soft deletes a specific version of a task. The version will no longer be
        accessible

        but the data is preserved for potential recovery.
      parameters:
        - name: taskId
          in: path
          required: true
          description: The ID of the task
          schema:
            type: string
            format: uuid
        - name: taskVersion
          in: path
          required: true
          description: The version to delete
          schema:
            type: string
            pattern: ^(draft|latest|\d+)$
      responses:
        '200':
          description: Task version deleted successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteTaskResponse'
        '404':
          description: Task or version not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to delete task version
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    DeleteTaskResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            success:
              type: boolean
              description: Whether the deletion was successful
            message:
              type: string
              description: Deletion result message
          required:
            - success
            - message
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