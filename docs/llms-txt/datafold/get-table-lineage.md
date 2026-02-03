# Source: https://docs.datafold.com/api-reference/lineagev2/get-table-lineage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Table Lineage

> Get upstream/downstream table lineage.

Args:
    table_id: Full table identifier (format: database.schema.table or similar path)
    direction: Lineage direction - "upstream", "downstream", or "both" (default: "both")
    depth: Maximum traversal depth (default: configured system depth, typically 3-5 hops)

Returns:
    TableLineageResponse containing:
    - dataset: The requested table/view with metadata
    - upstream: List of source tables this dataset depends on
    - downstream: List of dependent tables that use this dataset
    - edges: Dependency relationships between all returned datasets

Example:
    - Get full lineage: table_id="analytics.fact_orders", direction="both"
    - Get only sources: table_id="analytics.fact_orders", direction="upstream", depth=2
    - Get only consumers: table_id="raw.customers", direction="downstream"

Note: depth parameter is interpolated into Cypher query using f-string because
Cypher does not support parameterized variable-length path patterns (*1..{depth}).
Input is validated as int by FastAPI.



## OpenAPI

````yaml openapi-public.json get /api/internal/lineagev2/table-lineage/{table_id}
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
  /api/internal/lineagev2/table-lineage/{table_id}:
    get:
      tags:
        - lineagev2
      summary: Get Table Lineage
      description: >-
        Get upstream/downstream table lineage.


        Args:
            table_id: Full table identifier (format: database.schema.table or similar path)
            direction: Lineage direction - "upstream", "downstream", or "both" (default: "both")
            depth: Maximum traversal depth (default: configured system depth, typically 3-5 hops)

        Returns:
            TableLineageResponse containing:
            - dataset: The requested table/view with metadata
            - upstream: List of source tables this dataset depends on
            - downstream: List of dependent tables that use this dataset
            - edges: Dependency relationships between all returned datasets

        Example:
            - Get full lineage: table_id="analytics.fact_orders", direction="both"
            - Get only sources: table_id="analytics.fact_orders", direction="upstream", depth=2
            - Get only consumers: table_id="raw.customers", direction="downstream"

        Note: depth parameter is interpolated into Cypher query using f-string
        because

        Cypher does not support parameterized variable-length path patterns
        (*1..{depth}).

        Input is validated as int by FastAPI.
      operationId: get_table_lineage_api_internal_lineagev2_table_lineage__table_id__get
      parameters:
        - in: path
          name: table_id
          required: true
          schema:
            title: Table Id
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
                $ref: '#/components/schemas/TableLineageResponse'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    TableLineageResponse:
      properties:
        dataset:
          $ref: '#/components/schemas/DatasetNode'
        downstream:
          items:
            $ref: '#/components/schemas/DatasetNode'
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
            $ref: '#/components/schemas/DatasetNode'
          title: Upstream
          type: array
      required:
        - dataset
        - upstream
        - downstream
        - edges
      title: TableLineageResponse
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
    DatasetNode:
      properties:
        assetType:
          title: Assettype
          type: string
        columnCount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Columncount
        dashboard:
          anyOf:
            - type: string
            - type: 'null'
          title: Dashboard
        definitionSql:
          anyOf:
            - type: string
            - type: 'null'
          title: Definitionsql
        depth:
          default: 0
          title: Depth
          type: integer
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
        page:
          anyOf:
            - type: string
            - type: 'null'
          title: Page
        popularity:
          default: 0
          title: Popularity
          type: number
        report:
          anyOf:
            - type: string
            - type: 'null'
          title: Report
        rowCount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Rowcount
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
        totalQueries30d:
          anyOf:
            - type: integer
            - type: 'null'
          title: Totalqueries30D
        visualType:
          anyOf:
            - type: string
            - type: 'null'
          title: Visualtype
        workspace:
          anyOf:
            - type: string
            - type: 'null'
          title: Workspace
      required:
        - id
        - name
        - assetType
      title: DatasetNode
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