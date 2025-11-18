# Source: https://docs.anchorbrowser.io/api-reference/tools/get-webpage-content.md

# Get Webpage Content

> Retrieve the rendered content of a webpage, optionally formatted as Markdown or HTML.

## OpenAPI

````yaml openapi-mintlify.yaml post /v1/tools/fetch-webpage
paths:
  path: /v1/tools/fetch-webpage
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
                running browser session. If provided, the tool will execute
                within that browser session.
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
                    description: >-
                      The URL of the webpage to fetch content from. When left
                      empty, the current webpage is used.
              format:
                allOf:
                  - type: string
                    description: The output format of the content.
                    enum:
                      - html
                      - markdown
              wait:
                allOf:
                  - type: integer
                    description: >-
                      The time to wait for **dynamic** content to load in
                      **milliseconds**.
              new_page:
                allOf:
                  - type: boolean
                    description: Whether to create a new page for the content.
              page_index:
                allOf:
                  - type: integer
                    description: >-
                      The index of the page to fetch content from. **Overides
                      new_page**.
              return_partial_on_timeout:
                allOf:
                  - type: boolean
                    description: >-
                      Whether to return partial content if the content is not
                      loaded within the 20 seconds.
            required: true
            refIdentifier: '#/components/schemas/FetchWebpageRequestSchema'
        examples:
          example:
            value:
              url: <string>
              format: html
              wait: 123
              new_page: true
              page_index: 123
              return_partial_on_timeout: true
  response:
    '200':
      text/plain:
        schemaArray:
          - type: string
            description: The rendered content of the webpage.
        examples:
          example:
            value: <string>
        description: The fetched webpage content in the specified format.
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
        description: Invalid request, such as missing or invalid URL.
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
        description: Internal server error while processing the request.
  deprecated: false
  type: path
components:
  schemas: {}

````