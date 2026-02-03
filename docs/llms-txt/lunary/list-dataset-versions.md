# Source: https://docs.lunary.ai/docs/api/datasets-v2/list-dataset-versions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List dataset versions



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/datasets-v2/{datasetId}/versions
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets-v2/{datasetId}/versions:
    get:
      tags:
        - Datasets v2
      summary: List dataset versions
      parameters:
        - in: path
          name: datasetId
          required: true
          schema:
            type: string
            format: uuid
        - in: query
          name: limit
          required: false
          schema:
            type: integer
            minimum: 1
            maximum: 100
      responses:
        '200':
          description: Dataset versions
          content:
            application/json:
              schema:
                type: object
                properties:
                  versions:
                    type: array
                    items:
                      $ref: '#/components/schemas/DatasetV2Version'
      security:
        - BearerAuth: []
components:
  schemas:
    DatasetV2Version:
      type: object
      properties:
        id:
          type: string
          format: uuid
        datasetId:
          type: string
          format: uuid
        versionNumber:
          type: integer
        createdAt:
          type: string
          format: date-time
        createdBy:
          type: string
          format: uuid
          nullable: true
        restoredFromVersionId:
          type: string
          format: uuid
          nullable: true
        name:
          type: string
          nullable: true
        description:
          type: string
          nullable: true
        itemCount:
          type: integer
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````