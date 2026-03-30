# Source: https://docs.xano.com/api-reference/table-schema-type/create-a-text-column.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a text column

> Create a text column with formatting options and customizable validation rules
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Workspace Database: Create



## OpenAPI

````yaml apispec_meta_instance.json post /workspace/{workspace_id}/table/{table_id}/schema/type/text
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
  /workspace/{workspace_id}/table/{table_id}/schema/type/text:
    post:
      tags:
        - table / schema / type
      summary: Create a text column
      description: >-
        Create a text column with formatting options and customizable validation
        rules

        <br /><br />

        <b>Authentication:</b> required

        <br /><br />

        <b>Required API Scope:</b>

        Workspace Database: Create
      operationId: >-
        Xano Metadata
        API/workspace/{workspace_id}/table/{table_id}/schema/type/text|POST
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
                format:
                  type: string
                  description: ''
                  enum:
                    - ''
                    - plaintext
                    - yaml
                    - html
                    - xml
                    - markdown
                filters:
                  type: object
                  properties:
                    trim:
                      type: boolean
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
                    lower:
                      type: boolean
                      description: ''
                      nullable: true
                    upper:
                      type: boolean
                      description: ''
                      nullable: true
                    startsWith:
                      type: string
                      description: ''
                      nullable: true
                    alphaOk:
                      type: boolean
                      description: ''
                      nullable: true
                    digitOk:
                      type: boolean
                      description: ''
                      nullable: true
                    pattern:
                      type: string
                      description: ''
                      nullable: true
                    ok:
                      type: string
                      description: ''
                      nullable: true
                  nullable: true
              required:
                - name
              example:
                name: name
                filters:
                  trim: true
                  max: 100
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
                format:
                  type: string
                  description: ''
                  enum:
                    - ''
                    - plaintext
                    - yaml
                    - html
                    - xml
                    - markdown
                filters:
                  type: object
                  properties:
                    trim:
                      type: boolean
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
                    lower:
                      type: boolean
                      description: ''
                      nullable: true
                    upper:
                      type: boolean
                      description: ''
                      nullable: true
                    startsWith:
                      type: string
                      description: ''
                      nullable: true
                    alphaOk:
                      type: boolean
                      description: ''
                      nullable: true
                    digitOk:
                      type: boolean
                      description: ''
                      nullable: true
                    pattern:
                      type: string
                      description: ''
                      nullable: true
                    ok:
                      type: string
                      description: ''
                      nullable: true
                  nullable: true
              required:
                - name
              example:
                name: name
                filters:
                  trim: true
                  max: 100
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