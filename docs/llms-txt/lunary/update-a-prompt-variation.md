# Source: https://docs.lunary.ai/docs/api/datasets/update-a-prompt-variation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a prompt variation



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi patch /v1/datasets/variations/{variationId}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets/variations/{variationId}:
    patch:
      tags:
        - Datasets
        - Prompts
        - Variations
      summary: Update a prompt variation
      parameters:
        - in: path
          name: variationId
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                variables:
                  type: object
                idealOutput:
                  type: string
      responses:
        '200':
          description: Updated prompt variation
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