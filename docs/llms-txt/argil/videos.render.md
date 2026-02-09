# Source: https://docs.argil.ai/api-reference/endpoint/videos.render.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Render a Video by id

> Returns a single Video object, with its updated status and information



## OpenAPI

````yaml post /videos/{id}/render
openapi: 3.0.1
info:
  title: Argil API
  description: API for AI clone video generation
  version: 1.0.0
  license:
    name: MIT
servers:
  - url: https://api.argil.ai/v1
security:
  - ApiKeyAuth: []
paths:
  /videos/{id}/render:
    post:
      summary: Render a Video by id
      description: Returns a single Video object, with its updated status and information
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            description: The id of the Video to render
      responses:
        '200':
          description: Detailed information about the Video
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Video'
        '400':
          description: Unexpected error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          description: Video not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    Video:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time
        status:
          type: string
          description: >-
            Can be either `IDLE`, `GENERATING_AUDIO`, `GENERATING_VIDEO`, `DONE`
            or `FAILED`.
        moments:
          type: array
          description: >-
            An array of Moment items, each representing a portion of the
            complete video.
          items:
            type: object
            properties:
              transcript:
                type: string
                description: >-
                  A portion of the complete transcript. Current limit: 250
                  characters.
              avatarId:
                type: string
                description: The id of the avatar to be used for this moment.
              voiceId:
                type: string
                description: The id of the voice to be used for this moment.
              audioUrl:
                type: string
                description: >-
                  The audio that will be used for the video rendering.
                  Automatically generated from the transcript when not provided.
                  Current limit: 20 seconds.
              videoUrl:
                type: string
                description: The url of the avatar rendering video for this moment.
              gestureSlug:
                type: string
                description: The slug identifier of the gesture to be used for this moment.
        videoUrl:
          type: string
          description: >-
            The url of the final avatar rendering video, containing all the
            moments merged.
        videoUrlSubtitled:
          type: string
          description: >-
            The url of the final avatar rendering video with subtitles. Only
            available if subtitles are enabled.
        previewUrl:
          type: string
          description: >-
            Url to the embedable preview of the video. Can be watched from web
            browsers or integrated in other websites before launching the
            generation. For embedable mode, add ?embed=true to the url.
        aspectRatio:
          type: string
          enum:
            - '16:9'
            - '9:16'
          description: 'The aspect ratio of the video output: 16:9 or 9:16.'
        subtitles:
          type: object
          properties:
            enable:
              type: boolean
          description: Subtitles settings for the video
        extras:
          type: object
          description: >-
            A dictionary of custom key-value pairs to extend the video metadata.
            Maximum of 5 key-value pairs of 256 characters allowed.
          additionalProperties:
            type: string
          maxProperties: 10
    Error:
      type: object
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
      description: API key to be included in the x-api-key header

````