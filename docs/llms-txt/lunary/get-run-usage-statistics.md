# Source: https://docs.lunary.ai/docs/api/runs/get-run-usage-statistics.md

# Get run usage statistics

> Retrieve usage statistics for runs



## OpenAPI

````yaml https://api.lunary.ai/v1/openapi get /v1/runs/usage
openapi: 3.0.0
info:
  title: Lunary API
  version: 1.0.0
servers:
  - url: https://api.lunary.ai
security: []
tags: []
paths:
  /v1/runs/usage:
    get:
      tags:
        - Runs
      summary: Get run usage statistics
      description: Retrieve usage statistics for runs
      parameters:
        - in: query
          name: days
          required: true
          schema:
            type: string
        - in: query
          name: userId
          schema:
            type: string
        - in: query
          name: daily
          schema:
            type: string
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    date:
                      type: string
                    name:
                      type: string
                    type:
                      type: string
                    completion_tokens:
                      type: integer
                    prompt_tokens:
                      type: integer
                    cost:
                      type: number
                    errors:
                      type: integer
                    success:
                      type: integer
        '400':
          description: Invalid query parameters

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt