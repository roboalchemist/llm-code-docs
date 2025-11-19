# Source: https://docs.tavus.io/api-reference/video-request/delete-video.md

# Delete Video

> This endpoint deletes a single video by its unique identifier.


## OpenAPI

````yaml delete /v2/videos/{video_id}
paths:
  path: /v2/videos/{video_id}
  method: delete
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
              description: The unique identifier of the video generation.
              example: 8a4f94e736
      query:
        hard:
          schema:
            - type: boolean
              description: >-
                If set to true, the video and associated assets (such as
                thumbnail images) will be hard deleted. CAUTION: This action is
                irrevocable.
              example: false
      header: {}
      cookie: {}
    body: {}
  response:
    '200': {}
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