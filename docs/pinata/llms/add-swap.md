# Source: https://docs.pinata.cloud/sdk/files/public/add-swap.md

# Source: https://docs.pinata.cloud/sdk/files/private/add-swap.md

# Source: https://docs.pinata.cloud/api-reference/endpoint/add-swap.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Add Swap

> `org:files:write`




## OpenAPI

````yaml put /files/{network}/swap/{cid}
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
    put:
      tags:
        - Swaps
      summary: Add Swap
      description: |
        `org:files:write`
      operationId: add-swap
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
          description: The target original CID
          example: bafkreiccqfcxwp52uqwd7r5g7kdukgz7jvs6jcusetfnznj5jfch3r6wlm
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - swapCid
              properties:
                swapCid:
                  type: string
                  description: The CID you want to redirect to
              example:
                swapCid: bafkreig4zcnmqa23zff3ye7tuef6wrlq3aimffzm22axfeh3ddmawzlzz4
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Sun, 18 Aug 2024 19:36:29 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '114'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 576d0cc3a1b66e3b8938c90e0f45f3a7
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
                      mapped_cid:
                        type: string
                        description: >-
                          The current CID that is being pointed to from the
                          original
                      created_at:
                        type: string
                        description: The date this CID was updated
              example:
                data:
                  mapped_cid: bafkreig4zcnmqa23zff3ye7tuef6wrlq3aimffzm22axfeh3ddmawzlzz4
                  created_at: '2024-09-20T17:09:39.490275Z'
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````