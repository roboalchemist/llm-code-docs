# Source: https://dev.writer.com/api-reference-legacy/snippet/update-snippets.md

# Update snippets

## OpenAPI

````yaml put /snippet/organization/{organizationId}/team/{teamId}
paths:
  path: /snippet/organization/{organizationId}/team/{teamId}
  method: put
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
      query: {}
      header:
        Authorization:
          schema:
            - type: string
              required: true
        X-Request-ID:
          schema:
            - type: string
              required: false
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/SnippetUpdate'
            required: false
        examples:
          example:
            value:
              - id: <string>
                snippet: <string>
                shortcut: <string>
                description: <string>
                tags:
                  - tag: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/SnippetWithUser'
        examples:
          example:
            value:
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
    SnippetUpdate:
      required:
        - id
        - snippet
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
        tags:
          type: array
          items:
            $ref: '#/components/schemas/SnippetTagV2'
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