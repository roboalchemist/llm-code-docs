# Source: https://docs.solidfi.com/v2/api-reference/transactions/originate-a-debit-card-push.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Originate a Debit Card Push

> Originate a Debit Card Push



## OpenAPI

````yaml post /v2/payments/debitcard/push
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
  /v2/payments/debitcard/push:
    post:
      tags:
        - Transactions
      summary: Originate a Debit Card Push
      description: Originate a Debit Card Push
      operationId: originateADebitCardPush
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
                sub_account_id:
                  type: string
                  example: sub_bda1e562657c41e553104b10aad3fe70
                  description: unique id of the sub account
                counterparty_id:
                  type: string
                  example: ctp_8e5541c8a9e50c3af3b0daacf9175130
                  description: unique id of the counterparty
                amount:
                  type: string
                  example: '23.50'
                  description: amount of the transaction
                description:
                  type: string
                  example: Lunch expense
                  description: description of the transaction
                external_reference_id:
                  type: string
                  example: 123-9088-2
                  description: unique id to cross-reference records with external systems
            examples:
              Originate a Debit Card Push:
                value:
                  sub_account_id: sub_bda1e562657c41e553104b10aad3fe70
                  counterparty_id: ctp_8e5541c8a9e50c3af3b0daacf9175130
                  amount: '23.50'
                  description: Lunch expense
                  external_reference_id: 123-9088-2
      responses:
        '201':
          description: Originate a Debit Card Push
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/transaction'
                type: object
              examples:
                debit_card_push_transaction_example:
                  $ref: '#/components/examples/debit_card_push_transaction_example'
        '401':
          description: Unauthorized Error
          content:
            application/json:
              examples:
                debit_card_push_transaction_example:
                  $ref: '#/components/examples/unauth_error'
        '404':
          description: Not Found Error
          content:
            application/json:
              examples:
                debit_card_push_transaction_example:
                  $ref: '#/components/examples/master_account_not_found_error'
