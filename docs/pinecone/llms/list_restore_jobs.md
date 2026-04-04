# Source: https://docs.pinecone.io/reference/api/2025-10/control-plane/list_restore_jobs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List restore jobs

> List all restore jobs for a project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/restore-jobs" \
  	-H "X-Pinecone-Api-Version: 2025-10" \
  	-H "Api-Key: $PINECONE_API_KEY"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "data": [
      {
        "restore_job_id": "9857add2-99d4-4399-870e-aa7f15d8d326",
        "backup_id": "94a63aeb-efae-4f7a-b059-75d32c27ca57",
        "target_index_name": "restored-index",
        "target_index_id": "0d8aed24-adf8-4b77-8e10-fd674309dc85",
        "status": "Completed",
        "created_at": "2025-04-25T18:14:05.227526Z",
        "completed_at": "2025-04-25T18:14:11.074618Z",
        "percent_complete": 100
      },
      {
        "restore_job_id": "69acc1d0-9105-4fcb-b1db-ebf97b285c5e",
        "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
        "target_index_name": "restored-index2",
        "target_index_id": "e6c0387f-33db-4227-9e91-32181106e56b",
        "status": "Completed",
        "created_at": "2025-05-14T17:25:59.378989Z",
        "completed_at": "2025-05-14T17:26:23.997284Z",
        "percent_complete": 100
      }
    ],
    "pagination": null
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_control_2025-10.oas.yaml get /restore-jobs
openapi: 3.0.3
info:
  title: Pinecone Control Plane API
  description: >-
    Pinecone is a vector database that makes it easy to search and retrieve
    billions of high-dimensional vectors.
  contact:
    name: Pinecone Support
    url: https://support.pinecone.io
    email: support@pinecone.io
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0
  version: 2025-10
servers:
  - url: https://api.pinecone.io
    description: Production API endpoints
security:
  - ApiKeyAuth: []
tags:
  - name: Manage Indexes
    description: Actions that manage indexes
externalDocs:
  description: More Pinecone.io API docs
  url: https://docs.pinecone.io/introduction
paths:
  /restore-jobs:
    get:
      tags:
        - Manage Indexes
      summary: List restore jobs
      description: List all restore jobs for a project.
      operationId: list_restore_jobs
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
        - in: query
          name: limit
          description: The number of results to return per page.
          schema:
            default: 10
            type: integer
            minimum: 1
            maximum: 100
          style: form
        - in: query
          name: paginationToken
          description: The token to use to retrieve the next page of results.
          schema:
            type: string
          style: form
      responses:
        '200':
          description: >-
            This operation returns a list of all the restore jobs that you have
            previously created.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RestoreJobList'
              examples:
                paginated-restore-jobs:
                  summary: A list containing restore jobs.
                  value:
                    data:
                      - backup_id: 670e8400-e29b-41d4-a716-446655440000
                        completed_at: '2024-03-15T10:35:00.000Z'
                        created_at: '2024-03-15T10:30:00.000Z'
                        percent_complete: 100
                        restore_job_id: 670e8400-e29b-41d4-a716-446655440001
                        status: Completed
                        target_index_id: idx_456
                        target_index_name: my-index
                    pagination:
                      next: dXNlcl9pZD11c2VyXzE=
                non-paginated-restore-jobs:
                  summary: A list containing restore jobs.
                  value:
                    data:
                      - backup_id: 670e8400-e29b-41d4-a716-446655440000
                        completed_at: '2024-03-15T10:35:00.000Z'
                        created_at: '2024-03-15T10:30:00.000Z'
                        percent_complete: 100
                        restore_job_id: 670e8400-e29b-41d4-a716-446655440001
                        status: Completed
                        target_index_id: idx_456
                        target_index_name: my-index
                    pagination: null
                no-restore-jobs:
                  summary: An empty list.
                  value:
                    data: []
                    pagination: null
        '401':
          description: 'Unauthorized. Possible causes: Invalid API key.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                unauthorized:
                  summary: Unauthorized
                  value:
                    error:
                      code: UNAUTHENTICATED
                      message: Invalid API key.
                    status: 401
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                internal-server-error:
                  summary: Internal server error
                  value:
                    error:
                      code: UNKNOWN
                      message: Internal server error
                    status: 500
