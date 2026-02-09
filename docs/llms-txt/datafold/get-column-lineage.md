# Source: https://docs.datafold.com/api-reference/lineagev2/get-column-lineage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Column Lineage

> Get column-level lineage.

Args:
    column_id: Full column identifier (format: database.schema.table.column or similar path)
    direction: Lineage direction - "upstream", "downstream", or "both" (default: "both")
    depth: Maximum traversal depth (default: configured system depth, typically 3-5 hops)

Returns:
    ColumnLineageResponse containing:
    - column: The requested column with table context and metadata
    - upstream: List of source columns this column derives from
    - downstream: List of dependent columns derived from this column
    - edges: DERIVED_FROM relationships between all returned columns

Example:
    - Get full column lineage: column_id="analytics.fact_orders.customer_id", direction="both"
    - Trace column origin: column_id="analytics.dim_customer.email", direction="upstream"
    - Find column usage: column_id="raw.users.user_id", direction="downstream", depth=3

Note: depth parameter is interpolated into Cypher query using f-string because
Cypher does not support parameterized variable-length path patterns (*1..{depth}).
Input is validated as int by FastAPI.



## OpenAPI

````yaml openapi-public.json get /api/internal/lineagev2/column-lineage/{column_id}
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
  /api/internal/lineagev2/column-lineage/{column_id}:
    get:
      tags:
        - lineagev2
      summary: Get Column Lineage
      description: >-
        Get column-level lineage.


        Args:
            column_id: Full column identifier (format: database.schema.table.column or similar path)
            direction: Lineage direction - "upstream", "downstream", or "both" (default: "both")
            depth: Maximum traversal depth (default: configured system depth, typically 3-5 hops)

        Returns:
            ColumnLineageResponse containing:
            - column: The requested column with table context and metadata
            - upstream: List of source columns this column derives from
            - downstream: List of dependent columns derived from this column
            - edges: DERIVED_FROM relationships between all returned columns

        Example:
            - Get full column lineage: column_id="analytics.fact_orders.customer_id", direction="both"
            - Trace column origin: column_id="analytics.dim_customer.email", direction="upstream"
            - Find column usage: column_id="raw.users.user_id", direction="downstream", depth=3

        Note: depth parameter is interpolated into Cypher query using f-string
        because

        Cypher does not support parameterized variable-length path patterns
        (*1..{depth}).

        Input is validated as int by FastAPI.
      operationId: get_column_lineage_api_internal_lineagev2_column_lineage__column_id__get
      parameters:
        - in: path
          name: column_id
          required: true
          schema:
            title: Column Id
            type: string
        - in: query
          name: direction
          required: false
          schema:
            default: both
            title: Direction
            type: string
        - in: query
          name: depth
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            title: Depth
        - in: query
          name: debug
          required: false
          schema:
            default: false
            title: Debug
            type: boolean
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ColumnLineageResponse'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    ColumnLineageResponse:
      properties:
        column:
          $ref: '#/components/schemas/ColumnNode'
        downstream:
          items:
            $ref: '#/components/schemas/ColumnNode'
          title: Downstream
          type: array
        edges:
          items:
            $ref: '#/components/schemas/LineageEdge'
          title: Edges
          type: array
        queries:
          default: []
          items:
            $ref: '#/components/schemas/CypherQueryInfo'
          title: Queries
          type: array
        upstream:
          items:
            $ref: '#/components/schemas/ColumnNode'
          title: Upstream
          type: array
      required:
        - column
        - upstream
        - downstream
        - edges
      title: ColumnLineageResponse
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
    ColumnNode:
      properties:
        assetType:
          title: Assettype
          type: string
        definitionSql:
          anyOf:
            - type: string
            - type: 'null'
          title: Definitionsql
        depth:
          default: 0
          title: Depth
          type: integer
        expression:
          anyOf:
            - type: string
            - type: 'null'
          title: Expression
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
        semanticModel:
          anyOf:
            - type: string
            - type: 'null'
          title: Semanticmodel
        statementType:
          anyOf:
            - type: string
            - type: 'null'
          title: Statementtype
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
        transformType:
          anyOf:
            - type: string
            - type: 'null'
          title: Transformtype
        workspace:
          anyOf:
            - type: string
            - type: 'null'
          title: Workspace
      required:
        - id
        - name
        - tableId
        - tableName
        - assetType
      title: ColumnNode
      type: object
    LineageEdge:
      properties:
        source:
          title: Source
          type: string
        target:
          title: Target
          type: string
      required:
        - source
        - target
      title: LineageEdge
      type: object
    CypherQueryInfo:
      properties:
        name:
          title: Name
          type: string
        params:
          additionalProperties: true
          title: Params
          type: object
        query:
          title: Query
          type: string
      required:
        - name
        - query
        - params
      title: CypherQueryInfo
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