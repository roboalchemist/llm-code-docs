# Source: https://docs.lunary.ai/docs/api/datasets-v2/list-dataset-v2-items.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List dataset v2 items



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/datasets-v2/{datasetId}/items
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets-v2/{datasetId}/items:
    get:
      tags:
        - Datasets v2
      summary: List dataset v2 items
      parameters:
        - in: path
          name: datasetId
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Dataset items
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/DatasetV2Item'
      security:
        - BearerAuth: []
components:
  schemas:
    DatasetV2Item:
      type: object
      properties:
        id:
          type: string
          format: uuid
        datasetId:
          type: string
          format: uuid
        input:
          type: string
        groundTruth:
          type: string
          nullable: true
        output:
          type: string
          nullable: true
        evaluatorResult1:
          type: object
          nullable: true
        evaluatorResult2:
          type: object
          nullable: true
        evaluatorResult3:
          type: object
          nullable: true
        evaluatorResult4:
          type: object
          nullable: true
        evaluatorResult5:
          type: object
          nullable: true
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````