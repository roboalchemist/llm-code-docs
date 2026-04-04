# Source: https://docs.pinecone.io/reference/api/2025-10/control-plane/describe_restore_job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Describe a restore job

> Get a description of a restore job.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  JOB_ID="9857add2-99d4-4399-870e-aa7f15d8d326"

  curl "https://api.pinecone.io/restore-jobs/$JOB_ID" \
      -H "X-Pinecone-Api-Version: 2025-10" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H 'accept: application/json'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "restore_job_id": "9857add2-99d4-4399-870e-aa7f15d8d326",
    "backup_id": "94a63aeb-efae-4f7a-b059-75d32c27ca57",
    "target_index_name": "restored-index",
    "target_index_id": "0d8aed24-adf8-4b77-8e10-fd674309dc85",
    "status": "Completed",
    "created_at": "2025-04-25T18:14:05.227526Z",
    "completed_at": "2025-04-25T18:14:11.074618Z",
    "percent_complete": 100
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_control_2025-10.oas.yaml get /restore-jobs/{job_id}
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
  /restore-jobs/{job_id}:
    get:
      tags:
        - Manage Indexes
      summary: Describe a restore job
      description: Get a description of a restore job.
      operationId: describe_restore_job
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
        - in: path
          name: job_id
          description: The ID of the restore job to describe.
          required: true
          schema:
            type: string
          example: 670e8400-e29b-41d4-a716-446655440000
          style: simple
      responses:
        '200':
          description: Configuration information and deployment status of the restore job.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RestoreJobModel'
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
        '404':
          description: Restore job not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                restore-job-not-found:
                  summary: Restore job not found
                  value:
                    error:
                      code: NOT_FOUND
                      message: >-
                        Restore job 670e8400-e29b-41d4-a716-446655440002 not
                        found.
                    status: 404
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
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: >-
        An API Key is required to call Pinecone APIs. Get yours from the
        [console](https://app.pinecone.io/).

````