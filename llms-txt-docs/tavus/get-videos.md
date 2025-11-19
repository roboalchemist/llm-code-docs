# Source: https://docs.tavus.io/api-reference/video-request/get-videos.md

# List Videos

> This endpoint returns a list of all Videos created by the account associated with the API Key in use.


## OpenAPI

````yaml get /v2/videos
paths:
  path: /v2/videos
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
      path: {}
      query:
        limit:
          schema:
            - type: integer
              description: The number of videos to return per page. Default is 10.
        page:
          schema:
            - type: integer
              description: The page number to return. Default is 1.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        video_id:
                          type: string
                          description: A unique identifier for the video.
                          example: 783537ef5
                        video_name:
                          type: string
                          description: A name for the video.
                          example: My First Video
                        status:
                          type: string
                          description: >-
                            The status of the video. Possible values: queued,
                            generating, ready, deleted, error.
                          example: generating
                        data:
                          type: object
                          properties:
                            script:
                              type: string
                              description: >-
                                The script that was initially used to generate
                                the video.
                              example: Hello from Tavus! Enjoy your new replica
                        download_url:
                          type: string
                          description: A link to download the video.
                          example: ''
                        hosted_url:
                          type: string
                          description: A link to view the video.
                        stream_url:
                          type: string
                          description: A link to stream the video.
                          example: ''
                        status_details:
                          type: string
                          description: A detailed status of the video.
                          example: ''
                        background_url:
                          type: string
                          description: >-
                            A link to a website. This will be used as the
                            background for the video. The website must be
                            publicly accessible and properly formed.
                          example: ''
                        background_source_url:
                          type: string
                          description: >-
                            A direct link to a video that is publicly accessible
                            via a storage location such as an S3 bucket. This
                            will be used as the background for the video. The
                            video must be publicly accessible.
                          example: ''
                        still_image_thumbnail_url:
                          type: string
                          description: >-
                            A link to a still image that is a thumbnail of the
                            video.
                          example: ''
                        gif_thumbnail_url:
                          type: string
                          description: A link to a gif that is a thumbnail of the video.
                          example: ''
                        error_details:
                          type: string
                          description: >-
                            If the video has an error, this will contain the
                            error message.
                          example: ''
              total_count:
                allOf:
                  - type: integer
                    description: The total number of videos given the filters provided.
        examples:
          example:
            value:
              data:
                - video_id: 783537ef5
                  video_name: My First Video
                  status: generating
                  data:
                    script: Hello from Tavus! Enjoy your new replica
                  download_url: ''
                  hosted_url: <string>
                  stream_url: ''
                  status_details: ''
                  background_url: ''
                  background_source_url: ''
                  still_image_thumbnail_url: ''
                  gif_thumbnail_url: ''
                  error_details: ''
              total_count: 123
        description: ''
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