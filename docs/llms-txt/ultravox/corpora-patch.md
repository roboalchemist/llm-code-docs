# Source: https://docs.ultravox.ai/api-reference/corpora/corpora-patch.md

# Update Corpus

> Updates the specified corpus

Allows partial modifications to the corpus.


## OpenAPI

````yaml patch /api/corpora/{corpus_id}
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/corpora/{corpus_id}:
    patch:
      tags:
        - corpora
      operationId: corpora_partial_update
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
              $ref: '#/components/schemas/ultravox.v1.Corpus'
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ultravox.v1.Corpus'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    ultravox.v1.Corpus:
      type: object
      properties:
        corpusId:
          type: string
          description: The unique ID of this corpus.
        created:
          type: string
          description: When this corpus was created.
          format: date-time
        name:
          type: string
          description: The name of this corpus.
        description:
          type: string
          description: A description of this corpus.
        stats:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.CorpusStats'
          description: The current stats for this corpus.
      description: >-
        A queryable collection of documents. A corpus can be used to ground
        Ultravox
         with factual content for a particular domain.
    ultravox.v1.CorpusStats:
      type: object
      properties:
        status:
          enum:
            - CORPUS_STATUS_UNSPECIFIED
            - CORPUS_STATUS_EMPTY
            - CORPUS_STATUS_INITIALIZING
            - CORPUS_STATUS_READY
            - CORPUS_STATUS_UPDATING
          type: string
          description: >-
            The current status of this corpus, indicating whether it is
            queryable.
          format: enum
        lastUpdated:
          type: string
          description: The last time the contents of this corpus were updated.
          format: date-time
        numChunks:
          type: integer
          description: >-
            The number of chunks in this corpus. Chunks are subsets of
            documents.
          format: int32
        numDocs:
          type: integer
          description: The number of documents in this corpus.
          format: int32
        numVectors:
          type: integer
          description: >-
            The number of vectors in this corpus. Vectors are used for semantic
            search.
             Multiple vectors may correspond to a single chunk.
          format: int32
      description: |-
        The current stats for a corpus. This gives an indication of whether the
         corpus is queryable and what sorts of results can be expected.
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt