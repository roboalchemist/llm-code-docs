# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/gateway-domain-available.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Gateway Domain Available

> `org:gateways:read`




## OpenAPI

````yaml get /gateways/exists/{domain}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways/exists/{domain}:
    get:
      tags:
        - default
      summary: Gateway Domain Available
      description: |
        `org:gateways:read`
      parameters:
        - name: domain
          in: path
          schema:
            type: string
          required: true
          example: dweb
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Fri, 12 Jul 2024 15:12:23 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '25'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: ef5b3faec6d43df9556a0d3d697d9a31
            Strict-Transport-Security:
              schema:
                type: string
                example: max-age=15724800; includeSubDomains
          content:
            application/json:
              schema:
                type: object
              example:
                data:
                  exists: true
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````