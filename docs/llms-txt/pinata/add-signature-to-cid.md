# Source: https://docs.pinata.cloud/api-reference/endpoint/add-signature-to-cid.md

# Add Signature to CId

> `org:files:write`


## OpenAPI

````yaml post /files/{network}/signature/{cid}
paths:
  path: /files/{network}/signature/{cid}
  method: post
  servers:
    - url: https://api.pinata.cloud/v3
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        cid:
          schema:
            - type: string
              required: true
              description: Target CID to add a signature to
        network:
          schema:
            - type: enum<string>
              enum:
                - public
                - private
              required: true
              description: Target either the public or private IPFS network
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              signature:
                allOf:
                  - type: string
                    description: Signature for the target CID
              address:
                allOf:
                  - type: string
                    description: Wallet address that made the signature
            example:
              address: '0xbC18447255e86f7f6c01C25e82636dDc587Ef9dc'
              signature: >-
                0x1ba6c2a8412dc9b0be37b013ea5bddd97251dab4d435cc9c4c7bcf331d4017ca2de07485ad6a15ce60d3700cee802787bc7ede0c112c7843f702bb1e71b750911b
        examples:
          example:
            value:
              address: '0xbC18447255e86f7f6c01C25e82636dDc587Ef9dc'
              signature: >-
                0x1ba6c2a8412dc9b0be37b013ea5bddd97251dab4d435cc9c4c7bcf331d4017ca2de07485ad6a15ce60d3700cee802787bc7ede0c112c7843f702bb1e71b750911b
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
                      cid:
                        type: string
                      signature:
                        type: string
        examples:
          example:
            value:
              data:
                cid: QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU
                signature: >-
                  0x1ba6c2a8412dc9b0be37b013ea5bddd97251dab4d435cc9c4c7bcf331d4017ca2de07485ad6a15ce60d3700cee802787bc7ede0c112c7843f702bb1e71b750911b
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````