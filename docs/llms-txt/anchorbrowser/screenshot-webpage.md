# Source: https://docs.anchorbrowser.io/api-reference/tools/screenshot-webpage.md

# Screenshot Webpage

> This endpoint captures a screenshot of the specified webpage using Chromium. Users can customize the viewport dimensions and capture options.

## OpenAPI

````yaml openapi-mintlify.yaml post /v1/tools/screenshot
paths:
  path: /v1/tools/screenshot
  method: post
  servers:
    - url: https://api.anchorbrowser.io
      description: API server
  request:
    security:
      - title: api key header
        parameters:
          query: {}
          header:
            anchor-api-key:
              type: apiKey
              description: API key passed in the header
          cookie: {}
    parameters:
      path: {}
      query:
        sessionId:
          schema:
            - type: string
              description: >-
                An optional browser session identifier to reference an existing
                running browser sessions. When passed, the tool will be executed
                on the provided browser session.
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
                    description: The URL of the webpage to capture.
              width:
                allOf:
                  - type: integer
                    description: The width of the browser viewport in pixels.
              height:
                allOf:
                  - type: integer
                    description: The height of the browser viewport in pixels.
              image_quality:
                allOf:
                  - type: integer
                    description: >-
                      Quality of the output image, on the range 1-100. 100 will
                      not perform any compression.
              wait:
                allOf:
                  - type: integer
                    description: >-
                      Duration in milliseconds to wait after page has loaded,
                      mainly used for sites with JS animations.
              scroll_all_content:
                allOf:
                  - type: boolean
                    description: >-
                      If true, scrolls the page and captures all visible
                      content.
              capture_full_height:
                allOf:
                  - type: boolean
                    description: >-
                      If true, captures the entire height of the page, ignoring
                      the viewport height.
              s3_target_address:
                allOf:
                  - type: string
                    description: Presigned S3 url target to upload the image to.
            required: true
            refIdentifier: '#/components/schemas/ScreenshotRequestSchema'
        examples:
          example:
            value:
              url: <string>
              width: 123
              height: 123
              image_quality: 123
              wait: 123
              scroll_all_content: true
              capture_full_height: true
              s3_target_address: <string>
  response:
    '200':
      image/png:
        schemaArray:
          - type: file
            contentEncoding: binary
        examples:
          example: {}
        description: Screenshot successfully captured.
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: object
                    properties:
                      code:
                        type: integer
                      message:
                        type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Invalid input parameters.
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Failed to take screenshot.
  deprecated: false
  type: path
components:
  schemas: {}

````