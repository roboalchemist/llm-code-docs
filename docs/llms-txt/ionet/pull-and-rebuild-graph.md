# Source: https://io.net/docs/reference/rag/graphs/pull-and-rebuild-graph.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pull latest entities to the graph

> Adds documents to a graph by copying their entities and relationships.

This endpoint:

1. Copies document entities to the graphs\_entities table
2. Copies document relationships to the graphs\_relationships table
3. Associates the documents with the graph

When a document is added:

* Its entities and relationships are copied to graph-specific tables
* Existing entities/relationships are updated by merging their properties
* The document ID is recorded in the graph’s document\_ids array

Documents added to a graph will contribute their knowledge to:

* Graph analysis and querying
* Community detection
* Knowledge graph enrichment

The user must have access to both the graph and the documents being added.


## OpenAPI

````yaml openapi/rag-graphs/pull-and-rebuild-graph.json post /api/r2r/v3/graphs/{collection_id}/pull
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/graphs/{collection_id}/pull:
    post:
      summary: Pull latest entities to the graph
      description: Adds documents to a graph by copying their entities and relationships.
      operationId: pull-and-rebuild-graph
      parameters:
        - name: collection_id
          in: path
          description: ID of the collection to rebuild the graph for
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
                      success: true
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      success:
                        type: boolean
                        example: true
                        default: true
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