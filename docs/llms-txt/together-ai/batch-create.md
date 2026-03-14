# Source: https://docs.together.ai/reference/batch-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a batch job

> Create a new batch job with the given input file and endpoint



## OpenAPI

````yaml POST /batches
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /batches:
    post:
      tags:
        - Batches
      summary: Create a batch job
      description: Create a new batch job with the given input file and endpoint
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateBatchRequest'
      responses:
        '201':
          description: Job created (potentially with warnings)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchJobWithWarning'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchErrorResponse'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchErrorResponse'
        '429':
          description: Too Many Requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchErrorResponse'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchErrorResponse'
      security:
        - bearerAuth: []
      x-codeSamples:
        - lang: Python
          label: Together AI SDK (v2)
          source: >
            # Docs for v1 can be found by changing the above selector ^

            from together import Together

            import os


            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )


            batch = client.batches.create(input_file_id="file_id",
            endpoint="/v1/chat/completions")


            print(batch.job)
        - lang: Python
          label: Together AI SDK (v1)
          source: >
            from together import Together

            import os


            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )


            batch = client.batches.create_batch("file_id",
            endpoint="/v1/chat/completions")


            print(batch.id)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const batch = await client.batches.create({
              endpoint: "/v1/chat/completions",
              input_file_id: "file-id",
            });

            console.log(batch);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const batch = await client.batches.create({
              endpoint: "/v1/chat/completions",
              input_file_id: "file-id",
            });

            console.log(batch);
        - lang: Shell
          label: cURL
          source: |
            curl -X POST "https://api.together.xyz/v1/batches" \
                 -H "Authorization: Bearer $TOGETHER_API_KEY" \
                 -H "Content-Type: application/json" \
                 -d '{
                   "endpoint": "/v1/chat/completions",
                   "input_file_id": "file-id"
                 }'
components:
  schemas:
    CreateBatchRequest:
      type: object
      required:
        - endpoint
        - input_file_id
      properties:
        endpoint:
          type: string
          description: The endpoint to use for batch processing
          example: /v1/chat/completions
        input_file_id:
          type: string
          description: ID of the uploaded input file containing batch requests
          example: file-abc123def456ghi789
        completion_window:
          type: string
          description: Time window for batch completion (optional)
          example: 24h
        priority:
          type: integer
          description: Priority for batch processing (optional)
          example: 1
        model_id:
          type: string
          description: Model to use for processing batch requests
          example: meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo
    BatchJobWithWarning:
      type: object
      properties:
        job:
          $ref: '#/components/schemas/BatchJob'
        warning:
          type: string
    BatchErrorResponse:
      type: object
      properties:
        error:
          type: string
    BatchJob:
      type: object
      properties:
        id:
          type: string
          format: uuid
          example: 01234567-8901-2345-6789-012345678901
        user_id:
          type: string
          example: user_789xyz012
        input_file_id:
          type: string
          example: file-input123abc456def
        file_size_bytes:
          type: integer
          format: int64
          example: 1048576
          description: Size of input file in bytes
        status:
          $ref: '#/components/schemas/BatchJobStatus'
        job_deadline:
          type: string
          format: date-time
          example: '2024-01-15T15:30:00Z'
        created_at:
          type: string
          format: date-time
          example: '2024-01-15T14:30:00Z'
        endpoint:
          type: string
          example: /v1/chat/completions
        progress:
          type: number
          format: float64
          example: 75
          description: Completion progress (0.0 to 100)
        model_id:
          type: string
          example: meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo
          description: Model used for processing requests
        output_file_id:
          type: string
          example: file-output789xyz012ghi
        error_file_id:
          type: string
          example: file-errors456def789jkl
        error:
          type: string
        completed_at:
          type: string
          format: date-time
          example: '2024-01-15T15:45:30Z'
    BatchJobStatus:
      type: string
      enum:
        - VALIDATING
        - IN_PROGRESS
        - COMPLETED
        - FAILED
        - EXPIRED
        - CANCELLED
      example: IN_PROGRESS
      description: Current status of the batch job
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).