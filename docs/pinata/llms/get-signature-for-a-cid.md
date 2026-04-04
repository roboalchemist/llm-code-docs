# Source: https://docs.pinata.cloud/api-reference/endpoint/get-signature-for-a-cid.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Signature for a CID

> `org:files:read`




## OpenAPI

````yaml get /files/{network}/signature/{cid}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /files/{network}/signature/{cid}:
    get:
      tags:
        - default
      summary: Get Signature for a CID
      description: |
        `org:files:read`
      parameters:
        - name: network
          description: Target either the public or private IPFS network
          in: path
          schema:
            type: string
            enum:
              - public
              - private
          required: true
          example: public
        - name: cid
          in: path
          schema:
            type: string
          required: true
          example: bafkreigbicehros5mydclprafp7jxkcxprzkmthdz5aldofqnir4s24efa
          description: Target CID
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Mon, 22 Jul 2024 17:44:19 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '213'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 46a59cd880c3dff15201d19a25102c48
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
                      cid:
                        type: string
                      signature:
                        type: string
              example:
                data:
                  cid: QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU
                  signature: >-
                    0x1ba6c2a8412dc9b0be37b013ea5bddd97251dab4d435cc9c4c7bcf331d4017ca2de07485ad6a15ce60d3700cee802787bc7ede0c112c7843f702bb1e71b750911b
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````