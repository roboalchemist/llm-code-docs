# Source: https://docs.solidfi.com/v2/api-reference/counterparties/retrieve-bank-info.md

# Retrieve Bank Info

> Retrieve Bank Info

## OpenAPI

````yaml get /v2/payments/counterparty/bank
paths:
  path: /v2/payments/counterparty/bank
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
        type:
          schema:
            - type: enum<string>
              enum:
                - aba
                - swift
              description: routing number type - aba or swift
              example: aba
        routing_number:
          schema:
            - type: string
              description: bank routing number
              example: '021214189'
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              routing_number:
                allOf:
                  - type: string
                    example: '021214189'
                    description: routing number of the bank
              bank_name:
                allOf:
                  - type: string
                    example: ConnectOne Bank
                    description: name of the bank
              type:
                allOf:
                  - type: string
                    example: aba
                    description: routing number type - aba or swift
                    enum:
                      - aba
                      - swift
              payment_methods:
                allOf:
                  - type: array
                    description: >-
                      an array of supported payment methods. Example
                      ["ach","wire"]
                    items:
                      type: string
              address:
                allOf:
                  - type: object
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
            refIdentifier: '#/components/schemas/bank_info'
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
        description: Retrieve Bank Info
    '401':
      application/json:
        schemaArray:
          - type: any
        examples:
          bank_info_example:
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
  schemas: {}

````