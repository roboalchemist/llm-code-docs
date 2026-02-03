# Source: https://www.activepieces.com/docs/endpoints/templates/create.md

# Source: https://www.activepieces.com/docs/endpoints/projects/create.md

# Source: https://www.activepieces.com/docs/endpoints/project-releases/create.md

# Source: https://www.activepieces.com/docs/endpoints/folders/create.md

# Source: https://www.activepieces.com/docs/endpoints/flows/create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Flow

> Create a flow



## OpenAPI

````yaml POST /v1/flows
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
  /v1/flows:
    post:
      tags:
        - flows
      description: Create a flow
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                displayName:
                  type: string
                folderId:
                  type: string
                folderName:
                  type: string
                projectId:
                  type: string
                metadata:
                  type: object
                  additionalProperties: {}
              required:
                - displayName
                - projectId
        required: true
      responses:
        '201':
          description: Default Response
          content:
            application/json:
              schema:
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
                  ownerId:
                    type: string
                    nullable: true
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
                  operationStatus:
                    anyOf:
                      - type: string
                        enum:
                          - NONE
                      - type: string
                        enum:
                          - DELETING
                      - type: string
                        enum:
                          - ENABLING
                      - type: string
                        enum:
                          - DISABLING
                  timeSavedPerRun:
                    type: number
                    nullable: true
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
                      notes:
                        type: array
                        items:
                          type: object
                          properties:
                            id:
                              type: string
                            content:
                              type: string
                            ownerId:
                              type: string
                              nullable: true
                            color:
                              anyOf:
                                - type: string
                                  enum:
                                    - orange
                                - type: string
                                  enum:
                                    - red
                                - type: string
                                  enum:
                                    - green
                                - type: string
                                  enum:
                                    - blue
                                - type: string
                                  enum:
                                    - purple
                                - type: string
                                  enum:
                                    - yellow
                            position:
                              type: object
                              properties:
                                x:
                                  type: number
                                'y':
                                  type: number
                              required:
                                - x
                                - 'y'
                            size:
                              type: object
                              properties:
                                width:
                                  type: number
                                height:
                                  type: number
                              required:
                                - width
                                - height
                            createdAt:
                              type: string
                            updatedAt:
                              type: string
                          required:
                            - id
                            - content
                            - color
                            - position
                            - size
                            - createdAt
                            - updatedAt
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
                      - notes
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
                  - operationStatus
                  - version
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: http
      description: Use your api key generated from the admin console
      scheme: bearer

````