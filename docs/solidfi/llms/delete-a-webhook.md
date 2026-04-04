# Source: https://docs.solidfi.com/v2/api-reference/webhooks/delete-a-webhook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a Webhook

> Delete a Webhook



## OpenAPI

````yaml delete /v2/webhook/{webhook_id}
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
  /v2/webhook/{webhook_id}:
    parameters:
      - name: webhook_id
        in: path
        required: true
        schema:
          type: string
    delete:
      tags:
        - Webhooks
      summary: Delete a Webhook
      description: Delete a Webhook
      operationId: deleteAWebhook
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
        '204':
          description: The webhook was deleted successfully.

````