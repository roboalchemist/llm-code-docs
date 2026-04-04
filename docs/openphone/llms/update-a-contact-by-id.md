# Source: https://www.quo.com/docs/mdx/api-reference/contacts/update-a-contact-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.quo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a contact by ID

> Modify an existing contact in your OpenPhone workspace using the contact's unique identifier.



## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json patch /v1/contacts/{id}
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
  /v1/contacts/{id}:
    patch:
      tags:
        - Contacts
      summary: Update a contact by ID
      description: >-
        Modify an existing contact in your OpenPhone workspace using the
        contact's unique identifier.
      operationId: updateContactById_v1
      parameters:
        - in: path
          name: id
          required: true
          schema:
            description: The unique identifier of the contact.
            examples:
              - 66d0d87e8dc1211467372303
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                externalId:
                  anyOf:
                    - description: >-
                        A unique identifier from an external system that can
                        optionally be supplied when creating a contact. This ID
                        is used to associate the contact with records in other
                        systems and is required for retrieving the contact later
                        via the "List Contacts" endpoint. Ensure the
                        `externalId` is unique and consistent across systems for
                        accurate cross-referencing.
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
                        - https://openphone.co/contacts/664d0db69fcac7cf2e6ec
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
                              - description: >-
                                  The contact's email address. If set to null
                                  during a patch operation, it will remove the
                                  email item from the contact.
                                examples:
                                  - info@openphone.com
                                type: string
                              - type: 'null'
                          id:
                            description: The unique identifier for the contact email field.
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
                              The unique identifier of the contact phone number
                              field.
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
                  type: array
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
                required:
                  - data
        '400':
          description: Invalid Custom Field Item
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0801400'
                    type: string
                  status:
                    const: 400
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Invalid Custom Field Item
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
                  description:
                    const: Invalid Custom Field Item
                    type: string
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
                  - description
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
                    const: '0800401'
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
          description: Not Phone Number User
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0801403'
                    type: string
                  status:
                    const: 403
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Not Phone Number User
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
                  description:
                    const: Not Phone Number User
                    type: string
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
                  - description
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
                    const: '0800404'
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
        '409':
          description: Conflict
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0800409'
                    type: string
                  status:
                    const: 409
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Conflict
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
                    const: '0801500'
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