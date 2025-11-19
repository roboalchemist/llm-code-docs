# Source: https://docs.solidfi.com/v2/api-reference/card-holders/retrieve-a-card-holder.md

# Retrieve a Card Holder

> Retrieve a Card Holder

## OpenAPI

````yaml get /v2/issuing/card_holder/{card_holder_id}
paths:
  path: /v2/issuing/card_holder/{card_holder_id}
  method: get
  servers:
    - url: https://api.sandbox.solidfi.com
    - url: https://api.prod.solidfi.com
  request:
    security:
      - title: ''
        parameters:
          query: {}
          header: {}
          cookie: {}
    parameters:
      path:
        card_holder_id:
          schema:
            - type: string
              required: true
      query: {}
      header:
        api-key:
          schema:
            - type: string
              required: true
              description: >-
                API key is required to call Solid APIs. You can view and manage
                your API keys in the Solid dashboard.
              example: '{{api_key}}'
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
                    example: cah_a120a61f60dfd40fdb07b2e8bcd1f6f0
                    description: unique id of the card holder
              client_id:
                allOf:
                  - type: string
                    example: cli_64c6c87ee9d609f36a6f390dc378a4ce
                    description: unique id of the client that issued the card
              master_account_holder_id:
                allOf:
                  - type: string
                    example: mah_201e02c581a098a740456c5c19fcfcd6
                    description: unique id of the master account holder
              master_account_id:
                allOf:
                  - type: string
                    example: mas_743fa071316bc6beaf5dddfd05f49c30
                    description: unique id of the master account
              sub_account_holder_id:
                allOf:
                  - type: string
                    example: sah_5ccfeef0adf0cbe2aa0980d2c9505752
                    description: unique id of the sub account holder
              sub_account_id:
                allOf:
                  - type: string
                    example: sub_bda1e562657c41e553104b10aad3fe70
                    description: unique id of the sub account
              person:
                allOf:
                  - type: object
                    $ref: '#/components/schemas/person'
              external_reference_id:
                allOf:
                  - type: string
                    example: 6RPD1QW-W75
                    description: unique id to cross-reference records with external systems
              purpose:
                allOf:
                  - type: string
                    example: Ace Sales Rep
                    description: purpose of card holder
              ofac:
                allOf:
                  - type: object
                    $ref: '#/components/schemas/card_holder_ofac'
              attachments:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/attachment_object'
              metadata:
                allOf:
                  - type: object
                    $ref: '#/components/schemas/metadata'
              status:
                allOf:
                  - type: string
                    example: activated
                    description: status of card holder
                    enum:
                      - pending_activation
                      - activated
                      - suspended
                      - deactivated
                      - locked
              timestamps:
                allOf:
                  - type: object
                    $ref: '#/components/schemas/card_holder_timestamp'
            refIdentifier: '#/components/schemas/card_holder'
        examples:
          card_holder_example:
            value:
              id: cah_a120a61f60dfd40fdb07b2e8bcd1f6f0
              client_id: cli_64c6c87ee9d609f36a6f390dc378a4ce
              master_account_holder_id: mah_201e02c581a098a740456c5c19fcfcd6
              master_account_id: mas_743fa071316bc6beaf5dddfd05f49c30
              sub_account_holder_id: sah_5ccfeef0adf0cbe2aa0980d2c9505752
              sub_account_id: sub_bda1e562657c41e553104b10aad3fe70
              person:
                first_name: John
                last_name: Doe
                id_type: ssn
                id_number: '223902234'
                date_of_birth: '1974-01-25'
                phone: '+19418405843'
                email: john.doe@gmail.com
                address:
                  line1: 123 Main St
                  line2: ''
                  city: New York
                  state: NY
                  country: US
                  postal_code: '10001'
              external_reference_id: 6RPD1QW-W75
              purpose: Ace Sales Rep
              ofac:
                status: pass
                last_updated_at: '2024-04-01T21:00:00Z'
              metadata:
                designation: Senior Sales Manager
                employee_number: '77'
              attachments:
                - label: Employee Badge
                  id: att_a8d2b191fa0e960d8e49a4bfd320e07b
                  created_at: '2024-04-01T21:00:00Z'
              status: activated
              timestamps:
                created_at: '2024-04-01T21:00:00Z'
                updated_at: '2024-04-02T21:00:00Z'
                deactivated_at: '2024-04-02T21:00:00Z'
        description: Retrieve a Card Holder
    '401':
      application/json:
        schemaArray:
          - type: any
        examples:
          card_holder_example:
            value:
              request_id: req_01900e34c96d7abfa970a9f454ab2d5d
              client_id: ''
              method: GET
              status: 401
              error:
                code: ERROR_CODE_UNAUTHORIZED
                message: unauthorized
                field_name: ''
              created_at: '2024-06-12T20:47:38Z'
        description: Unauthorized Error
    '404':
      application/json:
        schemaArray:
          - type: any
        examples:
          master_account_example:
            value:
              request_id: req_01900e959896706b870affad1b4d71dd
              client_id: ''
              method: GET
              status: 404
              error:
                code: ERROR_CODE_RESOURCE_NOT_FOUND
                message: cannot find card holder by id in qldb
                field_name: ''
              created_at: '2024-06-12T22:33:23Z'
        description: Not Found Error
  deprecated: false
  type: path
