# Source: https://docs.pinata.cloud/api-reference/endpoint/remove-signature-from-cid.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove Signature from CID

> `org:files:write`




## OpenAPI

````yaml delete /files/{network}/signature/{cid}
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
    delete:
      tags:
        - default
      summary: Remove Signature from CID
      description: |
        `org:files:write`
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
          example: bafybeidzbfkjjz3ksfvxn7mcj3nuyprx4mhna5jsnfwrncoqbtppi45spe
          description: Target CID
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Mon, 22 Jul 2024 17:54:20 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '14'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 96e62eee654b71b0fc4dc66eefb6e999
            Strict-Transport-Security:
              schema:
                type: string
                example: max-age=15724800; includeSubDomains
          content:
            application/json:
              schema:
                type: object
              example:
                data: null
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````