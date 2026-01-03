# Source: https://docs.lunary.ai/docs/api/runs/update-run-tags.md

# Update run tags



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi patch /v1/runs/{id}/tags
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/runs/{id}/tags:
    patch:
      tags:
        - Runs
      summary: Update run tags
      parameters:
        - in: path
          name: id
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                tags:
                  type: array
                  items:
                    type: string
              example:
                tags:
                  - example
                  - test
      responses:
        '200':
          description: Tags updated successfully
        '400':
          description: Invalid input

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt