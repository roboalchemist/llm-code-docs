# Source: https://docs.solidfi.com/v2/api-reference/counterparties/update-a-counterparty.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a Counterparty

> Update a Counterparty



## OpenAPI

````yaml patch /v2/payments/counterparty/{counterparty_id}
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
  /v2/payments/counterparty/{counterparty_id}:
    parameters:
      - name: counterparty_id
        in: path
        required: true
        schema:
          type: string
    patch:
      tags:
        - Counterparties
      summary: Update a Counterparty
      description: Update a Counterparty
      operationId: updateACounterparty
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                label:
                  type: string
                  example: Development Vendor
                  description: label of the counterparty
                type:
                  type: string
                  example: person
                  description: type of counterparty
                  enum:
                    - person
                    - business
                person:
                  $ref: '#/components/schemas/person'
                  type: object
                business:
                  $ref: '#/components/schemas/business'
                  type: object
                intra_account:
                  $ref: '#/components/schemas/counterparty_intra_account'
                  type: object
                ach:
                  $ref: '#/components/schemas/counterparty_ach'
                  type: object
                domestic_wire:
                  $ref: '#/components/schemas/counterparty_domestic_wire'
                  type: object
                international_wire:
                  $ref: '#/components/schemas/counterparty_international_wire'
                  type: object
                rtp:
                  $ref: '#/components/schemas/counterparty_rtp'
                  type: object
                fednow:
                  $ref: '#/components/schemas/counterparty_fednow'
                  type: object
                check:
                  $ref: '#/components/schemas/counterparty_check'
                  type: object
                debit_card:
                  $ref: '#/components/schemas/counterparty_debit_card'
                  type: object
                purpose:
                  type: string
                  example: Offshore dev center
                  description: purpose of counterparty
                external_reference_id:
                  type: string
                  example: TW-9L1L2-UVV
                  description: unique id to cross-reference records with external systems
                metadata:
                  $ref: '#/components/schemas/metadata'
                  type: object
                status:
                  type: string
                  example: activated
                  description: status of counterparty
                  enum:
                    - pending_activation
                    - activated
                    - suspended
                    - deactivated
            examples:
              Update a Counterparty:
                value:
                  label: Utilities
      responses:
        '200':
          description: Update a Counterparty
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/counterparty'
                type: object
              examples:
                counterparty_example:
                  $ref: '#/components/examples/counterparty_example'
        '400':
          description: Unauthorized Error
          content:
            application/json:
              examples:
                counterparty_example:
                  $ref: '#/components/examples/counterparty_bad_request_error'
        '401':
          description: Unauthorized Error
          content:
            application/json:
              examples:
                counterparty_example:
                  $ref: '#/components/examples/unauth_error'
        '404':
          description: Not Found Error
          content:
            application/json:
              examples:
                master_account_example:
                  $ref: '#/components/examples/counterparty_not_found_error'
      security:
        - {}
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
    counterparty_intra_account:
      type: object
      properties:
        sub_account_number:
          type: string
          example: '95483674098723'
          description: sub account number of the counterparty
        sub_account_id:
          type: string
          example: sub_cda1e562657c41e553104b10aad3fe70
          description: sub account id of the counterparty
    counterparty_ach:
      type: object
      properties:
        account_number:
          type: string
          example: '98324502'
          description: bank account number of the counterparty
        routing_number:
          type: string
          example: '121042882'
          description: ACH routing number of the counterparty's bank
        account_type:
          type: string
          example: business_checking
          description: type of the counterparty's bank account
          enum:
            - business_checking
            - business_savings
            - personal_checking
            - personal_savings
        bank_name:
          type: string
          example: Wells Fargo
          description: name of counterparty's bank
        verification_status:
          type: string
          description: if the account is verified - true or false
          example: pass
          enum:
            - pass
            - fail
            - review
    counterparty_domestic_wire:
      type: object
      properties:
        account_number:
          type: string
          example: '98324502'
          description: bank account number of the counterparty
        routing_number:
          type: string
          example: '121042882'
          description: Wire routing number of the counterparty's bank
        account_type:
          type: string
          example: business_checking
          description: type of counterparty's bank account
          enum:
            - business_checking
            - business_savings
            - personal_checking
            - personal_savings
        bank_name:
          type: string
          example: Wells Fargo
          description: name of counterparty's bank
    counterparty_international_wire:
      type: object
      properties:
        account_number:
          type: string
          example: '920020006167511'
          description: bank account number of the counterparty
        beneficiary_bank:
          $ref: '#/components/schemas/counterparty_beneficiary_bank'
          type: object
        correspondent_bank:
          $ref: '#/components/schemas/counterparty_correspondent_bank'
          type: object
    counterparty_rtp:
      type: object
      properties:
        account_number:
          type: string
          example: '98324502'
          description: bank account number of the counterparty
        routing_number:
          type: string
          example: '121042882'
          description: RTP routing number of the counterparty's bank
        account_type:
          type: string
          example: business_checking
          description: type of the counterparty's bank account
          enum:
            - business_checking
            - business_savings
            - personal_checking
            - personal_savings
        bank_name:
          type: string
          example: Wells Fargo
          description: name of counterparty's bank
        verification_status:
          type: string
          example: pass
          description: if the account is verified
          enum:
            - pass
            - fail
            - review
    counterparty_fednow:
      type: object
      properties:
        account_number:
          type: string
          example: '98324502'
          description: bank account number of the counterparty
        routing_number:
          type: string
          example: '121042882'
          description: FedNow routing number of the counterparty's bank
        account_type:
          type: string
          example: business_checking
          description: type of the counterparty's bank account
          enum:
            - business_checking
            - business_savings
            - personal_checking
            - personal_savings
        bank_name:
          type: string
          example: Wells Fargo
          description: name of counterparty's bank
        verification_status:
          type: string
          example: pass
          description: if the account is verified or not
          enum:
            - pass
            - fail
            - review
    counterparty_check:
      type: object
      properties:
        address:
          type: object
          properties:
            line1:
              type: string
              example: 123 Main St
              description: line 1 of the address
            line2:
              type: string
              example: Suite 201
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
    counterparty_debit_card:
      type: object
      properties:
        card_number:
          type: string
          example: tok_live_6GVyHuQR7aAjCZivYzLbuP_9990
          description: tokenized card number of counterparty's debit card
        last4:
          type: string
          example: '9990'
          description: last4 of counterparty's debit card
        expiry_month:
          type: string
          example: '10'
          description: expiration month of counterparty's debit card
        expiry_year:
          type: string
          example: '2024'
          description: expiration year of counterparty's debit card
        cvv:
          type: string
          example: tok_live_7CVyHuQR7aAjCZivYzLbuP_9990
          description: cvv code of counterparty's debit card
        address:
          type: object
          properties:
            line1:
              type: string
              example: 123 Main St
              description: line 1 of the address
            line2:
              type: string
              example: Suite 201
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
        pull_enabled:
          type: string
          example: 'true'
          description: if debit pull is enabled or disabled by the debit card issuer
          enum:
            - 'true'
            - 'false'
        push_enabled:
          type: string
          example: 'true'
          description: if debit pull is enabled or disabled by the debit card issuer
          enum:
            - 'true'
            - 'false'
    metadata:
      type: object
      description: >-
        Metadata takes free-form key-value pairs. You may send metadata when you
        create an object (POST) and when updating the object (PATCH).  If you
        would like to remove metadata that is already on an object, you can
        unset it by passing in the key-value pair with an empty string, like
        this: 
         {"key": ""}
    counterparty:
      type: object
      properties:
        id:
          type: string
          example: ctp_8e5541c8a9e50c3af3b0daacf9175130
          description: unique id of the counterparty
        client_id:
          type: string
          example: cli_64c6c87ee9d609f36a6f390dc378a4ce
          description: unique id of the client to which the counterparty belongs
        master_account_holder_id:
          type: string
          example: mah_201e02c581a098a740456c5c19fcfcd6
          description: unique id of the master account holder
        master_account_id:
          type: string
          example: mas_743fa071316bc6beaf5dddfd05f49c30
          description: unique id of the master account
        sub_account_holder_id:
          type: string
          example: sah_5ccfeef0adf0cbe2aa0980d2c9505752
          description: unique id of the sub account holder
        sub_account_id:
          type: string
          example: sub_bda1e562657c41e553104b10aad3fe70
          description: >-
            unique id of the sub account under which the counterparty was
            created
        label:
          type: string
          example: Development Vendor
          description: label of the counterparty
        type:
          type: string
          example: person
          description: type of counterparty
          enum:
            - person
            - business
        person:
          $ref: '#/components/schemas/person'
          type: object
        business:
          $ref: '#/components/schemas/business'
          type: object
        intra_account:
          $ref: '#/components/schemas/counterparty_intra_account'
          type: object
        ach:
          $ref: '#/components/schemas/counterparty_ach'
          type: object
        domestic_wire:
          $ref: '#/components/schemas/counterparty_domestic_wire'
          type: object
        international_wire:
          $ref: '#/components/schemas/counterparty_international_wire'
          type: object
        rtp:
          $ref: '#/components/schemas/counterparty_rtp'
          type: object
        fednow:
          $ref: '#/components/schemas/counterparty_fednow'
          type: object
        check:
          $ref: '#/components/schemas/counterparty_check'
          type: object
        debit_card:
          $ref: '#/components/schemas/counterparty_debit_card'
          type: object
        purpose:
          type: string
          example: Offshore dev center
          description: purpose of counterparty
        external_reference_id:
          type: string
          example: TW-9L1L2-UVV
          description: unique id to cross-reference records with external systems
        ofac:
          $ref: '#/components/schemas/counterparty_ofac'
          type: object
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
          description: status of counterparty
          enum:
            - pending_activation
            - activated
            - suspended
            - deactivated
            - locked
        timestamps:
          $ref: '#/components/schemas/counterparty_timestamp'
          type: object
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
    counterparty_beneficiary_bank:
      type: object
      properties:
        identifier_code:
          type: string
          example: ICICINBBNRI
          description: SWIFT/BIC code of counterparty's bank
        name:
          type: string
          example: ICICI Bank
          description: name of counterparty's bank
        address:
          type: object
          properties:
            line1:
              type: string
              example: 256 Main St
              description: line 1 of the address
            line2:
              type: string
              example: Suite 201
              description: line 2 of the address
            city:
              type: string
              example: Bengaluru
              description: city of the address
            state:
              type: string
              example: KA
              description: '2-Letter state abbreviation (ex: CA)'
            country:
              type: string
              example: IN
              description: '2-letter abbreviated country code (ex: US)'
            postal_code:
              type: string
              example: '900009'
              description: postal code
    counterparty_correspondent_bank:
      type: object
      properties:
        identifier_code:
          type: string
          example: SCBLUS33XXX
          description: SWIFT/BIC code of counterparty's correspondent bank
        name:
          type: string
          example: STANDARD CHARTERED BANK
          description: name of counterparty's correspondent bank
        address:
          type: object
          properties:
            line1:
              type: string
              example: 1095 12th Ave
              description: line 1 of the address
            line2:
              type: string
              example: Suite 201
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
    counterparty_ofac:
      type: object
      properties:
        status:
          type: string
          example: pass
          description: ofac status of the counterparty
          enum:
            - pass
            - fail
        last_updated_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: >-
            last date and time at which the counterparty's ofac status was
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
    counterparty_timestamp:
      type: object
      properties:
        created_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the counterparty was created
        updated_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the counterparty was updated
        deactivated_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the counterparty was deactivated
  examples:
    counterparty_example:
      value:
        id: ctp_8e5541c8a9e50c3af3b0daacf9175130
        client_id: cli_64c6c87ee9d609f36a6f390dc378a4ce
        master_account_holder_id: mah_201e02c581a098a740456c5c19fcfcd6
        master_account_id: mas_743fa071316bc6beaf5dddfd05f49c30
        sub_account_holder_id: sah_5ccfeef0adf0cbe2aa0980d2c9505752
        sub_account_id: sub_bda1e562657c41e553104b10aad3fe70
        label: Development Vendor
        type: person
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
        intra_account:
          sub_account_number: '95483674098723'
          sub_account_id: sub_cda1e562657c41e553104b10aad3fe70
        ach:
          account_number: '98324502'
          routing_number: '121042882'
          account_type: business_checking
          bank_name: Wells Fargo
          verification_status: pass
        domestic_wire:
          account_number: '98324502'
          routing_number: '121042882'
          account_type: business_checking
          bank_name: Wells Fargo
        international_wire:
          account_number: '920020006167511'
          beneficiary_bank:
            identifier_code: ICICINBBNRI
            name: ICICI Bank
            address:
              line1: 256 Main St
              line2: ''
              city: Bengaluru
              state: KA
              country: IN
              postal_code: '900009'
          correspondent_bank:
            identifier_code: SCBLUS33XXX
            name: STANDARD CHARTERED BANK
            address:
              line1: 1095 12th Ave
              line2: ''
              city: New York
              state: NY
              country: US
              postal_code: '10001'
        rtp:
          account_number: '98324502'
          routing_number: '121042882'
          account_type: business_checking
          bank_name: Wells Fargo
          verification_status: pass
        fednow:
          account_number: '98324502'
          routing_number: '121042882'
          account_type: business_checking
          bank_name: Wells Fargo
          verification_status: pass
        check:
          address:
            line1: 123 Main St
            line2: ''
            city: New York
            state: NY
            country: US
            postal_code: '10001'
        debit_card:
          card_number: tok_live_6GVyHuQR7aAjCZivYzLbuP_9990
          last4: '9990'
          expiry_month: '10'
          expiry_year: '2024'
          cvv: tok_live_6GVyHuQR7aAjCZivYzLbuP_9990
          address:
            line1: 123 Main St
            line2: ''
            city: New York
            state: NY
            country: US
            postal_code: '10001'
          pull_enabled: true
          push_enabled: true
        purpose: Offshore dev center
        external_reference_id: TW-9L1L2-UVV
        ofac:
          status: pass
          last_updated_at: '2024-04-01T21:00:00Z'
        attachments:
          - label: Dev Contract
            id: att_a8d2b191fa0e960d8e49a4bfd320e07b
            created_at: '2024-04-01T21:00:00Z'
        metadata:
          vendor_id: VID-0987ACR
        status: activated
        timestamps:
          created_at: '2024-04-01T21:00:00Z'
          updated_at: '2024-04-01T21:00:00Z'
    counterparty_bad_request_error:
      value:
        request_id: req_01900eca101a7ca3ae62bf62191efadc
        client_id: ''
        method: POST
        status: 400
        error:
          code: ERROR_CODE_INVALID_FIELD
          message: type must be properly set
          field_name: ''
        created_at: '2024-06-12T23:30:41Z'
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
    counterparty_not_found_error:
      value:
        request_id: req_01900e959896706b870affad1b4d71dd
        client_id: ''
        method: GET
        status: 404
        error:
          code: ERROR_CODE_RESOURCE_NOT_FOUND
          message: cannot find counterparty by id in qldb
          field_name: ''
        created_at: '2024-06-12T22:33:23Z'

````