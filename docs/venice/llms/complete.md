# Source: https://docs.venice.ai/api-reference/endpoint/video/complete.md

# Complete Video

> Delete a video generation request from storage after it has been successfully downloaded. Videos can be automatically deleted after retrieval by setting the `delete_media_on_completion` flag to true when calling the retrieve API.

***


## OpenAPI

````yaml POST /video/complete
openapi: 3.0.0
info:
  description: The Venice.ai API.
  termsOfService: https://venice.ai/legal/tos
  title: Venice.ai API
  version: '20251230.213343'
servers:
  - url: https://api.venice.ai/api/v1
security:
  - BearerAuth: []
tags:
  - description: >-
      Given a list of messages comprising a conversation, the model will return
      a response. Supports multimodal inputs including text, images, audio
      (input_audio), and video (video_url) for compatible models.
    name: Chat
  - description: List and describe the various models available in the API.
    name: Models
  - description: Generate and manipulate images using AI models.
    name: Image
  - description: Generate videos using AI models.
    name: Video
  - description: List and retrieve character information for use in completions.
    name: Characters
externalDocs:
  description: Venice.ai API documentation
  url: https://docs.venice.ai
paths:
  /video/complete:
    post:
      tags:
        - Video
      summary: /api/v1/video/complete
      description: >-
        Delete a video generation request from storage after it has been
        successfully downloaded. Videos can be automatically deleted after
        retrieval by setting the `delete_media_on_completion` flag to true when
        calling the retrieve API.
      operationId: completeVideo
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CompleteVideoRequest'
      responses:
        '200':
          description: Video generation request completed successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    description: Indicates whether the video cleanup was successful.
                    example: true
                required:
                  - success
        '400':
          description: Invalid request parameters
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DetailedError'
        '401':
          description: Authentication failed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StandardError'
        '500':
          description: Inference processing failed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StandardError'
components:
  schemas:
    CompleteVideoRequest:
      type: object
      properties:
        model:
          type: string
          description: The ID of the model used for video generation.
          example: video-model-123
        queue_id:
          type: string
          description: The ID of the video generation request.
          example: 123e4567-e89b-12d3-a456-426614174000
      required:
        - model
        - queue_id
      additionalProperties: false
    DetailedError:
      type: object
      properties:
        details:
          type: object
          properties: {}
          description: Details about the incorrect input
          example:
            _errors: []
            field:
              _errors:
                - Field is required
        error:
          type: string
          description: A description of the error
      required:
        - error
    StandardError:
      type: object
      properties:
        error:
          type: string
          description: A description of the error
      required:
        - error
  securitySchemes:
    BearerAuth:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.venice.ai/llms.txt