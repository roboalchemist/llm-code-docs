# Source: https://www.activepieces.com/docs/endpoints/users/update.md

# Source: https://www.activepieces.com/docs/endpoints/projects/update.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/update.md

# Source: https://www.activepieces.com/docs/endpoints/folders/update.md

# Source: https://www.activepieces.com/docs/endpoints/flows/update.md

# Source: https://www.activepieces.com/docs/endpoints/users/update.md

# Source: https://www.activepieces.com/docs/endpoints/projects/update.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/update.md

# Source: https://www.activepieces.com/docs/endpoints/folders/update.md

# Source: https://www.activepieces.com/docs/endpoints/flows/update.md

# Source: https://www.activepieces.com/docs/endpoints/users/update.md

# Source: https://www.activepieces.com/docs/endpoints/projects/update.md

# Source: https://www.activepieces.com/docs/endpoints/mcp-servers/update.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/update.md

# Source: https://www.activepieces.com/docs/endpoints/folders/update.md

# Source: https://www.activepieces.com/docs/endpoints/flows/update.md

# Apply Flow Operation

> Apply an operation to a flow

## OpenAPI

````yaml POST /v1/flows/{id}
paths:
  path: /v1/flows/{id}
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - MOVE_ACTION
              request:
                allOf:
                  - type: object
                    properties:
                      name:
                        type: string
                      newParentStep:
                        type: string
                      stepLocationRelativeToNewParent:
                        anyOf:
                          - type: string
                            enum:
                              - AFTER
                          - type: string
                            enum:
                              - INSIDE_LOOP
                          - type: string
                            enum:
                              - INSIDE_BRANCH
                      branchIndex:
                        type: number
                    required:
                      - name
                      - newParentStep
            title: Move Action
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - CHANGE_STATUS
              request:
                allOf:
                  - type: object
                    properties:
                      status:
                        anyOf:
                          - type: string
                            enum:
                              - ENABLED
                          - type: string
                            enum:
                              - DISABLED
                    required:
                      - status
            title: Change Status
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - LOCK_AND_PUBLISH
              request:
                allOf:
                  - type: object
                    properties:
                      status:
                        anyOf:
                          - type: string
                            enum:
                              - ENABLED
                          - type: string
                            enum:
                              - DISABLED
            title: Lock and Publish
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - USE_AS_DRAFT
              request:
                allOf:
                  - type: object
                    properties:
                      versionId:
                        type: string
                    required:
                      - versionId
            title: Copy as Draft
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - LOCK_FLOW
              request:
                allOf:
                  - type: object
                    properties: {}
            title: Lock Flow
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - IMPORT_FLOW
              request:
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
                      schemaVersion:
                        type: string
                        nullable: true
                    required:
                      - displayName
                      - trigger
            title: Import Flow
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - CHANGE_NAME
              request:
                allOf:
                  - type: object
                    properties:
                      displayName:
                        type: string
                    required:
                      - displayName
            title: Change Name
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - DELETE_ACTION
              request:
                allOf:
                  - type: object
                    properties:
                      names:
                        type: array
                        items:
                          type: string
                    required:
                      - names
            title: Delete Action
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - UPDATE_ACTION
              request:
                allOf:
                  - anyOf:
                      - type: object
                        properties:
                          name:
                            type: string
                          valid:
                            type: boolean
                          displayName:
                            type: string
                          skip:
                            type: boolean
                          type:
                            type: string
                            enum:
                              - CODE
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
                              customLogoUrl:
                                type: string
                              sourceCode:
                                type: object
                                properties:
                                  packageJson:
                                    type: string
                                  code:
                                    type: string
                                required:
                                  - packageJson
                                  - code
                              input:
                                type: object
                                additionalProperties: {}
                              errorHandlingOptions:
                                type: object
                                properties:
                                  continueOnFailure:
                                    type: object
                                    properties:
                                      value:
                                        type: boolean
                                    required:
                                      - value
                                  retryOnFailure:
                                    type: object
                                    properties:
                                      value:
                                        type: boolean
                                    required:
                                      - value
                            required:
                              - sourceCode
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
                          skip:
                            type: boolean
                          type:
                            type: string
                            enum:
                              - LOOP_ON_ITEMS
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
                              customLogoUrl:
                                type: string
                              items:
                                type: string
                            required:
                              - items
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
                          skip:
                            type: boolean
                          type:
                            type: string
                            enum:
                              - PIECE
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
                              customLogoUrl:
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
                              pieceName:
                                type: string
                              pieceVersion:
                                pattern: ^([~^])?[0-9]+\.[0-9]+\.[0-9]+$
                                type: string
                              actionName:
                                type: string
                              input:
                                type: object
                                additionalProperties: {}
                              errorHandlingOptions:
                                type: object
                                properties:
                                  continueOnFailure:
                                    type: object
                                    properties:
                                      value:
                                        type: boolean
                                    required:
                                      - value
                                  retryOnFailure:
                                    type: object
                                    properties:
                                      value:
                                        type: boolean
                                    required:
                                      - value
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
                          skip:
                            type: boolean
                          type:
                            type: string
                            enum:
                              - ROUTER
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
                              customLogoUrl:
                                type: string
                              branches:
                                type: array
                                items:
                                  anyOf:
                                    - type: object
                                      properties:
                                        conditions:
                                          type: array
                                          items:
                                            type: array
                                            items:
                                              anyOf:
                                                - type: object
                                                  properties:
                                                    firstValue:
                                                      type: string
                                                    secondValue:
                                                      type: string
                                                    caseSensitive:
                                                      type: boolean
                                                    operator:
                                                      anyOf:
                                                        - type: string
                                                          enum:
                                                            - TEXT_CONTAINS
                                                        - type: string
                                                          enum:
                                                            - TEXT_DOES_NOT_CONTAIN
                                                        - type: string
                                                          enum:
                                                            - TEXT_EXACTLY_MATCHES
                                                        - type: string
                                                          enum:
                                                            - TEXT_DOES_NOT_EXACTLY_MATCH
                                                        - type: string
                                                          enum:
                                                            - TEXT_START_WITH
                                                        - type: string
                                                          enum:
                                                            - TEXT_DOES_NOT_START_WITH
                                                        - type: string
                                                          enum:
                                                            - TEXT_ENDS_WITH
                                                        - type: string
                                                          enum:
                                                            - TEXT_DOES_NOT_END_WITH
                                                        - type: string
                                                          enum:
                                                            - LIST_CONTAINS
                                                        - type: string
                                                          enum:
                                                            - LIST_DOES_NOT_CONTAIN
                                                  required:
                                                    - firstValue
                                                    - secondValue
                                                - type: object
                                                  properties:
                                                    firstValue:
                                                      type: string
                                                    secondValue:
                                                      type: string
                                                    operator:
                                                      anyOf:
                                                        - type: string
                                                          enum:
                                                            - NUMBER_IS_GREATER_THAN
                                                        - type: string
                                                          enum:
                                                            - NUMBER_IS_LESS_THAN
                                                        - type: string
                                                          enum:
                                                            - NUMBER_IS_EQUAL_TO
                                                  required:
                                                    - firstValue
                                                    - secondValue
                                                - type: object
                                                  properties:
                                                    firstValue:
                                                      type: string
                                                    secondValue:
                                                      type: string
                                                    operator:
                                                      anyOf:
                                                        - type: string
                                                          enum:
                                                            - DATE_IS_BEFORE
                                                        - type: string
                                                          enum:
                                                            - DATE_IS_EQUAL
                                                        - type: string
                                                          enum:
                                                            - DATE_IS_AFTER
                                                  required:
                                                    - firstValue
                                                    - secondValue
                                                - type: object
                                                  properties:
                                                    firstValue:
                                                      type: string
                                                    operator:
                                                      anyOf:
                                                        - type: string
                                                          enum:
                                                            - EXISTS
                                                        - type: string
                                                          enum:
                                                            - DOES_NOT_EXIST
                                                        - type: string
                                                          enum:
                                                            - BOOLEAN_IS_TRUE
                                                        - type: string
                                                          enum:
                                                            - BOOLEAN_IS_FALSE
                                                        - type: string
                                                          enum:
                                                            - LIST_IS_EMPTY
                                                        - type: string
                                                          enum:
                                                            - LIST_IS_NOT_EMPTY
                                                  required:
                                                    - firstValue
                                        branchType:
                                          type: string
                                          enum:
                                            - CONDITION
                                        branchName:
                                          type: string
                                      required:
                                        - conditions
                                        - branchType
                                        - branchName
                                    - type: object
                                      properties:
                                        branchType:
                                          type: string
                                          enum:
                                            - FALLBACK
                                        branchName:
                                          type: string
                                      required:
                                        - branchType
                                        - branchName
                              executionType:
                                anyOf:
                                  - type: string
                                    enum:
                                      - EXECUTE_ALL_MATCH
                                  - type: string
                                    enum:
                                      - EXECUTE_FIRST_MATCH
                            required:
                              - branches
                              - executionType
                        required:
                          - name
                          - valid
                          - displayName
                          - type
                          - settings
            title: Update Action
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - ADD_ACTION
              request:
                allOf:
                  - type: object
                    properties:
                      parentStep:
                        type: string
                      stepLocationRelativeToParent:
                        anyOf:
                          - type: string
                            enum:
                              - AFTER
                          - type: string
                            enum:
                              - INSIDE_LOOP
                          - type: string
                            enum:
                              - INSIDE_BRANCH
                      branchIndex:
                        type: number
                      action:
                        anyOf:
                          - type: object
                            properties:
                              name:
                                type: string
                              valid:
                                type: boolean
                              displayName:
                                type: string
                              skip:
                                type: boolean
                              type:
                                type: string
                                enum:
                                  - CODE
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
                                  customLogoUrl:
                                    type: string
                                  sourceCode:
                                    type: object
                                    properties:
                                      packageJson:
                                        type: string
                                      code:
                                        type: string
                                    required:
                                      - packageJson
                                      - code
                                  input:
                                    type: object
                                    additionalProperties: {}
                                  errorHandlingOptions:
                                    type: object
                                    properties:
                                      continueOnFailure:
                                        type: object
                                        properties:
                                          value:
                                            type: boolean
                                        required:
                                          - value
                                      retryOnFailure:
                                        type: object
                                        properties:
                                          value:
                                            type: boolean
                                        required:
                                          - value
                                required:
                                  - sourceCode
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
                              skip:
                                type: boolean
                              type:
                                type: string
                                enum:
                                  - LOOP_ON_ITEMS
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
                                  customLogoUrl:
                                    type: string
                                  items:
                                    type: string
                                required:
                                  - items
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
                              skip:
                                type: boolean
                              type:
                                type: string
                                enum:
                                  - PIECE
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
                                  customLogoUrl:
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
                                  pieceName:
                                    type: string
                                  pieceVersion:
                                    pattern: ^([~^])?[0-9]+\.[0-9]+\.[0-9]+$
                                    type: string
                                  actionName:
                                    type: string
                                  input:
                                    type: object
                                    additionalProperties: {}
                                  errorHandlingOptions:
                                    type: object
                                    properties:
                                      continueOnFailure:
                                        type: object
                                        properties:
                                          value:
                                            type: boolean
                                        required:
                                          - value
                                      retryOnFailure:
                                        type: object
                                        properties:
                                          value:
                                            type: boolean
                                        required:
                                          - value
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
                              skip:
                                type: boolean
                              type:
                                type: string
                                enum:
                                  - ROUTER
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
                                  customLogoUrl:
                                    type: string
                                  branches:
                                    type: array
                                    items:
                                      anyOf:
                                        - type: object
                                          properties:
                                            conditions:
                                              type: array
                                              items:
                                                type: array
                                                items:
                                                  anyOf:
                                                    - type: object
                                                      properties:
                                                        firstValue:
                                                          type: string
                                                        secondValue:
                                                          type: string
                                                        caseSensitive:
                                                          type: boolean
                                                        operator:
                                                          anyOf:
                                                            - type: string
                                                              enum:
                                                                - TEXT_CONTAINS
                                                            - type: string
                                                              enum:
                                                                - TEXT_DOES_NOT_CONTAIN
                                                            - type: string
                                                              enum:
                                                                - TEXT_EXACTLY_MATCHES
                                                            - type: string
                                                              enum:
                                                                - TEXT_DOES_NOT_EXACTLY_MATCH
                                                            - type: string
                                                              enum:
                                                                - TEXT_START_WITH
                                                            - type: string
                                                              enum:
                                                                - TEXT_DOES_NOT_START_WITH
                                                            - type: string
                                                              enum:
                                                                - TEXT_ENDS_WITH
                                                            - type: string
                                                              enum:
                                                                - TEXT_DOES_NOT_END_WITH
                                                            - type: string
                                                              enum:
                                                                - LIST_CONTAINS
                                                            - type: string
                                                              enum:
                                                                - LIST_DOES_NOT_CONTAIN
                                                      required:
                                                        - firstValue
                                                        - secondValue
                                                    - type: object
                                                      properties:
                                                        firstValue:
                                                          type: string
                                                        secondValue:
                                                          type: string
                                                        operator:
                                                          anyOf:
                                                            - type: string
                                                              enum:
                                                                - NUMBER_IS_GREATER_THAN
                                                            - type: string
                                                              enum:
                                                                - NUMBER_IS_LESS_THAN
                                                            - type: string
                                                              enum:
                                                                - NUMBER_IS_EQUAL_TO
                                                      required:
                                                        - firstValue
                                                        - secondValue
                                                    - type: object
                                                      properties:
                                                        firstValue:
                                                          type: string
                                                        secondValue:
                                                          type: string
                                                        operator:
                                                          anyOf:
                                                            - type: string
                                                              enum:
                                                                - DATE_IS_BEFORE
                                                            - type: string
                                                              enum:
                                                                - DATE_IS_EQUAL
                                                            - type: string
                                                              enum:
                                                                - DATE_IS_AFTER
                                                      required:
                                                        - firstValue
                                                        - secondValue
                                                    - type: object
                                                      properties:
                                                        firstValue:
                                                          type: string
                                                        operator:
                                                          anyOf:
                                                            - type: string
                                                              enum:
                                                                - EXISTS
                                                            - type: string
                                                              enum:
                                                                - DOES_NOT_EXIST
                                                            - type: string
                                                              enum:
                                                                - BOOLEAN_IS_TRUE
                                                            - type: string
                                                              enum:
                                                                - BOOLEAN_IS_FALSE
                                                            - type: string
                                                              enum:
                                                                - LIST_IS_EMPTY
                                                            - type: string
                                                              enum:
                                                                - LIST_IS_NOT_EMPTY
                                                      required:
                                                        - firstValue
                                            branchType:
                                              type: string
                                              enum:
                                                - CONDITION
                                            branchName:
                                              type: string
                                          required:
                                            - conditions
                                            - branchType
                                            - branchName
                                        - type: object
                                          properties:
                                            branchType:
                                              type: string
                                              enum:
                                                - FALLBACK
                                            branchName:
                                              type: string
                                          required:
                                            - branchType
                                            - branchName
                                  executionType:
                                    anyOf:
                                      - type: string
                                        enum:
                                          - EXECUTE_ALL_MATCH
                                      - type: string
                                        enum:
                                          - EXECUTE_FIRST_MATCH
                                required:
                                  - branches
                                  - executionType
                            required:
                              - name
                              - valid
                              - displayName
                              - type
                              - settings
                    required:
                      - parentStep
                      - action
            title: Add Action
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - UPDATE_TRIGGER
              request:
                allOf:
                  - anyOf:
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
            title: Update Trigger
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - CHANGE_FOLDER
              request:
                allOf:
                  - type: object
                    properties:
                      folderId:
                        type: string
                        nullable: true
            title: Change Folder
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - DUPLICATE_ACTION
              request:
                allOf:
                  - type: object
                    properties:
                      stepName:
                        type: string
                    required:
                      - stepName
            title: Duplicate Action
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - DELETE_BRANCH
              request:
                allOf:
                  - type: object
                    properties:
                      branchIndex:
                        type: number
                      stepName:
                        type: string
                    required:
                      - branchIndex
                      - stepName
            title: Delete Branch
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - ADD_BRANCH
              request:
                allOf:
                  - type: object
                    properties:
                      branchIndex:
                        type: number
                      stepName:
                        type: string
                      conditions:
                        type: array
                        items:
                          type: array
                          items:
                            anyOf:
                              - type: object
                                properties:
                                  firstValue:
                                    type: string
                                  secondValue:
                                    type: string
                                  caseSensitive:
                                    type: boolean
                                  operator:
                                    anyOf:
                                      - type: string
                                        enum:
                                          - TEXT_CONTAINS
                                      - type: string
                                        enum:
                                          - TEXT_DOES_NOT_CONTAIN
                                      - type: string
                                        enum:
                                          - TEXT_EXACTLY_MATCHES
                                      - type: string
                                        enum:
                                          - TEXT_DOES_NOT_EXACTLY_MATCH
                                      - type: string
                                        enum:
                                          - TEXT_START_WITH
                                      - type: string
                                        enum:
                                          - TEXT_DOES_NOT_START_WITH
                                      - type: string
                                        enum:
                                          - TEXT_ENDS_WITH
                                      - type: string
                                        enum:
                                          - TEXT_DOES_NOT_END_WITH
                                      - type: string
                                        enum:
                                          - LIST_CONTAINS
                                      - type: string
                                        enum:
                                          - LIST_DOES_NOT_CONTAIN
                                required:
                                  - firstValue
                                  - secondValue
                              - type: object
                                properties:
                                  firstValue:
                                    type: string
                                  secondValue:
                                    type: string
                                  operator:
                                    anyOf:
                                      - type: string
                                        enum:
                                          - NUMBER_IS_GREATER_THAN
                                      - type: string
                                        enum:
                                          - NUMBER_IS_LESS_THAN
                                      - type: string
                                        enum:
                                          - NUMBER_IS_EQUAL_TO
                                required:
                                  - firstValue
                                  - secondValue
                              - type: object
                                properties:
                                  firstValue:
                                    type: string
                                  secondValue:
                                    type: string
                                  operator:
                                    anyOf:
                                      - type: string
                                        enum:
                                          - DATE_IS_BEFORE
                                      - type: string
                                        enum:
                                          - DATE_IS_EQUAL
                                      - type: string
                                        enum:
                                          - DATE_IS_AFTER
                                required:
                                  - firstValue
                                  - secondValue
                              - type: object
                                properties:
                                  firstValue:
                                    type: string
                                  operator:
                                    anyOf:
                                      - type: string
                                        enum:
                                          - EXISTS
                                      - type: string
                                        enum:
                                          - DOES_NOT_EXIST
                                      - type: string
                                        enum:
                                          - BOOLEAN_IS_TRUE
                                      - type: string
                                        enum:
                                          - BOOLEAN_IS_FALSE
                                      - type: string
                                        enum:
                                          - LIST_IS_EMPTY
                                      - type: string
                                        enum:
                                          - LIST_IS_NOT_EMPTY
                                required:
                                  - firstValue
                      branchName:
                        type: string
                    required:
                      - branchIndex
                      - stepName
                      - branchName
            title: Add Branch
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - DUPLICATE_BRANCH
              request:
                allOf:
                  - type: object
                    properties:
                      branchIndex:
                        type: number
                      stepName:
                        type: string
                    required:
                      - branchIndex
                      - stepName
            title: Duplicate Branch
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - SET_SKIP_ACTION
              request:
                allOf:
                  - type: object
                    properties:
                      names:
                        type: array
                        items:
                          type: string
                      skip:
                        type: boolean
                    required:
                      - names
                      - skip
            title: Skip Action
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - UPDATE_METADATA
              request:
                allOf:
                  - type: object
                    properties:
                      metadata:
                        type: object
                        nullable: true
                        additionalProperties: {}
            title: Update Metadata
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - MOVE_BRANCH
              request:
                allOf:
                  - type: object
                    properties:
                      sourceBranchIndex:
                        type: number
                      targetBranchIndex:
                        type: number
                      stepName:
                        type: string
                    required:
                      - sourceBranchIndex
                      - targetBranchIndex
                      - stepName
            requiredProperties:
              - type
              - request
          - type: object
            properties:
              type:
                allOf:
                  - type: string
                    enum:
                      - SAVE_SAMPLE_DATA
              request:
                allOf:
                  - type: object
                    properties:
                      stepName:
                        type: string
                      payload: {}
                      type:
                        anyOf:
                          - type: string
                            enum:
                              - INPUT
                          - type: string
                            enum:
                              - OUTPUT
                      dataType:
                        anyOf:
                          - type: string
                            enum:
                              - JSON
                          - type: string
                            enum:
                              - STRING
                    required:
                      - stepName
                      - payload
                      - type
                      - dataType
            requiredProperties:
              - type
              - request
        examples:
          example:
            value:
              type: MOVE_ACTION
              request:
                name: <string>
                newParentStep: <string>
                stepLocationRelativeToNewParent: AFTER
                branchIndex: 123
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