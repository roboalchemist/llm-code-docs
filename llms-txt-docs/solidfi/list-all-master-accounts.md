# Source: https://docs.solidfi.com/v2/api-reference/master-accounts/list-all-master-accounts.md

# List all Master Accounts

> List all Master Accounts

## OpenAPI

````yaml get /v2/accounts/master_account
paths:
  path: /v2/accounts/master_account
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
      path: {}
      query:
        master_account_holder_id:
          schema:
            - type: string
              description: unique id of the master account holder
              example: mah_201e02c581a098a740456c5c19fcfcd6
        status:
          schema:
            - type: enum<string>
              enum:
                - open
                - closed
                - credit_blocked
                - debit_blocked
                - blocked
                - locked
              description: status of master account
              example: open
        limit:
          schema:
            - type: number
              description: number of records to return
              example: 10
        starting_after:
          schema:
            - type: string
              description: >-
                A cursor for use in pagination. `starting_after` is an ID that
                defines your place in the list. For instance, if you make a list
                request and receive 50 records, ending with
                `Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`, your
                subsequent call can include
                `starting_after=Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`
                in order to fetch the next page of the list.
              example: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
        ending_before:
          schema:
            - type: string
              description: >-
                A cursor for use in pagination. `ending_before` is an ID that
                defines your place in the list. For instance, if you make a list
                request and receive 50 records, starting with
                `Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`, your
                subsequent call can include `ending_before=
                Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky` in order to
                fetch the previous page of the list.
              example: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
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
              total:
                allOf:
                  - type: number
                    example: 1
                    description: total number of records
              data:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/master_account'
              has_more:
                allOf:
                  - type: string
                    example: 'true'
                    description: if there are more records to iterate or not
                    enum:
                      - 'true'
                      - 'false'
              starting_after:
                allOf:
                  - type: string
                    example: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
                    description: >-
                      A cursor for use in pagination. `starting_after` is an ID
                      that defines your place in the list. For instance, if you
                      make a list request and receive 50 records, ending with
                      `Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`, your
                      subsequent call can include
                      `starting_after=Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`
                      in order to fetch the next page of the list.
              ending_before:
                allOf:
                  - type: string
                    example: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
                    description: >-
                      A cursor for use in pagination. `ending_before` is an ID
                      that defines your place in the list. For instance, if you
                      make a list request and receive 50 records, starting with
                      `Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky`, your
                      subsequent call can include `ending_before=
                      Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky` in order
                      to fetch the previous page of the list.
            refIdentifier: '#/components/schemas/list_master_account'
        examples:
          list_master_account_example:
            value:
              total: 1
              data:
                - id: mas_743fa071316bc6beaf5dddfd05f49c30
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
              has_more: 'true'
              starting_after: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
              ending_before: Y2xpXzAxOGY4NjEzMDEyYjdlNTFiOTZjNmVlYWJiNmRiZTky
        description: List all Master Accounts
    '401':
      application/json:
        schemaArray:
          - type: any
        examples:
          list_master_account_example:
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
  deprecated: false
  type: path
components:
  schemas:
    master_account:
      type: object
      properties:
        id:
          type: string
          example: mas_743fa071316bc6beaf5dddfd05f49c30
          description: unique id of the master account
        client_id:
          type: string
          example: cli_64c6c87ee9d609f36a6f390dc378a4ce
          description: unique id of the client that created the master account
        master_account_holder_id:
          type: string
          example: mah_201e02c581a098a740456c5c19fcfcd6
          description: unique id of the master account holder
        label:
          type: string
          example: Payments Account
          description: label of the master account
        available_balance:
          type: string
          example: '104100.41'
          description: available balance in the master account
        pending_credits:
          type: string
          example: '1198.50'
          description: total pending credits to the master account
        pending_debits:
          type: string
          example: '390.10'
          description: total pending debits to the master account
        account_number:
          type: string
          example: '9545931209'
          description: account number of the master account
        routing_number:
          type: string
          example: '123321123'
          description: 9 digit routing number of the master account
        sponsor_bank:
          type: string
          example: Lewis and Clark Bank
          description: sponsor bank name
        currency:
          type: string
          example: usd
          description: currency of the master account
          enum:
            - usd
        external_reference_id:
          type: string
          example: XV-H27LGD-FX
          description: unique id to cross-reference records with external systems
        purpose:
          type: string
          example: Payment Ops Master Account
          description: purpose of master account
        attachments:
          type: array
          items:
            $ref: '#/components/schemas/attachment_object'
            description: ''
        metadata:
          type: object
          $ref: '#/components/schemas/metadata'
        status:
          type: string
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
          type: object
          $ref: '#/components/schemas/master_account_timestamp'
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