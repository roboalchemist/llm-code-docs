# Source: https://www.quo.com/docs/mdx/api-reference/phone-numbers/get-a-phone-number-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.quo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a phone number by ID

> Get a phone number by its unique identifier.



## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json get /v1/phone-numbers/{phoneNumberId}
openapi: 3.1.0
info:
  title: OpenPhone Public API
  version: 1.0.0
  description: API for connecting with OpenPhone.
  contact:
    name: OpenPhone Support
    email: support@openphone.com
    url: https://support.openphone.com/hc/en-us
  termsOfService: https://www.openphone.com/terms
servers:
  - description: Production server
    url: https://api.openphone.com
security:
  - apiKey: []
tags:
  - description: Operations related to calls
    name: Calls
  - description: >-
      Operations related to call summaries, including AI-generated summaries and
      Sona voice assistant summaries
    name: Call Summaries
  - description: >-
      Operations related to call transcripts, including AI-generated transcripts
      and Sona voice assistant transcripts
    name: Call Transcripts
  - description: Operations related to contacts
    name: Contacts
  - description: Operations related to conversations
    name: Conversations
  - description: Operations related to text messages
    name: Messages
  - description: Operations related to phone numbers
    name: Phone Numbers
  - description: Operations related to users
    name: Users
  - description: Operations related to webhooks
    name: Webhooks
paths:
  /v1/phone-numbers/{phoneNumberId}:
    get:
      tags:
        - Phone Numbers
      summary: Get a phone number by ID
      description: Get a phone number by its unique identifier.
      operationId: getPhoneNumberById_v1
      parameters:
        - in: path
          name: phoneNumberId
          required: true
          schema:
            description: Unique identifier of the phone number.
            examples:
              - PNlja6rrtI
            pattern: ^PN(.*)$
            type: string
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
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
                          - description: A human-readable representation of a phone number.
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
                          A phone number in E.164 format, including the country
                          code.
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
                                    The unique identifier of the group to which
                                    the user belongs.
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
                                  The phone-number usage restriction status for
                                  a specific region
                                examples:
                                  - unrestricted
                              Intl:
                                type: string
                                enum:
                                  - restricted
                                  - unrestricted
                                description: >-
                                  The phone-number usage restriction status for
                                  a specific region
                                examples:
                                  - unrestricted
                              US:
                                type: string
                                enum:
                                  - restricted
                                  - unrestricted
                                description: >-
                                  The phone-number usage restriction status for
                                  a specific region
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
                                  The phone-number usage restriction status for
                                  a specific region
                                examples:
                                  - unrestricted
                              Intl:
                                type: string
                                enum:
                                  - restricted
                                  - unrestricted
                                description: >-
                                  The phone-number usage restriction status for
                                  a specific region
                                examples:
                                  - unrestricted
                              US:
                                type: string
                                enum:
                                  - restricted
                                  - unrestricted
                                description: >-
                                  The phone-number usage restriction status for
                                  a specific region
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
                required:
                  - data
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0400400'
                    type: string
                  status:
                    const: 400
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Bad Request
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
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
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0400401'
                    type: string
                  status:
                    const: 401
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Unauthorized
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
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
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0400403'
                    type: string
                  status:
                    const: 403
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Forbidden
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
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
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0400404'
                    type: string
                  status:
                    const: 404
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Not Found
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
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
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '500':
          description: Unknown Error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0401500'
                    type: string
                  status:
                    const: 500
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Unknown
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
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
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      in: header
      name: Authorization
      type: apiKey

````