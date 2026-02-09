# Source: https://docs.datafold.com/api-reference/lineagev2/get-stats.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Stats

> Get graph statistics.

Returns:
    StatsResponse containing:
    - datasets: Total number of tables and views in the graph
    - columns: Total number of columns tracked
    - relationships: Total number of lineage edges (DEPENDS_ON + DERIVED_FROM)
    - queries: Total number of SELECT queries analyzed
    - sourceFiles: Total number of source SQL/dbt files processed

Example response:
    {
        "datasets": 1250,
        "columns": 15680,
        "relationships": 8932,
        "queries": 4521,
        "sourceFiles": 892
    }

Use this to assess lineage coverage and data quality.



## OpenAPI

````yaml openapi-public.json get /api/internal/lineagev2/stats
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
  /api/internal/lineagev2/stats:
    get:
      tags:
        - lineagev2
      summary: Get Stats
      description: |-
        Get graph statistics.

        Returns:
            StatsResponse containing:
            - datasets: Total number of tables and views in the graph
            - columns: Total number of columns tracked
            - relationships: Total number of lineage edges (DEPENDS_ON + DERIVED_FROM)
            - queries: Total number of SELECT queries analyzed
            - sourceFiles: Total number of source SQL/dbt files processed

        Example response:
            {
                "datasets": 1250,
                "columns": 15680,
                "relationships": 8932,
                "queries": 4521,
                "sourceFiles": 892
            }

        Use this to assess lineage coverage and data quality.
      operationId: get_stats_api_internal_lineagev2_stats_get
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StatsResponse'
          description: Successful Response
components:
  schemas:
    StatsResponse:
      properties:
        columns:
          title: Columns
          type: integer
        datasets:
          title: Datasets
          type: integer
        queries:
          title: Queries
          type: integer
        relationships:
          title: Relationships
          type: integer
        sourceFiles:
          title: Sourcefiles
          type: integer
      required:
        - datasets
        - columns
        - relationships
        - queries
        - sourceFiles
      title: StatsResponse
      type: object
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````