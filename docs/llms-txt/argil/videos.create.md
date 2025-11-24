# Source: https://docs.argil.ai/api-reference/endpoint/videos.create.md

# Create a new Video

> Creates a new Video with the specified details

## OpenAPI

````yaml post /videos
paths:
  path: /videos
  method: post
  servers:
    - url: https://api.argil.ai/v1
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
              description: API key to be included in the x-api-key header
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
              moments:
                allOf:
                  - type: array
                    description: >-
                      An array of Moment items, each representing a portion of
                      the complete video.
                    items:
                      type: object
                      required:
                        - transcript
                        - avatarId
                      properties:
                        transcript:
                          type: string
                          description: >-
                            A portion of the complete transcript. Current limit:
                            250 characters
                        avatarId:
                          type: string
                          description: The id of the avatar to be used for this moment
                        voiceId:
                          type: string
                          description: >-
                            The id of the voice to be used for this moment.
                            Optional, default is the avatar's voice.
                        gestureSlug:
                          type: string
                          description: >-
                            The slug identifier of the gesture to be used for
                            this moment
                        audioUrl:
                          type: string
                          description: >-
                            Optional url to the audio to be used for the video
                            rendering, for bypassing our audio generation model.
                            Current limit: 20 seconds
                        zoom:
                          type: object
                          description: >-
                            Controls the zoom level of the viewport/display,
                            allowing content to be scaled larger or smaller
                          required:
                            - level
                          properties:
                            level:
                              type: number
                              minimum: 1
                              maximum: 2
                              default: 1
                              description: >-
                                Specifies the zoom scaling factor where 1.0
                                represents 100% (original size), and 2.0 is 200%
                                (zoomed in)
                          additionalProperties: false
                      additionalProperties: false
              subtitles:
                allOf:
                  - type: object
                    properties:
                      enable:
                        type: boolean
                      styleId:
                        type: string
                        description: >-
                          ID of the subtitle style to apply. Styles can be
                          fetched from the /subtitles endpoint.
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
                allOf:
                  - type: string
                    enum:
                      - '16:9'
                      - '9:16'
                    description: >-
                      Select desired output aspectRatio: 16:9 or 9:16. Optional,
                      default depends on used avatar.
              enableAutoBrolls:
                allOf:
                  - type: boolean
                    description: >-
                      [DEPRECATED] Enable automatic B-roll generation and
                      placement. When enabled, the system will analyze your
                      content and automatically add relevant B-rolls to
                      appropriate moments.
              autoBrolls:
                allOf:
                  - type: object
                    description: >-
                      Configuration for automatic B-roll generation and
                      placement.
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
                          Source for B-rolls: 'GENERATION' for generated images
                          or 'GOOGLE_IMAGES' for images from Google,
                          'STOCKS_VIDEO' for GettyImages videos or
                          'AVATAR_ACTION' for generated videos including the
                          avatar (only available with AI Influencer avatars).
                      intensity:
                        type: string
                        enum:
                          - LOW
                          - MEDIUM
                          - HIGH
                        description: >-
                          Intensity level of B-rolls: 'LOW', 'MEDIUM', or
                          'HIGH'. Not available for 'AVATAR_ACTION' source.
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
                          Layout control for moments containing a B-roll.
                          Controls how the B-rolls appears relative to the
                          avatar.
                    required:
                      - enable
                      - source
                      - intensity
              extras:
                allOf:
                  - type: object
                    description: >-
                      Optional dictionary of custom key-value pairs to extend
                      the video metadata. Maximum of 5 key-value pairs of 256
                      characters allowed
                    additionalProperties:
                      type: string
                    maxProperties: 10
              backgroundMusic:
                allOf:
                  - type: object
                    description: Optional configuration for background music
                    properties:
                      assetId:
                        type: string
                        description: ID of an audio asset to use as background music
                      volume:
                        type: number
                        description: >-
                          Volume level of the background music (0-1). Default is
                          0.14
                        minimum: 0
                        maximum: 1
                    required:
                      - assetId
              model:
                allOf:
                  - type: string
                    enum:
                      - ARGIL_V1
                      - ARGIL_ATOM
                    description: Model to use for the video generation.
            required: true
            refIdentifier: '#/components/schemas/VideoCreateArgs'
            requiredProperties:
              - name
              - moments
        examples:
          example:
            value:
              name: <string>
              moments:
                - transcript: <string>
                  avatarId: <string>
                  voiceId: <string>
                  gestureSlug: <string>
                  audioUrl: <string>
                  zoom:
                    level: 1
              subtitles:
                enable: true
                styleId: <string>
                position: Top
                size: Small
              aspectRatio: '16:9'
              enableAutoBrolls: true
              autoBrolls:
                enable: true
                source: GENERATION
                intensity: LOW
                layout: FULLSCREEN
              extras: {}
              backgroundMusic:
                assetId: <string>
                volume: 0.5
              model: ARGIL_V1
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid
              name:
                allOf:
                  - type: string
              createdAt:
                allOf:
                  - type: string
                    format: date-time
              updatedAt:
                allOf:
                  - type: string
                    format: date-time
              status:
                allOf:
                  - type: string
                    description: >-
                      Can be either `IDLE`, `GENERATING_AUDIO`,
                      `GENERATING_VIDEO`, `DONE` or `FAILED`.
              moments:
                allOf:
                  - type: array
                    description: >-
                      An array of Moment items, each representing a portion of
                      the complete video.
                    items:
                      type: object
                      properties:
                        transcript:
                          type: string
                          description: >-
                            A portion of the complete transcript. Current limit:
                            250 characters.
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
                            Automatically generated from the transcript when not
                            provided. Current limit: 20 seconds.
                        videoUrl:
                          type: string
                          description: >-
                            The url of the avatar rendering video for this
                            moment.
                        gestureSlug:
                          type: string
                          description: >-
                            The slug identifier of the gesture to be used for
                            this moment.
              videoUrl:
                allOf:
                  - type: string
                    description: >-
                      The url of the final avatar rendering video, containing
                      all the moments merged.
              videoUrlSubtitled:
                allOf:
                  - type: string
                    description: >-
                      The url of the final avatar rendering video with
                      subtitles. Only available if subtitles are enabled.
              subtitles:
                allOf:
                  - type: object
                    properties:
                      enable:
                        type: boolean
                    description: Subtitles settings for the video
              extras:
                allOf:
                  - type: object
                    description: >-
                      A dictionary of custom key-value pairs to extend the video
                      metadata. Maximum of 5 key-value pairs of 256 characters
                      allowed.
                    additionalProperties:
                      type: string
                    maxProperties: 10
            refIdentifier: '#/components/schemas/Video'
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              name: <string>
              createdAt: '2023-11-07T05:31:56Z'
              updatedAt: '2023-11-07T05:31:56Z'
              status: <string>
              moments:
                - transcript: <string>
                  avatarId: <string>
                  voiceId: <string>
                  audioUrl: <string>
                  videoUrl: <string>
                  gestureSlug: <string>
              videoUrl: <string>
              videoUrlSubtitled: <string>
              subtitles:
                enable: true
              extras: {}
        description: Successfully created Video
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              code:
                allOf:
                  - type: integer
                    format: int32
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              code: 123
              message: <string>
        description: Validation error
  deprecated: false
  type: path
components:
  schemas: {}

````