# Source: https://docs.lunary.ai/docs/api/datasets-v2/create-dataset-v2.md

# Create dataset v2



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/datasets-v2
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets-v2:
    post:
      tags:
        - Datasets v2
      summary: Create dataset v2
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DatasetV2Input'
      responses:
        '201':
          description: Created dataset
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetV2'
      security:
        - BearerAuth: []
components:
  schemas:
    DatasetV2Input:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
          nullable: true
      required:
        - name
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt