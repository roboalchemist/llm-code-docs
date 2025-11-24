# Source: https://dev.writer.com/api-reference-legacy/cowrite/post-cowriteorganization-team-generate.md

# null

## OpenAPI

````yaml post /cowrite/organization/{organizationId}/team/{teamId}/generate
paths:
  path: /cowrite/organization/{organizationId}/team/{teamId}/generate
  method: post
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
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              templateId:
                allOf:
                  - type: string
              inputs:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/MagicRequestInput'
            required: true
            refIdentifier: '#/components/schemas/GenerateTemplateRequest'
            requiredProperties:
              - templateId
        examples:
          example:
            value:
              templateId: <string>
              inputs:
                - name: <string>
                  value:
                    - <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: integer
                    format: int64
              organizationId:
                allOf:
                  - type: integer
                    format: int64
              teamId:
                allOf:
                  - type: integer
                    format: int64
              documentId:
                allOf:
                  - type: string
              templateId:
                allOf:
                  - type: string
              body:
                allOf:
                  - type: string
              title:
                allOf:
                  - type: string
              inputs:
                allOf:
                  - $ref: '#/components/schemas/Json'
              deleted:
                allOf:
                  - type: boolean
              createdUserId:
                allOf:
                  - type: integer
                    format: int64
              creationTime:
                allOf:
                  - type: string
                    format: date-time
            refIdentifier: '#/components/schemas/Draft'
            requiredProperties:
              - organizationId
              - teamId
              - documentId
              - templateId
              - body
              - inputs
              - deleted
              - createdUserId
              - creationTime
        examples:
          example:
            value:
              id: 123
              organizationId: 123
              teamId: 123
              documentId: <string>
              templateId: <string>
              body: <string>
              title: <string>
              inputs: <any>
              deleted: true
              createdUserId: 123
              creationTime: '2023-11-07T05:31:56Z'
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
    Json: {}
    MagicRequestInput:
      required:
        - name
      type: object
      properties:
        name:
          type: string
        value:
          type: array
          items:
            type: string

````