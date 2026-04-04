# Source: https://docs.together.ai/reference/batch-cancel.md

# Cancel a batch job

> Cancel a batch job by ID



## OpenAPI

````yaml POST /batches/{id}/cancel
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
  /batches/{id}/cancel:
    post:
      tags:
        - Batches
      summary: Cancel a batch job
      description: Cancel a batch job by ID
      parameters:
        - name: id
          in: path
          required: true
          description: Job ID
          schema:
            type: string
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt