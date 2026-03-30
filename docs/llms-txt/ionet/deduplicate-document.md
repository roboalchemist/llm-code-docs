# Source: https://io.net/docs/reference/rag/documents/deduplicate-document.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deduplicate entities

> Deduplicates entities from a document.



## OpenAPI

````yaml openapi/rag-documents/deduplicate-document.json post /api/r2r/v3/documents/{id}/deduplicate
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/documents/{id}/deduplicate:
    post:
      summary: Deduplicate entities
      description: Deduplicates entities from a document.
      operationId: deduplicate-document
      parameters:
        - name: id
          in: path
          description: Document ID
          schema:
            type: string
          required: true
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                settings:
                  type: object
                  description: >-
                    Settings for the entities and relationships extraction
                    process.
                  properties:
                    graph_extraction_prompt:
                      type: string
                      description: The prompt to use for knowledge graph extraction.
                      default: graph_extraction
                    graph_entity_description_prompt:
                      type: string
                      description: The prompt to use for entity description generation.
                      default: graph_entity_description
                    entity_types:
                      type: string
                      description: The types of entities to extract.
                    relation_types:
                      type: string
                      description: The types of relations to extract.
                    chunk_merge_count:
                      type: integer
                      description: >-
                        The number of extractions to merge into a single graph
                        extraction.
                      default: 2
                      format: int32
                    max_knowledge_relationships:
                      type: integer
                      description: >-
                        The maximum number of knowledge relationships to extract
                        from each chunk.
                      default: 100
                      format: int32
                    max_description_input_length:
                      type: integer
                      description: >-
                        The maximum length of the description for a node in the
                        graph.
                      default: 65536
                      format: int32
                    generation_config:
                      type: object
                      description: >-
                        Configuration for text generation during graph
                        enrichment.
                      properties: {}
                    automatic_deduplication:
                      type: boolean
                      description: Whether to automatically deduplicate entities.
                      default: false
                run_with_orchestration:
                  type: boolean
                  description: >-
                    Whether to run the entities and relationships extraction
                    process with orchestration.
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