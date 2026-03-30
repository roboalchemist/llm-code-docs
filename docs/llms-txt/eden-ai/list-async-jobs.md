# Source: https://docs.edenai.co/api-reference/universal-ai/list-async-jobs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edenai.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List Async Jobs

> List all async jobs for the authenticated user.

Results are ordered by creation date (newest first). Supports filtering by feature, subfeature, and status.



## OpenAPI

````yaml openapi/v3-openapi.json get /v3/universal-ai/async
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
    get:
      tags:
        - Universal-ai
      summary: List Async Jobs
      description: >-
        List all async jobs for the authenticated user.


        Results are ordered by creation date (newest first). Supports filtering
        by feature, subfeature, and status.
      operationId: list_async_jobs_v3_universal_ai_async_get
      parameters:
        - name: feature
          in: query
          required: false
          schema:
            type: string
            description: Filter by feature (e.g., audio, ocr)
          description: Filter by feature
        - name: subfeature
          in: query
          required: false
          schema:
            type: string
            description: Filter by subfeature (e.g., speech_to_text_async)
          description: Filter by subfeature
        - name: status
          in: query
          required: false
          schema:
            type: string
            enum:
              - processing
              - success
              - fail
            description: Filter by job status
          description: Filter by job status
        - name: page
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
            default: 1
            description: Page number (1-indexed)
          description: Page number (1-indexed)
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
            maximum: 1000
            default: 100
            description: Maximum number of items per page
          description: Maximum number of items per page
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UniversalAIAsyncJobListResponse'
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
    UniversalAIAsyncJobListResponse:
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/UniversalAIAsyncJobListItem'
          title: Items
          description: List of async jobs
        total:
          type: integer
          title: Total
          description: Total number of items
        page:
          type: integer
          title: Page
          description: Current page number
        limit:
          type: integer
          title: Limit
          description: Items per page
        total_pages:
          type: integer
          title: Total Pages
          description: Total number of pages
      type: object
      required:
        - items
        - total
        - page
        - limit
        - total_pages
      title: UniversalAIAsyncJobListResponse
      description: Paginated response for listing async jobs.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    UniversalAIAsyncJobListItem:
      properties:
        public_id:
          type: string
          format: uuid
          title: Public ID
          description: Job ID
        status:
          type: string
          enum:
            - success
            - fail
            - processing
          title: Status
          description: Job status
        feature:
          type: string
          title: Feature
          description: Feature name
        subfeature:
          type: string
          title: Subfeature
          description: Subfeature name
        provider:
          type: string
          title: Provider
          description: Provider name
        model:
          anyOf:
            - type: string
            - type: 'null'
          title: Model
          description: Model name
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Job creation timestamp
      type: object
      required:
        - public_id
        - status
        - feature
        - subfeature
        - provider
        - created_at
      title: UniversalAIAsyncJobListItem
      description: Summary item for async job list.
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