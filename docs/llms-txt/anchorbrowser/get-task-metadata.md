# Source: https://docs.anchorbrowser.io/api-reference/tasks/get-task-metadata.md

# Get Task Metadata

> Retrieves task metadata without the code content. Useful for getting task information
without downloading the full task code.


## OpenAPI

````yaml openapi-mintlify.yaml get /v1/task/{taskId}
paths:
  path: /v1/task/{taskId}
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
              description: The ID of the task to retrieve
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
                  - $ref: '#/components/schemas/TaskMetadata'
            refIdentifier: '#/components/schemas/TaskMetadataResponse'
        examples:
          example:
            value:
              data:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                name: <string>
                teamId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                description: <string>
                latest: <string>
                deleted: true
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
        description: Task metadata retrieved successfully
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
        description: Failed to retrieve task
  deprecated: false
  type: path
components:
  schemas:
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

````