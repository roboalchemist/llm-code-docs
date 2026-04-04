# Source: https://docs.pinecone.io/reference/api/2025-10/control-plane/list_project_backups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List backups for all indexes in a project

> List all backups for a project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X GET "https://api.pinecone.io/backups" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2025-10" \
      -H "accept: application/json"
  ```
</RequestExample>

<ResponseExample>
  ```json curl  theme={null}
  {
    "data": [
      {
        "backup_id": "e12269b0-a29b-4af0-9729-c7771dec03e3",
        "source_index_id": "bcb5b3c9-903e-4cb6-8b37-a6072aeb874f",
        "source_index_name": "docs-example",
        "tags": null,
        "name": "example-backup",
        "description": null,
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 0,
        "record_count": 96,
        "namespace_count": 1,
        "size_bytes": 86393,
        "created_at": "2025-05-14T17:00:45.803146Z"
      },
      {
        "backup_id": "d686451d-1ede-4004-9f72-7d22cc799b6e",
        "source_index_id": "b49f27d1-1bf3-49c6-82b5-4ae46f00f0e6",
        "source_index_name": "docs-example2",
        "tags": null,
        "name": "example-backup2",
        "description": null,
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 1024,
        "record_count": 50,
        "namespace_count": 1,
        "size_bytes": 545171,
        "created_at": "2025-05-14T17:00:34.814371Z"
      },
      {
        "backup_id": "8c85e612-ed1c-4f97-9f8c-8194e07bcf71",
        "source_index_id": "f73b36c9-faf5-4a2c-b1d6-4013d8b1cc74",
        "source_index_name": "docs-example3",
        "tags": {},
        "name": "example-backup3",
        "description": "Monthly backup of production index",
        "status": "Ready",
        "cloud": "aws",
        "region": "us-east-1",
        "dimension": 1024,
        "record_count": 98,
        "namespace_count": 3,
        "size_bytes": 1069169,
        "created_at": "2025-05-14T16:37:25.625540Z"
      }
    ],
    "pagination": null
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_control_2025-10.oas.yaml get /backups
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
  /backups:
    get:
      tags:
        - Manage Indexes
      summary: List backups for all indexes in a project
      description: List all backups for a project.
      operationId: list_project_backups
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
            This operation returns a list of all the backups for the given index
            that you have previously created.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BackupList'
              examples:
                backups:
                  summary: A list containing backups.
                  value:
                    data:
                      - backup_id: 670e8400-e29b-41d4-a716-446655440000
                        cloud: aws
                        created_at: '2024-03-15T10:30:00.000Z'
                        description: Monthly backup of production index
                        dimension: 1536
                        metric: cosine
                        name: backup_2024_03_15
                        namespace_count: 3
                        record_count: 120000
                        region: us-east-1
                        schema:
                          fields:
                            genre:
                              filterable: true
                            title:
                              filterable: true
                        size_bytes: 10000000
                        source_index_id: idx_456
                        source_index_name: my-index
                        status: Ready
                        tags:
                          environment: production
                          type: monthly
                      - backup_id: 670e8400-e29b-41d4-a716-446655440001
                        cloud: aws
                        created_at: '2024-03-20T15:45:00.000Z'
                        description: Pre-deployment safety backup
                        dimension: 1536
                        metric: cosine
                        name: backup_2024_03_20
                        namespace_count: 4
                        record_count: 125000
                        region: us-east-1
                        schema:
                          fields:
                            genre:
                              filterable: true
                            title:
                              filterable: true
                        size_bytes: 10500000
                        source_index_id: idx_789
                        source_index_name: my-index-2
                        status: Ready
                        tags:
                          environment: production
                          type: pre-deploy
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
    BackupList:
      description: The list of backups that exist in the project.
      type: object
      properties:
        data:
          description: List of backup objects
          type: array
          items:
            $ref: '#/components/schemas/BackupModel'
        pagination:
          $ref: '#/components/schemas/PaginationResponse'
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
    BackupModel:
      description: >-
        The BackupModel describes the configuration and status of a Pinecone
        backup.
      type: object
      properties:
        backup_id:
          example: 670e8400-e29b-41d4-a716-446655440001
          description: Unique identifier for the backup.
          type: string
        source_index_name:
          example: my-index
          description: Name of the index from which the backup was taken.
          type: string
        source_index_id:
          example: 670e8400-e29b-41d4-a716-446655440000
          description: ID of the index.
          type: string
        name:
          example: backup-2025-02-04
          description: Optional user-defined name for the backup.
          type: string
        description:
          example: Backup before bulk update.
          description: Optional description providing context for the backup.
          type: string
        status:
          example: Ready
          description: Current status of the backup (e.g., Initializing, Ready, Failed).
          type: string
        cloud:
          example: aws
          description: Cloud provider where the backup is stored.
          type: string
        region:
          example: us-east-1
          description: Cloud region where the backup is stored.
          type: string
        dimension:
          example: 1536
          description: The dimensions of the vectors to be inserted in the index.
          type: integer
          format: int32
          minimum: 1
          maximum: 20000
        metric:
          description: >-
            The distance metric to be used for similarity search. You can use
            'euclidean', 'cosine', or 'dotproduct'. If the 'vector_type' is
            'sparse', the metric must be 'dotproduct'. If the `vector_type` is
            `dense`, the metric defaults to 'cosine'.

            Possible values: `cosine`, `euclidean`, or `dotproduct`.
          x-enum:
            - cosine
            - euclidean
            - dotproduct
          type: string
        schema:
          $ref: '#/components/schemas/MetadataSchema'
        record_count:
          example: 120000
          description: Total number of records in the backup.
          type: integer
        namespace_count:
          example: 3
          description: Number of namespaces in the backup.
          type: integer
        size_bytes:
          example: 10000000
          description: Size of the backup in bytes.
          type: integer
        tags:
          $ref: '#/components/schemas/IndexTags'
        created_at:
          description: Timestamp when the backup was created.
          type: string
      required:
        - backup_id
        - source_index_name
        - source_index_id
        - status
        - cloud
        - region
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
    MetadataSchema:
      example:
        fields:
          description:
            filterable: true
          genre:
            filterable: true
          year:
            filterable: true
      description: >-
        Schema for the behavior of Pinecone's internal metadata index. By
        default, all metadata is indexed; when `schema` is present, only fields
        which are present in the `fields` object with a `filterable: true` are
        indexed. Note that `filterable: false` is not currently supported.
      type: object
      properties:
        fields:
          description: >-
            A map of metadata field names to their configuration. The field name
            must be a valid metadata field name. The field name must be unique.
          type: object
          additionalProperties:
            type: object
            properties:
              filterable:
                description: >-
                  Whether the field is filterable. If true, the field is indexed
                  and can be used in filters. Only true values are allowed.
                type: boolean
      required:
        - fields
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
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: >-
        An API Key is required to call Pinecone APIs. Get yours from the
        [console](https://app.pinecone.io/).

````