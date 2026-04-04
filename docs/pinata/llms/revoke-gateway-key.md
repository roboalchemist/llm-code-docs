# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/revoke-gateway-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Revoke Gateway Key

> `org:gateways:write`




## OpenAPI

````yaml delete /gateways/{id}/access_tokens/{access_token_id}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways/{id}/access_tokens/{access_token_id}:
    delete:
      tags:
        - default
      summary: Revoke Gateway Key
      description: |
        `org:gateways:write`
      parameters:
        - name: id
          in: path
          schema:
            type: string
          required: true
          description: ID of the target Gateway
          example: 5eb8b151-77b3-4e46-8243-5b6282131a9e
        - name: access_token_id
          in: path
          schema:
            type: string
          required: true
          description: ID of the target Gateway Key
          example: 5cfe30af-1de5-409e-be09-f261445a2df6
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Fri, 12 Jul 2024 18:52:08 GMT
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
                example: bef4599a5d0de8322fff20dda15c82f9
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