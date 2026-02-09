# Source: https://docs.anchorbrowser.io/api-reference/tasks/list-task-executions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Task Executions

> Retrieves execution history for a task, including success/failure status,
execution times, and outputs. Results can be filtered by version and status.




## OpenAPI

````yaml openapi-mintlify.yaml get /v1/task/{taskId}/executions
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
  /v1/task/{taskId}/executions:
    get:
      tags:
        - Tasks
      summary: List Task Executions
      description: >
        Retrieves execution history for a task, including success/failure
        status,

        execution times, and outputs. Results can be filtered by version and
        status.
      parameters:
        - name: taskId
          in: path
          required: true
          description: The ID of the task
          schema:
            type: string
            format: uuid
        - name: page
          in: query
          required: false
          description: Page number
          schema:
            type: string
            pattern: ^[1-9]\d*$
            default: '1'
        - name: limit
          in: query
          required: false
          description: Number of results per page
          schema:
            type: string
            pattern: ^[1-9]\d*$
            default: '10'
        - name: status
          in: query
          required: false
          description: Filter by execution status
          schema:
            type: string
            enum:
              - success
              - failure
              - timeout
              - cancelled
              - queued
              - running
        - name: version
          in: query
          required: false
          description: Filter by task version
          schema:
            type: string
      responses:
        '200':
          description: Task executions retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaskExecutionResultsListResponse'
        '404':
          description: Task not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to retrieve task executions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    TaskExecutionResultsListResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            results:
              type: array
              items:
                $ref: '#/components/schemas/TaskExecutionResult'
            pagination:
              type: object
              properties:
                page:
                  type: integer
                  minimum: 1
                  description: Current page number
                limit:
                  type: integer
                  minimum: 1
                  description: Number of results per page
                total:
                  type: integer
                  minimum: 0
                  description: Total number of results
                totalPages:
                  type: integer
                  minimum: 0
                  description: Total number of pages
              required:
                - page
                - limit
                - total
                - totalPages
          required:
            - results
            - pagination
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