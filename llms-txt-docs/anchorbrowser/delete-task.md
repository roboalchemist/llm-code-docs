# Source: https://docs.anchorbrowser.io/api-reference/tasks/delete-task.md

# Delete Task

> Soft deletes a task and all its versions. The task will no longer be accessible
but the data is preserved for potential recovery.


## OpenAPI

````yaml openapi-mintlify.yaml delete /v1/task/{taskId}
paths:
  path: /v1/task/{taskId}
  method: delete
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
              description: The ID of the task to delete
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
                  - type: object
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
            refIdentifier: '#/components/schemas/DeleteTaskResponse'
        examples:
          example:
            value:
              data:
                success: true
                message: <string>
        description: Task deleted successfully
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
        description: Failed to delete task
  deprecated: false
  type: path
components:
  schemas: {}

````