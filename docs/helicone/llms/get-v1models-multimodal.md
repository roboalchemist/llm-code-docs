# Source: https://docs.helicone.ai/rest/ai-gateway/get-v1models-multimodal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Multimodal Models

> Returns all available multimodal models supported by Helicone AI Gateway (OpenAI-compatible endpoint)

This endpoint returns a list of all multimodal AI models supported by the Helicone AI Gateway. Multimodal models are those that support more than one input modality (e.g., text + images) or more than one output modality. This is an OpenAI-compatible endpoint that follows the same response format as OpenAI's `/v1/models` endpoint.

Use this endpoint to discover which multimodal models are available for routing through the AI Gateway.

## Endpoint URL

```
https://ai-gateway.helicone.ai/v1/models/multimodal
```

## What Makes a Model Multimodal?

A model is considered multimodal if it meets either of these criteria:

* **Multiple Input Modalities**: Accepts more than one type of input (e.g., text, images, audio)
* **Multiple Output Modalities**: Produces more than one type of output (e.g., text, images, audio)

## Example Request

```bash  theme={null}
curl https://ai-gateway.helicone.ai/v1/models/multimodal
```

## Example Response

```json  theme={null}
{
  "object": "list",
  "data": [
    {
      "id": "claude-sonnet-4-5",
      "object": "model",
      "created": 1747180800,
      "owned_by": "anthropic"
    },
    {
      "id": "gpt-4o",
      "object": "model",
      "created": 1715558400,
      "owned_by": "openai"
    },
    {
      "id": "gemini-1.5-pro",
      "object": "model",
      "created": 1704067200,
      "owned_by": "google"
    },
    ...
  ]
}
```

## Use Cases

* **OpenAI Compatibility**: Use this endpoint as a drop-in replacement for OpenAI's `/v1/models` endpoint with multimodal filtering
* **Multimodal Model Discovery**: Discover which multimodal models are available through Helicone AI Gateway
* **Vision/Audio Applications**: Find models that support image or audio inputs for your applications
* **Integration Testing**: Verify multimodal model availability for your applications


## OpenAPI

````yaml get /v1/models/multimodal
openapi: 3.0.0
info:
  title: helicone-api
  version: 1.0.0
  license:
    name: MIT
  contact: {}
servers:
  - url: https://api.helicone.ai/
  - url: http://localhost:8585/
security: []
paths:
  /v1/models/multimodal:
    get:
      tags:
        - Models
      operationId: GetMultimodalModels
      parameters: []
      responses:
        '200':
          description: Ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OAIModelsResponse'
      security: []
components:
  schemas:
    OAIModelsResponse:
      properties:
        object:
          type: string
          enum:
            - list
          nullable: false
        data:
          items:
            $ref: '#/components/schemas/OAIModel'
          type: array
      required:
        - object
        - data
      type: object
      additionalProperties: false
    OAIModel:
      properties:
        id:
          type: string
        object:
          type: string
          enum:
            - model
          nullable: false
        created:
          type: number
          format: double
        owned_by:
          type: string
      required:
        - id
        - object
        - created
        - owned_by
      type: object
      additionalProperties: false

````