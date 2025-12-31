# Source: https://www.activepieces.com/docs/endpoints/templates/create.md

# Source: https://www.activepieces.com/docs/endpoints/projects/create.md

# Source: https://www.activepieces.com/docs/endpoints/project-releases/create.md

# Source: https://www.activepieces.com/docs/endpoints/folders/create.md

# Source: https://www.activepieces.com/docs/endpoints/flows/create.md

# Source: https://www.activepieces.com/docs/endpoints/templates/create.md

# Source: https://www.activepieces.com/docs/endpoints/projects/create.md

# Source: https://www.activepieces.com/docs/endpoints/project-releases/create.md

# Source: https://www.activepieces.com/docs/endpoints/folders/create.md

# Source: https://www.activepieces.com/docs/endpoints/flows/create.md

# Source: https://www.activepieces.com/docs/endpoints/projects/create.md

# Source: https://www.activepieces.com/docs/endpoints/project-releases/create.md

# Source: https://www.activepieces.com/docs/endpoints/folders/create.md

# Source: https://www.activepieces.com/docs/endpoints/flows/create.md

# Source: https://www.activepieces.com/docs/endpoints/flow-templates/create.md

# Create Flow Template

> Create a flow template

## OpenAPI

````yaml POST /v1/flow-templates
paths:
  path: /v1/flow-templates
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
              description:
                allOf:
                  - type: string
              template:
                allOf:
                  - type: object
                    properties:
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
                      valid:
                        type: boolean
                      schemaVersion:
                        type: string
                        nullable: true
                      agentIds:
                        type: array
                        items:
                          type: string
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
                      - displayName
                      - trigger
                      - valid
                      - agentIds
                      - connectionIds
              blogUrl:
                allOf:
                  - type: string
              type:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - PLATFORM
                      - type: string
                        enum:
                          - PROJECT
              tags:
                allOf:
                  - type: array
                    items:
                      type: string
              id:
                allOf:
                  - type: string
              metadata:
                allOf:
                  - type: object
                    nullable: true
                    additionalProperties: {}
            required: true
            requiredProperties:
              - template
              - type
        examples:
          example:
            value:
              description: <string>
              template:
                displayName: <string>
                trigger:
                  name: <string>
                  valid: true
                  displayName: <string>
                  nextAction: <any>
                  type: PIECE_TRIGGER
                  settings:
                    sampleData:
                      sampleDataFileId: <string>
                      sampleDataInputFileId: <string>
                      lastTestDate: <string>
                    propertySettings: {}
                    customLogoUrl: <string>
                    pieceName: <string>
                    pieceVersion: <string>
                    triggerName: <string>
                    input: {}
                valid: true
                schemaVersion: <string>
                agentIds:
                  - <string>
                connectionIds:
                  - <string>
                backupFiles: {}
              blogUrl: <string>
              type: PLATFORM
              tags:
                - <string>
              id: <string>
              metadata: {}
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Default Response
        examples: {}
        description: Default Response
  deprecated: false
  type: path
components:
  schemas: {}

````