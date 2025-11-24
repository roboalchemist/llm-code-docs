# Source: https://docs.tavus.io/api-reference/video-request/get-video.md

# Get Video

> This endpoint returns a single video by its unique identifier. 

The response body will contain a `status` string that represents the status of the video. If the video is ready, the response body will also contain a `download_url`, `stream_url`, and `hosted_url` that can be used to download, stream, and view the video respectively.


## OpenAPI

````yaml get /v2/videos/{video_id}
paths:
  path: /v2/videos/{video_id}
  method: get
  servers:
    - url: https://tavusapi.com
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
          cookie: {}
    parameters:
      path:
        video_id:
          schema:
            - type: string
              required: true
              description: A unique identifier for the video.
      query:
        verbose:
          schema:
            - type: boolean
              description: >-
                If set to true, the response will include additional video data
                such as the thumbnail image and gif links.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              video_id:
                allOf:
                  - type: string
                    example: ''
                    description: A unique identifier for the video.
              video_name:
                allOf:
                  - type: string
                    description: The name of the video.
              status:
                allOf:
                  - type: string
                    example: ready
                    description: >-
                      The status of the video. Possible values: queued,
                      generating, ready, deleted, error.
              data:
                allOf:
                  - type: object
                    properties:
                      script:
                        type: string
                        description: >-
                          The script that was initially used to generate the
                          video.
              download_url:
                allOf:
                  - type: string
                    description: A direct link to download your generated video.
              stream_url:
                allOf:
                  - type: string
                    description: A direct link to stream your generated video.
              hosted_url:
                allOf:
                  - type: string
                    description: >-
                      A direct link to view your generated video, hosted by
                      Tavus.
              status_details:
                allOf:
                  - type: string
                    description: A detailed status of the video.
              created_at:
                allOf:
                  - type: string
                    description: The date and time the video was created.
              updated_at:
                allOf:
                  - type: string
                    description: The date and time of when the video was last updated.
              still_image_thumbnail_url:
                allOf:
                  - type: string
                    description: >-
                      Included if the `verbose` query parameter is set to true.
                      A link to an image thumbnail of the video.
              gif_thumbnail_url:
                allOf:
                  - type: string
                    description: >-
                      Included if the `verbose` query parameter is set to true.
                      A link to a gif thumbnail of the video.
        examples:
          example:
            value:
              video_id: ''
              video_name: <string>
              status: ready
              data:
                script: <string>
              download_url: <string>
              stream_url: <string>
              hosted_url: <string>
              status_details: <string>
              created_at: <string>
              updated_at: <string>
              still_image_thumbnail_url: <string>
              gif_thumbnail_url: <string>
        description: OK
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid video_id
        examples:
          example:
            value:
              error: Invalid video_id
        description: Bad Request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid access token
        examples:
          example:
            value:
              message: Invalid access token
        description: UNAUTHORIZED
  deprecated: false
  type: path
components:
  schemas: {}

````