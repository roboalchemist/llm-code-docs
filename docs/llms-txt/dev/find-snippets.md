# Source: https://dev.writer.com/api-reference-legacy/snippet/find-snippets.md

# Find snippets

## OpenAPI

````yaml get /snippet/organization/{organizationId}/team/{teamId}
paths:
  path: /snippet/organization/{organizationId}/team/{teamId}
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
        shortcuts:
          schema:
            - type: array
              items:
                allOf:
                  - type: string
              required: false
        search:
          schema:
            - type: string
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
                - shortcut
                - creationTime
                - modificationTime
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
                      $ref: '#/components/schemas/SnippetWithUser'
              totalCount:
                allOf:
                  - type: integer
                    format: int64
              pagination:
                allOf:
                  - $ref: '#/components/schemas/Pagination'
            refIdentifier: '#/components/schemas/PaginatedResult_SnippetWithUser'
            requiredProperties:
              - totalCount
              - pagination
        examples:
          example:
            value:
              result:
                - id: <string>
                  snippet: <string>
                  shortcut: <string>
                  description: <string>
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
                  tags:
                    - tag: <string>
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
    SnippetWithUser:
      required:
        - linkedId
        - id
        - snippet
        - creationTime
        - modificationTime
        - createdUser
        - modifiedUser
      type: object
      properties:
        id:
          type: string
        snippet:
          type: string
        shortcut:
          type: string
        description:
          type: string
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
        tags:
          type: array
          items:
            $ref: '#/components/schemas/SnippetTagV2'
    Pagination:
      type: object
      properties:
        offset:
          type: integer
          format: int64
        limit:
          type: integer
    Json: {}
    SnippetTagV2:
      required:
        - tag
      type: object
      properties:
        tag:
          type: string
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