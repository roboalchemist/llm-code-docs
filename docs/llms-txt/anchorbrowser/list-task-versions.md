# Source: https://docs.anchorbrowser.io/api-reference/tasks/list-task-versions.md

# List Task Versions

> Retrieves all versions of a specific task, including draft and published versions.


## OpenAPI

````yaml openapi-mintlify.yaml get /v1/task/{taskId}/versions
paths:
  path: /v1/task/{taskId}/versions
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
            refIdentifier: '#/components/schemas/TaskVersionsListResponse'
        examples:
          example:
            value:
              data:
                taskId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                versions:
                  - version: <string>
                    description: <string>
                    createdAt: '2023-11-07T05:31:56Z'
                    updatedAt: '2023-11-07T05:31:56Z'
        description: Task versions retrieved successfully
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
        description: Failed to retrieve task versions
  deprecated: false
  type: path
components:
  schemas: {}

````