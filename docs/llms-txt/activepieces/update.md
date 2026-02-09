# Source: https://www.activepieces.com/docs/endpoints/users/update.md

# Source: https://www.activepieces.com/docs/endpoints/projects/update.md

# Source: https://www.activepieces.com/docs/endpoints/global-connections/update.md

# Source: https://www.activepieces.com/docs/endpoints/folders/update.md

# Source: https://www.activepieces.com/docs/endpoints/flows/update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Apply Flow Operation

> Apply an operation to a flow



## OpenAPI

````yaml POST /v1/flows/{id}
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
  /v1/flows/{id}:
    post:
      tags:
        - flows
      description: Apply an operation to a flow
      parameters:
        - schema:
            pattern: ^[0-9a-zA-Z]{21}$
            type: string
          in: path
          name: id
          required: true
      requestBody:
        content:
          application/json:
            schema:
              anyOf:
                - title: Move Action
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - MOVE_ACTION
                    request:
                      type: object
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
                  required:
                    - type
                    - request
                - title: Change Status
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - CHANGE_STATUS
                    request:
                      type: object
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
                  required:
                    - type
                    - request
                - title: Lock and Publish
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - LOCK_AND_PUBLISH
                    request:
                      type: object
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
                    - type
                    - request
                - title: Copy as Draft
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - USE_AS_DRAFT
                    request:
                      type: object
                      properties:
                        versionId:
                          type: string
                      required:
                        - versionId
                  required:
                    - type
                    - request
                - title: Lock Flow
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - LOCK_FLOW
                    request:
                      type: object
                      properties: {}
                  required:
                    - type
                    - request
                - title: Import Flow
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - IMPORT_FLOW
                    request:
                      type: object
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
                          nullable: true
                      required:
                        - displayName
                        - trigger
                  required:
                    - type
                    - request
                - title: Change Name
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - CHANGE_NAME
                    request:
                      type: object
                      properties:
                        displayName:
                          type: string
                      required:
                        - displayName
                  required:
                    - type
                    - request
                - title: Delete Action
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - DELETE_ACTION
                    request:
                      type: object
                      properties:
                        names:
                          type: array
                          items:
                            type: string
                      required:
                        - names
                  required:
                    - type
                    - request
                - title: Update Action
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - UPDATE_ACTION
                    request:
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
                                    retryOnFailure:
                                      type: object
                                      properties:
                                        value:
                                          type: boolean
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
                                    retryOnFailure:
                                      type: object
                                      properties:
                                        value:
                                          type: boolean
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
                    - type
                    - request
                - title: Add Action
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - ADD_ACTION
                    request:
                      type: object
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
                                        retryOnFailure:
                                          type: object
                                          properties:
                                            value:
                                              type: boolean
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
                                        retryOnFailure:
                                          type: object
                                          properties:
                                            value:
                                              type: boolean
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
                  required:
                    - type
                    - request
                - title: Update Trigger
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - UPDATE_TRIGGER
                    request:
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
                  required:
                    - type
                    - request
                - title: Change Folder
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - CHANGE_FOLDER
                    request:
                      type: object
                      properties:
                        folderId:
                          type: string
                          nullable: true
                  required:
                    - type
                    - request
                - title: Duplicate Action
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - DUPLICATE_ACTION
                    request:
                      type: object
                      properties:
                        stepName:
                          type: string
                      required:
                        - stepName
                  required:
                    - type
                    - request
                - title: Delete Branch
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - DELETE_BRANCH
                    request:
                      type: object
                      properties:
                        branchIndex:
                          type: number
                        stepName:
                          type: string
                      required:
                        - branchIndex
                        - stepName
                  required:
                    - type
                    - request
                - title: Add Branch
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - ADD_BRANCH
                    request:
                      type: object
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
                  required:
                    - type
                    - request
                - title: Duplicate Branch
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - DUPLICATE_BRANCH
                    request:
                      type: object
                      properties:
                        branchIndex:
                          type: number
                        stepName:
                          type: string
                      required:
                        - branchIndex
                        - stepName
                  required:
                    - type
                    - request
                - title: Skip Action
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - SET_SKIP_ACTION
                    request:
                      type: object
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
                  required:
                    - type
                    - request
                - title: Update Metadata
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - UPDATE_METADATA
                    request:
                      type: object
                      properties:
                        metadata:
                          type: object
                          nullable: true
                          additionalProperties: {}
                  required:
                    - type
                    - request
                - type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - MOVE_BRANCH
                    request:
                      type: object
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
                  required:
                    - type
                    - request
                - type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - SAVE_SAMPLE_DATA
                    request:
                      type: object
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
                  required:
                    - type
                    - request
                - title: Update Minutes Saved
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - UPDATE_MINUTES_SAVED
                    request:
                      type: object
                      properties:
                        timeSavedPerRun:
                          type: number
                          nullable: true
                  required:
                    - type
                    - request
                - title: Update Owner
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - UPDATE_OWNER
                    request:
                      type: object
                      properties:
                        ownerId:
                          type: string
                      required:
                        - ownerId
                  required:
                    - type
                    - request
                - title: Update Note
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - UPDATE_NOTE
                    request:
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
                      required:
                        - id
                        - content
                        - color
                        - position
                        - size
                  required:
                    - type
                    - request
                - title: Delete Note
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - DELETE_NOTE
                    request:
                      type: object
                      properties:
                        id:
                          type: string
                      required:
                        - id
                  required:
                    - type
                    - request
                - title: Add Note
                  type: object
                  properties:
                    type:
                      type: string
                      enum:
                        - ADD_NOTE
                    request:
                      type: object
                      properties:
                        id:
                          type: string
                        content:
                          type: string
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
                      required:
                        - id
                        - content
                        - color
                        - position
                        - size
                  required:
                    - type
                    - request
      responses:
        '200':
          description: Default Response
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: http
      description: Use your api key generated from the admin console
      scheme: bearer

````