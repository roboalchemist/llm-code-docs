# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/gateway-custom-domain-details.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Gateway Custom Domain Details

> `org:gateways:read`




## OpenAPI

````yaml get /gateways/{id}/custom_domain/{custom_domain_id}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways/{id}/custom_domain/{custom_domain_id}:
    get:
      tags:
        - default
      summary: Gateway Custom Domain Details
      description: |
        `org:gateways:read`
      parameters:
        - name: id
          in: path
          schema:
            type: string
          required: true
          description: ID of the target Gateway
          example: 92c4666c-f9ec-4c72-ad47-7cef48440eaf
        - name: custom_domain_id
          in: path
          schema:
            type: string
          required: true
          description: Custom domain ID of the target Gateway
          example: 87980e39-fe71-4dba-9b05-3dfc66593539
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Fri, 12 Jul 2024 15:09:12 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '174'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 4ffa207d6f5bcd430acb6e04c3346ab3
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
                  domain: ipfs.pinata.cloud
                  domain_validation_status: pending
                  custom_domain_id: 87980e39-fe71-4dba-9b05-3dfc66593539
                  ssl_validation_status: initializing
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````