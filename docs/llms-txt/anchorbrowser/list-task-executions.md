# Source: https://docs.anchorbrowser.io/api-reference/tasks/list-task-executions.md

# List Task Executions

> Retrieves execution history for a task, including success/failure status,
execution times, and outputs. Results can be filtered by version and status.


## OpenAPI

````yaml openapi-mintlify.yaml get /v1/task/{taskId}/executions
paths:
  path: /v1/task/{taskId}/executions
  method: get
  servers:
    - url: https://api.anchorbrowser.io
      description: API server
  request:
    security:
      - title: api key header
        parameters:
          query: {}
          header:
            anchor-api-key:
              type: apiKey
              description: API key passed in the header
          cookie: {}
    parameters:
      path:
        taskId:
          schema:
            - type: string
              required: true
              description: The ID of the task
              format: uuid
      query:
        page:
          schema:
            - type: string
              required: false
              description: Page number
              default: '1'
        limit:
          schema:
            - type: string
              required: false
              description: Number of results per page
              default: '10'
        status:
          schema:
            - type: enum<string>
              enum:
                - success
                - failure
                - timeout
                - cancelled
                - queued
                - running
              required: false
              description: Filter by execution status
        version:
          schema:
            - type: string
              required: false
              description: Filter by task version
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
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
            refIdentifier: '#/components/schemas/TaskExecutionResultsListResponse'
        examples:
          example:
            value:
              data:
                results:
                  - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                    taskVersionId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                    version: <string>
                    status: success
                    output: <string>
                    errorMessage: <string>
                    startTime: '2023-11-07T05:31:56Z'
                    executionTime: 123
                pagination:
                  page: 2
                  limit: 2
                  total: 1
                  totalPages: 1
        description: Task executions retrieved successfully
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: object
                    properties:
                      code:
                        type: integer
                      message:
                        type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Task not found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Failed to retrieve task executions
  deprecated: false
  type: path
components:
  schemas:
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

````