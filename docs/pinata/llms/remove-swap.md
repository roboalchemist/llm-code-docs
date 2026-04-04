# Source: https://docs.pinata.cloud/api-reference/endpoint/remove-swap.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Remove Swap

> `org:files:write`




## OpenAPI

````yaml delete /files/{network}/swap/{cid}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /files/{network}/swap/{cid}:
    delete:
      tags:
        - Swaps
      summary: Remove Swap
      description: |
        `org:files:write`
      operationId: delete-swap
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
          description: Target CID to remove swap
          example: bafkreiccqfcxwp52uqwd7r5g7kdukgz7jvs6jcusetfnznj5jfch3r6wlm
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Sun, 18 Aug 2024 19:45:11 GMT
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
                example: cb4721118316fe9ac2e7ec44a2e25133
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