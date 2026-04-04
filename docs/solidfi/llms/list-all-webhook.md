# Source: https://docs.solidfi.com/v2/api-reference/webhooks/list-all-webhook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List all Webhooks

> List all Webhooks



## OpenAPI

````yaml get /v2/webhook
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
    get:
      tags:
        - Webhooks
      summary: List all Webhooks
      description: List all Webhooks
      operationId: listAllWebhooks
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
        - name: limit
          in: query
          schema:
            type: number
            example: 10
            description: number of records to return
        - name: starting_after
          in: query
          schema:
            type: string
            example: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
            description: >-
              A cursor for use in pagination. `starting_after` is an ID that
              defines your place in the list. For instance, if you make a list
              request and receive 50 records, ending with
              `Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`, your
              subsequent call can include
              `starting_after=Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`
              in order to fetch the next page of the list.
        - name: ending_before
          in: query
          schema:
            type: string
            example: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
            description: >-
              A cursor for use in pagination. `ending_before` is an ID that
              defines your place in the list. For instance, if you make a list
              request and receive 50 records, starting with
              `Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`, your
              subsequent call can include `ending_before=
              Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky` in order to
              fetch the previous page of the list.
      responses:
        '200':
          description: List all Webhooks
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/list_webhook'
                type: object
              examples:
                list_webhook_example:
                  $ref: '#/components/examples/list_webhook_example'
        '401':
          description: Unauthorized Error
          content:
            application/json:
              examples:
                list_webhook_example:
                  $ref: '#/components/examples/unauth_error'
      security:
        - {}
components:
  schemas:
    list_webhook:
      type: object
      properties:
        total:
          type: number
          example: 1
          description: total number of records
        data:
          type: array
          items:
            $ref: '#/components/schemas/webhook'
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
    webhook:
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
            example: transaction.status.declined
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
    list_webhook_example:
      value:
        total: 1
        data:
          - id: whk_0190e7185e4874dab687e7af88f6f368
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
        starting_after: ''
        ending_before: ''
        has_more: false
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