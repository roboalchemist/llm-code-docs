# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/list-marketplace-plugins.md

# List Marketplace Plugins

> `org:gateways:read`


## OpenAPI

````yaml get /gateways/plugins/marketplace
paths:
  path: /gateways/plugins/marketplace
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
      path: {}
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
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: number
                        name:
                          type: string
                        description:
                          type: string
                        image:
                          type: string
                        tags:
                          type: array
                          items:
                            type: string
        examples:
          example:
            value:
              data:
                - id: 1
                  name: Content Addressable Attestation
                  description: >-
                    Verify the authenticity and ownership of files added to the
                    IPFS network by signing them with your Ethereum wallet.
                  image: >-
                    https://mktg.mypinata.cloud/ipfs/QmVm3jRZ7S2KMmYEvkmkwncRCmBSUEuzNKfm2AgJkfBGKZ
                  tags:
                    - verifiability
                    - security
                - id: 2
                  name: Hot Swaps
                  description: >-
                    Make IPFS mutable by pointing your original CID to a new
                    file.
                  image: >-
                    https://mktg.mypinata.cloud/ipfs/QmVpy6v7YASWUQjmqgUxKwbn6zgzuVSRudzdZMynpBjSJo
                  tags:
                    - files
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````