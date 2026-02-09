# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/get-marketplace-plugin-details.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Marketplace Plugin Details

> `org:gateways:read`




## OpenAPI

````yaml get /gateways/plugins/marketplace/{id}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways/plugins/marketplace/{id}:
    get:
      tags:
        - default
      summary: Get Marketplace Plugin Details
      description: |
        `org:gateways:read`
      parameters:
        - name: id
          in: path
          schema:
            type: integer
          required: true
          example: '1'
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Mon, 22 Jul 2024 17:46:25 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '317'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: ef76dca037942684c6b4fb5280867057
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
                  id: 1
                  name: Content Addressable Attestation
                  description: >-
                    Verify the authenticity and ownership of files added to the
                    IPFS network by signing them with your Ethereum wallet.
                  image: >-
                    https://mktg.mypinata.cloud/ipfs/QmVm3jRZ7S2KMmYEvkmkwncRCmBSUEuzNKfm2AgJkfBGKZ
                  tags:
                    - verifiability
                    - security
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````