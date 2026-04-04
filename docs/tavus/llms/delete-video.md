# Source: https://docs.tavus.io/api-reference/video-request/delete-video.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Video

> This endpoint deletes a single video by its unique identifier.




## OpenAPI

````yaml delete /v2/videos/{video_id}
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
    delete:
      tags:
        - Videos
      summary: Delete Video
      description: |
        This endpoint deletes a single video by its unique identifier.
      operationId: deleteVideo
      parameters:
        - name: video_id
          in: path
          required: true
          description: The unique identifier of the video generation.
          schema:
            type: string
            example: 8a4f94e736
        - name: hard
          in: query
          schema:
            type: boolean
            example: false
          description: >-
            If set to true, the video and associated assets (such as thumbnail
            images) will be hard deleted. CAUTION: This action is irrevocable.
      responses:
        '200':
          description: ''
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