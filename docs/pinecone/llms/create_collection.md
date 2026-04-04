# Source: https://docs.pinecone.io/reference/api/2025-10/control-plane/create_collection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a collection

> Create a Pinecone collection.
  
Serverless indexes do not support collections.


<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -s "https://api.pinecone.io/collections" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
          "name": "example-collection",
          "source": "docs-example"
    }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
      "name": "example-collection",
      "status": "Initializing",
      "environment": "us-east-1-aws",
      "dimension": 1536
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_control_2025-10.oas.yaml post /collections
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
  /collections:
    post:
      tags:
        - Manage Indexes
      summary: Create a collection
      description: |
        Create a Pinecone collection.
          
        Serverless indexes do not support collections.
      operationId: create_collection
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
      requestBody:
        description: The desired configuration for the collection.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateCollectionRequest'
            examples:
              creating-collection:
                summary: Creating a collection
                value:
                  name: example-collection
                  source: example-source-index
        required: true
      responses:
        '201':
          description: The collection has been successfully created.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CollectionModel'
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
          description: You've exceed your collections quota.
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
                      message: >-
                        Collection exceeds quota. Maximum allowed on your
                        account is 1. Currently have 1.
                    status: 403
        '409':
          description: Collection of given name already exists.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                collection-name-already-exists:
                  summary: Collection name needs to be unique.
                  value:
                    error:
                      code: ALREADY_EXISTS
                      message: Resource already exists.
                    status: 409
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
    CreateCollectionRequest:
      description: The configuration needed to create a Pinecone collection.
      type: object
      properties:
        name:
          description: >
            The name of the collection to be created. Resource name must be 1-45
            characters long, start and end with an alphanumeric character, and
            consist only of lower case alphanumeric characters or '-'.
          type: string
          minLength: 1
          maxLength: 45
        source:
          example: example-source-index
          description: The name of the index to be used as the source for the collection.
          type: string
      required:
        - name
        - source
    CollectionModel:
      description: >-
        The CollectionModel describes the configuration and status of a Pinecone
        collection.
      type: object
      properties:
        name:
          example: example-collection
          description: The name of the collection.
          type: string
        size:
          example: 10000000
          description: The size of the collection in bytes.
          type: integer
          format: int64
        status:
          example: Initializing
          description: |-
            The status of the collection.
            Possible values: `Initializing`, `Ready`, or `Terminating`.
          x-enum:
            - Initializing
            - Ready
            - Terminating
          type: string
        dimension:
          example: 1536
          description: >-
            The dimension of the vectors stored in each record held in the
            collection.
          type: integer
          format: int32
          minimum: 1
          maximum: 20000
        vector_count:
          example: 120000
          description: The number of records stored in the collection.
          type: integer
          format: int32
        environment:
          example: us-east1-gcp
          description: The environment where the collection is hosted.
          type: string
      required:
        - name
        - status
        - environment
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