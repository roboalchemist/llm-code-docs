# Source: https://docs.xano.com/xano-features/metadata-api/instance_api/create_a_vector_column_for_storing_multi-dimensional_data_used_in_ai_and_ml_applications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a vector column for storing multi-dimensional data used in AI and ML applications

> Create a vector column for storing multi-dimensional data used in AI and ML applications



## OpenAPI

````yaml xano-features/metadata-api/metadata_api_instance.json post /workspace/{workspace_id}/table/{table_id}/schema/type/vector
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
  /workspace/{workspace_id}/table/{table_id}/schema/type/vector:
    post:
      tags:
        - table / schema / type
      summary: >-
        Create a vector column for storing multi-dimensional data used in AI and
        ML applications
      description: >-
        Create a vector column for storing multi-dimensional data used in AI and
        ML applications

        <br /><br />

        <b>Authentication:</b> required

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
                name:
                  type: string
                  description: ''
                description:
                  type: string
                  description: ''
                nullable:
                  type: boolean
                  description: ''
                  default: true
                default:
                  type: string
                  description: ''
                required:
                  type: boolean
                  description: ''
                access:
                  type: string
                  description: ''
                  enum:
                    - public
                    - private
                    - internal
                  default: public
                sensitive:
                  type: boolean
                  description: ''
                style:
                  type: string
                  description: ''
                  enum:
                    - single
                    - list
                  default: single
                vector:
                  type: object
                  properties:
                    size:
                      type: integer
                      format: int64
                      description: ''
                      default: 3
                filters:
                  type: object
                  properties:
                    min:
                      type: integer
                      format: int64
                      description: ''
                      nullable: true
                    max:
                      type: integer
                      format: int64
                      description: ''
                      nullable: true
                  nullable: true
              required:
                - name
                - vector
              example:
                name: name
                vector:
                  size: 3
          multipart/form-data:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: ''
                description:
                  type: string
                  description: ''
                nullable:
                  type: boolean
                  description: ''
                  default: true
                default:
                  type: string
                  description: ''
                required:
                  type: boolean
                  description: ''
                access:
                  type: string
                  description: ''
                  enum:
                    - public
                    - private
                    - internal
                  default: public
                sensitive:
                  type: boolean
                  description: ''
                style:
                  type: string
                  description: ''
                  enum:
                    - single
                    - list
                  default: single
                vector:
                  type: object
                  properties:
                    size:
                      type: integer
                      format: int64
                      description: ''
                      default: 3
                filters:
                  type: object
                  properties:
                    min:
                      type: integer
                      format: int64
                      description: ''
                      nullable: true
                    max:
                      type: integer
                      format: int64
                      description: ''
                      nullable: true
                  nullable: true
              required:
                - name
                - vector
              example:
                name: name
                vector:
                  size: 3
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                properties:
                  name:
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