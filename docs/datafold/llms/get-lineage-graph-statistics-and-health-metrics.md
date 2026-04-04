# Source: https://docs.datafold.com/api-reference/lineagev2/get-lineage-graph-statistics-and-health-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get lineage graph statistics and health metrics

> Get overall statistics about the lineage graph.

Returns counts of all major entities in the lineage graph including datasets,
columns, relationships, queries, and source files. Useful for understanding
the scope and health of the lineage data.

Use this to get a quick overview before exploring specific lineage paths.



## OpenAPI

````yaml openapi-public.json get /api/v1/lineagev2/stats
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
  /api/v1/lineagev2/stats:
    get:
      tags:
        - lineagev2
      summary: Get lineage graph statistics and health metrics
      description: >-
        Get overall statistics about the lineage graph.


        Returns counts of all major entities in the lineage graph including
        datasets,

        columns, relationships, queries, and source files. Useful for
        understanding

        the scope and health of the lineage data.


        Use this to get a quick overview before exploring specific lineage
        paths.
      operationId: lineagev2_stats
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