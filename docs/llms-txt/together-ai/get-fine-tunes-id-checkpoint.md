# Source: https://docs.together.ai/reference/get-fine-tunes-id-checkpoint.md

# List checkpoints

> List the checkpoints for a single fine-tuning job.



## OpenAPI

````yaml GET /fine-tunes/{id}/checkpoints
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
  /fine-tunes/{id}/checkpoints:
    get:
      tags:
        - Fine-tuning
      summary: List checkpoints
      description: List the checkpoints for a single fine-tuning job.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: List of fine-tune checkpoints
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FinetuneListCheckpoints'
components:
  schemas:
    FinetuneListCheckpoints:
      type: object
      required:
        - data
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/FineTuneCheckpoint'
    FineTuneCheckpoint:
      type: object
      required:
        - step
        - path
        - created_at
        - checkpoint_type
      properties:
        step:
          type: integer
        created_at:
          type: string
        path:
          type: string
        checkpoint_type:
          type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt