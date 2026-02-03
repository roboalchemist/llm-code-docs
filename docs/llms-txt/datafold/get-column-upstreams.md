# Source: https://docs.datafold.com/api-reference/explore/get-column-upstreams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get column upstreams

> Retrieve a list of columns or tables which the given column depends on.



## OpenAPI

````yaml openapi-public.json get /api/v1/explore/db/{data_connection_id}/columns/{column_path}/upstreams
openapi: 3.1.0
info:
  contact:
    email: support@datafold.com
    name: API Support
  description: >-
    The Datafold API reference is a guide to our available endpoints and
    authentication methods.

    If you're just getting started with Datafold, we recommend first checking
    out our [documentation](https://docs.datafold.com).


    :::info
      To use the Datafold API, you should first create a Datafold API Key,
      which should be stored as a local environment variable named DATAFOLD_API_KEY.
      This can be set in your Datafold Cloud's Settings under the Account page.
    :::
  title: Datafold API
  version: latest
servers:
  - description: Default server
    url: https://app.datafold.com
security:
  - ApiKeyAuth: []
paths:
  /api/v1/explore/db/{data_connection_id}/columns/{column_path}/upstreams:
    get:
      tags:
        - Explore
      summary: Get column upstreams
      description: Retrieve a list of columns or tables which the given column depends on.
      operationId: >-
        db_column_upstreams_api_v1_explore_db__data_connection_id__columns__column_path__upstreams_get
      parameters:
        - description: >-
            Unique ID for the Data Connection. Can be found in the Datafold app
            under Settings > Integrations > Data Connections.
          in: path
          name: data_connection_id
          required: true
          schema:
            description: >-
              Unique ID for the Data Connection. Can be found in the Datafold
              app under Settings > Integrations > Data Connections.
            minimum: 1
            title: Data Connection ID
            type: integer
        - description: >-
            Path to the column, e.g. `db.schema.table.column`. The path is case
            sensitive. If components of the path contain periods, they must be
            quoted: `db.my_schema."www.mysite.com visits"."visit.id"`.
          in: path
          name: column_path
          required: true
          schema:
            description: >-
              Path to the column, e.g. `db.schema.table.column`. The path is
              case sensitive. If components of the path contain periods, they
              must be quoted: `db.my_schema."www.mysite.com visits"."visit.id"`.
            title: Table Column Path
            type: string
        - description: Maximum depth of the lineage to retrieve.
          in: query
          name: max_depth
          required: false
          schema:
            default: 10
            description: Maximum depth of the lineage to retrieve.
            exclusiveMaximum: 100
            minimum: 1
            title: Max depth
            type: integer
        - description: Include Tables in the lineage calculation and in the output.
          in: query
          name: include_tabular_nodes
          required: false
          schema:
            default: true
            description: Include Tables in the lineage calculation and in the output.
            title: Include tabular nodes
            type: boolean
      responses:
        '200':
          content:
            application/json:
              schema:
                items:
                  anyOf:
                    - $ref: '#/components/schemas/Column'
                    - $ref: '#/components/schemas/Table'
                title: >-
                  Response Db Column Upstreams Api V1 Explore Db  Data
                  Connection Id  Columns  Column Path  Upstreams Get
                type: array
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    Column:
      description: Database table column.
      properties:
        name:
          title: Name
          type: string
        table:
          $ref: '#/components/schemas/datafold__lineage__api__db__TableReference'
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
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          title: Detail
          type: array
      title: HTTPValidationError
      type: object
    datafold__lineage__api__db__TableReference:
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
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````