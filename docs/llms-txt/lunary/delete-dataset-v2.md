# Source: https://docs.lunary.ai/docs/api/datasets-v2/delete-dataset-v2.md

# Delete dataset v2



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi delete /v1/datasets-v2/{datasetId}
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/datasets-v2/{datasetId}:
    delete:
      tags:
        - Datasets v2
      summary: Delete dataset v2
      parameters:
        - in: path
          name: datasetId
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '204':
          description: Dataset deleted
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt