# Source: https://docs.datafold.com/api-reference/lineagev2/execute-custom-cypher-queries-against-the-lineage-graph.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Execute custom Cypher queries against the lineage graph

> Execute custom Cypher queries for advanced lineage analysis.

Allows running arbitrary Cypher queries against the Memgraph lineage database.
Returns results in both tabular format and graph format (nodes and edges).

WARNING: This is a power-user endpoint. All queries are logged for audit purposes.

Use this for custom analysis beyond the standard lineage endpoints, such as:
- Finding circular dependencies
- Complex multi-hop patterns
- Aggregation queries across lineage paths
- Custom graph algorithms



## OpenAPI

````yaml openapi-public.json post /api/v1/lineagev2/cypher
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
  /api/v1/lineagev2/cypher:
    post:
      tags:
        - lineagev2
      summary: Execute custom Cypher queries against the lineage graph
      description: >-
        Execute custom Cypher queries for advanced lineage analysis.


        Allows running arbitrary Cypher queries against the Memgraph lineage
        database.

        Returns results in both tabular format and graph format (nodes and
        edges).


        WARNING: This is a power-user endpoint. All queries are logged for audit
        purposes.


        Use this for custom analysis beyond the standard lineage endpoints, such
        as:

        - Finding circular dependencies

        - Complex multi-hop patterns

        - Aggregation queries across lineage paths

        - Custom graph algorithms
      operationId: lineagev2_run_cypher
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CypherRequest'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CypherResponse'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    CypherRequest:
      properties:
        query:
          title: Query
          type: string
      required:
        - query
      title: CypherRequest
      type: object
    CypherResponse:
      properties:
        columns:
          items:
            type: string
          title: Columns
          type: array
        edges:
          items:
            $ref: '#/components/schemas/CypherEdge'
          title: Edges
          type: array
        nodes:
          items:
            $ref: '#/components/schemas/CypherNode'
          title: Nodes
          type: array
        results:
          items:
            additionalProperties: true
            type: object
          title: Results
          type: array
      required:
        - columns
        - results
        - nodes
        - edges
      title: CypherResponse
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
    CypherEdge:
      properties:
        id:
          title: Id
          type: string
        properties:
          additionalProperties: true
          title: Properties
          type: object
        source:
          title: Source
          type: string
        target:
          title: Target
          type: string
        type:
          title: Type
          type: string
      required:
        - id
        - source
        - target
        - type
        - properties
      title: CypherEdge
      type: object
    CypherNode:
      properties:
        id:
          title: Id
          type: string
        labels:
          items:
            type: string
          title: Labels
          type: array
        properties:
          additionalProperties: true
          title: Properties
          type: object
      required:
        - id
        - labels
        - properties
      title: CypherNode
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