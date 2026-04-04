# Source: https://docs.solidfi.com/v2/api-reference/sub-account-holders/submit-a-idv.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Submit an IDV

> Submit an IDV



## OpenAPI

````yaml post /v2/accounts/sub_account_holder/{sub_account_holder_id}/idv
openapi: 3.0.3
info:
  title: Solid v2
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.sandbox.solidfi.com
  - url: https://api.prod.solidfi.com
security: []
tags:
  - name: Master Accounts
  - name: Sub Account Holders
  - name: Sub Accounts
  - name: Counterparties
  - name: Card Holders
  - name: Cards
  - name: Transactions
  - name: Attachments
  - name: Webhooks
  - name: Simulation
  - name: ACH
  - name: Card
paths:
  /v2/accounts/sub_account_holder/{sub_account_holder_id}/idv:
    parameters:
      - name: sub_account_holder_id
        in: path
        required: true
        schema:
          type: string
    post:
      tags:
        - Sub Account Holders
      summary: Submit an IDV
      description: Submit an IDV
      operationId: SubmitAnIDV
      parameters:
        - name: api-key
          in: header
          schema:
            type: string
            example: '{{api_key}}'
            description: >-
              API key is required to call Solid APIs. You can view and manage
              your API keys in the Solid dashboard.
          required: true
      responses:
        '201':
          description: Submit an IDV
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sub_account_holder'
                type: object
              examples:
                sub_account_holder_example:
                  $ref: '#/components/examples/sub_account_holder_example'
        '400':
          description: Unauthorized Error
          content:
            application/json:
              examples:
                sub_account_holder_example:
                  $ref: '#/components/examples/sub_account_holder_bad_request_error'
        '401':
          description: Unauthorized Error
          content:
            application/json:
              examples:
                sub_account_holder_example:
                  $ref: '#/components/examples/unauth_error'
        '404':
          description: Not Found Error
          content:
            application/json:
              examples:
                master_account_example:
                  $ref: '#/components/examples/master_account_not_found_error'
      security:
        - {}
components:
  schemas:
    sub_account_holder:
      properties:
        id:
          type: string
          example: sah_5ccfeef0adf0cbe2aa0980d2c9505752
          description: unique id of the sub account holder
        client_id:
          type: string
          example: cli_64c6c87ee9d609f36a6f390dc378a4ce
          description: unique id of the client that created the sub account
        master_account_holder_id:
          type: string
          example: mah_201e02c581a098a740456c5c19fcfcd6
          description: unique id of the master account holder
        master_account_id:
          type: string
          example: mas_743fa071316bc6beaf5dddfd05f49c30
          description: unique id of the master account
        person:
          $ref: '#/components/schemas/person'
          type: object
        business:
          $ref: '#/components/schemas/business'
          type: object
        ofac:
          $ref: '#/components/schemas/sub_account_holder_ofac'
          type: object
        external_reference_id:
          type: string
          example: TW-9L1L2-UVV
          description: unique id to cross-reference records with external systems
        purpose:
          type: string
          example: Ace sub-account holder
          description: purpose of sub account holder
        attachments:
          type: array
          items:
            $ref: '#/components/schemas/attachment_object'
        metadata:
          $ref: '#/components/schemas/metadata'
          type: object
        status:
          type: string
          example: activated
          description: status of sub account holder
          enum:
            - pending_activation
            - activated
            - suspended
            - deactivated
            - locked
        timestamps:
          $ref: '#/components/schemas/sub_account_holder_timestamp'
          type: object
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
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                address:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                dob:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                ssn:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                phone:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                email:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                watchlist:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                fraud:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
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
    business:
      type: object
      properties:
        legal_name:
          type: string
          example: Ace LLC
          description: legal name of the business
        dba:
          type: string
          example: Ace Inc
          description: doing business as
        entity_type:
          type: string
          example: limited_liability_company
          description: entity type of the business
          enum:
            - sole_proprietor
            - single_member_llc
            - limited_liability_company
            - general_partnership
            - unlisted_corporation
            - publicly_traded_corporation
            - association
            - non_profit
            - government_organization
            - revocable_trust
            - irrevocable_trust
            - estate
            - professional_association
            - limited_partnership
            - limited_liability_partnership
            - professional_corporation
        id_type:
          type: string
          example: ein
          description: type of the business identity used
          enum:
            - ein
            - other
        id_number:
          type: string
          example: '187654321'
          description: |-
            - if id_type is ssn, id_number must be full SSN 
             - if id_type is ein, id_number must be ein number 
             - if id_type is other, id_number must be unique number of the id 
             
             id_number must be unique, as in, you cannot use the same id_number for two different businesses
        phone:
          type: string
          example: '16604491146'
          description: phone number of the business (E.164, max 16 chars, starts with +)
        email:
          type: string
          example: support@ace.com
          description: email of the business
        formation_date:
          type: string
          example: '2018-02-18'
          description: date business was formed (YYYY-MM-DD)
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
              description: line 2 of the address (optional)
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
        kyb:
          type: object
          properties:
            id:
              type: string
              example: kyb_7948d9a96706dd05360a340002de725f
              description: unique id of the KYB
            status:
              type: string
              example: pass
              description: status of the KYB
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
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                address:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                watchlist:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                fraud:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
        members:
          type: array
          items:
            $ref: '#/components/schemas/business_member'
    sub_account_holder_ofac:
      type: object
      properties:
        status:
          type: string
          example: pass
          description: ofac status of the sub account holder
          enum:
            - pass
            - fail
        last_updated_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: >-
            last date and time at which the sub account holder's ofac status was
            checked
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
    sub_account_holder_timestamp:
      type: object
      properties:
        created_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the sub account holder was created
        updated_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the sub account holder was updated
        deactivated_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the sub account holder was deactivated
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
    business_member:
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
              description: line 2 of the address (optional)
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
        ownership:
          type: number
          example: 50.59
          description: ownership percentage in the business
        title:
          type: string
          example: CEO
          description: title of the member in the business
        control_person:
          type: string
          example: 'true'
          description: true if this member is the control person of the business
          enum:
            - 'true'
            - 'false'
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
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                address:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                dob:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                ssn:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                phone:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                email:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                watchlist:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
                fraud:
                  $ref: '#/components/schemas/kyc_kyb'
                  type: object
  examples:
    sub_account_holder_example:
      value:
        id: sah_5ccfeef0adf0cbe2aa0980d2c9509b2d
        client_id: cli_64c6c87ee9d609f36a6f390dc378a4ce
        master_account_holder_id: mah_201e02c581a098a740456c5c19fcfcd6
        master_account_id: mas_743fa071316bc6beaf5dddfd05f49c30
        type: person
        person:
          first_name: Jane
          last_name: Doe
          id_type: ssn
          id_number: '223913234'
          date_of_birth: '1974-01-25'
          phone: '+19418405843'
          email: jane.doe@gmail.com
          address:
            line1: 123 Main St
            line2: ''
            city: New York
            state: NY
            country: US
            postal_code: '10001'
          kyc:
            id: kyc_01arz3ndektsv4rrffq69g5fav
            status: pass
            method: solid
            url: >-
              https://dashboard.solidfi.com/verify?id=kyc_01arz3ndektsv4rrffq69g5fav
            details:
              name:
                status: pass
                reasons: null
              address:
                status: pass
                reasons: null
              dob:
                status: pass
                reasons: null
              ssn:
                status: pass
                reasons: null
              phone:
                status: pass
                reasons: null
              email:
                status: pass
                reasons: null
              watchlist:
                status: pass
                reasons: null
              fraud:
                status: pass
                reasons: null
          idv:
            id: idv_01arz3ndektsv4rrffq69g5fav
            status: fail
            method: solid
            url: https://dashboard.solidfi.com/id=idv_01arz3ndektsv4rrffq69g5fav
            reasons: null
        business: null
        ofac:
          status: pass
          last_updated_at: '2024-04-01T21:00:00Z'
        external_reference_id: TW-9L1L2-UVV
        purpose: Ace sub-account holder
        attachments:
          - label: formation
            id: att_a8d2b191fa0e960d8e49a4bfd320e07b
            created_at: '2024-04-01T21:00:00Z'
        metadata:
          customer_code: '1501'
        status: activated
        timestamps:
          created_at: '2024-04-01T21:00:00Z'
          updated_at: '2024-04-01T21:00:00Z'
          deactivated_at: '2024-04-01T21:00:00Z'
    sub_account_holder_bad_request_error:
      value:
        request_id: req_01900ec5ebd37bf2a18b90948129e419
        client_id: ''
        method: POST
        status: 400
        error:
          code: ERROR_CODE_INVALID_FIELD
          message: no type specified!
          field_name: type
        created_at: '2024-06-12T23:26:10Z'
    unauth_error:
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
    master_account_not_found_error:
      value:
        request_id: req_01900e959896706b870affad1b4d71dd
        client_id: ''
        method: GET
        status: 404
        error:
          code: ERROR_CODE_RESOURCE_NOT_FOUND
          message: cannot find account by id in qldb
          field_name: ''
        created_at: '2024-06-12T22:33:23Z'

````