# Source: https://docs.venice.ai/api-reference/endpoint/video/retrieve.md

# Retrieve Video

> Retrieve a video generation result. Returns the video file if completed, or a status if the request is still processing.

***


## OpenAPI

````yaml POST /video/retrieve
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
  /video/retrieve:
    post:
      tags:
        - Video
      summary: /api/v1/video/retrieve
      description: >-
        Retrieve a video generation result. Returns the video file if completed,
        or a status if the request is still processing.
      operationId: retrieveVideo
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RetrieveVideoRequest'
      responses:
        '200':
          description: Video file if completed, or processing status if still in progress
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    enum:
                      - PROCESSING
                    description: The status of the video generation request.
                    example: PROCESSING
                  average_execution_time:
                    type: number
                    description: >-
                      The average execution time of the video generation request
                      in milliseconds.
                    example: 145000
                  execution_duration:
                    type: number
                    description: >-
                      The current duration of the video generation request in
                      milliseconds.
                    example: 53200
                required:
                  - status
                  - average_execution_time
                  - execution_duration
            video/mp4:
              schema:
                format: binary
                type: string
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
        '404':
          description: >-
            Media could not be found. Request may may be invalid, expired, or
            deleted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StandardError'
        '422':
          description: >-
            Your prompt violates the content policy of Venice.ai or the model
            provider
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
        '503':
          description: The model is at capacity. Please try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StandardError'
components:
  schemas:
    RetrieveVideoRequest:
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
        delete_media_on_completion:
          type: boolean
          default: false
          description: >-
            If true, the video media will be deleted from storage after the
            request is completed. If false, you can use the complete endpoint to
            remove the media once you have successfully downloaded the video.
          example: false
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