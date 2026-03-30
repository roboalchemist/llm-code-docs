# Source: https://tyk.io/docs/api-reference/llm-settings/create-new-llm-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create new LLM settings

> Create new LLM settings with the provided information



## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml post /llm-settings
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
  /llm-settings:
    post:
      tags:
        - llm-settings
      summary: Create new LLM settings
      description: Create new LLM settings with the provided information
      requestBody:
        description: LLM settings information
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/api.LLMSettingsInput'
        required: true
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
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
    api.LLMSettingsInput:
      type: object
      properties:
        data:
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
            type:
              type: string
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