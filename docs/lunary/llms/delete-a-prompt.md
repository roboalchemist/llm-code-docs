# Source: https://docs.lunary.ai/docs/api/datasets/delete-a-prompt.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a prompt



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi delete /v1/datasets/prompts/{id}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets/prompts/{id}:
    delete:
      tags:
        - Datasets
        - Prompts
      summary: Delete a prompt
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Prompt deleted successfully
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````