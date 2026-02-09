# Source: https://docs.datafold.com/api-reference/data-sources/execute-a-sql-query-against-a-data-source.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute a SQL query against a data source

> Executes a SQL query against the specified data source and returns the results.

This endpoint allows you to run ad-hoc SQL queries for data exploration, validation, or analysis.
The query is executed using the data source's native query runner with the appropriate credentials.

**Streaming mode**: Use query parameter `?stream=true` or set `X-Stream-Response: true` header.
Streaming is only supported for certain data sources (e.g., Databricks).
When streaming, results are sent incrementally as valid JSON for memory efficiency.

Returns:
- Query results as rows with column metadata (name, type, description)
- Limited to a reasonable number of rows for performance



## OpenAPI

````yaml openapi-public.json post /api/v1/data_sources/{data_source_id}/query
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
  /api/v1/data_sources/{data_source_id}/query:
    post:
      tags:
        - Data sources
      summary: Execute a SQL query against a data source
      description: >-
        Executes a SQL query against the specified data source and returns the
        results.


        This endpoint allows you to run ad-hoc SQL queries for data exploration,
        validation, or analysis.

        The query is executed using the data source's native query runner with
        the appropriate credentials.


        **Streaming mode**: Use query parameter `?stream=true` or set
        `X-Stream-Response: true` header.

        Streaming is only supported for certain data sources (e.g., Databricks).

        When streaming, results are sent incrementally as valid JSON for memory
        efficiency.


        Returns:

        - Query results as rows with column metadata (name, type, description)

        - Limited to a reasonable number of rows for performance
      operationId: run_query
      parameters:
        - in: path
          name: data_source_id
          required: true
          schema:
            title: Data source ID
            type: integer
        - description: Stream results as JSON
          in: query
          name: stream
          required: false
          schema:
            default: false
            description: Stream results as JSON
            title: Stream
            type: boolean
        - in: header
          name: X-Stream-Response
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: X-Stream-Response
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ApiQueryRequest'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiQueryResult'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    ApiQueryRequest:
      properties:
        params:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          description: Positional parameters for parameterized queries
          title: Params
        query:
          description: SQL query to execute
          title: Query
          type: string
      required:
        - query
      title: ApiQueryRequest
      type: object
    ApiQueryResult:
      properties:
        columns:
          anyOf:
            - items:
                $ref: '#/components/schemas/ApiQueryColumn'
              type: array
            - type: 'null'
          title: Columns
        rows:
          items:
            additionalProperties: true
            type: object
          title: Rows
          type: array
      required:
        - rows
      title: ApiQueryResult
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
    ApiQueryColumn:
      properties:
        db_type:
          anyOf:
            - type: string
            - type: 'null'
          title: Db Type
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
        is_nullable:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Nullable
        name:
          title: Name
          type: string
        number:
          anyOf:
            - type: integer
            - type: 'null'
          title: Number
        type:
          anyOf:
            - type: string
            - type: 'null'
          title: Type
      required:
        - name
      title: ApiQueryColumn
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