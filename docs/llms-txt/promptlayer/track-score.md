# Source: https://docs.promptlayer.com/reference/track-score.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

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
      parameters:
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
          description: Your PromptLayer API Key.
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
              required:
                - request_id
                - score
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