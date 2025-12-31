# Source: https://docs.datafold.com/api-reference/explore/get-column-upstreams.md

# Get column upstreams

> Retrieve a list of columns or tables which the given column depends on.

## OpenAPI

````yaml openapi-public.json get /api/v1/explore/db/{data_connection_id}/columns/{column_path}/upstreams
paths:
  path: /api/v1/explore/db/{data_connection_id}/columns/{column_path}/upstreams
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
        column_path:
          schema:
            - type: string
              required: true
              title: Table Column Path
              description: >-
                Path to the column, e.g. `db.schema.table.column`. The path is
                case sensitive. If components of the path contain periods, they
                must be quoted: `db.my_schema."www.mysite.com
                visits"."visit.id"`.
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
        include_tabular_nodes:
          schema:
            - type: boolean
              required: false
              title: Include tabular nodes
              description: Include Tables in the lineage calculation and in the output.
              default: true
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
                - anyOf:
                    - $ref: '#/components/schemas/Column'
                    - $ref: '#/components/schemas/Table'
            title: >-
              Response Db Column Upstreams Api V1 Explore Db  Data Connection
              Id  Columns  Column Path  Upstreams Get
        examples:
          example:
            value:
              - name: <string>
                table:
                  name: <string>
                  path:
                    - <string>
                type: Column
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
    Column:
      description: Database table column.
      properties:
        name:
          title: Name
          type: string
        table:
          $ref: '#/components/schemas/TableReference'
        type:
          const: Column
          default: Column
          title: Type
          type: string
      required:
        - name
        - table
      title: Column
      type: object
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
    TableReference:
      description: Database table reference.
      properties:
        name:
          title: Table name
          type: string
        path:
          items:
            type: string
          title: Table path
          type: array
      required:
        - name
        - path
      title: TableReference
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