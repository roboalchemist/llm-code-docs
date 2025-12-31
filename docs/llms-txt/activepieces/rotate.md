# Source: https://www.activepieces.com/docs/endpoints/mcp-servers/rotate.md

# Rotate MCP server token

> Rotate the MCP token

## OpenAPI

````yaml POST /v1/mcp-servers/{id}/rotate
paths:
  path: /v1/mcp-servers/{id}/rotate
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
      path:
        id:
          schema:
            - type: string
              required: true
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
              id:
                allOf:
                  - type: string
              created:
                allOf:
                  - type: string
              updated:
                allOf:
                  - type: string
              name:
                allOf:
                  - type: string
              projectId:
                allOf:
                  - pattern: ^[0-9a-zA-Z]{21}$
                    type: string
              token:
                allOf:
                  - pattern: ^[0-9a-zA-Z]{21}$
                    type: string
              agentId:
                allOf:
                  - pattern: ^[0-9a-zA-Z]{21}$
                    type: string
              externalId:
                allOf:
                  - pattern: ^[0-9a-zA-Z]{21}$
                    type: string
              tools:
                allOf:
                  - type: array
                    items:
                      anyOf:
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - PIECE
                            id:
                              type: string
                            created:
                              type: string
                            updated:
                              type: string
                            externalId:
                              pattern: ^[0-9a-zA-Z]{21}$
                              type: string
                            toolName:
                              type: string
                            mcpId:
                              pattern: ^[0-9a-zA-Z]{21}$
                              type: string
                            pieceMetadata:
                              type: object
                              properties:
                                pieceName:
                                  type: string
                                pieceVersion:
                                  type: string
                                actionName:
                                  type: string
                                actionDisplayName:
                                  type: string
                                logoUrl:
                                  type: string
                                connectionExternalId:
                                  type: string
                              required:
                                - pieceName
                                - pieceVersion
                                - actionName
                                - actionDisplayName
                                - logoUrl
                          required:
                            - type
                            - id
                            - created
                            - updated
                            - externalId
                            - mcpId
                            - pieceMetadata
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - FLOW
                            id:
                              type: string
                            created:
                              type: string
                            updated:
                              type: string
                            externalId:
                              pattern: ^[0-9a-zA-Z]{21}$
                              type: string
                            toolName:
                              type: string
                            mcpId:
                              pattern: ^[0-9a-zA-Z]{21}$
                              type: string
                            flowId:
                              pattern: ^[0-9a-zA-Z]{21}$
                              type: string
                            flow:
                              type: object
                              properties:
                                id:
                                  type: string
                                created:
                                  type: string
                                updated:
                                  type: string
                                projectId:
                                  type: string
                                externalId:
                                  type: string
                                folderId:
                                  type: string
                                  nullable: true
                                status:
                                  anyOf:
                                    - type: string
                                      enum:
                                        - ENABLED
                                    - type: string
                                      enum:
                                        - DISABLED
                                publishedVersionId:
                                  type: string
                                  nullable: true
                                metadata:
                                  type: object
                                  nullable: true
                                  additionalProperties: {}
                                version:
                                  type: object
                                  properties:
                                    id:
                                      type: string
                                    created:
                                      type: string
                                    updated:
                                      type: string
                                    flowId:
                                      type: string
                                    displayName:
                                      type: string
                                    trigger:
                                      anyOf:
                                        - type: object
                                          properties:
                                            name:
                                              type: string
                                            valid:
                                              type: boolean
                                            displayName:
                                              type: string
                                            nextAction: {}
                                            type:
                                              type: string
                                              enum:
                                                - PIECE_TRIGGER
                                            settings:
                                              type: object
                                              properties:
                                                sampleData:
                                                  additionalProperties: true
                                                  type: object
                                                  properties:
                                                    sampleDataFileId:
                                                      type: string
                                                    sampleDataInputFileId:
                                                      type: string
                                                    lastTestDate:
                                                      type: string
                                                propertySettings:
                                                  type: object
                                                  additionalProperties:
                                                    type: object
                                                    properties:
                                                      type:
                                                        anyOf:
                                                          - type: string
                                                            enum:
                                                              - MANUAL
                                                          - type: string
                                                            enum:
                                                              - DYNAMIC
                                                      schema: {}
                                                    required:
                                                      - type
                                                customLogoUrl:
                                                  type: string
                                                pieceName:
                                                  type: string
                                                pieceVersion:
                                                  pattern: ^([~^])?[0-9]+\.[0-9]+\.[0-9]+$
                                                  type: string
                                                triggerName:
                                                  type: string
                                                input:
                                                  type: object
                                                  additionalProperties: {}
                                              required:
                                                - propertySettings
                                                - pieceName
                                                - pieceVersion
                                                - input
                                          required:
                                            - name
                                            - valid
                                            - displayName
                                            - type
                                            - settings
                                        - type: object
                                          properties:
                                            name:
                                              type: string
                                            valid:
                                              type: boolean
                                            displayName:
                                              type: string
                                            nextAction: {}
                                            type:
                                              type: string
                                              enum:
                                                - EMPTY
                                            settings: {}
                                          required:
                                            - name
                                            - valid
                                            - displayName
                                            - type
                                            - settings
                                    updatedBy:
                                      type: string
                                      nullable: true
                                    valid:
                                      type: boolean
                                    schemaVersion:
                                      type: string
                                      nullable: true
                                    agentIds:
                                      type: array
                                      items:
                                        type: string
                                    state:
                                      anyOf:
                                        - type: string
                                          enum:
                                            - LOCKED
                                        - type: string
                                          enum:
                                            - DRAFT
                                    connectionIds:
                                      type: array
                                      items:
                                        type: string
                                    backupFiles:
                                      type: object
                                      nullable: true
                                      additionalProperties:
                                        type: string
                                  required:
                                    - id
                                    - created
                                    - updated
                                    - flowId
                                    - displayName
                                    - trigger
                                    - valid
                                    - agentIds
                                    - state
                                    - connectionIds
                                triggerSource:
                                  type: object
                                  properties:
                                    schedule:
                                      type: object
                                      properties:
                                        type:
                                          type: string
                                          enum:
                                            - CRON_EXPRESSION
                                        cronExpression:
                                          type: string
                                        timezone:
                                          type: string
                                      required:
                                        - type
                                        - cronExpression
                                        - timezone
                                      nullable: true
                              required:
                                - id
                                - created
                                - updated
                                - projectId
                                - externalId
                                - status
                                - version
                          required:
                            - type
                            - id
                            - created
                            - updated
                            - externalId
                            - mcpId
                            - flowId
                            - flow
                      discriminator:
                        propertyName: type
            requiredProperties:
              - id
              - created
              - updated
              - name
              - projectId
              - token
              - externalId
              - tools
        examples:
          example:
            value:
              id: <string>
              created: <string>
              updated: <string>
              name: <string>
              projectId: <string>
              token: <string>
              agentId: <string>
              externalId: <string>
              tools:
                - type: PIECE
                  id: <string>
                  created: <string>
                  updated: <string>
                  externalId: <string>
                  toolName: <string>
                  mcpId: <string>
                  pieceMetadata:
                    pieceName: <string>
                    pieceVersion: <string>
                    actionName: <string>
                    actionDisplayName: <string>
                    logoUrl: <string>
                    connectionExternalId: <string>
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````