components:
  schemas:
    person:
      type: object
      properties:
        first_name:
          type: string
          example: Jane
          description: first name of the person
        middle_name:
          type: string
          example: Jack
          description: middle name of the person
        last_name:
          type: string
          example: Doe
          description: last name of the person
        id_type:
          type: string
          example: ssn
          description: type of identity used
          enum:
            - ssn
            - passport
            - other
        id_number:
          type: string
          example: '945678934'
          description: |-
            - if id_type is ssn, id_number must be full SSN 
             - if id_type is passport, id_number must be passport number 
             - if id_type is other, id_number must be unique number of the id 
             
             id_number must be unique, as in, you cannot use the same id_number for two different persons
        date_of_birth:
          type: string
          example: '1974-01-01'
          description: date of birth of the person (YYYY-MM-DD)
        phone:
          type: string
          example: '+19418405843'
          description: phone number of the person (E.164, max 16 chars, starts with +)
        email:
          type: string
          example: jane.doe@gmail.com
          description: email of the person
        address:
          type: object
          properties:
            line1:
              type: string
              example: 123 Main St
              description: line 1 of the address
            line2:
              type: string
              example: ''
              description: line 2 of the address
            city:
              type: string
              example: New York
              description: city of the address
            state:
              type: string
              example: NY
              description: '2-Letter US state abbreviation (ex: CA)'
            country:
              type: string
              example: US
              description: '2-letter abbreviated country code (ex: US)'
            postal_code:
              type: string
              example: '10001'
              description: postal code
        kyc:
          type: object
          properties:
            id:
              type: string
              example: kyc_7948d9a96706dd05360a340002de725f
              description: unique id of the KYC
            status:
              type: string
              example: pass
              description: status of the KYC
              enum:
                - pass
                - fail
                - review
                - not_started
            method:
              type: string
              example: solid
              description: >-
                sub account holder verification method. It could be an external
                vendor(Ex: alloy) or Solid
            url:
              type: string
              example: >-
                https://dashboard.solidfi.com/id=kyc_7948d9a96706dd05360a340002de725f
              description: >-
                url to the person or business verification result. It could be a
                link to the external vendor or Solid
            details:
              type: object
              properties:
                name:
                  type: object
                  $ref: '#/components/schemas/kyc_kyb'
                address:
                  type: object
                  $ref: '#/components/schemas/kyc_kyb'
                dob:
                  type: object
                  $ref: '#/components/schemas/kyc_kyb'
                ssn:
                  type: object
                  $ref: '#/components/schemas/kyc_kyb'
                phone:
                  type: object
                  $ref: '#/components/schemas/kyc_kyb'
                email:
                  type: object
                  $ref: '#/components/schemas/kyc_kyb'
                watchlist:
                  type: object
                  $ref: '#/components/schemas/kyc_kyb'
                fraud:
                  type: object
                  $ref: '#/components/schemas/kyc_kyb'
        idv:
          type: object
          properties:
            id:
              type: string
              example: idv_7948d9a96706dd05360a340002de725f
              description: unique id of the IDV
            status:
              type: string
              example: pass
              description: status of the IDV
              enum:
                - pass
                - fail
                - review
                - not_started
            method:
              type: string
              example: solid
              description: >-
                sub account holder IDV method. It could be an external
                vendor(Ex: plaid) or Solid
            url:
              type: string
              example: >-
                https://dashboard.solidfi.com/id=kyc_7948d9a96706dd05360a340002de725f
              description: >-
                url to the identity verification result. It could be a link to
                the external vendor or Solid
            reasons:
              type: array
              items:
                $ref: '#/components/schemas/kyc_kyb_reasons'
    card_holder_ofac:
      type: object
      properties:
        status:
          type: string
          example: pass
          description: ofac status of the card holder
          enum:
            - pass
            - fail
        last_updated_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: >-
            last date and time at which the card holder's ofac status was
            checked
    kyc_kyb:
      type: object
      properties:
        status:
          type: string
          example: pass
          enum:
            - pass
            - fail
            - review
            - in_review
        reasons:
          type: array
          items:
            $ref: '#/components/schemas/kyc_kyb_reasons'
    kyc_kyb_reasons:
      type: object
      properties:
        code:
          type: string
          example: N001
          description: reason code
        description:
          type: string
          example: First name didn't match
          description: description of reason code
    attachment_object:
      type: object
      properties:
        id:
          type: string
          example: att_a8d2b191fa0e960d8e49a4bfd320e07b
          description: unique id of the attachment created
        label:
          type: string
          example: formation
          description: label of the attachment
        timestamps:
          type: object
          properties:
            created_at:
              type: string
              example: '2024-04-01T21:00:00Z'
              description: date and time at which the attachment was created
            deleted_at:
              type: string
              example: '2024-04-01T21:00:00Z'
              description: date and time at which the attachment was deleted
    metadata:
      type: object
      description: >-
        Metadata takes free-form key-value pairs. You may send metadata when you
        create an object (POST) and when updating the object (PATCH).  If you
        would like to remove metadata that is already on an object, you can
        unset it by passing in the key-value pair with an empty string, like
        this: 
         {"key": ""}
    card_holder_timestamp:
      type: object
      properties:
        created_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the card holder was created
        updated_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the card holder was updated
        deactivated_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the card holder was deactivated

````