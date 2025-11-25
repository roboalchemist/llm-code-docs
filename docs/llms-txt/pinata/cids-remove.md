# Source: https://docs.pinata.cloud/api-reference/endpoint/x402/cids-remove.md

# Remove CID from Payment Instruction

> Removes a CID association from a payment instruction

## OpenAPI

````yaml delete /x402/payment_instructions/{id}/cids/{cid}
paths:
  path: /x402/payment_instructions/{id}/cids/{cid}
  method: delete
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
                    nullable: true
        examples:
          example:
            value:
              data: {}
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