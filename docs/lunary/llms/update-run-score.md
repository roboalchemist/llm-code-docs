# Source: https://docs.lunary.ai/docs/api/runs/update-run-score.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update run score



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi patch /v1/runs/{id}/score
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/runs/{id}/score:
    patch:
      tags:
        - Runs
      summary: Update run score
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
                label:
                  type: string
                value:
                  type: number
                comment:
                  type: string
            example:
              label: accuracy
              value: 0.95
              comment: High accuracy score
      responses:
        '200':
          description: Score updated successfully
        '400':
          description: Invalid input

````