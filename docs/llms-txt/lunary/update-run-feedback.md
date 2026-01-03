# Source: https://docs.lunary.ai/docs/api/runs/update-run-feedback.md

# Update run feedback



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi patch /v1/runs/{id}/feedback
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/runs/{id}/feedback:
    patch:
      tags:
        - Runs
      summary: Update run feedback
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
              $ref: '#/components/schemas/Feedback'
            example:
              thumb: up
              comment: This response was very helpful!
      responses:
        '200':
          description: Feedback updated successfully
        '400':
          description: Invalid input
components:
  schemas:
    Feedback:
      type: object
      properties:
        score:
          type: number
        flags:
          type: array
          items:
            type: string
        comment:
          type: string

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt