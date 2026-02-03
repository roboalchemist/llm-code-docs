# Source: https://docs.lunary.ai/docs/api/datasets-v2/get-dataset-version.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get dataset version



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/datasets-v2/{datasetId}/versions/{versionId}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets-v2/{datasetId}/versions/{versionId}:
    get:
      tags:
        - Datasets v2
      summary: Get dataset version
      parameters:
        - in: path
          name: datasetId
          required: true
          schema:
            type: string
            format: uuid
        - in: path
          name: versionId
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Dataset version with items
          content:
            application/json:
              schema:
                type: object
                properties:
                  version:
                    $ref: '#/components/schemas/DatasetV2Version'
                  items:
                    type: array
                    items:
                      $ref: '#/components/schemas/DatasetV2VersionItem'
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
    DatasetV2VersionItem:
      type: object
      properties:
        id:
          type: string
          format: uuid
        versionId:
          type: string
          format: uuid
        datasetId:
          type: string
          format: uuid
        itemIndex:
          type: integer
        input:
          type: string
        groundTruth:
          type: string
          nullable: true
        output:
          type: string
          nullable: true
        sourceItemId:
          type: string
          format: uuid
          nullable: true
        sourceCreatedAt:
          type: string
          format: date-time
          nullable: true
        sourceUpdatedAt:
          type: string
          format: date-time
          nullable: true
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````