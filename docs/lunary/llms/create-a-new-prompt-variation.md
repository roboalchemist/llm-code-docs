# Source: https://docs.lunary.ai/docs/api/datasets/create-a-new-prompt-variation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new prompt variation



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/datasets/variations
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets/variations:
    post:
      tags:
        - Datasets
        - Prompts
        - Variations
      summary: Create a new prompt variation
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                promptId:
                  type: string
                variables:
                  type: object
                idealOutput:
                  type: string
      responses:
        '200':
          description: Created prompt variation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetPromptVariation'
      security:
        - BearerAuth: []
components:
  schemas:
    DatasetPromptVariation:
      type: object
      properties:
        id:
          type: string
        promptId:
          type: string
        variables:
          type: object
        idealOutput:
          type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````