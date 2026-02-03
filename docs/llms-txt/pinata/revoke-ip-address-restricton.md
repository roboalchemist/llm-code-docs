# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/revoke-ip-address-restricton.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Revoke IP Address Restricton

> `org:gateways:write:




## OpenAPI

````yaml delete /gateways/{id}/ips/{ip_id}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways/{id}/ips/{ip_id}:
    delete:
      tags:
        - default
      summary: Revoke IP Address Restricton
      description: |
        `org:gateways:write:
      parameters:
        - name: id
          in: path
          schema:
            type: string
          required: true
          description: ID of the target Gateway
          example: 5eb8b151-77b3-4e46-8243-5b6282131a9e
        - name: ip_id
          in: path
          schema:
            type: string
          required: true
          description: ID of the IP address entry
          example: 66b6f3c5-2733-442b-a558-960be4b5a921
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Fri, 12 Jul 2024 18:54:46 GMT
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
                example: c70075fc6823ef5234b62d35551be106
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