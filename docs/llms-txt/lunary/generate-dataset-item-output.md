# Source: https://docs.lunary.ai/docs/api/datasets-v2/generate-dataset-item-output.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate dataset item output



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/datasets-v2/{datasetId}/items/{itemId}/generate
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets-v2/{datasetId}/items/{itemId}/generate:
    post:
      tags:
        - Datasets v2
      summary: Generate dataset item output
      parameters:
        - in: path
          name: datasetId
          required: true
          schema:
            type: string
            format: uuid
        - in: path
          name: itemId
          required: true
          schema:
            type: string
            format: uuid
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                model:
                  type: string
                instructions:
                  type: string
      responses:
        '200':
          description: Generated output for the dataset item
          content:
            application/json:
              schema:
                type: object
                properties:
                  output:
                    type: string
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````