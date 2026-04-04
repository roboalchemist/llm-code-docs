# Source: https://docs.together.ai/reference/embeddings-2.md

# Create Embedding

> Query an embedding model for a given string of text.



## OpenAPI

````yaml POST /embeddings
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
  /embeddings:
    post:
      tags:
        - Embeddings
      summary: Create embedding
      description: Query an embedding model for a given string of text.
      operationId: embeddings
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EmbeddingsRequest'
      responses:
        '200':
          description: '200'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EmbeddingsResponse'
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
    EmbeddingsRequest:
      type: object
      required:
        - model
        - input
      properties:
        model:
          type: string
          description: >
            The name of the embedding model to use.<br> <br> [See all of
            Together AI's embedding
            models](https://docs.together.ai/docs/serverless-models#embedding-models)
          example: togethercomputer/m2-bert-80M-8k-retrieval
          anyOf:
            - type: string
              enum:
                - WhereIsAI/UAE-Large-V1
                - BAAI/bge-large-en-v1.5
                - BAAI/bge-base-en-v1.5
                - togethercomputer/m2-bert-80M-8k-retrieval
            - type: string
        input:
          oneOf:
            - type: string
              description: A string providing the text for the model to embed.
              example: >-
                Our solar system orbits the Milky Way galaxy at about 515,000
                mph
            - type: array
              items:
                type: string
                description: A string providing the text for the model to embed.
                example: >-
                  Our solar system orbits the Milky Way galaxy at about 515,000
                  mph
          example: Our solar system orbits the Milky Way galaxy at about 515,000 mph
    EmbeddingsResponse:
      type: object
      required:
        - object
        - model
        - data
      properties:
        object:
          type: string
          enum:
            - list
        model:
          type: string
        data:
          type: array
          items:
            type: object
            required:
              - index
              - object
              - embedding
            properties:
              object:
                type: string
                enum:
                  - embedding
              embedding:
                type: array
                items:
                  type: number
              index:
                type: integer
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt