# Source: https://docs.wandb.ai/weave/reference/service-api/inference/inference-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Inference Get

> OpenAI-compatible APIs.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /inference/v1{path}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /inference/v1{path}:
    get:
      tags:
        - Inference
      summary: Inference Get
      description: OpenAI-compatible APIs.
      operationId: inference_get_inference_v1_path__get
      parameters:
        - name: path
          in: path
          required: true
          schema:
            type: string
            title: Path
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - HTTPBearer: []
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
    HTTPBearer:
      type: http
      scheme: bearer

````