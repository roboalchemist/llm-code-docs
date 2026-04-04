# Source: https://io.net/docs/reference/rag/graphs/communities/build-graph-communities.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new community

> Creates communities in the graph by analyzing entity relationships and similarities.

Creates communities in the graph by analyzing entity relationships and similarities.

Communities are created through the following process:

1. Analyzes entity relationships and metadata to build a similarity graph
2. Applies advanced community detection algorithms (e.g. Leiden) to identify densely connected groups
3. Creates hierarchical community structure with multiple granularity levels
4. Generates natural language summaries and statistical insights for each community

The resulting communities can be used to:

* Understand high-level graph structure and organization
* Identify key entity groupings and their relationships
* Navigate and explore the graph at different levels of detail
* Generate insights about entity clusters and their characteristics

The community detection process is configurable through settings like:

* Community detection algorithm parameters
* Summary generation prompt


## OpenAPI

````yaml openapi/rag-graphs-communities/build-graph-communities.json post /api/r2r/v3/graphs/{collection_id}/communities/build
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/graphs/{collection_id}/communities/build:
    post:
      summary: Create a new community
      description: >-
        Creates communities in the graph by analyzing entity relationships and
        similarities.
      operationId: build-graph-communities
      parameters:
        - name: collection_id
          in: path
          description: ID of the collection
          schema:
            type: string
          required: true
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      message: message
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      message:
                        type: string
                        example: message
        '404':
          description: '404'
          content:
            application/json:
              examples:
                Result:
                  value: {}
              schema:
                type: object
                properties: {}
        '422':
          description: '422'
          content:
            text/plain:
              examples:
                Result:
                  value: ''
      deprecated: false
components:
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````