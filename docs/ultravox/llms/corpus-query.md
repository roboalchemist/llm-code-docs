# Source: https://docs.ultravox.ai/api-reference/corpora/corpus-query.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Corpus

> Queries the specified corpus and returns the specified number of results

<Warning>
  <b>Use the queryCorpus Tool</b>

  <br />

  Any agents that you deploy should use the <a href="/tools/built-in-tools#querycorpus">built-in queryCorpus tool</a>.

  <br />

  This endpoint should be use for testing.
</Warning>


## OpenAPI

````yaml post /api/corpora/{corpus_id}/query
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/corpora/{corpus_id}/query:
    post:
      tags:
        - corpora
      operationId: corpora_query
      parameters:
        - in: path
          name: corpus_id
          schema:
            type: string
            format: uuid
          required: true
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ultravox.v1.QueryCorpusRequest'
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/ultravox.v1.CorpusQueryResult'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    ultravox.v1.QueryCorpusRequest:
      type: object
      properties:
        query:
          type: string
          description: The query to run.
        maxResults:
          type: integer
          description: The maximum number of results to return.
          format: int32
      description: A request to query a corpus.
    ultravox.v1.CorpusQueryResult:
      type: object
      properties:
        content:
          type: string
          description: The content of the retrieved chunk.
        score:
          type: number
          description: >-
            The score of this chunk, with higher scores indicating better
            matches.
          format: double
        citation:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CorpusQueryResult_Citation'
          description: A citation for this chunk.
      description: A single result from a corpus query (corresponding to a chunk).
    ultravox.v1.CorpusQueryResult_Citation:
      type: object
      properties:
        sourceId:
          type: string
          description: >-
            The source that provided the document from which this chunk was
            retrieved.
        documentId:
          type: string
          description: The document from which this chunk was retrieved.
        publicUrl:
          type: string
          description: The public URL of the document, if any.
        title:
          type: string
          description: The title of the document, if known.
      description: A citation for a query result.
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````