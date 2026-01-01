# Source: https://docs.lunary.ai/docs/api/datasets-v2/import-dataset-items-from-csv-or-jsonl.md

# Import dataset items from CSV or JSONL



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi post /v1/datasets-v2/{datasetId}/import
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets-v2/{datasetId}/import:
    post:
      tags:
        - Datasets v2
      summary: Import dataset items from CSV or JSONL
      parameters:
        - in: path
          name: datasetId
          required: true
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DatasetV2ImportRequest'
      responses:
        '200':
          description: Number of imported items
          content:
            application/json:
              schema:
                type: object
                properties:
                  insertedCount:
                    type: integer
      security:
        - BearerAuth: []
components:
  schemas:
    DatasetV2ImportRequest:
      type: object
      properties:
        format:
          type: string
          enum:
            - csv
            - jsonl
        content:
          type: string
      required:
        - format
        - content
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt