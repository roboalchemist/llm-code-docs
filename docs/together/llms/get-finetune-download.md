# Source: https://docs.together.ai/reference/get-finetune-download.md

# Download Model

> Receive a compressed fine-tuned model or checkpoint.



## OpenAPI

````yaml GET /finetune/download
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
  /finetune/download:
    get:
      tags:
        - Fine-tuning
      summary: Download model
      description: Receive a compressed fine-tuned model or checkpoint.
      parameters:
        - in: query
          name: ft_id
          schema:
            type: string
          required: true
          description: Fine-tune ID to download. A string that starts with `ft-`.
        - in: query
          name: checkpoint_step
          schema:
            type: integer
          required: false
          description: >-
            Specifies step number for checkpoint to download. Ignores
            `checkpoint` value if set.
        - in: query
          name: checkpoint
          schema:
            type: string
            enum:
              - merged
              - adapter
              - model_output_path
          description: >-
            Specifies checkpoint type to download - `merged` vs `adapter`. This
            field is required if the checkpoint_step is not set.
      responses:
        '200':
          description: Successfully downloaded the fine-tuned model or checkpoint.
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
        '400':
          description: Invalid request parameters.
        '404':
          description: Fine-tune ID not found.
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt