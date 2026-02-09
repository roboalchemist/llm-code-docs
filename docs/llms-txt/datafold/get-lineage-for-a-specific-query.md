# Source: https://docs.datafold.com/api-reference/lineagev2/get-lineage-for-a-specific-query.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get lineage for a specific query

> Returns tables and columns used by a query with lineage relationships.



## OpenAPI

````yaml openapi-public.json get /api/v1/lineagev2/query/{fingerprint}/lineage
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
  /api/v1/lineagev2/query/{fingerprint}/lineage:
    get:
      tags:
        - lineagev2
      summary: Get lineage for a specific query
      description: Returns tables and columns used by a query with lineage relationships.
      operationId: lineagev2_query_lineage
      parameters:
        - in: path
          name: fingerprint
          required: true
          schema:
            title: Fingerprint
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueryLineageResponse'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    QueryLineageResponse:
      properties:
        columnLineage:
          items:
            additionalProperties:
              type: string
            type: object
          title: Columnlineage
          type: array
        outputColumns:
          items:
            additionalProperties:
              type: string
            type: object
          title: Outputcolumns
          type: array
        query:
          $ref: '#/components/schemas/QueryInfo'
        tablesRead:
          items:
            $ref: >-
              #/components/schemas/datafold__api__internal__lineagev2__api__TableReference
          title: Tablesread
          type: array
      required:
        - query
        - tablesRead
        - outputColumns
        - columnLineage
      title: QueryLineageResponse
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
    QueryInfo:
      properties:
        avgDurationMs:
          anyOf:
            - type: number
            - type: 'null'
          title: Avgdurationms
        executionCount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Executioncount
        fingerprint:
          title: Fingerprint
          type: string
        lastExecuted:
          anyOf:
            - type: string
            - type: 'null'
          title: Lastexecuted
        normalizedSql:
          anyOf:
            - type: string
            - type: 'null'
          title: Normalizedsql
        popularity:
          anyOf:
            - type: number
            - type: 'null'
          title: Popularity
        sqlPreview:
          anyOf:
            - type: string
            - type: 'null'
          title: Sqlpreview
        statementType:
          anyOf:
            - type: string
            - type: 'null'
          title: Statementtype
        uniqueUsers:
          anyOf:
            - type: integer
            - type: 'null'
          title: Uniqueusers
      required:
        - fingerprint
      title: QueryInfo
      type: object
    datafold__api__internal__lineagev2__api__TableReference:
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
        rowCount:
          anyOf:
            - type: integer
            - type: 'null'
          title: Rowcount
      required:
        - id
        - name
        - assetType
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
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````