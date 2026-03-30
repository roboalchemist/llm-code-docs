# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/create_a_vector_index_on_a_table_column_with_support_for_inner_product_cosine_l1_and_l2_distance_operations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a vector index on a table column with support for Inner Product, Cosine, L1, and L2 distance operations

> Options include `vector_ip_ops` (Inner Product), `vector_cosine_ops` (Cosine), `vector_l1_ops` (L1 Distance), `vector_l2_ops` (L2 Distance)



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json post /workspace/{workspace_id}/table/{table_id}/index/vector
openapi: 3.0.0
info:
  title: Xano Metadata API (beta)
  description: >-
    The <a href="https://docs.xano.com/xano-features/metadata-api"
    target="_blank">Metadata API</a>

    is currently in <strong>beta</strong> and is the next
      evolution of the Developer API. It provides support
    to programatically manage your Xano instance and uses Access Tokens to

    control access.
  version: 0.0.1
servers:
  - url: https://x8ki-letl-twmt.n7.xano.io/api:meta
security: []
paths:
  /workspace/{workspace_id}/table/{table_id}/index/vector:
    post:
      tags:
        - table / index
      summary: >-
        Create a vector index on a table column with support for Inner Product,
        Cosine, L1, and L2 distance operations
      description: >-
        Options include `vector_ip_ops` (Inner Product), `vector_cosine_ops`
        (Cosine), `vector_l1_ops` (L1 Distance), `vector_l2_ops` (L2 Distance)

        <br /><br />

        <b>Required API Scope:</b>

        Workspace Database: Create
      parameters:
        - name: workspace_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
        - name: table_id
          in: path
          description: ''
          required: true
          schema:
            type: integer
            format: int64
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                fields:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: ''
                      op:
                        type: string
                        description: ''
                        enum:
                          - vector_ip_ops
                          - vector_cosine_ops
                          - vector_l1_ops
                          - vector_l2_ops
                    required:
                      - name
                      - op
              required:
                - fields
              example:
                fields:
                  - name: name
                    op: vector_ip_ops
          multipart/form-data:
            schema:
              type: object
              properties:
                fields:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: ''
                      op:
                        type: string
                        description: ''
                        enum:
                          - vector_ip_ops
                          - vector_cosine_ops
                          - vector_l1_ops
                          - vector_l2_ops
                    required:
                      - name
                      - op
              required:
                - fields
              example:
                fields:
                  - name: name
                    op: vector_ip_ops
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
        '400':
          description: Input Error. Check the request payload for issues.
        '401':
          description: Unauthorized
        '403':
          description: >-
            Access denied. Additional privileges are needed access the requested
            resource.
        '404':
          description: Not Found. The requested resource does not exist.
        '429':
          description: Rate Limited. Too many requests.
        '500':
          description: Unexpected error
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````

Built with [Mintlify](https://mintlify.com).