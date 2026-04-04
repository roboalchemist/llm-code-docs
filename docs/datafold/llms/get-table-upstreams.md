# Source: https://docs.datafold.com/api-reference/explore/get-table-upstreams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get table upstreams

> Retrieve a list of tables which the given table depends on.



## OpenAPI

````yaml openapi-public.json get /api/v1/explore/db/{data_connection_id}/tables/{table_path}/upstreams
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
  /api/v1/explore/db/{data_connection_id}/tables/{table_path}/upstreams:
    get:
      tags:
        - Explore
      summary: Get table upstreams
      description: Retrieve a list of tables which the given table depends on.
      operationId: >-
        db_table_upstreams_api_v1_explore_db__data_connection_id__tables__table_path__upstreams_get
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
            Path to the table, e.g. `db.schema.table`. The path is case
            sensitive. If components of the path contain periods, they must be
            quoted: `db."my.schema"."www.mysite.com visits"`.
          in: path
          name: table_path
          required: true
          schema:
            description: >-
              Path to the table, e.g. `db.schema.table`. The path is case
              sensitive. If components of the path contain periods, they must be
              quoted: `db."my.schema"."www.mysite.com visits"`.
            title: Table Path
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
      responses:
        '200':
          content:
            application/json:
              schema:
                items:
                  $ref: '#/components/schemas/Table'
                title: >-
                  Response Db Table Upstreams Api V1 Explore Db  Data Connection
                  Id  Tables  Table Path  Upstreams Get
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