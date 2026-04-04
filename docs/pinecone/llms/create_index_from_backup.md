# Source: https://docs.pinecone.io/reference/api/2025-10/control-plane/create_index_from_backup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an index from a backup

> Create an index from a backup.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  BACKUP_ID="a65ff585-d987-4da5-a622-72e19a6ed5f4"

  curl "https://api.pinecone.io/backups/$BACKUP_ID/create-index" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -H 'Content-Type: application/json' \
    -d '{
          "name": "restored-index",
          "tags": {
            "tag0": "val0",
            "tag1": "val1"
          },
          "deletion_protection": "enabled"
        }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
      "restore_job_id":"e9ba8ff8-7948-4cfa-ba43-34227f6d30d4",
      "index_id":"025117b3-e683-423c-b2d1-6d30fbe5027f"
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_control_2025-10.oas.yaml post /backups/{backup_id}/create-index
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
  /backups/{backup_id}/create-index:
    post:
      tags:
        - Manage Indexes
      summary: Create an index from a backup
      description: Create an index from a backup.
      operationId: create_index_from_backup_operation
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
          name: backup_id
          description: The ID of the backup to create an index from.
          required: true
          schema:
            type: string
          example: 670e8400-e29b-41d4-a716-446655440000
          style: simple
      requestBody:
        description: The desired configuration for the index created from a backup.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateIndexFromBackupRequest'
        required: true
      responses:
        '202':
          description: The request to create the index has been accepted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateIndexFromBackupResponse'
        '400':
          description: Bad request. The request body included invalid request parameters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                index-metric-validation-error:
                  summary: Validation error
                  value:
                    error:
                      code: INVALID_ARGUMENT
                      message: >-
                        Bad request. The request body included invalid request
                        parameters.
                    status: 400
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
        '402':
          description: >-
            Payment required. Organization is on a paid plan and is delinquent
            on payment.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                payment-required:
                  summary: Payment required
                  value:
                    error:
                      code: PAYMENT_REQUIRED
                      message: >-
                        Request failed. Pay all past due invoices to lift
                        restrictions on your account.
                    status: 402
        '403':
          description: You've exceed your pod quota.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                unauthorized:
                  summary: Forbidden
                  value:
                    error:
                      code: FORBIDDEN
                      message: Increase your quota or upgrade to create more indexes.
                    status: 403
        '404':
          description: Backup not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                backup-not-found:
                  summary: Backup not found
                  value:
                    error:
                      code: NOT_FOUND
                      message: Backup bkp_123abc not found.
                    status: 404
        '409':
          description: Index of given name already exists.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '422':
          description: Unprocessable entity. The request body could not be deserialized.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                missing-field:
                  summary: Unprocessable entity
                  value:
                    error:
                      code: UNPROCESSABLE_ENTITY
                      message: >-
                        Failed to deserialize the JSON body into the target
                        type: missing field `metric` at line 1 column 16
                    status: 422
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
    CreateIndexFromBackupRequest:
      description: The configuration needed to create a Pinecone index from a backup.
      type: object
      properties:
        name:
          example: example-index
          description: >
            The name of the index. Resource name must be 1-45 characters long,
            start and end with an alphanumeric character, and consist only of
            lower case alphanumeric characters or '-'.
          type: string
          minLength: 1
          maxLength: 45
        tags:
          $ref: '#/components/schemas/IndexTags'
        deletion_protection:
          $ref: '#/components/schemas/DeletionProtection'
      required:
        - name
    CreateIndexFromBackupResponse:
      description: The response for creating an index from a backup.
      type: object
      properties:
        restore_job_id:
          example: 670e8400-e29b-41d4-a716-446655440000
          description: The ID of the restore job that was created.
          type: string
        index_id:
          example: 123e4567-e89b-12d3-a456-426614174000
          description: The ID of the index that was created from the backup.
          type: string
      required:
        - restore_job_id
        - index_id
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
    IndexTags:
      example:
        tag0: val0
        tag1: val1
      description: >-
        Custom user tags added to an index. Keys must be 80 characters or less.
        Values must be 120 characters or less. Keys must be alphanumeric, '_',
        or '-'.  Values must be alphanumeric, ';', '@', '_', '-', '.', '+', or '
        '. To unset a key, set the value to be an empty string.
      type: object
      additionalProperties:
        type: string
    DeletionProtection:
      description: >-
        Whether [deletion
        protection](http://docs.pinecone.io/guides/manage-data/manage-indexes#configure-deletion-protection)
        is enabled/disabled for the index.

        Possible values: `disabled` or `enabled`.
      default: disabled
      x-enum:
        - disabled
        - enabled
      type: string
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: >-
        An API Key is required to call Pinecone APIs. Get yours from the
        [console](https://app.pinecone.io/).

````