# Source: https://docs.tavus.io/api-reference/video-request/patch-video-name.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Rename Video

> This endpoint renames a single video by its unique identifier.




## OpenAPI

````yaml patch /v2/videos/{video_id}/name
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
  /v2/videos/{video_id}/name:
    parameters:
      - name: video_id
        in: path
        required: true
        description: The unique identifier of the video generation.
        schema:
          type: string
          example: 8a4f94e736
    patch:
      tags:
        - Videos
      summary: Rename Video
      description: |
        This endpoint renames a single video by its unique identifier.
      operationId: renameVideo
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                video_name:
                  type: string
                  example: Sales
              required:
                - video_name
            examples:
              Rename Video:
                value:
                  video_name: Sales
      responses:
        '200':
          description: OK
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