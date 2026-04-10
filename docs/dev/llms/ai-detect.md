# Source: https://dev.writer.com/home/ai-detect.md

# Source: https://dev.writer.com/api-reference/tool-api/ai-detect.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AI detection

> Detects if content is AI- or human-generated, with a confidence score. Content must have at least 350 characters

<Warning>
  **Deprecation notice**: The [AI detection API endpoint](/api-reference/tool-api/ai-detect) at `/v1/tools/ai-detect` is deprecated and will be removed on **December 22, 2025**.

  This endpoint will no longer be available after the removal date. Please plan to migrate any integrations that currently use this endpoint to alternative solutions.
</Warning>


## OpenAPI

````yaml post /v1/tools/ai-detect
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/tools/ai-detect:
    post:
      tags:
        - Tools API
      summary: AI detection
      description: >-
        Detects if content is AI- or human-generated, with a confidence score.
        Content must have at least 350 characters
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ai_detection_request'
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ai_detection_response'
      security:
        - bearerAuth: []
components:
  schemas:
    ai_detection_request:
      title: ai_detection_request
      required:
        - input
      type: object
      properties:
        input:
          type: string
          description: >-
            The content to determine if it is AI- or human-generated. Content
            must have at least 350 characters.
          example: >-
            AI and ML continue to be at the forefront of technological
            advancements. In 2025, we can expect more sophisticated AI systems
            that can handle complex tasks with greater efficiency. AI will play
            a crucial role in various sectors, including healthcare, finance,
            and manufacturing. For instance, AI-powered diagnostic tools will
            become more accurate, helping doctors detect diseases at an early
            stage. In finance, AI algorithms will enhance fraud detection and
            risk management.
    ai_detection_response:
      title: ai_detection_response
      required:
        - label
        - score
      type: object
      properties:
        label:
          type: string
          enum:
            - fake
            - real
          example: fake
        score:
          type: number
          format: double
          example: 0.6265060305595398
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        Bearer authentication header of the form `Bearer <token>`, where
        `<token>` is your [Writer API
        key](https://dev.writer.com/api-reference/api-keys).

````