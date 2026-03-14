# Source: https://docs.edenai.co/api-reference/universal-ai/create-async-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Async Job

> Submit an asynchronous Universal AI job for long-running AI features.

Model format: feature/subfeature/provider[/model]

Use this endpoint for features that require processing time (e.g., speech-to-text, OCR on large documents). The response returns a job ID that you can poll using `GET /v3/universal-ai/async/{job_id}`.

Request body is identical to the sync endpoint (`POST /v3/universal-ai`).

Example:
```json
{
    "model": "audio/speech_to_text_async/google",
    "input": {"file": "YOUR_FILE_UUID_OR_URL", "language": "en"}
}
```

Response (202 Accepted):
```json
{
    "public_id": "abc123-def456",
    "status": "processing",
    "cost": "0.000",
    "provider": "google",
    "feature": "audio",
    "subfeature": "speech_to_text_async",
    "output": null,
    "error": null,
    "model": null,
    "created_at": "2025-01-01T00:00:00Z"
}
```



## OpenAPI

````yaml openapi/v3-openapi.json post /v3/universal-ai/async
openapi: 3.1.0
info:
  title: Eden AI API V3
  version: 3.0.0
servers:
  - url: https://api.edenai.run
    description: Production server
security: []
paths:
  /v3/universal-ai/async:
    post:
      tags:
        - Universal-ai
      summary: Create Async Job
      description: >-
        Submit an asynchronous Universal AI job for long-running AI features.


        Model format: feature/subfeature/provider[/model]


        Use this endpoint for features that require processing time (e.g.,
        speech-to-text, OCR on large documents). The response returns a job ID
        that you can poll using `GET /v3/universal-ai/async/{job_id}`.


        Request body is identical to the sync endpoint (`POST
        /v3/universal-ai`).


        Example:

        ```json

        {
            "model": "audio/speech_to_text_async/google",
            "input": {"file": "YOUR_FILE_UUID_OR_URL", "language": "en"}
        }

        ```


        Response (202 Accepted):

        ```json

        {
            "public_id": "abc123-def456",
            "status": "processing",
            "cost": "0.000",
            "provider": "google",
            "feature": "audio",
            "subfeature": "speech_to_text_async",
            "output": null,
            "error": null,
            "model": null,
            "created_at": "2025-01-01T00:00:00Z"
        }

        ```
      operationId: create_async_job_v3_universal_ai_async_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UniversalAIBody'
        required: true
      responses:
        '202':
          description: Job Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UniversalAIAsyncResponse'
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
    UniversalAIAsyncResponse:
      properties:
        public_id:
          type: string
          format: uuid
          title: Public ID
          description: Job ID for polling status
        status:
          type: string
          enum:
            - success
            - fail
            - processing
          title: Status
          description: 'Job status: processing (still running), success, or fail'
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
          description: Feature category (e.g., audio, ocr, image)
        subfeature:
          type: string
          title: Subfeature
          description: Specific subfeature (e.g., speech_to_text_async, ocr_async)
        output:
          anyOf:
            - {}
            - type: 'null'
          title: Output
          description: Normalized output from the provider (null while processing)
        error:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Error
          description: Error details from the provider (only present when status is 'fail')
        original_response:
          anyOf:
            - {}
            - type: 'null'
          title: Original Response
          description: Raw response from the provider (if show_original_response=true)
        model:
          anyOf:
            - type: string
            - type: 'null'
          title: Model
          description: Model name if specified in the request
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Job creation timestamp
      type: object
      required:
        - public_id
        - status
        - cost
        - provider
        - feature
        - subfeature
        - created_at
      title: UniversalAIAsyncResponse
      description: >-
        Response from the async universal-ai endpoint. Used for both job
        creation (202) and job status polling (GET).
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