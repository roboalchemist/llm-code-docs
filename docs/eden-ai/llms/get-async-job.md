# Source: https://docs.edenai.co/api-reference/universal-ai/get-async-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Async Job

> Retrieve the status and results of an async job.

Poll this endpoint until `status` changes from `"processing"` to `"success"` or `"fail"`.

Example response (completed):
```json
{
    "public_id": "abc123-def456",
    "status": "success",
    "cost": "0.005",
    "provider": "google",
    "feature": "audio",
    "subfeature": "speech_to_text_async",
    "output": {"text": "Hello world", ...},
    "error": null,
    "model": null,
    "created_at": "2025-01-01T00:00:00Z"
}
```



## OpenAPI

````yaml openapi/v3-openapi.json get /v3/universal-ai/async/{job_id}
openapi: 3.1.0
info:
  title: Eden AI API V3
  version: 3.0.0
servers:
  - url: https://api.edenai.run
    description: Production server
security: []
paths:
  /v3/universal-ai/async/{job_id}:
    get:
      tags:
        - Universal-ai
      summary: Get Async Job
      description: >-
        Retrieve the status and results of an async job.


        Poll this endpoint until `status` changes from `"processing"` to
        `"success"` or `"fail"`.


        Example response (completed):

        ```json

        {
            "public_id": "abc123-def456",
            "status": "success",
            "cost": "0.005",
            "provider": "google",
            "feature": "audio",
            "subfeature": "speech_to_text_async",
            "output": {"text": "Hello world", ...},
            "error": null,
            "model": null,
            "created_at": "2025-01-01T00:00:00Z"
        }

        ```
      operationId: get_async_job_v3_universal_ai_async__job_id__get
      parameters:
        - name: job_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Job ID
            description: The job ID returned from POST /v3/universal-ai/async
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UniversalAIAsyncResponse'
        '404':
          description: Job not found
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