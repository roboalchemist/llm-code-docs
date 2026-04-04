# Source: https://docs.datafold.com/api-reference/lineagev2/get-dataset-column-lineage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Dataset Column Lineage

> Get column-level lineage for a dataset.



## OpenAPI

````yaml openapi-public.json get /api/internal/lineagev2/dataset-column-lineage/{dataset_id}
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
  /api/internal/lineagev2/dataset-column-lineage/{dataset_id}:
    get:
      tags:
        - lineagev2
      summary: Get Dataset Column Lineage
      description: Get column-level lineage for a dataset.
      operationId: >-
        get_dataset_column_lineage_api_internal_lineagev2_dataset_column_lineage__dataset_id__get
      parameters:
        - in: path
          name: dataset_id
          required: true
          schema:
            title: Dataset Id
            type: string
        - in: query
          name: direction
          required: false
          schema:
            default: upstream
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
                $ref: '#/components/schemas/DatasetColumnLineageResponse'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    DatasetColumnLineageResponse:
      properties:
        columns:
          items:
            $ref: '#/components/schemas/ColumnNodeExtended'
          title: Columns
          type: array
        dataset:
          $ref: '#/components/schemas/DatasetInfo'
        downstream:
          items:
            $ref: '#/components/schemas/ColumnNodeExtended'
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
            $ref: '#/components/schemas/ColumnNodeExtended'
          title: Upstream
          type: array
      required:
        - dataset
        - columns
        - upstream
        - downstream
        - edges
      title: DatasetColumnLineageResponse
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
    ColumnNodeExtended:
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
        isSelected:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Isselected
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
      title: ColumnNodeExtended
      type: object
    DatasetInfo:
      properties:
        assetType:
          title: Assettype
          type: string
        id:
          title: Id
          type: string
        name:
          title: Name
          type: string
      required:
        - id
        - name
        - assetType
      title: DatasetInfo
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