components:
  schemas:
    RestoreJobList:
      description: The list of restore jobs that exist in the project.
      type: object
      properties:
        data:
          description: List of restore job objects
          type: array
          items:
            $ref: '#/components/schemas/RestoreJobModel'
        pagination:
          $ref: '#/components/schemas/PaginationResponse'
      required:
        - data
    ErrorResponse:
      example:
        error:
          code: QUOTA_EXCEEDED
          message: >-
            The index exceeds the project quota of 5 pods by 2 pods. Upgrade
            your account or change the project settings to increase the quota.
        status: 429
      description: The response shape used for all error responses.
      type: object
      properties:
        status:
          example: 500
          description: The HTTP status code of the error.
          type: integer
        error:
          example:
            code: INVALID_ARGUMENT
            message: >-
              Index name must contain only lowercase alphanumeric characters or
              hyphens, and must not begin or end with a hyphen.
          description: Detailed information about the error that occurred.
          type: object
          properties:
            code:
              description: >-
                The error code.

                Possible values: `OK`, `UNKNOWN`, `INVALID_ARGUMENT`,
                `DEADLINE_EXCEEDED`, `QUOTA_EXCEEDED`, `NOT_FOUND`,
                `ALREADY_EXISTS`, `PERMISSION_DENIED`, `UNAUTHENTICATED`,
                `RESOURCE_EXHAUSTED`, `FAILED_PRECONDITION`, `ABORTED`,
                `OUT_OF_RANGE`, `UNIMPLEMENTED`, `INTERNAL`, `UNAVAILABLE`,
                `DATA_LOSS`, `FORBIDDEN`, `UNPROCESSABLE_ENTITY`, or
                `PAYMENT_REQUIRED`.
              x-enum:
                - OK
                - UNKNOWN
                - INVALID_ARGUMENT
                - DEADLINE_EXCEEDED
                - QUOTA_EXCEEDED
                - NOT_FOUND
                - ALREADY_EXISTS
                - PERMISSION_DENIED
                - UNAUTHENTICATED
                - RESOURCE_EXHAUSTED
                - FAILED_PRECONDITION
                - ABORTED
                - OUT_OF_RANGE
                - UNIMPLEMENTED
                - INTERNAL
                - UNAVAILABLE
                - DATA_LOSS
                - FORBIDDEN
                - UNPROCESSABLE_ENTITY
                - PAYMENT_REQUIRED
              type: string
            message:
              example: >-
                Index name must contain only lowercase alphanumeric characters
                or hyphens, and must not begin or end with a hyphen.
              description: A human-readable description of the error
              type: string
            details:
              description: >-
                Additional information about the error. This field is not
                guaranteed to be present.
              type: object
          required:
            - code
            - message
      required:
        - status
        - error
    RestoreJobModel:
      description: The RestoreJobModel describes the status of a restore job.
      type: object
      properties:
        restore_job_id:
          example: 670e8400-e29b-41d4-a716-446655440001
          description: Unique identifier for the restore job
          type: string
        backup_id:
          example: 670e8400-e29b-41d4-a716-446655440000
          description: Backup used for the restore
          type: string
        target_index_name:
          example: sample-index
          description: Name of the index into which data is being restored
          type: string
        target_index_id:
          example: 670e8400-e29b-41d4-a716-446655440002
          description: ID of the index
          type: string
        status:
          example: Completed
          description: Status of the restore job
          type: string
        created_at:
          example: '2025-02-04T13:00:00.000Z'
          description: Timestamp when the restore job started
          type: string
          format: date-time
        completed_at:
          example: '2025-02-04T14:00:00.000Z'
          description: Timestamp when the restore job finished
          type: string
          format: date-time
        percent_complete:
          example: 42.2
          description: The progress made by the restore job out of 100
          type: number
          format: float
          minimum: 0
          maximum: 100
      required:
        - restore_job_id
        - backup_id
        - target_index_name
        - target_index_id
        - status
        - created_at
    PaginationResponse:
      example:
        next: dXNlcl9pZD11c2VyXzE=
      description: The pagination object that is returned with paginated responses.
      type: object
      properties:
        next:
          example: dXNlcl9pZD11c2VyXzE=
          description: The token to use to retrieve the next page of results.
          type: string
      required:
        - next
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: >-
        An API Key is required to call Pinecone APIs. Get yours from the
        [console](https://app.pinecone.io/).

````