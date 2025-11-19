# Source: https://docs.tavus.io/api-reference/video-request/patch-video-name.md

# Rename Video

> This endpoint renames a single video by its unique identifier.


## OpenAPI

````yaml patch /v2/videos/{video_id}/name
paths:
  path: /v2/videos/{video_id}/name
  method: patch
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              video_name:
                allOf:
                  - type: string
                    example: Sales
            requiredProperties:
              - video_name
        examples:
          Rename Video:
            value:
              video_name: Sales
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: OK
        examples: {}
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