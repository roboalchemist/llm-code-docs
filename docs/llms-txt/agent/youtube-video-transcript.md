# Source: https://docs.agent.ai/api-reference/get-data/youtube-video-transcript.md

# YouTube Video Transcript

> Fetches the transcript of a YouTube video using the video URL.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_youtube_transcript
paths:
  path: /action/get_youtube_transcript
  method: post
  servers:
    - url: https://api-lr.agent.ai/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer token from your account
                ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))
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
              url:
                allOf:
                  - type: string
                    format: url
                    description: URL of the YouTube video.
                    example: https://youtube.com/watch?v=example
            required: true
            requiredProperties:
              - url
        examples:
          example:
            value:
              url: https://youtube.com/watch?v=example
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    description: HTTP status code of the action response
              metadata:
                allOf:
                  - type: object
                    description: Video metadata from the action
              response:
                allOf:
                  - type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/YouTubeVideoTranscriptResponse'
        examples:
          example:
            value:
              status: 200
              metadata:
                author: Sequoia Capital
                category: People & Blogs
                channel_id: UCWrF0oN6unbXrWsTN7RctTw
                channel_link: http://www.youtube.com/@sequoiacapital
                channel_name: Sequoia Capital
                description: >-
                  The landscape is wide open. The opportunity set is massive. At
                  our second Sequoia Capital AI Ascent, Sonya Huang, Pat Grady,
                  and Konstantine Buhler discuss the way AI is already providing
                  glimpses of enduring value, and how this technology will help
                  us do more with less so that we can solve more problems,
                  create more, and build a better future.


                  #AI #AIAscent #Sequoia #Startup #Founder #entrepreneur
                id: TDPqt7ONUCY
                key_moments: []
                length_seconds: 1616
                likes: 1800
                published_time: Mar 26, 2024
                thumbnail: https://i.ytimg.com/vi_webp/TDPqt7ONUCY/maxresdefault.webp
                title: >-
                  The AI opportunity: Sequoia Capital's AI Ascent 2024 opening
                  remarks
                views: 101403
              response: >-
                The AI opportunity: Sequoia Capital's AI Ascent 2024 opening
                remarks

                my name is pack Rady I'm one of the members...
        description: Transcript of the YouTube video
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 400
              response: null
              error: >-
                The requested page doesn't exist or there are no translations
                available for the video.
        description: Transcript of the YouTube video
  deprecated: false
  type: path
components:
  schemas: {}

````