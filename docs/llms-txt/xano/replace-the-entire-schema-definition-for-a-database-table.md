# Source: https://docs.xano.com/api-reference/table-schema/replace-the-entire-schema-definition-for-a-database-table.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Replace the entire schema definition for a database table

> Replace the entire schema definition for a database table
<br /><br />
<b>Authentication:</b> required
<br /><br />
<b>Required API Scope:</b>
Workspace Database: Update



## OpenAPI

````yaml apispec_meta_instance.json put /workspace/{workspace_id}/table/{table_id}/schema
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
  /workspace/{workspace_id}/table/{table_id}/schema:
    put:
      tags:
        - table / schema
      summary: Replace the entire schema definition for a database table
      description: |-
        Replace the entire schema definition for a database table
        <br /><br />
        <b>Authentication:</b> required
        <br /><br />
        <b>Required API Scope:</b>
        Workspace Database: Update
      operationId: Xano Metadata API/workspace/{workspace_id}/table/{table_id}/schema|PUT
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
                schema:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: ''
                      type:
                        type: string
                        description: ''
                        enum:
                          - attachment
                          - audio
                          - bool
                          - date
                          - decimal
                          - email
                          - enum
                          - geo_linestring
                          - geo_multilinestring
                          - geo_multipoint
                          - geo_multipolygon
                          - geo_point
                          - geo_polygon
                          - image
                          - int
                          - json
                          - object
                          - password
                          - text
                          - timestamp
                          - uuid
                          - vector
                          - video
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
                      values:
                        type: array
                        items:
                          type: object
                          description: ''
                      sensitive:
                        type: boolean
                        description: ''
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
                        nullable: true
                      tableref_id:
                        type: integer
                        format: int64
                        description: ''
                        nullable: true
                      access:
                        type: string
                        description: ''
                        enum:
                          - public
                          - private
                          - internal
                        default: public
                      style:
                        type: string
                        description: ''
                        enum:
                          - single
                          - list
                        default: single
                      children:
                        type: array
                        items:
                          type: object
                          properties:
                            name:
                              type: string
                              description: ''
                            type:
                              type: string
                              description: ''
                              enum:
                                - attachment
                                - audio
                                - bool
                                - date
                                - decimal
                                - email
                                - enum
                                - geo_linestring
                                - geo_multilinestring
                                - geo_multipoint
                                - geo_multipolygon
                                - geo_point
                                - geo_polygon
                                - image
                                - int
                                - json
                                - object
                                - password
                                - text
                                - timestamp
                                - uuid
                                - vector
                                - video
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
                            values:
                              type: array
                              items:
                                type: object
                                description: ''
                            sensitive:
                              type: boolean
                              description: ''
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
                              nullable: true
                            tableref_id:
                              type: integer
                              format: int64
                              description: ''
                              nullable: true
                            vector:
                              type: object
                              properties:
                                size:
                                  type: integer
                                  format: int64
                                  description: ''
                                  default: 3
                            access:
                              type: string
                              description: ''
                              enum:
                                - public
                                - private
                                - internal
                              default: public
                            style:
                              type: string
                              description: ''
                              enum:
                                - single
                                - list
                              default: single
                            children:
                              type: array
                              items:
                                type: object
                                description: ''
                            validators:
                              type: object
                              properties:
                                trim:
                                  type: boolean
                                  description: ''
                                lower:
                                  type: boolean
                                  description: ''
                              nullable: true
                          required:
                            - name
                            - type
                            - nullable
                            - required
                      vector:
                        type: object
                        properties:
                          size:
                            type: integer
                            format: int64
                            description: ''
                            default: 3
                      validators:
                        type: object
                        properties:
                          trim:
                            type: boolean
                            description: ''
                          lower:
                            type: boolean
                            description: ''
                        nullable: true
                    required:
                      - name
                      - type
                      - nullable
                      - required
              required:
                - schema
              example:
                schema:
                  - name: id
                    type: int
                    description: ''
                    nullable: false
                    default: ''
                    required: true
                    access: public
                    sensitive: false
                    style: single
                  - name: created_at
                    type: timestamp
                    description: ''
                    nullable: false
                    default: ''
                    required: true
                    access: public
                    sensitive: false
                    style: single
                  - name: name
                    type: text
                    description: ''
                    nullable: false
                    default: ''
                    required: true
                    access: public
                    sensitive: false
                    style: single
          multipart/form-data:
            schema:
              type: object
              properties:
                schema:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                        description: ''
                      type:
                        type: string
                        description: ''
                        enum:
                          - attachment
                          - audio
                          - bool
                          - date
                          - decimal
                          - email
                          - enum
                          - geo_linestring
                          - geo_multilinestring
                          - geo_multipoint
                          - geo_multipolygon
                          - geo_point
                          - geo_polygon
                          - image
                          - int
                          - json
                          - object
                          - password
                          - text
                          - timestamp
                          - uuid
                          - vector
                          - video
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
                      values:
                        type: array
                        items:
                          type: object
                          description: ''
                      sensitive:
                        type: boolean
                        description: ''
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
                        nullable: true
                      tableref_id:
                        type: integer
                        format: int64
                        description: ''
                        nullable: true
                      access:
                        type: string
                        description: ''
                        enum:
                          - public
                          - private
                          - internal
                        default: public
                      style:
                        type: string
                        description: ''
                        enum:
                          - single
                          - list
                        default: single
                      children:
                        type: array
                        items:
                          type: object
                          properties:
                            name:
                              type: string
                              description: ''
                            type:
                              type: string
                              description: ''
                              enum:
                                - attachment
                                - audio
                                - bool
                                - date
                                - decimal
                                - email
                                - enum
                                - geo_linestring
                                - geo_multilinestring
                                - geo_multipoint
                                - geo_multipolygon
                                - geo_point
                                - geo_polygon
                                - image
                                - int
                                - json
                                - object
                                - password
                                - text
                                - timestamp
                                - uuid
                                - vector
                                - video
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
                            values:
                              type: array
                              items:
                                type: object
                                description: ''
                            sensitive:
                              type: boolean
                              description: ''
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
                              nullable: true
                            tableref_id:
                              type: integer
                              format: int64
                              description: ''
                              nullable: true
                            vector:
                              type: object
                              properties:
                                size:
                                  type: integer
                                  format: int64
                                  description: ''
                                  default: 3
                            access:
                              type: string
                              description: ''
                              enum:
                                - public
                                - private
                                - internal
                              default: public
                            style:
                              type: string
                              description: ''
                              enum:
                                - single
                                - list
                              default: single
                            children:
                              type: array
                              items:
                                type: object
                                description: ''
                            validators:
                              type: object
                              properties:
                                trim:
                                  type: boolean
                                  description: ''
                                lower:
                                  type: boolean
                                  description: ''
                              nullable: true
                          required:
                            - name
                            - type
                            - nullable
                            - required
                      vector:
                        type: object
                        properties:
                          size:
                            type: integer
                            format: int64
                            description: ''
                            default: 3
                      validators:
                        type: object
                        properties:
                          trim:
                            type: boolean
                            description: ''
                          lower:
                            type: boolean
                            description: ''
                        nullable: true
                    required:
                      - name
                      - type
                      - nullable
                      - required
              required:
                - schema
              example:
                schema:
                  - name: id
                    type: int
                    description: ''
                    nullable: false
                    default: ''
                    required: true
                    access: public
                    sensitive: false
                    style: single
                  - name: created_at
                    type: timestamp
                    description: ''
                    nullable: false
                    default: ''
                    required: true
                    access: public
                    sensitive: false
                    style: single
                  - name: name
                    type: text
                    description: ''
                    nullable: false
                    default: ''
                    required: true
                    access: public
                    sensitive: false
                    style: single
      responses:
        '200':
          description: Success!
          content:
            application/json:
              schema:
                type: object
                description: ''
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