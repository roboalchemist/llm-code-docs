# Source: https://docs.tavus.io/api-reference/video-request/get-video.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Video

> This endpoint returns a single video by its unique identifier. 

The response body will contain a `status` string that represents the status of the video. If the video is ready, the response body will also contain a `download_url`, `stream_url`, and `hosted_url` that can be used to download, stream, and view the video respectively.




## OpenAPI

````yaml get /v2/videos/{video_id}
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
  /v2/videos/{video_id}:
    get:
      tags:
        - Videos
      summary: Get Video
      description: >
        This endpoint returns a single video by its unique identifier. 


        The response body will contain a `status` string that represents the
        status of the video. If the video is ready, the response body will also
        contain a `download_url`, `stream_url`, and `hosted_url` that can be
        used to download, stream, and view the video respectively.
      operationId: getVideo
      parameters:
        - in: path
          name: video_id
          required: true
          schema:
            type: string
          description: A unique identifier for the video.
        - in: query
          name: verbose
          schema:
            type: boolean
          description: >-
            If set to true, the response will include additional video data such
            as the thumbnail image and gif links.
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  video_id:
                    type: string
                    example: ''
                    description: A unique identifier for the video.
                  video_name:
                    type: string
                    description: The name of the video.
                  status:
                    type: string
                    example: ready
                    description: >-
                      The status of the video. Possible values: queued,
                      generating, ready, deleted, error.
                  data:
                    type: object
                    properties:
                      script:
                        type: string
                        description: >-
                          The script that was initially used to generate the
                          video.
                  download_url:
                    type: string
                    description: A direct link to download your generated video.
                  stream_url:
                    type: string
                    description: A direct link to stream your generated video.
                  hosted_url:
                    type: string
                    description: >-
                      A direct link to view your generated video, hosted by
                      Tavus.
                  status_details:
                    type: string
                    description: A detailed status of the video.
                  created_at:
                    type: string
                    description: The date and time the video was created.
                  updated_at:
                    type: string
                    description: The date and time of when the video was last updated.
                  still_image_thumbnail_url:
                    type: string
                    description: >-
                      Included if the `verbose` query parameter is set to true.
                      A link to an image thumbnail of the video.
                  gif_thumbnail_url:
                    type: string
                    description: >-
                      Included if the `verbose` query parameter is set to true.
                      A link to a gif thumbnail of the video.
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message.
                    example: Invalid video_id
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