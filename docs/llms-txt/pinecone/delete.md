# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete vectors

> Delete vectors by id from a single namespace.

For guidance and examples, see [Delete data](https://docs.pinecone.io/guides/manage-data/delete-data).

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/vectors/delete" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
      "ids": [
        "id-1", 
        "id-2"
      ],
      "namespace": "example-namespace"
    }
  '
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {}
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_data_2025-10.oas.yaml post /vectors/delete
openapi: 3.0.3
info:
  title: Pinecone Data Plane API
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
  - url: https://{index_host}
    variables:
      index_host:
        default: unknown
        description: host of the index
security:
  - ApiKeyAuth: []
tags:
  - name: Vector Operations
  - name: Bulk Operations
  - name: Namespace Operations
externalDocs:
  description: More Pinecone.io API docs
  url: https://docs.pinecone.io/introduction
paths:
  /vectors/delete:
    post:
      tags:
        - Vector Operations
      summary: Delete vectors
      description: >-
        Delete vectors by id from a single namespace.


        For guidance and examples, see [Delete
        data](https://docs.pinecone.io/guides/manage-data/delete-data).
      operationId: deleteVectors
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
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DeleteRequest'
        required: true
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteResponse'
        '400':
          description: Bad request. The request body included invalid request parameters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/rpcStatus'
        4XX:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/rpcStatus'
        5XX:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/rpcStatus'
components:
  schemas:
    DeleteRequest:
      description: The request for the `delete` operation.
      type: object
      properties:
        ids:
          example:
            - id-0
            - id-1
          description: Vectors to delete.
          type: array
          items:
            type: string
          minLength: 1
          maxLength: 1000
        deleteAll:
          example: false
          description: >-
            This indicates that all vectors in the index namespace should be
            deleted.
          default: false
          type: boolean
        namespace:
          example: example-namespace
          description: The namespace to delete vectors from, if applicable.
          type: string
        filter:
          description: >-
            If specified, the metadata filter here will be used to select the
            vectors to delete. This is mutually exclusive with specifying ids to
            delete in the ids param or using delete_all=True. See [Delete
            data](https://docs.pinecone.io/guides/manage-data/delete-data#delete-records-by-metadata).
          type: object
    DeleteResponse:
      description: The response for the `delete` operation.
      type: object
    rpcStatus:
      type: object
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
        details:
          type: array
          items:
            $ref: '#/components/schemas/protobufAny'
    protobufAny:
      type: object
      properties:
        typeUrl:
          type: string
        value:
          type: string
          format: byte
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: >-
        An API Key is required to call Pinecone APIs. Get yours from the
        [console](https://app.pinecone.io/).

````