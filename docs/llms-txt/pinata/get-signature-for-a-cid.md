# Source: https://docs.pinata.cloud/api-reference/endpoint/get-signature-for-a-cid.md

# Get Signature for a CID

> `org:files:read`


## OpenAPI

````yaml get /files/{network}/signature/{cid}
paths:
  path: /files/{network}/signature/{cid}
  method: get
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
        network:
          schema:
            - type: enum<string>
              enum:
                - public
                - private
              required: true
              description: Target either the public or private IPFS network
        cid:
          schema:
            - type: string
              required: true
              description: Target CID
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