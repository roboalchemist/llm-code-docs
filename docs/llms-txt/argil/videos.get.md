# Source: https://docs.argil.ai/api-reference/endpoint/videos.get.md

# Get a Video by id

> Returns a single Video identified by its id

## OpenAPI

````yaml get /videos/{id}
paths:
  path: /videos/{id}
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: The id of the Video to retrieve
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
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
        description: Detailed information about the Video
    '404':
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
        description: Video not found
  deprecated: false
  type: path
components:
  schemas: {}

````