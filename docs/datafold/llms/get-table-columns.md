# Source: https://docs.datafold.com/api-reference/lineagev2/get-table-columns.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Table Columns

> Get all columns for a table.

Args:
    table_id: Full table identifier (format: database.schema.table or similar path)

Returns:
    TableColumnsResponse containing:
    - columns: List of all columns in the table with:
        - id: Unique column identifier
        - name: Column name
        - dataType: Column data type (if available)
        - totalQueries30d: Number of queries using this column in last 30 days
        - popularity: Relative popularity score (0-100) based on query usage

Example:
    - List table schema: table_id="analytics.fact_orders"
    - Returns all columns like order_id, customer_id, amount, created_at with their metadata

Use this to understand table structure and identify important columns before
exploring column-level lineage.



## OpenAPI

````yaml openapi-public.json get /api/internal/lineagev2/table/{table_id}/columns
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
  /api/internal/lineagev2/table/{table_id}/columns:
    get:
      tags:
        - lineagev2
      summary: Get Table Columns
      description: >-
        Get all columns for a table.


        Args:
            table_id: Full table identifier (format: database.schema.table or similar path)

        Returns:
            TableColumnsResponse containing:
            - columns: List of all columns in the table with:
                - id: Unique column identifier
                - name: Column name
                - dataType: Column data type (if available)
                - totalQueries30d: Number of queries using this column in last 30 days
                - popularity: Relative popularity score (0-100) based on query usage

        Example:
            - List table schema: table_id="analytics.fact_orders"
            - Returns all columns like order_id, customer_id, amount, created_at with their metadata

        Use this to understand table structure and identify important columns
        before

        exploring column-level lineage.
      operationId: get_table_columns_api_internal_lineagev2_table__table_id__columns_get
      parameters:
        - in: path
          name: table_id
          required: true
          schema:
            title: Table Id
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TableColumnsResponse'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    TableColumnsResponse:
      properties:
        columns:
          items:
            $ref: '#/components/schemas/ColumnInfo'
          title: Columns
          type: array
      required:
        - columns
      title: TableColumnsResponse
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
    ColumnInfo:
      properties:
        dataType:
          anyOf:
            - type: string
            - type: 'null'
          title: Datatype
        id:
          title: Id
          type: string
        name:
          title: Name
          type: string
        popularity:
          default: 0
          title: Popularity
          type: number
        totalQueries30d:
          anyOf:
            - type: integer
            - type: 'null'
          title: Totalqueries30D
      required:
        - id
        - name
      title: ColumnInfo
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