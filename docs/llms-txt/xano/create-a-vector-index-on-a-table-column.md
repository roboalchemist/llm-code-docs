# Source: https://docs.xano.com/api-reference/table-index/create-a-vector-index-on-a-table-column.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a vector index on a table column

> Options include `vector_ip_ops` (Inner Product), `vector_cosine_ops` (Cosine), `vector_l1_ops` (L1 Distance), `vector_l2_ops` (L2 Distance)
<br /><br />
<b>Required API Scope:</b>
Workspace Database: Create



## OpenAPI

````yaml apispec_meta_instance.json post /workspace/{workspace_id}/table/{table_id}/index/vector
openapi: 3.0.0
info:
  title: Xano Metadata API
  description: >-
    The <a href="https://docs.xano.com/xano-features/metadata-api"
    target="_blank">Metadata API</a> provides support

    to programatically manage your Xano instance and uses Access Tokens to

    control access.
  version: 0.0.1
servers:
  - url: https://your-xano-instance.xano.io/api:meta
security: []
paths:
  /workspace/{workspace_id}/table/{table_id}/index/vector:
    post:
      tags:
        - table / index
      summary: Create a vector index on a table column
      description: >-
        Options include `vector_ip_ops` (Inner Product), `vector_cosine_ops`
        (Cosine), `vector_l1_ops` (L1 Distance), `vector_l2_ops` (L2 Distance)

        <br /><br />

        <b>Required API Scope:</b>

        Workspace Database: Create
      operationId: >-
        Xano Metadata
        API/workspace/{workspace_id}/table/{table_id}/index/vector|POST
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