# Source: https://docs.argil.ai/api-reference/endpoint/videos.list.md

# Paginated list of Videos

> Returns a paginated array of Videos

## OpenAPI

````yaml get /videos
paths:
  path: /videos
  method: get
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
      query:
        page:
          schema:
            - type: integer
              required: false
              description: Page number of the video list
              default: 1
        limit:
          schema:
            - type: integer
              required: false
              description: Number of videos per page
              default: 10
        nameSearchQuery:
          schema:
            - type: string
              required: false
              description: Filter videos by name, case-insensitive substring match.
        avatarId:
          schema:
            - type: string
              required: false
              description: Filter videos by avatar ID.
        voiceId:
          schema:
            - type: string
              required: false
              description: Filter videos by voice ID.
        extrasFilter:
          schema:
            - type: string
              required: false
              description: >-
                A JSON string representing filters to apply on the extras JSON
                field. Must be a valid JSON object as a string, specifying
                properties and values to match.
              example: '{"X_ID": "YOUR_CUSTOM_ID"}'
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              totalItems:
                allOf:
                  - type: integer
                    description: Total number of videos available
              totalPages:
                allOf:
                  - type: integer
                    description: Total number of pages
              currentPage:
                allOf:
                  - type: integer
                    description: Current page number
              itemsPerPage:
                allOf:
                  - type: integer
                    description: Number of items per page
              videos:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/Video'
        examples:
          example:
            value:
              totalItems: 123
              totalPages: 123
              currentPage: 123
              itemsPerPage: 123
              videos:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
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
        description: A paginated list of Videos
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
        description: Unexpected error
  deprecated: false
  type: path
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

````