# Source: https://docs.solidfi.com/v2/api-reference/webhooks/create-a-webhook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a Webhook

> Create a Webhook



## OpenAPI

````yaml post /v2/webhook
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
  /v2/webhook:
    post:
      tags:
        - Webhooks
      summary: Create a Webhook
      description: Create a Webhook
      operationId: createAWebhook
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
                description:
                  type: string
                  example: Transaction webhook
                  description: description of the webhook
                url:
                  type: string
                  example: http://test-url.com/txn-webhook
                  description: url of the webhook endpoint
                events:
                  type: array
                  description: >-
                    an array of events to enable for this webhook endpoint.
                    Example
                    ["transaction.status.declined","transaction.status.received"]
                  items:
                    type: string
                    example: transaction.status.declined
            examples:
              Create a Webhook:
                value:
                  description: Transaction Webhook
                  url: http://test-url.com/txn-webhook
                  events:
                    - transaction.status.declined
                    - transaction.status.received
      responses:
        '201':
          description: Create a Webhook
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/create_webhook_response'
                type: object
              examples:
                create_webhook_example:
                  $ref: '#/components/examples/webhook_example'
        '401':
          description: Unauthorized Error
          content:
            application/json:
              examples:
                create_webhook_example:
                  $ref: '#/components/examples/unauth_error'
      security:
        - {}
components:
  schemas:
    create_webhook_response:
      type: object
      properties:
        id:
          type: string
          example: whk_a8d2b191fa0e960d8e49a4bfd320e07b
          description: unique id of the webhook created
        client_id:
          type: string
          example: cli_64c6c87ee9d609f36a6f390dc378a4ce
          description: unique id of the client that issued the card
        description:
          type: string
          example: Transaction webhook
          description: description of the webhook
        url:
          type: string
          example: http://test-url.com/txn-webhook
          description: url of the webhook endpoint
        events:
          type: array
          description: >-
            an array of events to enable for this webhook endpoint. Example
            ["transaction.status.declined","transaction.status.received"]
          items:
            type: string
        secret:
          type: string
          example: pPibTgWHeiAAlJR7I0gzuXJpU3iNcwlf
          description: >-
            webhook signing secret which is returned only at the time of webhook
            creation
        status:
          type: string
          example: active
          description: status of the webhook
          enum:
            - active
            - inactive
        timestamps:
          type: object
          properties:
            created_at:
              type: string
              example: '2024-04-04T11:06:00Z'
              description: time at which the webhook was created
            updated_at:
              type: string
              example: '2024-04-04T11:06:00Z'
              description: time at which the webhook was updated
            deleted_at:
              type: string
              example: '2024-04-04T11:06:00Z'
              description: time at which the webhook was deleted
  examples:
    webhook_example:
      value:
        id: whk_0190e7185e4874dab687e7af88f6f368
        client_id: cli_01901368dbc174a9864a7cb156b0a207
        description: Transaction Webhook
        url: http://test-url.com/txn-webhook
        events:
          - transaction.status.declined
          - transaction.status.received
        status: active
        timestamps:
          created_at: '2024-07-24T23:34:12Z'
          updated_at: '2024-07-25T10:22:11Z'
          deleted_at: '2024-07-26T05:45:19Z'
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