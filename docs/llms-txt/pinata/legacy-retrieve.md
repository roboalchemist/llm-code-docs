# Source: https://docs.pinata.cloud/api-reference/endpoint/x402/legacy-retrieve.md

# Retrieve a Private File (Legacy x402)

> Retrieves a private file from IPFS by its CID

## OpenAPI

````yaml pinata-x402-api-v1.yaml get /retrieve/private/{cid}
paths:
  path: /retrieve/private/{cid}
  method: get
  servers:
    - url: https://402.pinata.cloud/v1
      description: Production server
  request:
    security:
      - title: x402Payment
        parameters:
          query: {}
          header:
            X-PAYMENT:
              type: apiKey
              description: Base64 encoded x402 payment payload
          cookie: {}
    parameters:
      path:
        cid:
          schema:
            - type: string
              required: true
              description: Content Identifier (CID) of the file
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
              url:
                allOf:
                  - type: string
                    description: URL to access the private file
        examples:
          example:
            value:
              url: <string>
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
    '500':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Server error
        examples: {}
        description: Server error
  deprecated: false
  type: path
components:
  schemas: {}

````