components:
  schemas:
    transaction:
      type: object
      properties:
        id:
          type: string
          example: txn_817d2a074042bb4ec54e08fd82b1e0a8
          description: unique id of the transaction
        sub_account_id:
          type: string
          example: sub_bda1e562657c41e553104b10aad3fe70
          description: unique id of the sub account
        master_account_id:
          type: string
          example: mas_743fa071316bc6beaf5dddfd05f49c30
          description: unique id of the master account holder
        status:
          type: string
          example: originated
          description: status of the transaction
          enum:
            - originated
            - pending
            - clearing
            - cleared
            - settled
            - canceled
            - in_review
            - returned
            - reversed
            - received
            - declined
            - refunded
        amount:
          type: string
          example: '93.50'
          description: amount of the transaction
        currency:
          type: string
          example: usd
          description: currency of the transaction
          enum:
            - usd
        direction:
          type: string
          example: debit
          description: if transaction is debit or credit
          enum:
            - debit
            - credit
        method:
          type: string
          example: ach
          description: payment method for the transaction
          enum:
            - ach
            - domestic_wire
            - international_wire
            - check
            - fednow
            - rtp
            - debit_card
            - card_issuing
        type:
          type: string
          example: push
          description: type within the payment method used for the transaction
          enum:
            - push
            - pull
            - decline
            - cancel
            - return
            - send
            - deposit
            - request
            - auth
            - adjust
            - reverse
            - refund
        message:
          type: string
          example: outgoing
          description: if transaction is incoming or outgoing
          enum:
            - incoming
            - outgoing
        description:
          type: string
          example: Invoice payment
          description: description of the transaction
        available_balance:
          type: string
          example: '500.00'
          description: available balance in the sub account after the transaction
        pending_credits:
          type: string
          example: '0.00'
          description: total pending credits to the sub account after the transaction
        pending_debits:
          type: string
          example: '93.50'
          description: total pending debits to the sub account after the transaction
        counterparty:
          $ref: '#/components/schemas/transaction_counterparty'
          type: object
        ach:
          $ref: '#/components/schemas/transaction_ach'
          type: object
        domestic_wire:
          $ref: '#/components/schemas/transaction_domestic_wire'
          type: object
        international_wire:
          $ref: '#/components/schemas/transaction_international_wire'
          type: object
        rtp:
          $ref: '#/components/schemas/transaction_rtp'
          type: object
        fednow:
          $ref: '#/components/schemas/transaction_fednow'
          type: object
        check:
          $ref: '#/components/schemas/transaction_check'
          type: object
        card:
          $ref: '#/components/schemas/transaction_card'
          type: object
        external_reference_id:
          type: string
          example: 123-9088-2
          description: unique id to cross-reference records with external systems
        purpose:
          type: string
          example: May Invoice
          description: purpose of the transaction
        ofac:
          $ref: '#/components/schemas/transaction_ofac'
          type: object
        attachments:
          type: array
          items:
            $ref: '#/components/schemas/attachment_object'
        metadata:
          $ref: '#/components/schemas/metadata'
          type: object
        reconciliation:
          $ref: '#/components/schemas/transaction_reconciliation'
          type: object
        timestamps:
          $ref: '#/components/schemas/transaction_timestamp'
          type: object
    transaction_counterparty:
      type: object
      properties:
        id:
          type: string
          example: ctp_8e5541c8a9e50c3af3b0daacf9175130
          description: unique id of the counterparty
        name:
          type: string
          example: John Doe
          description: name of the counterparty
        verification_status:
          type: string
          example: pass
          description: account verification status of the counterparty
          enum:
            - pass
            - fail
            - review
        account_number:
          type: string
          example: '98324502'
          description: bank account number of the counterparty
        routing_number:
          type: string
          example: '121042882'
          description: routing number of the counterparty's bank
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
        beneficiary_bank:
          $ref: '#/components/schemas/counterparty_beneficiary_bank'
          type: object
        correspondent_bank:
          $ref: '#/components/schemas/counterparty_correspondent_bank'
          type: object
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
    transaction_ach:
      type: object
      properties:
        effective_date:
          type: string
          example: '2024-05-05'
          description: date on which the ACH must post on the beneficiary's bank account
        company_discretionary_data:
          type: string
          example: DIRECT DEPOSIT
          description: >-
            text field within the ACH batch file used to reference ACH
            originator details like name, etc.
        company_entry_description:
          type: string
          example: PAYROLL
          description: >-
            text field within the ACH batch file that describes the purpose of
            the ACH transaction
        trace_number:
          type: string
          example: '12309876564'
          description: unique identifier within the ACH batch file
        return_code:
          type: string
          example: R01
          description: reason code given in case of ACH return
        rta_id:
          type: string
          example: rta_64c6c87ee9d609f36a6f390dc378a4ce
          description: unique id for real time authorization
    transaction_domestic_wire:
      type: object
      properties:
        imad:
          type: string
          example: 20240520D2B74A1C002742
          description: >-
            IMAD (Input Message Accountability Data) number is a unique number
            generated by FedwireService for tracking purposes.
        omad:
          type: string
          example: 20240520L1B7832F000914
          description: >-
            OMAD (Output Message Accountability Data) number is a unique number
            generated by FedwireService for tracking purposes.
    transaction_international_wire:
      type: object
      properties:
        imad:
          type: string
          example: 20240520D2B74A1C002742
          description: >-
            IMAD (Input Message Accountability Data) number is a unique number
            generated by FedwireService for tracking purposes.
        omad:
          type: string
          example: 20240520L1B7832F000914
          description: >-
            OMAD (Output Message Accountability Data) number is a unique number
            generated by FedwireService for tracking purposes.
    transaction_rtp:
      type: object
      properties:
        reference_number:
          type: string
          example: 20240410T110000Z
          description: >-
            reference number of the RTP transaction that shown to the
            beneficiary
    transaction_fednow:
      type: object
      properties:
        reference_number:
          type: string
          example: 20240410T110000Z
          description: >-
            reference number of the FedNow transaction that shown to the
            beneficiary
    transaction_check:
      type: object
      properties:
        check_number:
          type: string
          example: '98987679'
          description: check number
        cashed:
          type: string
          example: 'true'
          description: if the check is cashed or not
    transaction_card:
      type: object
      properties:
        id:
          type: string
          example: crd_7948d9a96706dd05360a340002de725f
          description: unique id of the card
        cardholder_id:
          type: string
          example: cah_a120a61f60dfd40fdb07b2e8bcd1f6f0
          description: unique id of the card holder
        merchant:
          type: string
          example: Walmart
          description: merchant the card was used at
        auth_method:
          type: string
          example: online
          description: method of use for the card transaction
        wallet:
          type: string
          example: google_pay
          description: digital wallet type
        rta_id:
          type: string
          example: rta_a120a61f60dfd40fdb07b2e8bcd1f6f0
          description: unique id for real time authorization
        local_transaction:
          type: object
          properties:
            amount:
              type: string
              example: '10.00'
              description: transaction amount in local currency
            currency:
              type: string
              example: usd
              description: local currency code
            conversion_rate:
              type: string
              example: '1.00'
              description: currency conversion rate
        available_limit:
          type: object
          properties:
            period:
              type: string
              example: daily
              description: >-
                time period available in which the maximum amount is allowed to
                be spent
              enum:
                - daily
                - per_transaction
                - weekly
                - monthly
                - yearly
                - all_time
            max_spend_amount:
              type: string
              example: '50.00'
              description: maximum amount available to be spent in the set period
    transaction_ofac:
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
    metadata:
      type: object
      description: >-
        Metadata takes free-form key-value pairs. You may send metadata when you
        create an object (POST) and when updating the object (PATCH).  If you
        would like to remove metadata that is already on an object, you can
        unset it by passing in the key-value pair with an empty string, like
        this: 
         {"key": ""}
    transaction_reconciliation:
      type: object
      properties:
        status:
          type: string
          example: reconciled
          description: reconciliation status of the transaction
          enum:
            - reconciled
            - not_reconciled
        master_account:
          type: array
          items:
            $ref: '#/components/schemas/transaction_master_account_reconciliation'
        sub_account:
          type: array
          items:
            $ref: '#/components/schemas/transaction_sub_account_reconciliation'
    transaction_timestamp:
      type: object
      properties:
        created_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the transaction was created
        updated_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the transaction was updated
        settled_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the transaction was settled
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
    transaction_master_account_reconciliation:
      type: object
      properties:
        id:
          type: string
          example: mas_bda1e562657c41e553104b10aad3fe70
          description: unique id of the master account
        transaction_id:
          type: string
          example: txn_817d2a074042bb4ec54e08fd82b1e0a8
          description: unique id of the master account transaction
        amount:
          type: string
          example: '93.50'
          description: master account transaction amount
    transaction_sub_account_reconciliation:
      type: object
      properties:
        id:
          type: string
          example: sub_bda1e562657c41e553104b10aad3fe70
          description: unique id of the sub account
        transaction_id:
          type: string
          example: txn_a0b56852400c9fede6233fd8c2e60f9c
          description: unique id of the sub account transaction
        amount:
          type: string
          example: '93.50'
          description: sub account transaction amount
  examples:
    debit_card_push_transaction_example:
      value:
        id: txn_817d2a074042bb4ec54e08fd82b1e0a8
        client_id: cli_64c6c87ee9d609f36a6f390dc378a4ce
        master_account_holder_id: mah_201e02c581a098a740456c5c19fcfcd6
        master_account_id: mas_743fa071316bc6beaf5dddfd05f49c30
        sub_account_holder_id: sah_5ccfeef0adf0cbe2aa0980d2c9505752
        sub_account_id: sub_bda1e562657c41e553104b10aad3fe70
        status: originated
        amount: '23.50'
        currency: usd
        direction: debit
        method: debitcard
        type: push
        message: outgoing
        description: Tips Payout
        available_balance: '90.00'
        pending_credits: '0.00'
        pending_debits: '23.50'
        counterparty:
          id: ctp_8e5541c8a9e50c3af3b0daacf9175130
          name: John Doe
          verification_status: pass
          account_number: ''
          routing_number: ''
          account_type: ''
          bank_name: ''
          beneficiary_bank: null
          correspondent_bank: null
          shipping_address: null
        parent_transaction_id: ''
        external_reference_id: 123-9088-2
        purpose: ''
        ofac:
          status: pass
          last_updated_at: '2024-04-01T21:00:00Z'
        attachments: null
        metadata: null
        reconciliation:
          status: not_reconciled
          master_account: null
          sub_account:
            - id: sub_bda1e562657c41e553104b10aad3fe70
              transaction_id: txn_817d2a074042bb4ec54e08fd82b1e0a8
              amount: '23.50'
        timestamps:
          created_at: '2024-04-04T11:06:00Z'
          updated_at: '2024-04-04T11:06:00Z'
          settled_at: '2024-04-04T11:06:00Z'
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