# Source: https://docs.lunary.ai/docs/api/datasets-v2/run-all-evaluators-attached-to-a-dataset-on-every-item.md

# Run all evaluators attached to a dataset on every item



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/datasets-v2/{datasetId}/evaluators/run
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets-v2/{datasetId}/evaluators/run:
    post:
      tags:
        - Datasets v2
      summary: Run all evaluators attached to a dataset on every item
      parameters:
        - in: path
          name: datasetId
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Evaluator results updated
          content:
            application/json:
              schema:
                type: object
                properties:
                  updatedItemCount:
                    type: integer
                  dataset:
                    $ref: '#/components/schemas/DatasetV2WithItems'
      security:
        - BearerAuth: []
components:
  schemas:
    DatasetV2WithItems:
      allOf:
        - $ref: '#/components/schemas/DatasetV2'
        - type: object
          properties:
            items:
              type: array
              items:
                $ref: '#/components/schemas/DatasetV2Item'
    DatasetV2:
      type: object
      properties:
        id:
          type: string
          format: uuid
        projectId:
          type: string
          format: uuid
        ownerId:
          type: string
          format: uuid
          nullable: true
        ownerName:
          type: string
          nullable: true
        ownerEmail:
          type: string
          nullable: true
        name:
          type: string
        description:
          type: string
          nullable: true
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time
        itemCount:
          type: integer
        currentVersionId:
          type: string
          format: uuid
          nullable: true
        currentVersionNumber:
          type: integer
        currentVersionCreatedAt:
          type: string
          format: date-time
          nullable: true
        currentVersionCreatedBy:
          type: string
          format: uuid
          nullable: true
        currentVersionRestoredFromVersionId:
          type: string
          format: uuid
          nullable: true
        evaluatorSlot1Id:
          type: string
          format: uuid
          nullable: true
        evaluatorSlot2Id:
          type: string
          format: uuid
          nullable: true
        evaluatorSlot3Id:
          type: string
          format: uuid
          nullable: true
        evaluatorSlot4Id:
          type: string
          format: uuid
          nullable: true
        evaluatorSlot5Id:
          type: string
          format: uuid
          nullable: true
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt