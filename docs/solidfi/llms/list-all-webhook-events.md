# Source: https://docs.solidfi.com/v2/api-reference/webhooks/list-all-webhook-events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List all Webhook Events

> List all Webhook Events



## OpenAPI

````yaml get /v2/webhook/events
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
  /v2/webhook/events:
    get:
      tags:
        - Webhooks
      summary: List all Webhook Events
      description: List all Webhook Events
      operationId: listAllWebhookEvents
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
          description: List all Webhook Events
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/list_webhook_events'
                type: object
              examples:
                list_webhook_events_example:
                  $ref: '#/components/examples/list_webhook_events_example'
        '401':
          description: Unauthorized Error
          content:
            application/json:
              examples:
                list_webhook_events_example:
                  $ref: '#/components/examples/unauth_error'
      security:
        - {}
components:
  schemas:
    list_webhook_events:
      type: object
      properties:
        total:
          type: number
          example: 1
          description: total number of records
        data:
          type: array
          items:
            type: string
            example: transaction.status.pending
            enum:
              - counterparty.status.deactivated
              - transaction.status.pending
              - transaction.status.reversed
              - client_member.status.locked
              - sub_account_holder.status.deactivated
              - sub_account_holder.status.locked
              - sub_account.updated
              - client.status.pending_activation
              - client_member.updated
              - transaction.status.declined
              - card_holder.status.locked
              - card.status.debit_blocked
              - card.status.blocked
              - client_member.status.activated
              - master_account.created
              - sub_account.status.locked
              - card_holder.updated
              - card_holder.status.suspended
              - transaction.status.received
              - master_account.status.open
              - master_account.status.debit_blocked
              - sub_account.created
              - card_holder.status.pending_activation
              - client_member.created
              - master_account_holder.status.locked
              - client.status.deactivated
              - card_holder.created
              - counterparty.status.suspended
              - client_member.status.pending_activation
              - master_account_holder.created
              - master_account.updated
              - counterparty.updated
              - transaction.created
              - sub_account_holder.created
              - sub_account_holder.status.pending_activation
              - sub_account.status.blocked
              - card.status.open
              - counterparty.status.activated
              - counterparty.status.locked
              - card_holder.status.deactivated
              - transaction.status.cleared
              - client_member.status.deactivated
              - master_account.status.locked
              - sub_account.status.open
              - card.status.credit_blocked
              - client.status.locked
              - master_account_holder.status.suspended
              - sub_account.status.debit_blocked
              - counterparty.status.pending_activation
              - sub_account_holder.updated
              - counterparty.created
              - transaction.status.clearing
              - sub_account.status.credit_blocked
              - card.created
              - transaction.status.returned
              - card_holder.status.activated
              - client.status.suspended
              - master_account_holder.status.pending_activation
              - master_account_holder.status.deactivated
              - master_account.status.credit_blocked
              - transaction.status.canceled
              - client.updated
              - client.status.activated
              - master_account.status.blocked
              - sub_account.status.closed
              - card.status.closed
              - card.status.locked
              - transaction.status.refunded
              - client_member.status.suspended
              - master_account_holder.updated
              - master_account.status.closed
              - card.updated
              - transaction.status.settled
              - transaction.status.in_review
              - master_account_holder.status.activated
              - sub_account_holder.status.activated
              - sub_account_holder.status.suspended
              - transaction.updated
        has_more:
          type: string
          example: 'true'
          description: if there are more records to iterate or not
          enum:
            - 'true'
            - 'false'
        starting_after:
          type: string
          example: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
          description: >-
            A cursor for use in pagination. `starting_after` is an ID that
            defines your place in the list. For instance, if you make a list
            request and receive 50 records, ending with
            `Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`, your subsequent
            call can include
            `starting_after=Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky` in
            order to fetch the next page of the list.
        ending_before:
          type: string
          example: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
          description: >-
            A cursor for use in pagination. `ending_before` is an ID that
            defines your place in the list. For instance, if you make a list
            request and receive 50 records, starting with
            `Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`, your subsequent
            call can include `ending_before=
            Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky` in order to fetch
            the previous page of the list.
  examples:
    list_webhook_events_example:
      value:
        total: 78
        data:
          - counterparty.status.deactivated
          - transaction.status.pending
          - transaction.status.reversed
          - client_member.status.locked
          - sub_account_holder.status.deactivated
          - sub_account_holder.status.locked
          - sub_account.updated
          - client.status.pending_activation
          - client_member.updated
          - transaction.status.declined
          - card_holder.status.locked
          - card.status.debit_blocked
          - card.status.blocked
          - client_member.status.activated
          - master_account.created
          - sub_account.status.locked
          - card_holder.updated
          - card_holder.status.suspended
          - transaction.status.received
          - master_account.status.open
          - master_account.status.debit_blocked
          - sub_account.created
          - card_holder.status.pending_activation
          - client_member.created
          - master_account_holder.status.locked
          - client.status.deactivated
          - card_holder.created
          - counterparty.status.suspended
          - client_member.status.pending_activation
          - master_account_holder.created
          - master_account.updated
          - counterparty.updated
          - transaction.created
          - sub_account_holder.created
          - sub_account_holder.status.pending_activation
          - sub_account.status.blocked
          - card.status.open
          - counterparty.status.activated
          - counterparty.status.locked
          - card_holder.status.deactivated
          - transaction.status.cleared
          - client_member.status.deactivated
          - master_account.status.locked
          - sub_account.status.open
          - card.status.credit_blocked
          - client.status.locked
          - master_account_holder.status.suspended
          - sub_account.status.debit_blocked
          - counterparty.status.pending_activation
          - sub_account_holder.updated
          - counterparty.created
          - transaction.status.clearing
          - sub_account.status.credit_blocked
          - card.created
          - transaction.status.returned
          - card_holder.status.activated
          - client.status.suspended
          - master_account_holder.status.pending_activation
          - master_account_holder.status.deactivated
          - master_account.status.credit_blocked
          - transaction.status.canceled
          - client.updated
          - client.status.activated
          - master_account.status.blocked
          - sub_account.status.closed
          - card.status.closed
          - card.status.locked
          - transaction.status.refunded
          - client_member.status.suspended
          - master_account_holder.updated
          - master_account.status.closed
          - card.updated
          - transaction.status.settled
          - transaction.status.in_review
          - master_account_holder.status.activated
          - sub_account_holder.status.activated
          - sub_account_holder.status.suspended
          - transaction.updated
        has_more: 'false'
        starting_after: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
        ending_before: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
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