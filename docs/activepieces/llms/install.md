# Source: https://www.activepieces.com/docs/endpoints/pieces/install.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Install Piece

> Add a piece to a platform



## OpenAPI

````yaml POST /v1/pieces
openapi: 3.0.3
info:
  title: Activepieces Documentation
  version: 0.0.0
servers:
  - url: https://cloud.activepieces.com/api
    description: Production Server
security: []
externalDocs:
  url: https://www.activepieces.com/docs
  description: Find more info here
paths:
  /v1/pieces:
    post:
      tags:
        - pieces
      summary: Add a piece to a platform
      description: Add a piece to a platform
      requestBody:
        content:
          application/json:
            schema:
              anyOf:
                - title: Private Piece
                  type: object
                  properties:
                    packageType:
                      type: string
                      enum:
                        - ARCHIVE
                    scope:
                      type: string
                      enum:
                        - PLATFORM
                    pieceName:
                      minLength: 1
                      type: string
                    pieceVersion:
                      pattern: ^[0-9]+\.[0-9]+\.[0-9]+$
                      type: string
                    pieceArchive:
                      type: object
                      properties:
                        filename:
                          type: string
                        data: {}
                        type:
                          type: string
                          enum:
                            - file
                        mimetype:
                          type: string
                      required:
                        - filename
                        - data
                        - type
                  required:
                    - packageType
                    - scope
                    - pieceName
                    - pieceVersion
                    - pieceArchive
                - title: NPM Piece
                  type: object
                  properties:
                    projectId:
                      type: string
                    packageType:
                      type: string
                      enum:
                        - REGISTRY
                    scope:
                      type: string
                      enum:
                        - PLATFORM
                    pieceName:
                      minLength: 1
                      type: string
                    pieceVersion:
                      pattern: ^[0-9]+\.[0-9]+\.[0-9]+$
                      type: string
                  required:
                    - projectId
                    - packageType
                    - scope
                    - pieceName
                    - pieceVersion
      responses:
        '201':
          description: Default Response
          content:
            application/json:
              schema:
                type: object
                properties: {}
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: http
      description: Use your api key generated from the admin console
      scheme: bearer

````