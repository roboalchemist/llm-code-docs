# Source: https://docs.solidfi.com/v2/api-reference/cards/set-a-pin.md

# Set a PIN

> Setting a PIN is a two-step process 
 1. Get a one-time PIN token 
 2. Use the PIN token in Solid's SDK to set a PIN. Solid will provide access to the SDK during the implementation.

## OpenAPI

````yaml post /v2/issuing/card/{card_id}/set_pin_token
paths:
  path: /v2/issuing/card/{card_id}/set_pin_token
  method: post
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
        card_id:
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
                    example: crd_7948d9a96706dd05360a340002de725f
                    description: unique id of the card
              set_pin_token:
                allOf:
                  - type: string
                    example: card_pin_test_01920c6725b4707688fa0ad517bdeddb
                    description: set PIN token
        examples:
          set_pin_example:
            value:
              id: crd_7948d9a96706dd05360a340002de725f
              set_pin_token: card_pin_test_01920c6725b4707688fa0ad517bdeddb
        description: Set a PIN
    '401':
      application/json:
        schemaArray:
          - type: any
        examples:
          show_card_example:
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
                message: cannot find card holder by id in qldb
                field_name: ''
              created_at: '2024-06-12T22:33:23Z'
        description: Not Found Error
  deprecated: false
  type: path
components:
  schemas: {}

````