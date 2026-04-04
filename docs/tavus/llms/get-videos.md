# Source: https://docs.tavus.io/api-reference/video-request/get-videos.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Videos

> This endpoint returns a list of all Videos created by the account associated with the API Key in use.




## OpenAPI

````yaml get /v2/videos
openapi: 3.0.3
info:
  title: Tavus Developer API Collection
  version: 1.0.0
  contact: {}
servers:
  - url: https://tavusapi.com
security:
  - apiKey: []
tags:
  - name: Videos
  - name: Replicas
  - name: Conversations
  - name: Personas
  - name: Replacements
  - name: Transcriptions
  - name: Documents
paths:
  /v2/videos:
    get:
      tags:
        - Videos
      summary: List Videos
      description: >
        This endpoint returns a list of all Videos created by the account
        associated with the API Key in use.
      operationId: listVideos
      parameters:
        - in: query
          name: limit
          schema:
            type: integer
          description: The number of videos to return per page. Default is 10.
        - in: query
          name: page
          schema:
            type: integer
          description: The page number to return. Default is 1.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
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
                    type: integer
                    description: The total number of videos given the filters provided.
        '401':
          description: UNAUTHORIZED
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: The error message.
                    example: Invalid access token
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````