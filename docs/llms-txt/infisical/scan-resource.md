# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/gitlab/scan-resource.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/github/scan-resource.md

# Source: https://infisical.com/docs/api-reference/endpoints/secret-scanning/data-sources/bitbucket/scan-resource.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Scan Resource

> Trigger a scan for the specified Bitbucket Data Source resource.



## OpenAPI

````yaml POST /api/v2/secret-scanning/data-sources/bitbucket/{dataSourceId}/resources/{resourceId}/scan
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
  /api/v2/secret-scanning/data-sources/bitbucket/{dataSourceId}/resources/{resourceId}/scan:
    post:
      tags:
        - Secret Scanning
      description: Trigger a scan for the specified Bitbucket Data Source resource.
      operationId: triggerBitbucketDataSourceResourceScan
      parameters:
        - schema:
            type: string
            format: uuid
          in: path
          name: dataSourceId
          required: true
          description: The ID of the Bitbucket Data Source to trigger a scan for.
        - schema:
            type: string
            format: uuid
          in: path
          name: resourceId
          required: true
          description: The ID of the individual Data Source resource to trigger a scan for.
      responses:
        '200':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties:
                  dataSource:
                    type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      externalId:
                        type: string
                        nullable: true
                      name:
                        type: string
                      description:
                        type: string
                        nullable: true
                      encryptedCredentials:
                        nullable: true
                      isAutoScanEnabled:
                        type: boolean
                        default: true
                        nullable: true
                      projectId:
                        type: string
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
                        type: string
                        format: date-time
                      isDisconnected:
                        type: boolean
                        default: false
                      type:
                        type: string
                        enum:
                          - bitbucket
                      connectionId:
                        type: string
                        format: uuid
                      connection:
                        type: object
                        properties:
                          app:
                            type: string
                            enum:
                              - bitbucket
                          name:
                            type: string
                          id:
                            type: string
                            format: uuid
                        required:
                          - app
                          - name
                          - id
                        additionalProperties: false
                      config:
                        type: object
                        properties:
                          workspaceSlug:
                            type: string
                            minLength: 1
                            maxLength: 128
                            description: The workspace to scan.
                          includeRepos:
                            type: array
                            items:
                              type: string
                              minLength: 1
                              maxLength: 256
                            minItems: 1
                            maxItems: 100
                            default:
                              - '*'
                            description: >-
                              The repositories to include when scanning.
                              Defaults to all repositories (["*"]).
                        required:
                          - workspaceSlug
                        additionalProperties: false
                    required:
                      - id
                      - name
                      - projectId
                      - createdAt
                      - updatedAt
                      - type
                      - connectionId
                      - connection
                      - config
                    additionalProperties: false
                    title: Bitbucket
                required:
                  - dataSource
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