# Source: https://docs.edenai.co/api-reference/completions/list-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List Models

> List available LLM models with extended metadata.



## OpenAPI

````yaml openapi/v3-openapi.json get /v3/llm/models
openapi: 3.1.0
info:
  title: Eden AI API V3
  version: 3.0.0
servers:
  - url: https://api.edenai.run
    description: Production server
security: []
paths:
  /v3/llm/models:
    get:
      tags:
        - Completions
      summary: List Models
      description: List available LLM models with extended metadata.
      operationId: list_models_v3_llm_models_get
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListModelsResponse'
components:
  schemas:
    ListModelsResponse:
      properties:
        object:
          type: string
          const: list
          title: Object
          description: Object type
          default: list
        data:
          items:
            $ref: '#/components/schemas/ModelObject'
          type: array
          title: Data
          description: List of models
      type: object
      required:
        - data
      title: ListModelsResponse
      description: List models response.
    ModelObject:
      properties:
        id:
          type: string
          title: Id
          description: Model identifier (e.g., 'openai/gpt-4')
        object:
          type: string
          const: model
          title: Object
          description: Object type
          default: model
        created:
          type: integer
          title: Created
          description: Unix timestamp of model creation/release
        owned_by:
          type: string
          title: Owned By
          description: Provider/organization that owns the model
        model_name:
          type: string
          title: Model Name
          description: Model name without provider prefix
        context_length:
          anyOf:
            - type: integer
            - type: 'null'
          title: Context Length
          description: Maximum context length in tokens
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: Model description
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
          description: Model source URL
        capabilities:
          additionalProperties: true
          type: object
          title: Capabilities
          description: Model capabilities
        pricing:
          additionalProperties: true
          type: object
          title: Pricing
          description: Pricing information
      type: object
      required:
        - id
        - created
        - owned_by
        - model_name
      title: ModelObject
      description: Extended model object with full metadata.

````

Built with [Mintlify](https://mintlify.com).