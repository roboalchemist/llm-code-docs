# Source: https://docs.together.ai/reference/batch-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a batch job

> Get details of a batch job by ID



## OpenAPI

````yaml GET /batches/{id}
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
  /batches/{id}:
    get:
      tags:
        - Batches
      summary: Get a batch job
      description: Get details of a batch job by ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            description: The ID of the batch job to retrieve
            example: batch_job_abc123def456
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchJob'
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
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchErrorResponse'
        '404':
          description: Not Found
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
          source: |
            # Docs for v1 can be found by changing the above selector ^
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            batch = client.batches.retrieve("batch_id")

            print(batch)
        - lang: Python
          label: Together AI SDK (v1)
          source: |
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            batch = client.batches.get_batch("batch_id")

            print(batch)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const batch = await client.batches.retrieve("batch-id");

            console.log(batch);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const batch = await client.batches.retrieve("batch-id");

            console.log(batch);
        - lang: Shell
          label: cURL
          source: |
            curl "https://api.together.xyz/v1/batches/ID" \
                 -H "Authorization: Bearer $TOGETHER_API_KEY" \
                 -H "Content-Type: application/json"
components:
  schemas:
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
    BatchErrorResponse:
      type: object
      properties:
        error:
          type: string
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