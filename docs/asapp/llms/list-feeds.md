# Source: https://docs.asapp.com/apis/file-exporter/list-feeds.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List feeds

> Lists feed names for a company




## OpenAPI

````yaml api-specs/fileexporter.yaml post /fileexporter/v1/static/listfeeds
openapi: 3.0.1
info:
  title: File Exporter API
  description: >
    The File Exporter API is a batch mechanism for exporting data to your data
    warehouse. The service provides a file link to access requested data based
    on the  parameters of the request that include the feed, version, format,
    date, and time interval of interest.
  version: 1.0.0
servers:
  - url: https://api.sandbox.asapp.com
security:
  - API-ID: []
    API-Secret: []
tags:
  - name: File Exporter
    description: API to get client exports
paths:
  /fileexporter/v1/static/listfeeds:
    post:
      tags:
        - File Exporter
      summary: List feeds
      description: |
        Lists feed names for a company
      operationId: listFeeds
      responses:
        '200':
          description: Successfully requested feed names
          content:
            application/json:
              schema:
                description: Get feed names for a company
                type: object
                properties:
                  feeds:
                    type: array
                    items:
                      type: string
                    example:
                      - feed_1
                      - feed_2
                      - feed_3
        '422':
          description: 422 - Unprocessable Entity
          content:
            application/json:
              schema:
                description: Unprocessable Entity response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 422-01
                      message: Unprocessable Entity
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
        default:
          description: 500 - Internal Server Error
          content:
            application/json:
              schema:
                description: Default error response
                type: object
                properties:
                  error:
                    example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 500-01
                      message: Internal server error
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
components:
  securitySchemes:
    API-ID:
      type: apiKey
      in: header
      name: asapp-api-id
    API-Secret:
      type: apiKey
      in: header
      name: asapp-api-secret

````