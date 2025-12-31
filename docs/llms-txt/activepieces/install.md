# Source: https://www.activepieces.com/docs/endpoints/pieces/install.md

# Install Piece

> Add a piece to a platform

## OpenAPI

````yaml POST /v1/pieces
paths:
  path: /v1/pieces
  method: post
  servers:
    - url: https://cloud.activepieces.com/api
      description: Production Server
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Use your api key generated from the admin console
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              packageType:
                allOf:
                  - type: string
                    enum:
                      - ARCHIVE
              scope:
                allOf:
                  - type: string
                    enum:
                      - PLATFORM
              pieceName:
                allOf:
                  - minLength: 1
                    type: string
              pieceVersion:
                allOf:
                  - pattern: ^[0-9]+\.[0-9]+\.[0-9]+$
                    type: string
              pieceArchive:
                allOf:
                  - type: object
                    properties:
                      filename:
                        type: string
                      data: {}
                      type:
                        type: string
                        enum:
                          - file
                    required:
                      - filename
                      - data
                      - type
            title: Private Piece
            requiredProperties:
              - packageType
              - scope
              - pieceName
              - pieceVersion
              - pieceArchive
          - type: object
            properties:
              packageType:
                allOf:
                  - type: string
                    enum:
                      - REGISTRY
              scope:
                allOf:
                  - type: string
                    enum:
                      - PLATFORM
              pieceName:
                allOf:
                  - minLength: 1
                    type: string
              pieceVersion:
                allOf:
                  - pattern: ^[0-9]+\.[0-9]+\.[0-9]+$
                    type: string
            title: NPM Piece
            requiredProperties:
              - packageType
              - scope
              - pieceName
              - pieceVersion
        examples:
          example:
            value:
              packageType: ARCHIVE
              scope: PLATFORM
              pieceName: <string>
              pieceVersion: <string>
              pieceArchive:
                filename: <string>
                data: <any>
                type: file
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties: {}
        examples:
          example:
            value: {}
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````