# Source: https://docs.fireworks.ai/api-reference/rerank-documents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Rerank documents

> Rerank documents for a query using relevance scoring



## OpenAPI

````yaml post /rerank
openapi: 3.0.0
info:
  title: Fireworks REST API
  description: REST API for performing inference on Fireworks large language models (LLMs).
  version: 0.0.1
servers:
  - url: https://api.fireworks.ai/inference/v1/
security:
  - BearerAuth: []
paths:
  /rerank:
    post:
      summary: Rerank documents
      description: Rerank documents for a query using relevance scoring
      operationId: createRerank
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateRerankRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateRerankResponse'
components:
  schemas:
    CreateRerankRequest:
      type: object
      additionalProperties: false
      properties:
        model:
          type: string
          description: The name of the reranker model to use.
          example: accounts/fireworks/models/qwen3-reranker-8b
          nullable: true
        query:
          type: string
          description: The search query to use for reranking documents.
          example: What is machine learning?
        documents:
          type: array
          description: A list of documents to rerank. Each document is a string.
          minItems: 1
          items:
            type: string
          example:
            - Machine learning is a subset of AI.
            - The weather is sunny today.
        top_n:
          type: integer
          description: >-
            The number of most relevant documents to return. If not specified,
            all documents are returned.
          nullable: true
          minimum: 1
        return_documents:
          type: boolean
          description: >-
            Whether to return the document text in the response. Defaults to
            true.
          default: true
        task:
          type: string
          description: Optional task description to guide the reranking process.
          nullable: true
          example: >-
            Given a web search query, retrieve relevant passages that answer the
            query
      required:
        - query
        - documents
    CreateRerankResponse:
      type: object
      properties:
        object:
          type: string
          description: The object type, which is always "list".
          enum:
            - list
        model:
          type: string
          description: The name of the model used for reranking.
        data:
          type: array
          description: >-
            The list of reranked documents, ordered by relevance score (highest
            first).
          items:
            $ref: '#/components/schemas/RerankResult'
        usage:
          type: object
          description: The usage information for the request.
          properties:
            prompt_tokens:
              type: integer
              description: The number of tokens used by the prompt.
            total_tokens:
              type: integer
              description: The total number of tokens used by the request.
          required:
            - prompt_tokens
            - total_tokens
      required:
        - object
        - model
        - data
        - usage
    RerankResult:
      type: object
      description: Represents a reranked document result.
      properties:
        index:
          type: integer
          description: The original index of the document in the input array.
        relevance_score:
          type: number
          description: >-
            The relevance score between 0 and 1, with higher scores indicating
            greater relevance.
          format: float
          minimum: 0
          maximum: 1
        document:
          type: string
          description: The document text. Only included if return_documents is true.
          nullable: true
      required:
        - index
        - relevance_score
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````