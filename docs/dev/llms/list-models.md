# Source: https://dev.writer.com/api-reference/completion-api/list-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List models

> Retrieve a list of available models that can be used for text generation, chat completions, and other AI tasks.



## OpenAPI

````yaml get /v1/models
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/models:
    get:
      tags:
        - Generation API
      summary: List models
      description: >-
        Retrieve a list of available models that can be used for text
        generation, chat completions, and other AI tasks.
      operationId: models
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/models_response'
      security:
        - bearerAuth: []
components:
  schemas:
    models_response:
      required:
        - models
      type: object
      properties:
        models:
          type: array
          description: >-
            The [ID of the model](https://dev.writer.com/home/models) to use for
            processing the request.
          items:
            $ref: '#/components/schemas/model_info'
      example:
        models:
          - name: Palmyra X 003 Instruct
            id: palmyra-x-003-instruct
          - name: Palmyra Med
            id: palmyra-med
          - name: Palmyra Financial
            id: palmyra-fin
          - name: Palmyra X4
            id: palmyra-x4
          - name: Palmyra X5
            id: palmyra-x5
          - name: Palmyra Creative
            id: palmyra-creative
    model_info:
      required:
        - name
        - id
      type: object
      properties:
        name:
          type: string
          description: The name of the particular LLM that you want to use.
        id:
          type: string
          description: The ID of the particular LLM that you want to use
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        Bearer authentication header of the form `Bearer <token>`, where
        `<token>` is your [Writer API
        key](https://dev.writer.com/api-reference/api-keys).

````