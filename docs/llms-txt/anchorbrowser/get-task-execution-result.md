# Source: https://docs.anchorbrowser.io/api-reference/tasks/get-task-execution-result.md

# Get Task Execution Result

> Retrieves a single execution result by its ID. This endpoint is useful for polling
execution status in async mode or retrieving detailed execution information.


## OpenAPI

````yaml openapi-mintlify.yaml get /v1/task/{taskId}/executions/{executionId}
paths:
  path: /v1/task/{taskId}/executions/{executionId}
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
        executionId:
          schema:
            - type: string
              required: true
              description: The ID of the execution result
              format: uuid
      query: {}
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
                  - $ref: '#/components/schemas/TaskExecutionResult'
            refIdentifier: '#/components/schemas/TaskExecutionResultResponse'
        examples:
          example:
            value:
              data:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                taskVersionId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                version: <string>
                status: success
                output: <string>
                errorMessage: <string>
                startTime: '2023-11-07T05:31:56Z'
                executionTime: 123
        description: Execution result retrieved successfully
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
        description: Task or execution result not found
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
        description: Failed to retrieve execution result
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