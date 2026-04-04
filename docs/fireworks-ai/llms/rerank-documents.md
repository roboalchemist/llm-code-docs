# Source: https://docs.fireworks.ai/api-reference/rerank-documents.md

# Rerank documents

> Rerank documents for a query using relevance scoring

## OpenAPI

````yaml post /rerank
paths:
  path: /rerank
  method: post
  servers:
    - url: https://api.fireworks.ai/inference/v1/
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              model:
                allOf:
                  - type: string
                    description: The name of the reranker model to use.
                    example: accounts/fireworks/models/qwen3-reranker-8b
                    nullable: true
              query:
                allOf:
                  - type: string
                    description: The search query to use for reranking documents.
                    example: What is machine learning?
              documents:
                allOf:
                  - type: array
                    description: A list of documents to rerank. Each document is a string.
                    minItems: 1
                    items:
                      type: string
                    example:
                      - Machine learning is a subset of AI.
                      - The weather is sunny today.
              top_n:
                allOf:
                  - type: integer
                    description: >-
                      The number of most relevant documents to return. If not
                      specified, all documents are returned.
                    nullable: true
                    minimum: 1
              return_documents:
                allOf:
                  - type: boolean
                    description: >-
                      Whether to return the document text in the response.
                      Defaults to true.
                    default: true
              task:
                allOf:
                  - type: string
                    description: Optional task description to guide the reranking process.
                    nullable: true
                    example: >-
                      Given a web search query, retrieve relevant passages that
                      answer the query
            required: true
            refIdentifier: '#/components/schemas/CreateRerankRequest'
            requiredProperties:
              - query
              - documents
            additionalProperties: false
        examples:
          example:
            value:
              model: accounts/fireworks/models/qwen3-reranker-8b
              query: What is machine learning?
              documents:
                - Machine learning is a subset of AI.
                - The weather is sunny today.
              top_n: 2
              return_documents: true
              task: >-
                Given a web search query, retrieve relevant passages that answer
                the query
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              object:
                allOf:
                  - type: string
                    description: The object type, which is always "list".
                    enum:
                      - list
              model:
                allOf:
                  - type: string
                    description: The name of the model used for reranking.
              data:
                allOf:
                  - type: array
                    description: >-
                      The list of reranked documents, ordered by relevance score
                      (highest first).
                    items:
                      $ref: '#/components/schemas/RerankResult'
              usage:
                allOf:
                  - type: object
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
            refIdentifier: '#/components/schemas/CreateRerankResponse'
            requiredProperties:
              - object
              - model
              - data
              - usage
        examples:
          example:
            value:
              object: list
              model: <string>
              data:
                - index: 123
                  relevance_score: 0.5
                  document: <string>
              usage:
                prompt_tokens: 123
                total_tokens: 123
        description: OK
  deprecated: false
  type: path
components:
  schemas:
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

````