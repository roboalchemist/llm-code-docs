# Source: https://docs.solidfi.com/v2/api-reference/cards/update-a-card.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a Card

> Update a Card



## OpenAPI

````yaml patch /v2/issuing/card/{card_id}
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
  /v2/issuing/card/{card_id}:
    parameters:
      - name: card_id
        in: path
        required: true
        schema:
          type: string
    patch:
      tags:
        - Cards
      summary: Update a Card
      description: Update a Card
      operationId: updateACard
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
                  example: Travel Expense Card
                  description: label of the card
                controls:
                  type: object
                  properties:
                    allowed:
                      type: object
                      properties:
                        merchants:
                          type: array
                          description: >-
                            an array of merchant names to allow on the card.
                            Example ["Amazon","Netflix"]
                          items:
                            type: string
                        categories:
                          type: array
                          description: >-
                            an array of mcc codes to allow on the card. Example
                            ["0742","0763"]
                          items:
                            type: string
                        countries:
                          type: array
                          description: >-
                            an array of country codes to allow on the card.
                            Example ["US","IN"]
                          items:
                            type: string
                    blocked:
                      type: object
                      properties:
                        merchants:
                          type: array
                          description: >-
                            an array of merchant names to block on the card.
                            Example ["Amazon","Netflix"]
                          items:
                            type: string
                        categories:
                          type: array
                          description: >-
                            an array of mcc codes to block on the card. Example
                            ["0742","0763"]
                          items:
                            type: string
                        countries:
                          type: array
                          description: >-
                            an array of country codes to block on the card.
                            Example ["US","IN"]
                          items:
                            type: string
                    limit:
                      type: object
                      properties:
                        period:
                          type: string
                          example: daily
                          description: >-
                            time period in which the maximum amount is allowed
                            to be spent
                          enum:
                            - daily
                            - per_transaction
                            - weekly
                            - monthly
                            - yearly
                            - all_time
                        max_spend_amount:
                          type: string
                          example: '500.00'
                          description: maximum amount allowed to be spent in the set period
                    atm_enabled:
                      type: string
                      example: 'true'
                      description: >-
                        atm access for the card, true means enabled (by
                        default), false means disabled
                external_reference_id:
                  type: string
                  example: XV-H27LGD-FX
                  description: unique id to cross-reference records with external systems
                metadata:
                  $ref: '#/components/schemas/metadata'
                  type: object
                status:
                  type: string
                  example: open
                  description: status of the card
                  enum:
                    - open
                    - closed
                    - blocked
            examples:
              Update a Card:
                value:
                  label: Travel Expense Card
      responses:
        '200':
          description: Update a Card
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/card'
                type: object
              examples:
                card_example:
                  $ref: '#/components/examples/card_example'
        '400':
          description: Unauthorized Error
          content:
            application/json:
              examples:
                card_example:
                  $ref: '#/components/examples/card_bad_request_error'
        '401':
          description: Unauthorized Error
          content:
            application/json:
              examples:
                card_example:
                  $ref: '#/components/examples/unauth_error'
        '404':
          description: Not Found Error
          content:
            application/json:
              examples:
                master_account_example:
                  $ref: '#/components/examples/card_not_found_error'
      security:
        - {}
components:
  schemas:
    metadata:
      type: object
      description: >-
        Metadata takes free-form key-value pairs. You may send metadata when you
        create an object (POST) and when updating the object (PATCH).  If you
        would like to remove metadata that is already on an object, you can
        unset it by passing in the key-value pair with an empty string, like
        this: 
         {"key": ""}
    card:
      type: object
      properties:
        id:
          type: string
          example: crd_7948d9a96706dd05360a340002de725f
          description: unique id of the card
        client_id:
          type: string
          example: cli_64c6c87ee9d609f36a6f390dc378a4ce
          description: unique id of the client that created the card
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
          description: unique id of the sub account under which the card was created
        cardholder_id:
          type: string
          example: cah_a120a61f60dfd40fdb07b2e8bcd1f6f0
          description: unique id of the card holder
        label:
          type: string
          example: Travel
          description: label of the card
        product:
          type: string
          example: business_spend
          description: type of card product configured based on the client's use case
          enum:
            - business_spend
            - consumer_debit
            - business_debit
            - consumer_gpr
            - consumer_gpnr
            - consumer_payroll
            - consumer_hsa
            - consumer_fsa
            - consumer_govt_benefits
        theme:
          type: string
          example: metallic
          description: theme of the card configured as part of the client use case
        type:
          type: string
          example: physical
          description: type of card
          enum:
            - physical
            - virtual
        expiry_month:
          type: string
          example: '12'
          description: expiration month of the card
        expiry_year:
          type: string
          example: '2025'
          description: expiration year of the card
        last4:
          type: string
          example: '5275'
          description: last 4 digits of the card number
        card_fulfilment:
          type: object
          properties:
            embossing:
              type: object
              properties:
                card_holder_name:
                  type: string
                  example: John Doe
                  description: name of the person to be embossed on the card
                business_name:
                  type: string
                  example: Ace Inc
                  description: name of the business to be embossed on the card
            shipping_address:
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
            tracking:
              type: object
              properties:
                status:
                  type: string
                  example: delivered
                  description: delivery status of the card
                  enum:
                    - pending
                    - delivered
                    - canceled
                    - failure
                    - returned
                    - shipped
                eta:
                  type: string
                  example: '2024-05-02'
                  description: estimated date of arrival for the shipped card
                number:
                  type: string
                  example: '1231233'
                  description: tracking number if shipped via USPS Priority or UPS Next Day
                url:
                  type: string
                  example: >-
                    https://tools.usps.com/go/TrackConfirmAction_input?strOrigTrackNum=120635849224
                  description: tracking URL if shipped via USPS Priority or UPS Next Day
                provider:
                  type: string
                  example: usps
                  description: shipping provider (eg. USPS) that shipped the card
        controls:
          type: object
          properties:
            allowed:
              type: object
              properties:
                merchants:
                  type: array
                  description: >-
                    an array of merchant names to allow on the card. Example
                    ["Amazon","Netflix"]
                  items:
                    type: string
                categories:
                  type: array
                  description: >-
                    an array of mcc codes to allow on the card. Example
                    ["0742","0763"]
                  items:
                    type: string
                countries:
                  type: array
                  description: >-
                    an array of country codes to allow on the card. Example
                    ["US","IN"]
                  items:
                    type: string
            blocked:
              type: object
              properties:
                merchants:
                  type: array
                  description: >-
                    an array of merchant names to block on the card. Example
                    ["Amazon","Netflix"]
                  items:
                    type: string
                categories:
                  type: array
                  description: >-
                    an array of mcc codes to block on the card. Example
                    ["0742","0763"]
                  items:
                    type: string
                countries:
                  type: array
                  description: >-
                    an array of country codes to block on the card. Example
                    ["US","IN"]
                  items:
                    type: string
            limit:
              type: object
              properties:
                period:
                  type: string
                  example: daily
                  description: >-
                    time period in which the maximum amount is allowed to be
                    spent
                  enum:
                    - daily
                    - per_transaction
                    - weekly
                    - monthly
                    - yearly
                    - all_time
                max_spend_amount:
                  type: string
                  example: '500.00'
                  description: maximum amount allowed to be spent in the set period
            atm_enabled:
              type: string
              example: 'true'
              description: >-
                atm access for the card, true means enabled (by default), false
                means disabled
        external_reference_id:
          type: string
          example: XV-H27LGD-FX
          description: unique id to cross-reference records with external systems
        attachments:
          type: array
          items:
            $ref: '#/components/schemas/attachment_object'
        metadata:
          $ref: '#/components/schemas/metadata'
          type: object
        status:
          type: string
          example: open
          description: status of the card
          enum:
            - open
            - closed
            - blocked
            - locked
        timestamps:
          $ref: '#/components/schemas/card_timestamp'
          type: object
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
    card_timestamp:
      type: object
      properties:
        created_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the card was created
        updated_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the card was updated
        closed_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the card was closed
  examples:
    card_example:
      value:
        id: crd_7948d9a96706dd05360a340002de725f
        client_id: cli_64c6c87ee9d609f36a6f390dc378a4ce
        master_account_holder_id: mah_201e02c581a098a740456c5c19fcfcd6
        master_account_id: mas_743fa071316bc6beaf5dddfd05f49c30
        sub_account_holder_id: sah_5ccfeef0adf0cbe2aa0980d2c9505752
        sub_account_id: sub_bda1e562657c41e553104b10aad3fe70
        card_holder_id: cah_a120a61f60dfd40fdb07b2e8bcd1f6f0
        label: Travel
        product: business_spend
        theme: metallic
        type: physical
        expiry_month: '12'
        expiry_year: '2022'
        last4: '5275'
        card_fulfilment:
          embossing:
            card_holder_name: John Doe
            business_name: Ace Inc
          shipping_address:
            line1: 123 Main St
            line2: ''
            city: New York
            state: NY
            country: US
            postal_code: '10001'
          tracking:
            status: delivered
            eta: '2024-05-02'
            number: '1231233'
            url: >-
              https://tools.usps.com/go/TrackConfirmAction_input?strOrigTrackNum=120635849224
            provider: usps
        controls:
          allowed:
            merchants: []
            categories: []
            countries: []
          blocked:
            merchants: []
            categories: []
            countries: []
          limit:
            period: daily
            max_spend_amount: '500.00'
            max_spend_per_transaction: '100.00'
            max_spend_count: '10'
          atm_enabled: 'true'
        external_reference_id: FSY52RAZ-4X
        attachments:
          - label: United
            id: att_a8d2b191fa0e960d8e49a4bfd320e07b
            created_at: '2024-04-01T21:00:00Z'
        metadata:
          description: Sales Team Card
        status: activated
        timestamps:
          created_at: '2024-04-01T21:00:00Z'
          updated_at: '2024-04-02T21:00:00Z'
          closed_at: '2024-04-02T21:00:00Z'
    card_bad_request_error:
      value:
        request_id: req_01900ecf1c067ef39e132557e0a5cd39
        client_id: ''
        method: POST
        status: 400
        error:
          code: ERROR_CODE_INVALID_FIELD
          message: enum is required
          field_name: card_type
        created_at: '2024-06-12T23:36:12Z'
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
    card_not_found_error:
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

````