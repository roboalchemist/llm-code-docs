# Source: https://docs.pinata.cloud/api-reference/endpoint/x402/cids-list.md

# List CIDs for Payment Instruction

> Returns a paginated list of CIDs associated with a payment instruction

## OpenAPI

````yaml get /x402/payment_instructions/{id}/cids
paths:
  path: /x402/payment_instructions/{id}/cids
  method: get
  servers:
    - url: https://api.pinata.cloud/v3
      description: Production server
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Pinata API JWT token
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: Payment instruction ID
      query:
        limit:
          schema:
            - type: integer
              description: Number of items to return
              maximum: 1000
              minimum: 1
              default: 20
        pageToken:
          schema:
            - type: string
              description: Token for pagination
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    properties:
                      cids:
                        type: array
                        items:
                          type: string
                      next_page_token:
                        type: string
                        description: Token for next page (omitted on last page)
        examples:
          example:
            value:
              data:
                cids:
                  - <string>
                next_page_token: <string>
        description: Successful operation
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Unauthorized
        examples: {}
        description: Unauthorized
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Forbidden
        examples: {}
        description: Forbidden
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Not found
        examples: {}
        description: Not found
  deprecated: false
  type: path
components:
  schemas: {}

````