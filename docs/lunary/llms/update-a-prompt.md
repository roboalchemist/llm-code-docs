# Source: https://docs.lunary.ai/docs/api/datasets/update-a-prompt.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a prompt



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi patch /v1/datasets/prompts/{id}
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
    patch:
      tags:
        - Datasets
        - Prompts
      summary: Update a prompt
      parameters:
        - in: path
          name: id
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
                messages:
                  oneOf:
                    - type: array
                      items:
                        type: object
                        properties:
                          role:
                            type: string
                          content:
                            type: string
                    - type: string
      responses:
        '200':
          description: Updated prompt
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetPrompt'
      security:
        - BearerAuth: []
components:
  schemas:
    DatasetPrompt:
      type: object
      properties:
        id:
          type: string
        datasetId:
          type: string
        messages:
          oneOf:
            - type: array
              items:
                type: object
                properties:
                  role:
                    type: string
                  content:
                    type: string
            - type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````