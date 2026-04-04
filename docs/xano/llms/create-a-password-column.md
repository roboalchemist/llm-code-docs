# Source: https://docs.xano.com/api-reference/table-schema-type/create-a-password-column.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a password column

> Create a password column with automatic hashing and complexity validation rules
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Workspace Database: Create



## OpenAPI

````yaml apispec_meta_instance.json post /workspace/{workspace_id}/table/{table_id}/schema/type/password
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
  /workspace/{workspace_id}/table/{table_id}/schema/type/password:
    post:
      tags:
        - table / schema / type
      summary: Create a password column
      description: >-
        Create a password column with automatic hashing and complexity
        validation rules

        <br /><br />

        <b>Authentication:</b> required

        <br /><br />

        <b>Required API Scope:</b>

        Workspace Database: Create
      operationId: >-
        Xano Metadata
        API/workspace/{workspace_id}/table/{table_id}/schema/type/password|POST
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
                filters:
                  type: object
                  properties:
                    salt:
                      type: string
                      description: ''
                      nullable: true
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
                    minAlpha:
                      type: integer
                      format: int64
                      description: ''
                      nullable: true
                    minLowerAlpha:
                      type: integer
                      format: int64
                      description: ''
                      nullable: true
                    minUpperAlpha:
                      type: integer
                      format: int64
                      description: ''
                      nullable: true
                    minDigit:
                      type: integer
                      format: int64
                      description: ''
                      nullable: true
                    minSymbol:
                      type: integer
                      format: int64
                      description: ''
                      nullable: true
                  nullable: true
              required:
                - name
              example:
                name: password
                filters:
                  min: 8
                  max: 64
                  minAlpha: 1
                  minDigit: 1
                  minSymbol: 1
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
                filters:
                  type: object
                  properties:
                    salt:
                      type: string
                      description: ''
                      nullable: true
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
                    minAlpha:
                      type: integer
                      format: int64
                      description: ''
                      nullable: true
                    minLowerAlpha:
                      type: integer
                      format: int64
                      description: ''
                      nullable: true
                    minUpperAlpha:
                      type: integer
                      format: int64
                      description: ''
                      nullable: true
                    minDigit:
                      type: integer
                      format: int64
                      description: ''
                      nullable: true
                    minSymbol:
                      type: integer
                      format: int64
                      description: ''
                      nullable: true
                  nullable: true
              required:
                - name
              example:
                name: password
                filters:
                  min: 8
                  max: 64
                  minAlpha: 1
                  minDigit: 1
                  minSymbol: 1
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