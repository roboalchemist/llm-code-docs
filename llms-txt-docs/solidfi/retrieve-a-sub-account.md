# Source: https://docs.solidfi.com/v2/api-reference/sub-accounts/retrieve-a-sub-account.md

# Retrieve a Sub Account

> Retrieve a Sub Account

## OpenAPI

````yaml get /v2/accounts/sub_account/{sub_account_id}
paths:
  path: /v2/accounts/sub_account/{sub_account_id}
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
        sub_account_id:
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
                    example: sub_bda1e562657c41e553104b10aad3fe70
                    description: unique id of the sub account
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
              master_account_id:
                allOf:
                  - type: string
                    example: mas_743fa071316bc6beaf5dddfd05f49c30
                    description: >-
                      unique id of the master account under which the sub
                      account was created
              sub_account_holder_id:
                allOf:
                  - type: string
                    example: sah_5ccfeef0adf0cbe2aa0980d2c9505752
                    description: unique id of the sub account holder
              sub_account_holder_name:
                allOf:
                  - type: string
                    example: Ace LLC
                    description: sub account holder name
              label:
                allOf:
                  - type: string
                    example: Ace payments
                    description: label of the sub account
              type:
                allOf:
                  - type: string
                    example: cash
                    description: type of the sub account
                    enum:
                      - cash
                      - prepaid
                      - checking
              account_number:
                allOf:
                  - type: string
                    example: '9540861337293709'
                    description: account number of the sub account
              routing_number:
                allOf:
                  - type: string
                    example: '123206972'
                    description: 9 digit routing number of the sub account
              sponsor_bank:
                allOf:
                  - type: string
                    example: Lewis and Clark Bank
                    description: sponsor bank name
              available_balance:
                allOf:
                  - type: string
                    example: '0.00'
                    description: 'available balance in the sub account '
              pending_credits:
                allOf:
                  - type: string
                    example: '0.00'
                    description: total pending credits to the sub account
              pending_debits:
                allOf:
                  - type: string
                    example: '0.00'
                    description: total pending debits to the sub account
              currency:
                allOf:
                  - type: string
                    example: usd
                    description: currency of the sub account
                    enum:
                      - usd
              external_reference_id:
                allOf:
                  - type: string
                    example: XVH-27LGDFX
                    description: unique id to cross-reference records with external systems
              purpose:
                allOf:
                  - type: string
                    example: Sub account to pay offshore dev team
                    description: purpose of sub account
              attachments:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/attachment_object'
              metadata:
                allOf:
                  - type: object
                    $ref: '#/components/schemas/metadata'
              status:
                allOf:
                  - type: string
                    example: open
                    description: status of sub account
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
                    $ref: '#/components/schemas/sub_account_timestamp'
            refIdentifier: '#/components/schemas/sub_account'
        examples:
          sub_account_example:
            value:
              id: sub_bda1e562657c41e553104b10aad3fe70
              client_id: cli_64c6c87ee9d609f36a6f390dc378a4ce
              master_account_holder_id: mah_201e02c581a098a740456c5c19fcfcd6
              master_account_id: mas_743fa071316bc6beaf5dddfd05f49c30
              sub_account_holder_id: sah_5ccfeef0adf0cbe2aa0980d2c9505752
              sub_account_holder_name: Ace LLC
              label: Payments Account
              type: cash
              available_balance: '0.00'
              pending_credits: '0.00'
              pending_debits: '0.00'
              account_number: '9540861337293709'
              routing_number: '123321123'
              sponsor_bank: Sponsor Bank
              currency: usd
              external_reference_id: XV-H27LGD-FX
              purpose: Sub account to pay offshore dev team
              attachments:
                - label: contract
                  id: att_a8d2b191fa0e960d8e49a4bfd320e07b
                  created_at: '2024-04-01T21:00:00Z'
              metadata:
                master_account_code: '001'
              status: open
              timestamps:
                created_at: '2024-04-01T21:00:00Z'
                updated_at: '2024-04-02T21:00:00Z'
                deactivated_at: '2024-04-03T21:00:00Z'
        description: Retrieve a Sub Account
    '401':
      application/json:
        schemaArray:
          - type: any
        examples:
          sub_account_example:
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
    sub_account_timestamp:
      type: object
      properties:
        created_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the sub account was created
        updated_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the sub account was updated
        closed_at:
          type: string
          example: '2024-04-01T21:00:00Z'
          description: date and time at which the sub account was closed

````