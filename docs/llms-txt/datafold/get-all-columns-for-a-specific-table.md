# Source: https://docs.datafold.com/api-reference/lineagev2/get-all-columns-for-a-specific-table.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all columns for a specific table

> List all columns in a dataset with metadata.

Returns the complete schema of a table/view including column names, data types,
usage statistics, and popularity scores. Useful for exploring table structure
before diving into column-level lineage.



## OpenAPI

````yaml openapi-public.json get /api/v1/lineagev2/table/{table_id}/columns
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
  /api/v1/lineagev2/table/{table_id}/columns:
    get:
      tags:
        - lineagev2
      summary: Get all columns for a specific table
      description: >-
        List all columns in a dataset with metadata.


        Returns the complete schema of a table/view including column names, data
        types,

        usage statistics, and popularity scores. Useful for exploring table
        structure

        before diving into column-level lineage.
      operationId: lineagev2_table_columns
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