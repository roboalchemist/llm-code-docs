# Source: https://docs.argil.ai/api-reference/endpoint/videos.list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Paginated list of Videos

> Returns a paginated array of Videos



## OpenAPI

````yaml get /videos
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
  /videos:
    get:
      summary: Paginated list of Videos
      description: Returns a paginated array of Videos
      parameters:
        - name: page
          in: query
          description: Page number of the video list
          required: false
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          description: Number of videos per page
          required: false
          schema:
            type: integer
            default: 10
        - name: nameSearchQuery
          in: query
          description: Filter videos by name, case-insensitive substring match.
          required: false
          schema:
            type: string
        - name: avatarId
          in: query
          description: Filter videos by avatar ID.
          required: false
          schema:
            type: string
        - name: voiceId
          in: query
          description: Filter videos by voice ID.
          required: false
          schema:
            type: string
        - name: extrasFilter
          in: query
          description: >-
            A JSON string representing filters to apply on the extras JSON
            field. Must be a valid JSON object as a string, specifying
            properties and values to match.
          required: false
          schema:
            type: string
            example: '{"X_ID": "YOUR_CUSTOM_ID"}'
      responses:
        '200':
          description: A paginated list of Videos
          content:
            application/json:
              schema:
                type: object
                properties:
                  totalItems:
                    type: integer
                    description: Total number of videos available
                  totalPages:
                    type: integer
                    description: Total number of pages
                  currentPage:
                    type: integer
                    description: Current page number
                  itemsPerPage:
                    type: integer
                    description: Number of items per page
                  videos:
                    type: array
                    items:
                      $ref: '#/components/schemas/Video'
        '400':
          description: Unexpected error
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