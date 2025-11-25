# Source: https://www.quo.com/docs/mdx/api-reference/phone-numbers/list-phone-numbers.md

# List phone numbers

> Retrieve the list of phone numbers and users associated with your OpenPhone workspace.

## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json get /v1/phone-numbers
paths:
  path: /v1/phone-numbers
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
      query:
        userId:
          schema:
            - type: string
              required: false
              description: >-
                Filter results to return only phone numbers associated with the
                specified user"s unique identifier.
              examples:
                - US123abc
              example: US123abc
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
                        id:
                          description: The unique identifier of OpenPhone phone number.
                          examples:
                            - PN123bc
                          pattern: ^PN(.*)$
                          type: string
                        groupId:
                          description: >-
                            The unique identifier of the group to which the
                            OpenPhone number belongs.
                          examples:
                            - '1234'
                          type: string
                        portRequestId:
                          anyOf:
                            - description: >-
                                Unique identifier for the phone number’s porting
                                request, if applicable.
                              examples:
                                - 123abc
                              type: string
                            - type: 'null'
                        formattedNumber:
                          anyOf:
                            - description: >-
                                A human-readable representation of a phone
                                number.
                              examples:
                                - '+15555555555'
                              type: string
                            - type: 'null'
                        forward:
                          anyOf:
                            - description: >-
                                Forwarding number for incoming calls, null if no
                                forwarding number is configured.
                              examples:
                                - '+15555555555'
                              type: string
                            - type: 'null'
                        name:
                          description: The display name of the phone number
                          examples:
                            - My phone number
                          type: string
                        number:
                          description: >-
                            A phone number in E.164 format, including the
                            country code.
                          examples:
                            - '+15555555555'
                          pattern: ^\+[1-9]\d{1,14}$
                          type: string
                        portingStatus:
                          anyOf:
                            - description: >-
                                Current status of the porting process, if
                                applicable.
                              examples:
                                - completed
                              type: string
                            - type: 'null'
                        symbol:
                          anyOf:
                            - description: >-
                                Custom symbol or emoji associated with the phone
                                number.
                              examples:
                                - 🏡
                              type: string
                            - type: 'null'
                        users:
                          type: array
                          items:
                            type: object
                            allOf:
                              - type: object
                                properties:
                                  email:
                                    description: The user's email address.
                                    examples:
                                      - my@email.com
                                    format: email
                                    type: string
                                  firstName:
                                    anyOf:
                                      - description: The user's first name.
                                        examples:
                                          - John
                                        type: string
                                      - type: 'null'
                                  lastName:
                                    anyOf:
                                      - description: The user's last name.
                                        examples:
                                          - Doe
                                        type: string
                                      - type: 'null'
                                  id:
                                    pattern: ^US(.*)$
                                    type: string
                                  role:
                                    type: string
                                    enum:
                                      - owner
                                      - admin
                                      - member
                                    description: The user's role in the organization.
                                    examples:
                                      - owner
                                      - admin
                                      - member
                                required:
                                  - email
                                  - firstName
                                  - lastName
                                  - id
                                  - role
                              - type: object
                                properties:
                                  groupId:
                                    description: >-
                                      The unique identifier of the group to
                                      which the user belongs.
                                    examples:
                                      - GRcei8k90o
                                    pattern: ^GR(.*)$
                                    type: string
                                required:
                                  - groupId
                        createdAt:
                          description: >-
                            Timestamp of when the phone number was added to the
                            account in ISO 8601 format.
                          examples:
                            - ' ''2022-01-01T00:00:00Z'''
                          type: string
                        updatedAt:
                          description: >-
                            Timestamp of the last update to the phone number's
                            details in ISO 8601 format.
                          examples:
                            - ' ''2022-01-01T00:00:00Z'''
                          type: string
                        restrictions:
                          type: object
                          properties:
                            calling:
                              type: object
                              properties:
                                CA:
                                  type: string
                                  enum:
                                    - restricted
                                    - unrestricted
                                  description: >-
                                    The phone-number usage restriction status
                                    for a specific region
                                  examples:
                                    - unrestricted
                                Intl:
                                  type: string
                                  enum:
                                    - restricted
                                    - unrestricted
                                  description: >-
                                    The phone-number usage restriction status
                                    for a specific region
                                  examples:
                                    - unrestricted
                                US:
                                  type: string
                                  enum:
                                    - restricted
                                    - unrestricted
                                  description: >-
                                    The phone-number usage restriction status
                                    for a specific region
                                  examples:
                                    - unrestricted
                              required:
                                - CA
                                - Intl
                                - US
                            messaging:
                              type: object
                              properties:
                                CA:
                                  type: string
                                  enum:
                                    - restricted
                                    - unrestricted
                                  description: >-
                                    The phone-number usage restriction status
                                    for a specific region
                                  examples:
                                    - unrestricted
                                Intl:
                                  type: string
                                  enum:
                                    - restricted
                                    - unrestricted
                                  description: >-
                                    The phone-number usage restriction status
                                    for a specific region
                                  examples:
                                    - unrestricted
                                US:
                                  type: string
                                  enum:
                                    - restricted
                                    - unrestricted
                                  description: >-
                                    The phone-number usage restriction status
                                    for a specific region
                                  examples:
                                    - unrestricted
                              required:
                                - CA
                                - Intl
                                - US
                          required:
                            - calling
                            - messaging
                      required:
                        - id
                        - groupId
                        - portRequestId
                        - formattedNumber
                        - forward
                        - name
                        - number
                        - portingStatus
                        - symbol
                        - users
                        - createdAt
                        - updatedAt
                        - restrictions
            refIdentifier: '#/components/schemas/ListPhoneNumbersResponse'
            requiredProperties:
              - data
        examples:
          example:
            value:
              data:
                - id: PN123bc
                  groupId: '1234'
                  portRequestId: 123abc
                  formattedNumber: '+15555555555'
                  forward: '+15555555555'
                  name: My phone number
                  number: '+15555555555'
                  portingStatus: completed
                  symbol: 🏡
                  users:
                    - email: my@email.com
                      firstName: John
                      lastName: Doe
                      id: <string>
                      role: owner
                      groupId: GRcei8k90o
                  createdAt: ' ''2022-01-01T00:00:00Z'''
                  updatedAt: ' ''2022-01-01T00:00:00Z'''
                  restrictions:
                    calling:
                      CA: unrestricted
                      Intl: unrestricted
                      US: unrestricted
                    messaging:
                      CA: unrestricted
                      Intl: unrestricted
                      US: unrestricted
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
                  - const: '0400400'
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
                  - const: '0400401'
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
                  - const: '0400403'
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
                  - const: '0400404'
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
                  - const: '0401500'
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