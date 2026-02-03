# Source: https://docs.argil.ai/api-reference/endpoint/videos.create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new Video

> Creates a new Video with the specified details



## OpenAPI

````yaml post /videos
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
    post:
      summary: Create a new Video
      description: Creates a new Video with the specified details
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/VideoCreateArgs'
      responses:
        '201':
          description: Successfully created Video
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Video'
        '400':
          description: Validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    VideoCreateArgs:
      type: object
      required:
        - name
        - moments
      properties:
        name:
          type: string
        moments:
          type: array
          description: >-
            An array of Moment items, each representing a portion of the
            complete video.
          items:
            type: object
            required:
              - transcript
              - avatarId
            properties:
              transcript:
                type: string
                description: >-
                  A portion of the complete transcript. Current limit: 250
                  characters
              avatarId:
                type: string
                description: The id of the avatar to be used for this moment
              voiceId:
                type: string
                description: >-
                  The id of the voice to be used for this moment. Optional,
                  default is the avatar's voice.
              gestureSlug:
                type: string
                description: The slug identifier of the gesture to be used for this moment
              audioUrl:
                type: string
                description: >-
                  Optional url to the audio to be used for the video rendering,
                  for bypassing our audio generation model. Current limit: 20
                  seconds
              zoom:
                type: object
                description: >-
                  Controls the zoom level of the viewport/display, allowing
                  content to be scaled larger or smaller
                required:
                  - level
                properties:
                  level:
                    type: number
                    minimum: 1
                    maximum: 2
                    default: 1
                    description: >-
                      Specifies the zoom scaling factor where 1.0 represents
                      100% (original size), and 2.0 is 200% (zoomed in)
                additionalProperties: false
            additionalProperties: false
        subtitles:
          type: object
          properties:
            enable:
              type: boolean
            styleId:
              type: string
              description: >-
                ID of the subtitle style to apply. Styles can be fetched from
                the /subtitles endpoint.
            position:
              type: string
              enum:
                - Top
                - Middle
                - Bottom
              description: Position of subtitles on the video
            size:
              type: string
              enum:
                - Small
                - Medium
                - Large
              description: Size of the subtitle text
          required:
            - enable
          additionalProperties: false
          description: Subtitles settings for the video
        aspectRatio:
          type: string
          enum:
            - '16:9'
            - '9:16'
          description: >-
            Select desired output aspectRatio: 16:9 or 9:16. Optional, default
            depends on used avatar.
        enableAutoBrolls:
          type: boolean
          description: >-
            [DEPRECATED] Enable automatic B-roll generation and placement. When
            enabled, the system will analyze your content and automatically add
            relevant B-rolls to appropriate moments.
        autoBrolls:
          type: object
          description: Configuration for automatic B-roll generation and placement.
          properties:
            enable:
              type: boolean
              description: Enable or disable automatic B-roll generation.
            source:
              type: string
              enum:
                - GENERATION
                - GOOGLE_IMAGES
                - STOCKS_VIDEO
                - AVATAR_ACTION
              description: >-
                Source for B-rolls: 'GENERATION' for generated images or
                'GOOGLE_IMAGES' for images from Google, 'STOCKS_VIDEO' for
                GettyImages videos or 'AVATAR_ACTION' for generated videos
                including the avatar (only available with AI Influencer
                avatars).
            intensity:
              type: string
              enum:
                - LOW
                - MEDIUM
                - HIGH
              description: >-
                Intensity level of B-rolls: 'LOW', 'MEDIUM', or 'HIGH'. Not
                available for 'AVATAR_ACTION' source.
            layout:
              type: string
              enum:
                - FULLSCREEN
                - AVATAR_BOTTOM_LEFT
                - AVATAR_BOTTOM_RIGHT
                - AVATAR_TOP_LEFT
                - AVATAR_TOP_RIGHT
                - SPLIT_AVATAR_LEFT
                - SPLIT_AVATAR_RIGHT
                - SPLIT_AVATAR_TOP
                - SPLIT_AVATAR_BOTTOM
                - BACKGROUND
              description: >-
                Layout control for moments containing a B-roll. Controls how the
                B-rolls appears relative to the avatar.
          required:
            - enable
            - source
            - intensity
        extras:
          type: object
          description: >-
            Optional dictionary of custom key-value pairs to extend the video
            metadata. Maximum of 5 key-value pairs of 256 characters allowed
          additionalProperties:
            type: string
          maxProperties: 10
        backgroundMusic:
          type: object
          description: Optional configuration for background music
          properties:
            assetId:
              type: string
              description: ID of an audio asset to use as background music
            volume:
              type: number
              description: Volume level of the background music (0-1). Default is 0.14
              minimum: 0
              maximum: 1
          required:
            - assetId
        model:
          type: string
          enum:
            - ARGIL_V1
            - ARGIL_ATOM
          description: Model to use for the video generation.
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