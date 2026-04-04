# Source: https://docs.solidfi.com/v2/api-reference/counterparties/retrieve-bank-info.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve Bank Info

> Retrieve Bank Info



## OpenAPI

````yaml get /v2/payments/counterparty/bank
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
  /v2/payments/counterparty/bank:
    get:
      tags:
        - Counterparties
      summary: Retrieve Bank Info
      description: Retrieve Bank Info
      operationId: retrieveBankInfo
      parameters:
        - name: type
          in: query
          schema:
            type: string
            example: aba
            description: routing number type - aba or swift
            enum:
              - aba
              - swift
        - name: routing_number
          in: query
          schema:
            type: string
            example: '021214189'
            description: bank routing number
      responses:
        '200':
          description: Retrieve Bank Info
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/bank_info'
                type: object
              examples:
                bank_info_example:
                  $ref: '#/components/examples/bank_info_example'
        '401':
          description: Unauthorized Error
          content:
            application/json:
              examples:
                bank_info_example:
                  $ref: '#/components/examples/unauth_error'
      security:
        - {}
components:
  schemas:
    bank_info:
      type: object
      properties:
        routing_number:
          type: string
          example: '021214189'
          description: routing number of the bank
        bank_name:
          type: string
          example: ConnectOne Bank
          description: name of the bank
        type:
          type: string
          example: aba
          description: routing number type - aba or swift
          enum:
            - aba
            - swift
        payment_methods:
          type: array
          description: an array of supported payment methods. Example ["ach","wire"]
          items:
            type: string
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
  examples:
    bank_info_example:
      value:
        routing_number: '021214189'
        bank_name: ConnectOne Bank
        type: aba
        payment_methods:
          - ach
          - wire
        address:
          line1: 1365 Palisades Ave
          line2: ''
          city: Fort Lee
          state: NJ
          country: US
          postal_code: 07024-5242
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

````