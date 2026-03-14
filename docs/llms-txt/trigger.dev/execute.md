# Source: https://trigger.dev/docs/management/query/execute.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute a query

> Execute a TRQL (Trigger.dev Query Language) query against your run data. TRQL is a SQL-style query language that allows you to analyze runs, calculate metrics, and export data.

See the [Query documentation](/observability/query#example-queries) for comprehensive examples including:

* Failed runs analysis
* Task success rates over time
* Cost tracking and optimization
* Performance metrics and percentiles


## OpenAPI

````yaml v3-openapi POST /api/v1/query
openapi: 3.1.0
info:
  title: Trigger.dev v3 REST API
  description: >-
    The REST API lets you trigger and manage runs on Trigger.dev. You can
    trigger a run, get the status of a run, and get the results of a run. 
  version: 2024-04
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html
servers:
  - url: https://api.trigger.dev
    description: Trigger.dev API
security: []
paths:
  /api/v1/query:
    post:
      tags:
        - query
      summary: Execute a TRQL query
      description: >-
        Execute a TRQL (Trigger.dev Query Language) query against your run data.
        TRQL is a SQL-style query language that allows you to analyze runs,
        calculate metrics, and export data.
      operationId: execute_query_v1
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ExecuteQueryRequestBody'
      responses:
        '200':
          description: Query executed successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExecuteQueryResponse'
        '400':
          description: Invalid query or request parameters
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: Error message describing the query error
        '401':
          description: Unauthorized - API key is missing or invalid
        '500':
          description: Internal server error during query execution
      security:
        - secretKey: []
      x-codeSamples:
        - lang: typescript
          label: SDK - Basic query
          source: |-
            import { query } from "@trigger.dev/sdk";

            // Basic query with defaults (environment scope, json format)
            const result = await query.execute(
              "SELECT run_id, status FROM runs LIMIT 10"
            );
            console.log(result.results);
        - lang: typescript
          label: SDK - Type-safe query
          source: |-
            import { query, type QueryTable } from "@trigger.dev/sdk";

            // Type-safe query using QueryTable
            const result = await query.execute<
              QueryTable<"runs", "run_id" | "status" | "triggered_at">
            >(
              "SELECT run_id, status, triggered_at FROM runs LIMIT 10"
            );

            result.results.forEach(row => {
              console.log(row.run_id, row.status); // Fully typed!
            });
        - lang: typescript
          label: SDK - With options
          source: |-
            import { query } from "@trigger.dev/sdk";

            const result = await query.execute(
              "SELECT COUNT(*) as count FROM runs WHERE status = 'Failed'",
              {
                scope: "project",       // Query across all environments
                period: "7d",           // Last 7 days
                format: "json"
              }
            );
        - lang: typescript
          label: SDK - CSV export
          source: |-
            import { query } from "@trigger.dev/sdk";

            const csvResult = await query.execute(
              "SELECT run_id, status, triggered_at FROM runs",
              {
                format: "csv",
                period: "30d"
              }
            );

            // csvResult.results is a CSV string
            const lines = csvResult.results.split('\n');
        - lang: curl
          label: cURL - Basic query
          source: |-
            curl -X POST "https://api.trigger.dev/api/v1/query" \
              -H "Authorization: Bearer tr_dev_1234" \
              -H "Content-Type: application/json" \
              -d '{
                "query": "SELECT run_id, status FROM runs LIMIT 10",
                "scope": "environment",
                "period": "7d",
                "format": "json"
              }'
        - lang: curl
          label: cURL - Aggregation query
          source: |-
            curl -X POST "https://api.trigger.dev/api/v1/query" \
              -H "Authorization: Bearer tr_dev_1234" \
              -H "Content-Type: application/json" \
              -d '{
                "query": "SELECT task_identifier, count() as runs, countIf(status = '\''Failed'\'') as failures FROM runs GROUP BY task_identifier",
                "scope": "environment",
                "from": "2024-01-01T00:00:00Z",
                "to": "2024-01-31T23:59:59Z",
                "format": "json"
              }'
components:
  schemas:
    ExecuteQueryRequestBody:
      type: object
      required:
        - query
      properties:
        query:
          type: string
          description: The TRQL query to execute
          example: >-
            SELECT run_id, status, triggered_at FROM runs WHERE status =
            'Failed' LIMIT 10
        scope:
          type: string
          enum:
            - environment
            - project
            - organization
          default: environment
          description: >-
            The scope of data to query - environment (default), project, or
            organization
        period:
          type: string
          nullable: true
          description: >-
            Time period shorthand (e.g., "7d", "30d", "1h"). Cannot be used with
            from/to.
          example: 7d
        from:
          type: string
          format: date-time
          nullable: true
          description: Start of time range as ISO 8601 timestamp. Must be used with 'to'.
          example: '2024-01-01T00:00:00Z'
        to:
          type: string
          format: date-time
          nullable: true
          description: End of time range as ISO 8601 timestamp. Must be used with 'from'.
          example: '2024-01-31T23:59:59Z'
        format:
          type: string
          enum:
            - json
            - csv
          default: json
          description: >-
            Response format - "json" returns structured data (default), "csv"
            returns CSV string
    ExecuteQueryResponse:
      oneOf:
        - type: object
          description: JSON format response
          properties:
            format:
              type: string
              enum:
                - json
            results:
              type: array
              items:
                type: object
              description: Array of result rows
        - type: object
          description: CSV format response
          properties:
            format:
              type: string
              enum:
                - csv
            results:
              type: string
              description: CSV-formatted results
  securitySchemes:
    secretKey:
      type: http
      scheme: bearer
      description: >
        Use your project-specific Secret API key. Will start with `tr_dev_`,
        `tr_prod`, `tr_stg`, etc.


        You can find your Secret API key in the API Keys section of your
        Trigger.dev project dashboard.


        Our TypeScript SDK will default to using the value of the
        `TRIGGER_SECRET_KEY` environment variable if it is set. If you are using
        the SDK in a different environment, you can set the key using the
        `configure` function.


        ```typescript

        import { configure } from "@trigger.dev/sdk";


        configure({ accessToken: "tr_dev_1234" });

        ```

````

Built with [Mintlify](https://mintlify.com).