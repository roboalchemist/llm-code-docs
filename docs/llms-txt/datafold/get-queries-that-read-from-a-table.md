# Source: https://docs.datafold.com/api-reference/lineagev2/get-queries-that-read-from-a-table.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get queries that read from a table

> Returns queries that read from this table, ordered by execution count.



## OpenAPI

````yaml openapi-public.json get /api/v1/lineagev2/table/{table_id}/queries
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
  /api/v1/lineagev2/table/{table_id}/queries:
    get:
      tags:
        - lineagev2
      summary: Get queries that read from a table
      description: Returns queries that read from this table, ordered by execution count.
      operationId: lineagev2_table_queries
      parameters:
        - in: path
          name: table_id
          required: true
          schema:
            title: Table Id
            type: string
        - in: query
          name: limit
          required: false
          schema:
            default: 20
            title: Limit
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueriesResponse'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    QueriesResponse:
      properties:
        queries:
          items:
            $ref: '#/components/schemas/QueryInfo'
          title: Queries
          type: array
      required:
        - queries
      title: QueriesResponse
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