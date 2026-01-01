# Source: https://docs.promptlayer.com/reference/track-score.md

# Track Score

Track score allows you to associate a score 0-100 with each request.


## OpenAPI

````yaml POST /rest/track-score
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /rest/track-score:
    post:
      tags:
        - score
      summary: Track Score
      operationId: trackScore
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                request_id:
                  type: integer
                  description: The `request_id` from tracking a request.
                score:
                  type: integer
                  description: The score you would like to give to this request (0 - 100).
                  minimum: 0
                  maximum: 100
                name:
                  type: string
                  description: >-
                    A name for this request score. If not provided, the score
                    will be tracked as `default`.
                  optional: true
                api_key:
                  type: string
                  description: Your PromptLayer API Key.
              required:
                - request_id
                - score
                - api_key
      responses:
        '200':
          description: Score tracked successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  message:
                    type: string
                required:
                  - success
                  - message
        '400':
          description: Bad Request
        '401':
          description: Unauthorized

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt