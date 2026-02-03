# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/list-marketplace-plugins.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# List Marketplace Plugins

> `org:gateways:read`




## OpenAPI

````yaml get /gateways/plugins/marketplace
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways/plugins/marketplace:
    get:
      tags:
        - default
      summary: List Marketplace Plugins
      description: |
        `org:gateways:read`
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Mon, 22 Jul 2024 17:45:26 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '533'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: ce0dff9549abcb756b0a44af221d6feb
            Strict-Transport-Security:
              schema:
                type: string
                example: max-age=15724800; includeSubDomains
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
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
              example:
                data:
                  - id: 1
                    name: Content Addressable Attestation
                    description: >-
                      Verify the authenticity and ownership of files added to
                      the IPFS network by signing them with your Ethereum
                      wallet.
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
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````