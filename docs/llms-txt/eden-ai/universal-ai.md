# Source: https://docs.edenai.co/api-reference/universal-ai/universal-ai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Universal Ai

> Universal AI endpoint for all non-LLM AI features.

Model format: feature/subfeature/provider[/model]

Request body:
- model: Model string in format feature/subfeature/provider[/model]
- input: Feature-specific input parameters
- provider_params: Optional provider-specific parameters
- show_original_response: Include raw provider response (default: false)

Example:
```json
{
    "model": "text/moderation/google",
    "input": {"text": "Content to moderate"}
}
```

Response:
```json
{
    "status": "success",
    "cost": "0.001",
    "provider": "google",
    "feature": "text",
    "subfeature": "moderation",
    "output": {...},
    "error": null
}
```



## OpenAPI

````yaml openapi/v3-openapi.json post /v3/universal-ai
openapi: 3.1.0
info:
  title: Eden AI API V3
  version: 3.0.0
servers:
  - url: https://api.edenai.run
    description: Production server
security: []
paths:
  /v3/universal-ai:
    post:
      tags:
        - Universal-ai
      summary: Universal Ai
      description: |-
        Universal AI endpoint for all non-LLM AI features.

        Model format: feature/subfeature/provider[/model]

        Request body:
        - model: Model string in format feature/subfeature/provider[/model]
        - input: Feature-specific input parameters
        - provider_params: Optional provider-specific parameters
        - show_original_response: Include raw provider response (default: false)

        Example:
        ```json
        {
            "model": "text/moderation/google",
            "input": {"text": "Content to moderate"}
        }
        ```

        Response:
        ```json
        {
            "status": "success",
            "cost": "0.001",
            "provider": "google",
            "feature": "text",
            "subfeature": "moderation",
            "output": {...},
            "error": null
        }
        ```
      operationId: universal_ai_v3_universal_ai_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UniversalAIBody'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UniversalAIResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - AuthBearer: []
components:
  schemas:
    UniversalAIBody:
      properties:
        model:
          type: string
          title: Model
          description: 'Model in format: feature/subfeature/provider[/model]'
          examples:
            - text/moderation/google
            - ocr/ocr/amazon
            - image/generation/google/imagen-3
        provider_params:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Provider Params
          description: Provider-specific parameters
        input:
          additionalProperties: true
          type: object
          title: Input
          description: >-
            Feature-specific input parameters. Required fields depend on the
            feature/subfeature specified in provider. Examples:

            - text/moderation: {'text': 'content to moderate'}

            - text/embeddings: {'texts': ['text1', 'text2']}

            - ocr/ocr: {'file_id': 'abc123', 'language': 'en'}

            - image/generation: {'text': 'prompt', 'resolution': '1024x1024'}

            - translation/document_translation: {'file_id': 'abc123',
            'target_language': 'fr'}
          examples:
            - text: Content to moderate for harmful material
            - dimensions: 512
              texts:
                - text1
                - text2
            - file_id: abc123
              language: en
        show_original_response:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Show Original Response
          description: Include raw provider response in the output
          default: false
      type: object
      required:
        - model
        - input
      title: UniversalAIBody
      description: |-
        Universal AI request body.

        Model format: feature/subfeature/provider[/model]

        Examples:
            - text/moderation/google
            - ocr/ocr/amazon
            - image/generation/google/imagen-3

        The `input` dict contains feature-specific parameters that are
        validated at runtime based on the parsed feature/subfeature.
    UniversalAIResponse:
      properties:
        status:
          type: string
          enum:
            - success
            - fail
          title: Status
          description: Whether the request succeeded or failed
        cost:
          type: string
          pattern: ^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$
          title: Cost
          description: Cost in credits for this request
        provider:
          type: string
          title: Provider
          description: Provider name that processed the request
        feature:
          type: string
          title: Feature
          description: Feature category (e.g., text, ocr, image)
        subfeature:
          type: string
          title: Subfeature
          description: Specific subfeature (e.g., ai_detection, sentiment)
        output:
          title: Output
          description: Normalized output from the provider
        error:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Error
          description: Error message from the provider (only present when status is 'fail')
        original_response:
          anyOf:
            - {}
            - type: 'null'
          title: Original Response
          description: Raw response from the provider (if show_original_response=true)
      type: object
      required:
        - status
        - cost
        - provider
        - feature
        - subfeature
        - output
      title: UniversalAIResponse
      description: >-
        Normalized response from universal-ai endpoint.


        All responses have a consistent structure regardless of the
        feature/subfeature.
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
    AuthBearer:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).