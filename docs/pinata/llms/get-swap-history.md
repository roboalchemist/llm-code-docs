# Source: https://docs.pinata.cloud/sdk/files/public/get-swap-history.md

# Source: https://docs.pinata.cloud/sdk/files/private/get-swap-history.md

# Source: https://docs.pinata.cloud/api-reference/endpoint/get-swap-history.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Swap History

> `org:files:read`




## OpenAPI

````yaml get /files/{network}/swap/{cid}
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
    get:
      tags:
        - Swaps
      summary: Get Swap History
      description: |
        `org:files:read`
      operationId: get-swap
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
        - name: domain
          in: query
          schema:
            type: string
            description: The domain of the gateway that has the Hot Swaps plugin installed
          required: true
          example: discordpinnie.mypinata.cloud
        - name: cid
          in: path
          schema:
            type: string
            description: The original CID that is in the Gateway path
          required: true
          example: bafkreiccqfcxwp52uqwd7r5g7kdukgz7jvs6jcusetfnznj5jfch3r6wlm
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Sun, 18 Aug 2024 19:44:14 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '116'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 32947ddd9c147410acebab6b9221f523
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
                  - mapped_cid: >-
                      bafkreig4zcnmqa23zff3ye7tuef6wrlq3aimffzm22axfeh3ddmawzlzz4
                    created_at: '2024-09-20T17:09:39.490275Z'
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````