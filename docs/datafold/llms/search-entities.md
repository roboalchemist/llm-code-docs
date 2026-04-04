# Source: https://docs.datafold.com/api-reference/lineagev2/search-entities.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Search Entities

> Search for datasets and columns by name.

Args:
    q: Search query string (minimum 2 characters). Searches in dataset/column names and IDs.
    limit: Maximum number of results to return per type (default: 50)

Returns:
    SearchResponse containing:
    - datasets: List of matching tables/views with metadata (asset type, column count, row count, popularity)
    - columns: List of matching columns with table context and popularity

Example:
    - Search for tables: q="customer" returns all datasets with "customer" in the name
    - Search for columns: q="email" returns all columns with "email" in the name



## OpenAPI

````yaml openapi-public.json get /api/internal/lineagev2/search
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
  /api/internal/lineagev2/search:
    get:
      tags:
        - lineagev2
      summary: Search Entities
      description: |-
        Search for datasets and columns by name.

        Args:
            q: Search query string (minimum 2 characters). Searches in dataset/column names and IDs.
            limit: Maximum number of results to return per type (default: 50)

        Returns:
            SearchResponse containing:
            - datasets: List of matching tables/views with metadata (asset type, column count, row count, popularity)
            - columns: List of matching columns with table context and popularity

        Example:
            - Search for tables: q="customer" returns all datasets with "customer" in the name
            - Search for columns: q="email" returns all columns with "email" in the name
      operationId: search_entities_api_internal_lineagev2_search_get
      parameters:
        - in: query
          name: q
          required: true
          schema:
            title: Q
            type: string
        - in: query
          name: limit
          required: false
          schema:
            default: 50
            title: Limit
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SearchResponse'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    SearchResponse:
      properties:
        columns:
          items:
            $ref: '#/components/schemas/ColumnSearchResult'
          title: Columns
          type: array
        datasets:
          items:
            $ref: '#/components/schemas/DatasetSearchResult'
          title: Datasets
          type: array
      required:
        - datasets
        - columns
      title: SearchResponse
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
    ColumnSearchResult:
      properties:
        id:
          title: Id
          type: string
        isSource:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Issource
        name:
          title: Name
          type: string
        popularity:
          default: 0
          title: Popularity
          type: number
        tableId:
          title: Tableid
          type: string
        tableName:
          title: Tablename
          type: string
        totalQueries30d:
          anyOf:
            - type: integer
            - type: 'null'
          title: Totalqueries30D
      required:
        - id
        - name
        - tableId
        - tableName
      title: ColumnSearchResult
      type: object
    DatasetSearchResult:
      properties:
        assetType:
          title: Assettype
          type: string
        columnCount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Columncount
        definitionSql:
          anyOf:
            - type: string
            - type: 'null'
          title: Definitionsql
        id:
          title: Id
          type: string
        isSource:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Issource
        name:
          title: Name
          type: string
        popularity:
          default: 0
          title: Popularity
          type: number
        rowCount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Rowcount
        statementType:
          anyOf:
            - type: string
            - type: 'null'
          title: Statementtype
        totalQueries30d:
          anyOf:
            - type: integer
            - type: 'null'
          title: Totalqueries30D
      required:
        - id
        - name
        - assetType
      title: DatasetSearchResult
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