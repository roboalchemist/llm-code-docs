# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/gitlab/list-scans.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/github/list-scans.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/bitbucket/list-scans.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Scans

> Get the scans associated with the specified Bitbucket Data Source by ID.



## OpenAPI

````yaml GET /api/v2/secret-scanning/data-sources/bitbucket/{dataSourceId}/scans
openapi: 3.0.3
info:
  title: Infisical API
  description: List of all available APIs that can be consumed
  version: 0.0.1
servers:
  - url: https://us.infisical.com
    description: Production server (US)
  - url: https://eu.infisical.com
    description: Production server (EU)
  - url: http://localhost:8080
    description: Local server
security: []
paths:
  /api/v2/secret-scanning/data-sources/bitbucket/{dataSourceId}/scans:
    get:
      tags:
        - Secret Scanning
      description: Get the scans associated with the specified Bitbucket Data Source by ID.
      operationId: listBitbucketDataSourceScans
      parameters:
        - schema:
            type: string
            format: uuid
          in: path
          name: dataSourceId
          required: true
          description: The ID of the Bitbucket Data Source to list scans for.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  scans:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          format: uuid
                        status:
                          type: string
                          default: queued
                        statusMessage:
                          type: string
                          nullable: true
                        type:
                          type: string
                        resourceId:
                          type: string
                          format: uuid
                        createdAt:
                          type: string
                          format: date-time
                          nullable: true
                      required:
                        - id
                        - type
                        - resourceId
                      additionalProperties: false
                required:
                  - scans
                additionalProperties: false
        '400':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 400
                  message:
                    type: string
                  error:
                    type: string
                  details: {}
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '401':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 401
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '403':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 403
                  message:
                    type: string
                  details: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '404':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 404
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false
        '422':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 422
                  message: {}
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - error
                additionalProperties: false
        '500':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  reqId:
                    type: string
                  statusCode:
                    type: number
                    enum:
                      - 500
                  message:
                    type: string
                  error:
                    type: string
                required:
                  - reqId
                  - statusCode
                  - message
                  - error
                additionalProperties: false

````