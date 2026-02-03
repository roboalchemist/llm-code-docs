# Source: https://docs.datafold.com/api-reference/lineagev2/run-cypher.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Cypher

> Execute arbitrary Cypher query and return results.

Args:
    request: CypherRequest with query string

Returns:
    CypherResponse containing:
    - columns: List of column names returned by the query
    - results: List of result rows as dictionaries (tabular view)
    - nodes: All graph nodes returned by the query
    - edges: All graph edges/relationships returned by the query

Example queries:
    - Find all tables: "MATCH (t:Dataset) RETURN t.name LIMIT 10"
    - Find circular dependencies: "MATCH (t:Dataset)-[:DEPENDS_ON*]->(t) RETURN t"
    - Count by type: "MATCH (d:Dataset) RETURN d.asset_type, count(*) as count"
    - Complex lineage: "MATCH path=(c1:Column)-[:DERIVED_FROM*1..3]->(c2:Column) RETURN path"

WARNING: This endpoint executes arbitrary Cypher queries. It is intended for
internal debugging and power users only. All queries are logged for audit purposes.

Note: Results include both tabular data (for displaying in tables) and graph data
(nodes/edges for graph visualization).



## OpenAPI

````yaml openapi-public.json post /api/internal/lineagev2/cypher
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
  /api/internal/lineagev2/cypher:
    post:
      tags:
        - lineagev2
      summary: Run Cypher
      description: >-
        Execute arbitrary Cypher query and return results.


        Args:
            request: CypherRequest with query string

        Returns:
            CypherResponse containing:
            - columns: List of column names returned by the query
            - results: List of result rows as dictionaries (tabular view)
            - nodes: All graph nodes returned by the query
            - edges: All graph edges/relationships returned by the query

        Example queries:
            - Find all tables: "MATCH (t:Dataset) RETURN t.name LIMIT 10"
            - Find circular dependencies: "MATCH (t:Dataset)-[:DEPENDS_ON*]->(t) RETURN t"
            - Count by type: "MATCH (d:Dataset) RETURN d.asset_type, count(*) as count"
            - Complex lineage: "MATCH path=(c1:Column)-[:DERIVED_FROM*1..3]->(c2:Column) RETURN path"

        WARNING: This endpoint executes arbitrary Cypher queries. It is intended
        for

        internal debugging and power users only. All queries are logged for
        audit purposes.


        Note: Results include both tabular data (for displaying in tables) and
        graph data

        (nodes/edges for graph visualization).
      operationId: run_cypher_api_internal_lineagev2_cypher_post
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