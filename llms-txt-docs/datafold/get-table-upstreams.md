# Source: https://docs.datafold.com/api-reference/explore/get-table-upstreams.md

# Get table upstreams

> Retrieve a list of tables which the given table depends on.

## OpenAPI

````yaml openapi-public.json get /api/v1/explore/db/{data_connection_id}/tables/{table_path}/upstreams
paths:
  path: /api/v1/explore/db/{data_connection_id}/tables/{table_path}/upstreams
  method: get
  servers:
    - url: https://app.datafold.com
      description: Default server
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: Use the 'Authorization' header with the format 'Key <api-key>'
          cookie: {}
    parameters:
      path:
        data_connection_id:
          schema:
            - type: integer
              required: true
              title: Data Connection ID
              description: >-
                Unique ID for the Data Connection. Can be found in the Datafold
                app under Settings > Integrations > Data Connections.
              minimum: 1
        table_path:
          schema:
            - type: string
              required: true
              title: Table Path
              description: >-
                Path to the table, e.g. `db.schema.table`. The path is case
                sensitive. If components of the path contain periods, they must
                be quoted: `db."my.schema"."www.mysite.com visits"`.
      query:
        max_depth:
          schema:
            - type: integer
              required: false
              title: Max depth
              description: Maximum depth of the lineage to retrieve.
              maximum: 100
              exclusiveMaximum: true
              minimum: 1
              default: 10
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/Table'
            title: >-
              Response Db Table Upstreams Api V1 Explore Db  Data Connection Id 
              Tables  Table Path  Upstreams Get
        examples:
          example:
            value:
              - columns:
                  - name: <string>
                name: <string>
                path:
                  - <string>
                type: Table
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    title: Detail
                    type: array
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
    ColumnReference:
      description: Database table column reference.
      properties:
        name:
          title: Column name
          type: string
      required:
        - name
      title: ColumnReference
      type: object
    Table:
      description: Database table.
      properties:
        columns:
          items:
            $ref: '#/components/schemas/ColumnReference'
          title: Columns
          type: array
        name:
          title: Name
          type: string
        path:
          items:
            type: string
          title: Table path
          type: array
        type:
          const: Table
          default: Table
          title: Type
          type: string
      required:
        - name
        - columns
        - path
      title: Table
      type: object
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          title: Location
          type: array
        msg:
          title: Message
          type: string
        type:
          title: Error Type
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
      type: object

````