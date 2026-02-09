# Source: https://docs.lunary.ai/docs/api/datasets-v2/delete-dataset-v2-item.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete dataset v2 item



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi delete /v1/datasets-v2/{datasetId}/items/{itemId}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets-v2/{datasetId}/items/{itemId}:
    delete:
      tags:
        - Datasets v2
      summary: Delete dataset v2 item
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
      responses:
        '204':
          description: Dataset item deleted
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````