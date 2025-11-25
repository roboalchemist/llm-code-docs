# Source: https://www.quo.com/docs/mdx/api-reference/contacts/update-a-contact-by-id.md

# Update a contact by ID

> Modify an existing contact in your OpenPhone workspace using the contact's unique identifier.

## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json patch /v1/contacts/{id}
paths:
  path: /v1/contacts/{id}
  method: patch
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the contact.
              examples:
                - 66d0d87e8dc1211467372303
              example: 66d0d87e8dc1211467372303
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              externalId:
                allOf:
                  - anyOf:
                      - description: >-
                          A unique identifier from an external system that can
                          optionally be supplied when creating a contact. This
                          ID is used to associate the contact with records in
                          other systems and is required for retrieving the
                          contact later via the "List Contacts" endpoint. Ensure
                          the `externalId` is unique and consistent across
                          systems for accurate cross-referencing.
                        examples:
                          - 664d0db69fcac7cf2e6ec
                        minLength: 1
                        maxLength: 75
                        type: string
                      - type: 'null'
              source:
                allOf:
                  - anyOf:
                      - description: >-
                          Indicates how the contact was created or where it
                          originated from.
                        examples:
                          - public-api
                        minLength: 1
                        maxLength: 75
                        type: string
                      - type: 'null'
              sourceUrl:
                allOf:
                  - anyOf:
                      - description: A link to the contact in the source system.
                        format: uri
                        examples:
                          - https://openphone.co/contacts/664d0db69fcac7cf2e6ec
                        minLength: 1
                        maxLength: 200
                        type: string
                      - type: 'null'
              defaultFields:
                allOf:
                  - type: object
                    properties:
                      company:
                        anyOf:
                          - description: The contact's company name.
                            examples:
                              - OpenPhone
                            type: string
                          - type: 'null'
                      emails:
                        type: array
                        items:
                          type: object
                          properties:
                            name:
                              description: The name for the contact's email address.
                              examples:
                                - company email
                              type: string
                            value:
                              anyOf:
                                - description: >-
                                    The contact's email address. If set to null
                                    during a patch operation, it will remove the
                                    email item from the contact.
                                  examples:
                                    - info@openphone.com
                                  type: string
                                - type: 'null'
                            id:
                              description: >-
                                The unique identifier for the contact email
                                field.
                              examples:
                                - acb123
                              type: string
                          required:
                            - name
                            - value
                      firstName:
                        anyOf:
                          - description: The contact's first name.
                            examples:
                              - John
                            type: string
                          - type: 'null'
                      lastName:
                        anyOf:
                          - description: The contact's last name.
                            examples:
                              - Doe
                            type: string
                          - type: 'null'
                      phoneNumbers:
                        type: array
                        items:
                          type: object
                          properties:
                            name:
                              description: The name of the contact's phone number.
                              examples:
                                - company phone
                              type: string
                            value:
                              anyOf:
                                - description: >-
                                    The contact's phone number. If set to null
                                    during a patch operation, it will remove the
                                    phone number item from the contact.
                                  examples:
                                    - '+15555555555'
                                  type: string
                                - type: 'null'
                            id:
                              description: >-
                                The unique identifier of the contact phone
                                number field.
                              examples:
                                - acb123
                              type: string
                          required:
                            - name
                            - value
                      role:
                        anyOf:
                          - description: The contact's role.
                            examples:
                              - Sales
                            type: string
                          - type: 'null'
              customFields:
                allOf:
                  - type: array
                    items:
                      allOf:
                        - type: object
                          properties:
                            key:
                              description: The identifying key for contact custom field.
                              examples:
                                - inbound-lead
                              type: string
                            id:
                              description: >-
                                The unique identifier for the contact custom
                                field.
                              examples:
                                - 66d0d87d534de8fd1c433cec3
                              type: string
                        - anyOf:
                            - type: object
                              properties:
                                value:
                                  anyOf:
                                    - type: array
                                      items:
                                        type: string
                                    - type: 'null'
                              required:
                                - value
                            - type: object
                              properties:
                                value:
                                  anyOf:
                                    - type: string
                                    - type: 'null'
                              required:
                                - value
                            - type: object
                              properties:
                                value:
                                  anyOf:
                                    - type: boolean
                                    - type: 'null'
                              required:
                                - value
                            - type: object
                              properties:
                                value:
                                  anyOf:
                                    - format: date-time
                                      type: string
                                    - type: 'null'
                              required:
                                - value
                            - type: object
                              properties:
                                value:
                                  anyOf:
                                    - type: number
                                    - type: 'null'
                              required:
                                - value
            required: true
        examples:
          example:
            value:
              externalId: 664d0db69fcac7cf2e6ec
              source: public-api
              sourceUrl: https://openphone.co/contacts/664d0db69fcac7cf2e6ec
              defaultFields:
                company: OpenPhone
                emails:
                  - name: company email
                    value: info@openphone.com
                    id: acb123
                firstName: John
                lastName: Doe
                phoneNumbers:
                  - name: company phone
                    value: '+15555555555'
                    id: acb123
                role: Sales
              customFields:
                - key: inbound-lead
                  id: 66d0d87d534de8fd1c433cec3
                  value:
                    - <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    properties:
                      id:
                        description: The unique identifier of the contact.
                        examples:
                          - 664d0db69fcac7cf2e6ec
                        type: string
                      externalId:
                        anyOf:
                          - description: >-
                              A unique identifier from an external system that
                              can optionally be supplied when creating a
                              contact. This ID is used to associate the contact
                              with records in other systems and is required for
                              retrieving the contact later via the "List
                              Contacts" endpoint. Ensure the `externalId` is
                              unique and consistent across systems for accurate
                              cross-referencing.
                            examples:
                              - 664d0db69fcac7cf2e6ec
                            minLength: 1
                            maxLength: 75
                            type: string
                          - type: 'null'
                      source:
                        anyOf:
                          - description: >-
                              Indicates how the contact was created or where it
                              originated from.
                            examples:
                              - public-api
                            minLength: 1
                            maxLength: 75
                            type: string
                          - type: 'null'
                      sourceUrl:
                        anyOf:
                          - description: A link to the contact in the source system.
                            format: uri
                            examples:
                              - >-
                                https://openphone.co/contacts/664d0db69fcac7cf2e6ec
                            minLength: 1
                            maxLength: 200
                            type: string
                          - type: 'null'
                      defaultFields:
                        type: object
                        properties:
                          company:
                            anyOf:
                              - description: The contact's company name.
                                examples:
                                  - OpenPhone
                                type: string
                              - type: 'null'
                          emails:
                            type: array
                            items:
                              type: object
                              properties:
                                name:
                                  description: The name for the contact's email address.
                                  examples:
                                    - company email
                                  type: string
                                value:
                                  anyOf:
                                    - description: The contact's email address.
                                      examples:
                                        - abc@example.com
                                      type: string
                                    - type: 'null'
                                id:
                                  description: >-
                                    The unique identifier for the contact email
                                    field.
                                  examples:
                                    - acb123
                                  type: string
                              required:
                                - name
                                - value
                          firstName:
                            anyOf:
                              - description: The contact's first name.
                                examples:
                                  - John
                                type: string
                              - type: 'null'
                          lastName:
                            anyOf:
                              - description: The contact's last name.
                                examples:
                                  - Doe
                                type: string
                              - type: 'null'
                          phoneNumbers:
                            type: array
                            items:
                              type: object
                              properties:
                                name:
                                  description: The name of the contact's phone number.
                                  examples:
                                    - company phone
                                  type: string
                                value:
                                  anyOf:
                                    - description: The contact's phone number.
                                      examples:
                                        - '+12345678901'
                                      type: string
                                    - type: 'null'
                                id:
                                  description: >-
                                    The unique identifier of the contact phone
                                    number field.
                                  examples:
                                    - acb123
                                  type: string
                              required:
                                - name
                                - value
                          role:
                            anyOf:
                              - description: The contact's role.
                                examples:
                                  - Sales
                                type: string
                              - type: 'null'
                        required:
                          - company
                          - emails
                          - firstName
                          - lastName
                          - phoneNumbers
                          - role
                      customFields:
                        type: array
                        items:
                          allOf:
                            - type: object
                              properties:
                                name:
                                  description: >-
                                    The name of the custom contact field. This
                                    name is set by users in the OpenPhone
                                    interface when the custom field is created.
                                  examples:
                                    - Inbound Lead
                                  type: string
                                key:
                                  description: >-
                                    The identifying key for contact custom
                                    field.
                                  examples:
                                    - inbound-lead
                                  type: string
                              required:
                                - name
                            - anyOf:
                                - type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - multi-select
                                    value:
                                      anyOf:
                                        - type: array
                                          items:
                                            type: string
                                        - type: 'null'
                                  required:
                                    - type
                                    - value
                                - type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - address
                                        - string
                                        - url
                                    value:
                                      anyOf:
                                        - type: string
                                        - type: 'null'
                                  required:
                                    - type
                                    - value
                                - type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - boolean
                                    value:
                                      anyOf:
                                        - type: boolean
                                        - type: 'null'
                                  required:
                                    - type
                                    - value
                                - type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - date
                                    value:
                                      anyOf:
                                        - format: date-time
                                          type: string
                                        - type: 'null'
                                  required:
                                    - type
                                    - value
                                - type: object
                                  properties:
                                    type:
                                      type: string
                                      enum:
                                        - number
                                    value:
                                      anyOf:
                                        - type: number
                                        - type: 'null'
                                  required:
                                    - type
                                    - value
                      createdAt:
                        description: Timestamp of contact creation in ISO 8601 format.
                        examples:
                          - '2022-01-01T00:00:00Z'
                        format: date-time
                        type: string
                      updatedAt:
                        description: Timestamp of last contact update in ISO 8601 format.
                        examples:
                          - '2022-01-01T00:00:00Z'
                        format: date-time
                        type: string
                      createdByUserId:
                        description: >-
                          The unique identifier of the user who created the
                          contact.
                        examples:
                          - US123abc
                        pattern: ^US(.*)$
                        type: string
                    required:
                      - id
                      - externalId
                      - source
                      - sourceUrl
                      - defaultFields
                      - customFields
                      - createdAt
                      - updatedAt
                      - createdByUserId
            requiredProperties:
              - data
        examples:
          example:
            value:
              data:
                id: 664d0db69fcac7cf2e6ec
                externalId: 664d0db69fcac7cf2e6ec
                source: public-api
                sourceUrl: https://openphone.co/contacts/664d0db69fcac7cf2e6ec
                defaultFields:
                  company: OpenPhone
                  emails:
                    - name: company email
                      value: abc@example.com
                      id: acb123
                  firstName: John
                  lastName: Doe
                  phoneNumbers:
                    - name: company phone
                      value: '+12345678901'
                      id: acb123
                  role: Sales
                customFields:
                  - name: Inbound Lead
                    key: inbound-lead
                    type: multi-select
                    value:
                      - <string>
                createdAt: '2022-01-01T00:00:00Z'
                updatedAt: '2022-01-01T00:00:00Z'
                createdByUserId: US123abc
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
                  - const: '0801400'
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
                  - const: Invalid Custom Field Item
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
              description:
                allOf:
                  - const: Invalid Custom Field Item
                    type: string
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
              - description
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
              description: <string>
        description: Invalid Custom Field Item
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
                  - const: '0800401'
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
                  - const: '0801403'
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
                  - const: Not Phone Number User
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
              description:
                allOf:
                  - const: Not Phone Number User
                    type: string
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
              - description
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
              description: <string>
        description: Not Phone Number User
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
                  - const: '0800404'
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
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0800409'
                    type: string
              status:
                allOf:
                  - const: 409
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Conflict
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
        description: Conflict
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
                  - const: '0801500'
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