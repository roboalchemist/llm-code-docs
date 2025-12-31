# Source: https://docs.solidfi.com/v2/api-reference/master-accounts/retrieve-a-master-account.md

# Retrieve a Master Account

> Retrieve a Master Account

## OpenAPI

````yaml get /v2/accounts/master_account/{master_account_id}
paths:
  path: /v2/accounts/master_account/{master_account_id}
  method: get
  servers:
    - url: https://api.sandbox.solidfi.com
    - url: https://api.prod.solidfi.com
  request:
    security:
      - title: ''
        parameters:
          query: {}
          header: {}
          cookie: {}
    parameters:
      path:
        master_account_id:
          schema:
            - type: string
              required: true
      query: {}
      header:
        api-key:
          schema:
            - type: string
              required: true
              description: >-
                API key is required to call Solid APIs. You can view and manage
                your API keys in the Solid dashboard.
              example: '{{api_key}}'
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    example: mas_743fa071316bc6beaf5dddfd05f49c30
                    description: unique id of the master account
              client_id:
                allOf:
                  - type: string
                    example: cli_64c6c87ee9d609f36a6f390dc378a4ce
                    description: unique id of the client that created the master account
              master_account_holder_id:
                allOf:
                  - type: string
                    example: mah_201e02c581a098a740456c5c19fcfcd6
                    description: unique id of the master account holder
              label:
                allOf:
                  - type: string
                    example: Payments Account
                    description: label of the master account
              available_balance:
                allOf:
                  - type: string
                    example: '104100.41'
                    description: available balance in the master account
              pending_credits:
                allOf:
                  - type: string
                    example: '1198.50'
                    description: total pending credits to the master account
              pending_debits:
                allOf:
                  - type: string
                    example: '390.10'
                    description: total pending debits to the master account
              account_number:
                allOf:
                  - type: string
                    example: '9545931209'
                    description: account number of the master account
              routing_number:
                allOf:
                  - type: string
                    example: '123321123'
                    description: 9 digit routing number of the master account
              sponsor_bank:
                allOf:
                  - type: string
                    example: Lewis and Clark Bank
                    description: sponsor bank name
              currency:
                allOf:
                  - type: string
                    example: usd
                    description: currency of the master account
                    enum:
                      - usd
              external_reference_id:
                allOf:
                  - type: string
                    example: XV-H27LGD-FX
                    description: unique id to cross-reference records with external systems
              purpose:
                allOf:
                  - type: string
                    example: Payment Ops Master Account
                    description: purpose of master account
              attachments:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/attachment_object'
                      description: ''
              metadata:
                allOf:
                  - type: object
                    $ref: '#/components/schemas/metadata'
              status:
                allOf:
                  - type: string
                    example: open
                    description: status of master account
                    enum:
                      - open
                      - closed
                      - credit_blocked
                      - debit_blocked
                      - blocked
                      - locked
              timestamps:
                allOf:
                  - type: object
                    $ref: '#/components/schemas/master_account_timestamp'
            refIdentifier: '#/components/schemas/master_account'
        examples:
          master_account_example:
            value:
              id: mas_743fa071316bc6beaf5dddfd05f49c30
              client_id: cli_64c6c87ee9d609f36a6f390dc378a4ce
              master_account_holder_id: mah_201e02c581a098a740456c5c19fcfcd6
              label: Payments Account
              available_balance: '104100.41'
              pending_credits: '1198.50'
              pending_debits: '390.10'
              account_number: '9545931209'
              routing_number: '123321123'
              sponsor_bank: Sponsor Bank
              currency: usd
              external_reference_id: XV-H27LGD-FX
              purpose: Payment Ops Master Account
              attachments:
                - label: flow of funds doc
                  id: att_a8d2b191fa0e960d8e49a4bfd320e07b
                  created_at: '2024-04-01T21:00:00Z'
              metadata:
                master_account_code: '001'
              status: open
              timestamps:
                created_at: '2024-04-01T21:00:00Z'
                updated_at: '2024-04-02T21:00:00Z'
                closed_at: '2024-04-03T21:00:00Z'
        description: Retrieve a Master Account
    '401':
      application/json:
        schemaArray:
          - type: any
        examples:
          master_account_example:
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
        description: Unauthorized Error
    '404':
      application/json:
        schemaArray:
          - type: any
        examples:
          master_account_example:
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
        description: Not Found Error
  deprecated: false
  type: path
components:
  schemas:
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
    master_account_timestamp:
      type: object
      properties:
        created_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the master account was created
        updated_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the master account was updated
        closed_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the master account was closed

````