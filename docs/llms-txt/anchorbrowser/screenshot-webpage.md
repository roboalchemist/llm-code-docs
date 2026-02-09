# Source: https://docs.anchorbrowser.io/api-reference/tools/screenshot-webpage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Screenshot Webpage

> This endpoint captures a screenshot of the specified webpage using Chromium. Users can customize the viewport dimensions and capture options.



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/tools/screenshot
openapi: 3.1.0
info:
  title: AnchorBrowser API
  version: 1.0.0
  description: APIs to manage all browser-related actions and configuration.
servers:
  - url: https://api.anchorbrowser.io
    description: API server
security: []
paths:
  /v1/tools/screenshot:
    post:
      tags:
        - Tools
      summary: Screenshot Webpage
      description: >-
        This endpoint captures a screenshot of the specified webpage using
        Chromium. Users can customize the viewport dimensions and capture
        options.
      parameters:
        - in: query
          name: sessionId
          schema:
            type: string
          description: >-
            An optional browser session identifier to reference an existing
            running browser sessions. When passed, the tool will be executed on
            the provided browser session.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ScreenshotRequestSchema'
      responses:
        '200':
          description: Screenshot successfully captured.
          content:
            image/png:
              schema:
                type: string
                format: binary
        '400':
          description: Invalid input parameters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to take screenshot.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    ScreenshotRequestSchema:
      type: object
      properties:
        url:
          type: string
          description: The URL of the webpage to capture.
        width:
          type: integer
          description: The width of the browser viewport in pixels.
        height:
          type: integer
          description: The height of the browser viewport in pixels.
        image_quality:
          type: integer
          description: >-
            Quality of the output image, on the range 1-100. 100 will not
            perform any compression.
        wait:
          type: integer
          description: >-
            Duration in milliseconds to wait after page has loaded, mainly used
            for sites with JS animations.
        scroll_all_content:
          type: boolean
          description: If true, scrolls the page and captures all visible content.
        capture_full_height:
          type: boolean
          description: >-
            If true, captures the entire height of the page, ignoring the
            viewport height.
        s3_target_address:
          type: string
          description: Presigned S3 url target to upload the image to.
    ErrorResponse:
      type: object
      properties:
        error:
          type: object
          properties:
            code:
              type: integer
            message:
              type: string
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````