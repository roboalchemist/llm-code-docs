# Source: https://docs.pinata.cloud/api-reference/endpoint/x402/cids-add.md

# Add CID to Payment Instruction

> Associates a CID with a payment instruction

## OpenAPI

````yaml put /x402/payment_instructions/{id}/cids/{cid}
paths:
  path: /x402/payment_instructions/{id}/cids/{cid}
  method: put
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
        cid:
          schema:
            - type: string
              required: true
              description: Content Identifier (CID)
      query: {}
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
                      payment_instruction_id:
                        type: string
                      cid:
                        type: string
                      created_at:
                        type: string
                        format: date-time
        examples:
          example:
            value:
              data:
                payment_instruction_id: <string>
                cid: <string>
                created_at: '2023-11-07T05:31:56Z'
        description: Successful operation
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Bad request
        examples: {}
        description: Bad request
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