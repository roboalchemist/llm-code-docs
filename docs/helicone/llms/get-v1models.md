# Source: https://docs.helicone.ai/rest/ai-gateway/get-v1models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Models

> Returns all available models supported by Helicone AI Gateway (OpenAI-compatible endpoint)

This endpoint returns a list of all AI models supported by the Helicone AI Gateway. This is an OpenAI-compatible endpoint that follows the same response format as OpenAI's `/v1/models` endpoint.

Use this endpoint to discover which models are available for routing through the AI Gateway.

## Endpoint URL

```
https://ai-gateway.helicone.ai/v1/models
```

## Example Request

```bash  theme={null}
curl https://ai-gateway.helicone.ai/v1/models
```

## Example Response

```json  theme={null}
{
  "object": "list",
  "data": [
    {
      "id": "claude-opus-4",
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
    ...
  ]
}
```

## Use Cases

* **OpenAI Compatibility**: Use this endpoint as a drop-in replacement for OpenAI's `/v1/models` endpoint
* **Model Discovery**: Discover which models are available through Helicone AI Gateway
* **Integration Testing**: Verify model availability for your applications


## OpenAPI

````yaml get /v1/models
openapi: 3.0.0
info:
  title: Helicone AI Gateway API
  version: 1.0.0
  description: OpenAPI spec derived from Zod schemas for AI Gateway.
servers:
  - url: https://ai-gateway.helicone.ai
security: []
paths:
  /v1/models:
    get:
      summary: Get Models
      description: >-
        Returns all available models supported by Helicone AI Gateway
        (OpenAI-compatible endpoint)
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  object:
                    type: string
                    enum:
                      - list
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: Model identifier
                        object:
                          type: string
                          enum:
                            - model
                        created:
                          type: integer
                          description: Unix timestamp of model creation
                        owned_by:
                          type: string
                          description: Organization that owns the model
                      required:
                        - id
                        - object
                        - created
                        - owned_by
                required:
                  - object
                  - data
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: object
                    properties:
                      message:
                        type: string
                      type:
                        type: string

````