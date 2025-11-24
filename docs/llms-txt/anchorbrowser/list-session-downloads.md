# Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/list-session-downloads.md

# List Session Downloads

> Retrieves metadata of files downloaded during a browser session. Requires a valid API key for authentication.

## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{session_id}/downloads
paths:
  path: /v1/sessions/{session_id}/downloads
  method: get
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
      path:
        session_id:
          schema:
            - type: string
              required: true
              description: >-
                The unique identifier of the browser session to retrieve
                downloads for.
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    properties:
                      count:
                        type: integer
                        description: Total number of downloads
                      items:
                        type: array
                        items:
                          $ref: '#/components/schemas/DownloadItem'
            refIdentifier: '#/components/schemas/DownloadListResponse'
        examples:
          example:
            value:
              data:
                count: 123
                items:
                  - id: <string>
                    file_link: <string>
                    original_download_url: <string>
                    origin_url: <string>
                    suggested_file_name: <string>
                    original_file_name: <string>
                    duration: 123
                    size: 123
                    created_at: '2023-11-07T05:31:56Z'
        description: A list of download metadata associated with the browser session.
    '401':
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
        description: Invalid or missing API key.
    '404':
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
        description: The browser session or its downloads metadata could not be found.
    '429':
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
        description: Too many requests, please try again later.
  deprecated: false
  type: path
components:
  schemas:
    DownloadItem:
      type: object
      properties:
        id:
          type: string
          description: The unique ID of the download record.
        file_link:
          type: string
          format: uri
          description: >-
            The URL to download the file from anchorbrowser servers. Requires
            api key authentication.
        original_download_url:
          type: string
          format: uri
          description: The URL used to download the file.
        origin_url:
          type: string
          format: uri
          description: The original URL where the file was found.
        suggested_file_name:
          type: string
          description: The suggested file name for saving the file.
        original_file_name:
          type: string
          description: The original file name before any modification.
        duration:
          type: integer
          description: The time it took to process or download the file, in milliseconds.
        size:
          type: integer
          description: The size of the file in bytes.
        created_at:
          type: string
          format: date-time
          description: The timestamp when the file record was created.

````