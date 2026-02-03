# Source: https://docs.anchorbrowser.io/api-reference/tasks/get-task-execution-result.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Task Execution Result

> Retrieves a single execution result by its ID. This endpoint is useful for polling
execution status in async mode or retrieving detailed execution information.




## OpenAPI

````yaml openapi-mintlify.yaml get /v1/task/{taskId}/executions/{executionId}
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
  /v1/task/{taskId}/executions/{executionId}:
    get:
      tags:
        - Tasks
      summary: Get Task Execution Result
      description: >
        Retrieves a single execution result by its ID. This endpoint is useful
        for polling

        execution status in async mode or retrieving detailed execution
        information.
      parameters:
        - name: taskId
          in: path
          required: true
          description: The ID of the task
          schema:
            type: string
            format: uuid
        - name: executionId
          in: path
          required: true
          description: The ID of the execution result
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Execution result retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskExecutionResultResponse'
        '404':
          description: Task or execution result not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to retrieve execution result
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    TaskExecutionResultResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/TaskExecutionResult'
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
    TaskExecutionResult:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the execution result
        taskVersionId:
          type: string
          format: uuid
          description: Task version identifier
        version:
          type: string
          description: Version that was executed
        status:
          type: string
          enum:
            - success
            - failure
            - timeout
            - cancelled
            - queued
            - running
          description: Execution status
        output:
          type: string
          nullable: true
          description: Task execution output
        errorMessage:
          type: string
          nullable: true
          description: Error message if execution failed
        startTime:
          type: string
          format: date-time
          description: Execution start time
        executionTime:
          type: number
          nullable: true
          description: Execution duration in milliseconds
      required:
        - id
        - taskVersionId
        - version
        - status
        - startTime
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````