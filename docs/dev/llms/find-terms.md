# Source: https://dev.writer.com/api-reference-legacy/terminology/find-terms.md

# Find terms

## OpenAPI

````yaml get /terminology/organization/{organizationId}/team/{teamId}
paths:
  path: /terminology/organization/{organizationId}/team/{teamId}
  method: get
  servers:
    - url: https://enterprise-api.writer.com
  request:
    security: []
    parameters:
      path:
        organizationId:
          schema:
            - type: integer
              required: true
        teamId:
          schema:
            - type: integer
              required: true
      query:
        type:
          schema:
            - type: enum<string>
              enum:
                - approved
                - banned
                - pending
              required: false
        term:
          schema:
            - type: string
              required: false
        partOfSpeech:
          schema:
            - type: enum<string>
              enum:
                - noun
                - verb
                - adverb
                - adjective
              required: false
        tags:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
              required: false
        sortField:
          schema:
            - type: enum<string>
              enum:
                - term
                - creationTime
                - modificationTime
                - type
              required: false
        sortOrder:
          schema:
            - type: enum<string>
              enum:
                - asc
                - desc
              required: false
        offset:
          schema:
            - type: integer
              required: false
        limit:
          schema:
            - type: integer
              required: false
      header:
        Authorization:
          schema:
            - type: string
              required: true
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              result:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/FullTermWithUser'
              totalCount:
                allOf:
                  - type: integer
                    format: int64
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            refIdentifier: '#/components/schemas/PaginatedResult_FullTermWithUser'
            requiredProperties:
              - totalCount
              - pagination
        examples:
          example:
            value:
              result:
                - id: 123
                  termBankId: 123
                  term: <string>
                  type: approved
                  pos: noun
                  caseSensitive: true
                  description: <string>
                  highlight: true
                  creationTime: '2023-11-07T05:31:56Z'
                  modificationTime: '2023-11-07T05:31:56Z'
                  createdUser:
                    id: 123
                    fullName: <string>
                    email: <string>
                  modifiedUser:
                    id: 123
                    fullName: <string>
                    email: <string>
                  examples:
                    - id: 123
                      termId: 123
                      termBankId: 123
                      example: <string>
                      type: good
                  mistakes:
                    - id: 123
                      termId: 123
                      termBankId: 123
                      mistake: <string>
                      pos: noun
                      caseSensitive: true
                  tags:
                    - id: 123
                      tag: <string>
                      termId: 123
                      parentTagId: 123
                  linkedTerms:
                    - id: 123
                      termId: 123
                      linkedTermId: 123
                      term: <string>
                      pos: noun
                      caseSensitive: true
                      approvedTermExtension:
                        id: 123
                        termId: 123
                        capitalize: true
                        fixCommonMistakes: true
                        fixCase: true
                  backlinkedTerms:
                    - id: 123
                      termId: 123
                      linkedTermId: 123
                      term: <string>
                      pos: noun
                      caseSensitive: true
                      approvedTermExtension:
                        id: 123
                        termId: 123
                        capitalize: true
                        fixCommonMistakes: true
                        fixCase: true
                  approvedTermExtension:
                    id: 123
                    termId: 123
                    capitalize: true
                    fixCommonMistakes: true
                    fixCase: true
              totalCount: 123
              pagination:
                offset: 123
                limit: 123
        description: ''
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - &ref_0
                    type: string
              errors:
                allOf:
                  - &ref_1
                    type: array
                    items:
                      $ref: '#/components/schemas/FailMessage'
              extras:
                allOf:
                  - &ref_2
                    $ref: '#/components/schemas/Json'
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: &ref_3
              - tpe
              - extras
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Bad Request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Not Found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Internal Server Error
  deprecated: false
  type: path
components:
  schemas:
    FailMessage:
      required:
        - description
        - key
        - extras
      type: object
      properties:
        description:
          type: string
        key:
          type: string
        extras:
          $ref: '#/components/schemas/Json'
    Pagination:
      type: object
      properties:
        offset:
          type: integer
          format: int64
        limit:
          type: integer
    TermTagResponse:
      required:
        - id
        - tag
        - termId
        - parentTagId
      type: object
      properties:
        id:
          type: integer
          format: int64
        tag:
          type: string
        termId:
          type: integer
          format: int64
        parentTagId:
          type: integer
          format: int64
    TermExample:
      required:
        - termId
        - termBankId
        - example
        - type
      type: object
      properties:
        id:
          type: integer
          format: int64
        termId:
          type: integer
          format: int64
        termBankId:
          type: integer
          format: int64
        example:
          type: string
        type:
          type: string
          enum:
            - good
            - bad
    FullLinkedTerm:
      required:
        - termId
        - linkedTermId
        - term
        - caseSensitive
      type: object
      properties:
        id:
          type: integer
          format: int64
        termId:
          type: integer
          format: int64
        linkedTermId:
          type: integer
          format: int64
        term:
          type: string
        pos:
          type: string
          enum:
            - noun
            - verb
            - adverb
            - adjective
        caseSensitive:
          type: boolean
        approvedTermExtension:
          $ref: '#/components/schemas/ApprovedTermExtension'
    Json: {}
    ApprovedTermExtension:
      required:
        - termId
        - capitalize
        - fixCommonMistakes
        - fixCase
      type: object
      properties:
        id:
          type: integer
          format: int64
        termId:
          type: integer
          format: int64
        capitalize:
          type: boolean
        fixCommonMistakes:
          type: boolean
        fixCase:
          type: boolean
    TermMistake:
      required:
        - termId
        - termBankId
        - mistake
        - caseSensitive
      type: object
      properties:
        id:
          type: integer
          format: int64
        termId:
          type: integer
          format: int64
        termBankId:
          type: integer
          format: int64
        mistake:
          type: string
        pos:
          type: string
          enum:
            - noun
            - verb
            - adverb
            - adjective
        caseSensitive:
          type: boolean
    FullTermWithUser:
      required:
        - id
        - termBankId
        - term
        - type
        - caseSensitive
        - highlight
        - creationTime
        - modificationTime
        - createdUser
        - modifiedUser
      type: object
      properties:
        id:
          type: integer
          format: int64
        termBankId:
          type: integer
          format: int64
        term:
          type: string
        type:
          type: string
          enum:
            - approved
            - banned
            - pending
        pos:
          type: string
          enum:
            - noun
            - verb
            - adverb
            - adjective
        caseSensitive:
          type: boolean
        description:
          type: string
        highlight:
          type: boolean
        creationTime:
          type: string
          format: date-time
        modificationTime:
          type: string
          format: date-time
        createdUser:
          $ref: '#/components/schemas/TerminologyUser'
        modifiedUser:
          $ref: '#/components/schemas/TerminologyUser'
        examples:
          type: array
          items:
            $ref: '#/components/schemas/TermExample'
        mistakes:
          type: array
          items:
            $ref: '#/components/schemas/TermMistake'
        tags:
          type: array
          items:
            $ref: '#/components/schemas/TermTagResponse'
        linkedTerms:
          type: array
          items:
            $ref: '#/components/schemas/FullLinkedTerm'
        backlinkedTerms:
          type: array
          items:
            $ref: '#/components/schemas/FullLinkedTerm'
        approvedTermExtension:
          $ref: '#/components/schemas/ApprovedTermExtension'
    TerminologyUser:
      required:
        - id
      type: object
      properties:
        id:
          type: integer
          format: int64
        fullName:
          type: string
        email:
          type: string

````