# Source: https://docs.together.ai/reference/rerank-1.md

# Create A Rerank Request

> Query a reranker model



## OpenAPI

````yaml POST /rerank
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /rerank:
    post:
      tags:
        - Rerank
      summary: Create a rerank request
      description: Query a reranker model
      operationId: rerank
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RerankRequest'
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RerankResponse'
        '400':
          description: BadRequest
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '404':
          description: NotFound
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '429':
          description: RateLimit
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '503':
          description: Overloaded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '504':
          description: Timeout
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
      deprecated: false
components:
  schemas:
    RerankRequest:
      type: object
      properties:
        model:
          type: string
          description: >
            The model to be used for the rerank request.<br> <br> [See all of
            Together AI's rerank
            models](https://docs.together.ai/docs/serverless-models#rerank-models)
          example: Salesforce/Llama-Rank-V1
          anyOf:
            - type: string
              enum:
                - Salesforce/Llama-Rank-v1
            - type: string
        query:
          type: string
          description: The search query to be used for ranking.
          example: What animals can I find near Peru?
        documents:
          description: List of documents, which can be either strings or objects.
          oneOf:
            - type: array
              items:
                type: object
                additionalProperties: true
            - type: array
              items:
                type: string
                example: >-
                  Our solar system orbits the Milky Way galaxy at about 515,000
                  mph
          example:
            - title: Llama
              text: >-
                The llama is a domesticated South American camelid, widely used
                as a meat and pack animal by Andean cultures since the
                pre-Columbian era.
            - title: Panda
              text: >-
                The giant panda (Ailuropoda melanoleuca), also known as the
                panda bear or simply panda, is a bear species endemic to China.
            - title: Guanaco
              text: >-
                The guanaco is a camelid native to South America, closely
                related to the llama. Guanacos are one of two wild South
                American camelids; the other species is the vicuña, which lives
                at higher elevations.
            - title: Wild Bactrian camel
              text: >-
                The wild Bactrian camel (Camelus ferus) is an endangered species
                of camel endemic to Northwest China and southwestern Mongolia.
        top_n:
          type: integer
          description: The number of top results to return.
          example: 2
        return_documents:
          type: boolean
          description: Whether to return supplied documents with the response.
          example: true
        rank_fields:
          type: array
          items:
            type: string
          description: >-
            List of keys in the JSON Object document to rank by. Defaults to use
            all supplied keys for ranking.
          example:
            - title
            - text
      required:
        - model
        - query
        - documents
      additionalProperties: false
    RerankResponse:
      type: object
      required:
        - object
        - model
        - results
      properties:
        object:
          type: string
          description: Object type
          enum:
            - rerank
          example: rerank
        id:
          type: string
          description: Request ID
          example: 9dfa1a09-5ebc-4a40-970f-586cb8f4ae47
        model:
          type: string
          description: The model to be used for the rerank request.
          example: salesforce/turboranker-0.8-3778-6328
        results:
          type: array
          items:
            type: object
            required:
              - index
              - relevance_score
              - document
            properties:
              index:
                type: integer
              relevance_score:
                type: number
              document:
                type: object
                properties:
                  text:
                    type: string
                    nullable: true
          example:
            - index: 0
              relevance_score: 0.29980177813003117
              document:
                text: >-
                  {"title":"Llama","text":"The llama is a domesticated South
                  American camelid, widely used as a meat and pack animal by
                  Andean cultures since the pre-Columbian era."}
            - index: 2
              relevance_score: 0.2752447527354349
              document:
                text: >-
                  {"title":"Guanaco","text":"The guanaco is a camelid native to
                  South America, closely related to the llama. Guanacos are one
                  of two wild South American camelids; the other species is the
                  vicuña, which lives at higher elevations."}
        usage:
          $ref: '#/components/schemas/UsageData'
          example:
            prompt_tokens: 1837
            completion_tokens: 0
            total_tokens: 1837
    ErrorData:
      type: object
      required:
        - error
      properties:
        error:
          type: object
          properties:
            message:
              type: string
              nullable: false
            type:
              type: string
              nullable: false
            param:
              type: string
              nullable: true
              default: null
            code:
              type: string
              nullable: true
              default: null
          required:
            - type
            - message
    UsageData:
      type: object
      properties:
        prompt_tokens:
          type: integer
        completion_tokens:
          type: integer
        total_tokens:
          type: integer
      required:
        - prompt_tokens
        - completion_tokens
        - total_tokens
      nullable: true
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt