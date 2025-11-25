# Source: https://www.quo.com/docs/mdx/api-reference/contact-custom-fields/get-contact-custom-fields.md

# Get contact custom fields

> Custom contact fields enhance your OpenPhone contacts with additional information beyond standard details like name, company, role, emails and phone numbers. These user-defined fields let you capture business-specific data. While you can only create or modify these fields in OpenPhone itself, this endpoint retrieves your existing custom properties. Use this information to accurately map and include important custom data when creating new contacts via the API.

## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json get /v1/contact-custom-fields
paths:
  path: /v1/contact-custom-fields
  method: get
  servers:
    - url: https://api.openphone.com
      description: Production server
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
          cookie: {}
    parameters:
      path: {}
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
              data:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        name:
                          description: >-
                            The name of the custom contact field. This name is
                            set by users in the OpenPhone interface when the
                            custom field is created.
                          examples:
                            - Inbound Lead
                          type: string
                        key:
                          description: The identifying key for contact custom field.
                          examples:
                            - inbound-lead
                          type: string
                        type:
                          type: string
                          enum:
                            - address
                            - boolean
                            - date
                            - multi-select
                            - number
                            - string
                            - url
                          description: >-
                            The data type of the custom contact field,
                            determining what kind of information can be stored
                            and how it should be formatted.
                          examples:
                            - boolean
                      required:
                        - name
                        - key
                        - type
            requiredProperties:
              - data
        examples:
          example:
            value:
              data:
                - name: Inbound Lead
                  key: inbound-lead
                  type: boolean
        description: Success
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0700400'
                    type: string
              status:
                allOf:
                  - const: 400
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Bad Request
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
        description: Bad Request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0700401'
                    type: string
              status:
                allOf:
                  - const: 401
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Unauthorized
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
        description: Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0700403'
                    type: string
              status:
                allOf:
                  - const: 403
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Forbidden
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
        description: Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0700404'
                    type: string
              status:
                allOf:
                  - const: 404
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Not Found
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
        description: Not Found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0701500'
                    type: string
              status:
                allOf:
                  - const: 500
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Unknown
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
        description: Unknown Error
  deprecated: false
  type: path
components:
  schemas: {}

````