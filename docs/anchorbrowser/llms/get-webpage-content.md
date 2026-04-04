# Source: https://docs.anchorbrowser.io/api-reference/tools/get-webpage-content.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Webpage Content

> Retrieve the rendered content of a webpage, optionally formatted as Markdown or HTML.



## OpenAPI

````yaml openapi-mintlify.yaml post /v1/tools/fetch-webpage
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
  /v1/tools/fetch-webpage:
    post:
      tags:
        - Tools
      summary: Get Webpage Content
      description: >-
        Retrieve the rendered content of a webpage, optionally formatted as
        Markdown or HTML.
      parameters:
        - in: query
          name: sessionId
          schema:
            type: string
          description: >-
            An optional browser session identifier to reference an existing
            running browser session. If provided, the tool will execute within
            that browser session.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FetchWebpageRequestSchema'
      responses:
        '200':
          description: The fetched webpage content in the specified format.
          content:
            text/plain:
              schema:
                type: string
                description: The rendered content of the webpage.
        '400':
          description: Invalid request, such as missing or invalid URL.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal server error while processing the request.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    FetchWebpageRequestSchema:
      type: object
      properties:
        url:
          type: string
          description: >-
            The URL of the webpage to fetch content from. When left empty, the
            current webpage is used.
        format:
          type: string
          description: The output format of the content.
          enum:
            - html
            - markdown
        wait:
          type: integer
          description: >-
            The time to wait for **dynamic** content to load in
            **milliseconds**.
        new_page:
          type: boolean
          description: Whether to create a new page for the content.
        page_index:
          type: integer
          description: The index of the page to fetch content from. **Overides new_page**.
        return_partial_on_timeout:
          type: boolean
          description: >-
            Whether to return partial content if the content is not loaded
            within the 20 seconds.
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