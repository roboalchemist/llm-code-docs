# Source: https://tyk.io/docs/api-reference/llm-settings/search-llm-settings-by-model-name.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search LLM settings by model name

> Search for LLM settings using a model name stub



## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml get /llm-settings/search
openapi: 3.0.1
info:
  title: AI Studio API
  description: This is the API for the AI Studio user and group management system.
  termsOfService: http://swagger.io/terms/
  contact:
    name: API Support
    url: http://www.swagger.io/support
    email: support@tyk.io
  license:
    name: Apache 2.0
    url: http://www.apache.org/licenses/LICENSE-2.0.html
  version: '1.0'
servers:
  - url: //localhost:8080/api/v1
security:
  - BearerAuth: []
paths:
  /llm-settings/search:
    get:
      tags:
        - llm-settings
      summary: Search LLM settings by model name
      description: Search for LLM settings using a model name stub
      parameters:
        - name: model_name
          in: query
          description: Model name stub to search for
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/api.LLMSettingsResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.ErrorResponse'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/api.ErrorResponse'
      security:
        - BearerAuth: []
components:
  schemas:
    api.LLMSettingsResponse:
      type: object
      properties:
        attributes:
          type: object
          properties:
            max_length:
              type: integer
            max_tokens:
              type: integer
            metadata:
              type: object
              additionalProperties: true
            min_length:
              type: integer
            model_name:
              type: string
            repetition_penalty:
              type: number
            seed:
              type: integer
            stop_words:
              type: array
              items:
                type: string
            temperature:
              type: number
            top_k:
              type: integer
            top_p:
              type: number
        id:
          type: string
        type:
          type: string
    api.ErrorResponse:
      type: object
      properties:
        errors:
          type: array
          items:
            type: object
            properties:
              detail:
                type: string
              title:
                type: string
      description: Error response model
  securitySchemes:
    BearerAuth:
      type: apiKey
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).