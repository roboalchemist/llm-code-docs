# Source: https://docs.datafold.com/api-reference/lineagev2/get-queries.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Queries

> Get top queries by execution count.



## OpenAPI

````yaml openapi-public.json get /api/internal/lineagev2/queries
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
  /api/internal/lineagev2/queries:
    get:
      tags:
        - lineagev2
      summary: Get Queries
      description: Get top queries by execution count.
      operationId: get_queries_api_internal_lineagev2_queries_get
      parameters:
        - in: query
          name: limit
          required: false
          schema:
            default: 100
            title: Limit
            type: integer
        - in: query
          name: statement_type
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Statement Type
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