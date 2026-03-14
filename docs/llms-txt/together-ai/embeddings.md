# Source: https://docs.together.ai/reference/embeddings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Embedding

> Generate vector embeddings for one or more text inputs. Returns numerical arrays representing semantic meaning, useful for search, classification, and retrieval.



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
      description: >-
        Generate vector embeddings for one or more text inputs. Returns
        numerical arrays representing semantic meaning, useful for search,
        classification, and retrieval.
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
      x-codeSamples:
        - lang: Python
          label: Together AI SDK (v2)
          source: |
            # Docs for v1 can be found by changing the above selector ^
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            response = client.embeddings.create(
                model="BAAI/bge-large-en-v1.5",
                input="New York City",
            )

            print(response.data[0].embedding)
        - lang: Python
          label: Together AI SDK (v1)
          source: |
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            response = client.embeddings.create(
                model="BAAI/bge-large-en-v1.5",
                input="New York City",
            )

            print(response.data[0].embedding)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const response = await client.embeddings.create({
              model: "BAAI/bge-large-en-v1.5",
              input: "New York City",
            });

            console.log(response.data[0].embedding);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const response = await client.embeddings.create({
              model: "BAAI/bge-large-en-v1.5",
              input: "New York City",
            });

            console.log(response.data[0].embedding);
        - lang: Shell
          label: cURL
          source: |
            curl -X POST "https://api.together.xyz/v1/embeddings" \
                 -H "Authorization: Bearer $TOGETHER_API_KEY" \
                 -H "Content-Type: application/json" \
                 -d '{
                   "model": "BAAI/bge-large-en-v1.5",
                   "input": "New York City"
                 }'
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
                - intfloat/multilingual-e5-large-instruct
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
          description: The object type, which is always `list`.
          const: list
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
                description: The object type, which is always `embedding`.
                const: embedding
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

Built with [Mintlify](https://mintlify.com).