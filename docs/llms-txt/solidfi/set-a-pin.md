# Source: https://docs.solidfi.com/v2/api-reference/cards/set-a-pin.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set a PIN

> Setting a PIN is a two-step process 
 1. Get a one-time PIN token 
 2. Use the PIN token in Solid's SDK to set a PIN. Solid will provide access to the SDK during the implementation.



## OpenAPI

````yaml post /v2/issuing/card/{card_id}/set_pin_token
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
  /v2/issuing/card/{card_id}/set_pin_token:
    parameters:
      - name: card_id
        in: path
        required: true
        schema:
          type: string
    post:
      tags:
        - Cards
      summary: Set a PIN
      description: |-
        Setting a PIN is a two-step process 
         1. Get a one-time PIN token 
         2. Use the PIN token in Solid's SDK to set a PIN. Solid will provide access to the SDK during the implementation.
      operationId: setAPIN
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
        '200':
          description: Set a PIN
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: crd_7948d9a96706dd05360a340002de725f
                    description: unique id of the card
                  set_pin_token:
                    type: string
                    example: card_pin_test_01920c6725b4707688fa0ad517bdeddb
                    description: set PIN token
              examples:
                set_pin_example:
                  value:
                    id: crd_7948d9a96706dd05360a340002de725f
                    set_pin_token: card_pin_test_01920c6725b4707688fa0ad517bdeddb
        '401':
          description: Unauthorized Error
          content:
            application/json:
              examples:
                show_card_example:
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
  examples:
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