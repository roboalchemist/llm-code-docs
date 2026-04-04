# Source: https://docs.venice.ai/api-reference/endpoint/video/quote.md

# Quote Video Generation

> Quote a video generation request. Utilizes the same parameters as the queue API and will return the price in USD for the request.

***


## OpenAPI

````yaml POST /video/quote
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
  /video/quote:
    post:
      tags:
        - Video
      summary: /api/v1/video/quote
      description: >-
        Quote a video generation request. Utilizes the same parameters as the
        queue API and will return the price in USD for the request.
      operationId: quoteVideo
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/QueueVideoRequest'
      responses:
        '200':
          description: Video generation price quote
          content:
            application/json:
              schema:
                type: object
                properties:
                  quote:
                    type: number
                required:
                  - quote
        '400':
          description: Invalid request parameters
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DetailedError'
components:
  schemas:
    QueueVideoRequest:
      type: object
      properties:
        model:
          type: string
          description: The model to use for image generation.
          example: wan-2.5-preview-image-to-video
        prompt:
          type: string
          minLength: 1
          maxLength: 2500
          description: >-
            The prompt to use for video generation. The maximum length is 2500
            characters.
          example: Commerce being conducted in the city of Venice, Italy.
        negative_prompt:
          type: string
          maxLength: 2500
          default: low resolution, error, worst quality, low quality, defects
          description: >-
            The negative prompt to use for video generation. The maximum length
            is 2500 characters.
          example: low resolution, error, worst quality, low quality, defects
        duration:
          type: string
          enum:
            - 5s
            - 10s
          description: The duration of the video to generate.
          example: 5s
        aspect_ratio:
          description: The aspect ratio of the video to generate.
          example: '16:9'
        resolution:
          type: string
          enum:
            - 1080p
            - 720p
            - 480p
          default: 720p
          description: The resolution of the video to generate.
          example: 720p
        audio:
          description: >-
            For models which support audio generation and configuration,
            indicates if audio should be generated. Defaults to true.
          example: true
        image_url:
          type: string
          description: >-
            For image to video models, the reference image to use for video
            generation. Must be either a URL (starting with "http://" or
            "https://") or a data URL (starting with "data:").
          example: data:image/png;base64,iVBORw0K...
        audio_url:
          type: string
          description: >-
            For models that support audio input, the audio file to use as
            background music. Must be either a URL or a data URL. Supported
            formats: WAV, MP3. Max duration: 30s. Max size: 15MB.
          example: data:audio/mpeg;base64,SUQzBAA...
        video_url:
          description: >-
            For models that support video input, the video file to use as a
            reference. Must be either a URL or a data URL. Supported formats:
            MP4, MOV, WebM.
          example: data:video/mp4;base64,AAAAFGZ0eXA...
      required:
        - model
        - prompt
        - duration
        - image_url
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
  securitySchemes:
    BearerAuth:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.venice.ai/llms.txt