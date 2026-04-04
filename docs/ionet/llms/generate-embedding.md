# Source: https://io.net/docs/reference/rag/retrieval/generate-embedding.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Embeddings

> The R2R Embedding endpoint generates vector embeddings from text using a specified model. It supports single or batch input, returning semantic vectors for use in search, clustering, and RAG applications.

The **Embedding** endpoint generates **vector embeddings** for the provided text using a specified model.

Embeddings are dense numerical representations of text that capture semantic meaning, enabling downstream applications such as **semantic search**, **clustering**, **classification**, and **RAG (Retrieval-Augmented Generation)** operations.

This endpoint provides a simple and efficient way to convert text into machine-readable vector form for use within R2R’s retrieval and analysis systems.

### Use Cases

Embeddings generated via this endpoint can be used for:

* **Semantic search** — Compare embedding vectors to find related content.
* **Clustering and classification** — Group similar documents or classify them by meaning.
* **Knowledge graph enhancement** — Connect semantically related entities.
* **RAG workflows** — Retrieve relevant content before passing context to language models.


## OpenAPI

````yaml openapi/rag-retrieval/generate-embedding.json post /api/r2r/v3/retrieval/embedding
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/retrieval/embedding:
    post:
      tags:
        - R2R-compatible API
        - R2R-compatible API
      summary: Reverse Proxy Auth
      operationId: reverse_proxy_auth_r2r_v3_retrieval_embedding_post
      parameters:
        - name: token
          in: header
          required: false
          schema:
            type: string
            description: JWT token
            title: Token
          description: JWT token
        - name: Authorization
          in: header
          required: false
          schema:
            type: string
            description: io.net provided API Key
            title: Authorization
          description: io.net provided API Key
        - name: x-api-key
          in: header
          required: false
          schema:
            type: string
            description: API key set by an SDK client
            title: X-Api-Key
          description: API key set by an SDK client
      requestBody:
        required: true
        description: Raw JSON body for the embedding request. Example inputs shown below.
        content:
          application/json:
            schema:
              type: object
              additionalProperties: true
              example:
                model: text-embedding-3-large
                input: hello world
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '404':
          description: Not found
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````