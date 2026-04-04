# Source: https://docs.lunary.ai/docs/api/datasets/list-datasets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List datasets



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/datasets
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets:
    get:
      tags:
        - Datasets
      summary: List datasets
      responses:
        '200':
          description: List of datasets
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Dataset'
      security:
        - BearerAuth: []
components:
  schemas:
    Dataset:
      type: object
      properties:
        id:
          type: string
        slug:
          type: string
        format:
          type: string
          enum:
            - text
            - chat
        ownerId:
          type: string
        projectId:
          type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````