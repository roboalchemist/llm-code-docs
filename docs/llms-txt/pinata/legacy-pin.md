# Source: https://docs.pinata.cloud/api-reference/endpoint/x402/legacy-pin.md

# Upload a File (Legacy x402)

> Uploads a file to Pinata's public IPFS network

## OpenAPI

````yaml pinata-x402-api-v1.yaml post /pin/{network}
paths:
  path: /pin/{network}
  method: post
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
        network:
          schema:
            - type: enum<string>
              enum:
                - public
                - private
              required: true
              description: Upload to either public or private IPFS network
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              fileSize:
                allOf:
                  - type: integer
                    description: Size of the file to be uploaded in bytes
            required: true
            requiredProperties:
              - fileSize
        examples:
          example:
            value:
              fileSize: 123
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              url:
                allOf:
                  - type: string
                    description: The signed URL for file upload
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
  deprecated: false
  type: path
components:
  schemas: {}

````