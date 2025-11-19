# Source: https://dev.writer.com/api-reference-legacy/cowrite/get-cowriteorganization-team-template.md

# null

## OpenAPI

````yaml get /cowrite/organization/{organizationId}/team/{teamId}/template/{templateId}
paths:
  path: /cowrite/organization/{organizationId}/team/{teamId}/template/{templateId}
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
        templateId:
          schema:
            - type: string
              required: true
      query: {}
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
              id:
                allOf:
                  - type: string
              name:
                allOf:
                  - type: string
              description:
                allOf:
                  - type: string
              categoryId:
                allOf:
                  - type: integer
                    format: int64
              inputs:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/Input'
              guideUrl:
                allOf:
                  - type: string
              creationTime:
                allOf:
                  - type: string
                    format: date-time
              modificationTime:
                allOf:
                  - type: string
                    format: date-time
            refIdentifier: '#/components/schemas/TemplateDetailsResponse'
            requiredProperties:
              - id
              - name
              - categoryId
              - creationTime
              - modificationTime
        examples:
          example:
            value:
              id: <string>
              name: <string>
              description: <string>
              categoryId: 123
              inputs:
                - name: <string>
                  type: textbox
                  help: <string>
                  subtitle: <string>
                  required: true
                  options:
                    - <string>
                  dynamic: true
                  minFields: 123
                  maxFields: 123
                  unitCopy: <string>
              guideUrl: <string>
              creationTime: '2023-11-07T05:31:56Z'
              modificationTime: '2023-11-07T05:31:56Z'
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
    Input:
      required:
        - name
        - type
        - required
        - dynamic
      type: object
      properties:
        name:
          type: string
        type:
          type: string
          enum:
            - textbox
            - textarea
            - dropdown
        help:
          type: string
        subtitle:
          type: string
        required:
          type: boolean
        options:
          type: array
          items:
            type: string
        dynamic:
          type: boolean
        minFields:
          type: integer
        maxFields:
          type: integer
        unitCopy:
          type: string

````