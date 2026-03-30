# Source: https://io.net/docs/reference/ai-agents/workflows-schema.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Get a list of default workflows.

# Workflows Schema

<Warning>
  **Beta Notice:** This project is in rapid development and may not be stable for production use.
</Warning>


## OpenAPI

````yaml openapi/ai-agents/workflows-schema.json get /api/v1/workflows/schema
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/v1/workflows/schema:
    get:
      tags:
        - agents
      summary: Get Default Workflows
      operationId: get_default_workflows_v1_workflows_schema_get
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