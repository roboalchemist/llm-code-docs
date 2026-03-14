# Source: https://tyk.io/docs/api-reference/catalogues/add-an-llm-to-a-catalogue.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add an LLM to a catalogue

> Add an LLM to a specific catalogue



## OpenAPI

````yaml swagger/5.8/ai-studio-swagger.yml post /catalogues/{id}/llms
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
  /catalogues/{id}/llms:
    post:
      tags:
        - catalogues
      summary: Add an LLM to a catalogue
      description: Add an LLM to a specific catalogue
      parameters:
        - name: id
          in: path
          description: Catalogue ID
          required: true
          schema:
            type: integer
      requestBody:
        description: LLM to add
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/api.CatalogueLLMInput'
        required: true
      responses:
        '204':
          description: No Content
          content: {}
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
    api.CatalogueLLMInput:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
            type:
              type: string
      description: Catalogue-LLM relationship input model
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