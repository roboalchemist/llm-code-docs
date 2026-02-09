# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-gateway-ip-address-restriction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Gateway IP Address Restriction

> `org:gateways:write`




## OpenAPI

````yaml post /gateways/{id}/ips
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways/{id}/ips:
    post:
      tags:
        - default
      summary: Create Gateway IP Address Restriction
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                ip:
                  type: string
                  description: IP for the target Gateway
              example:
                ip: 1.1.1.1
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Fri, 12 Jul 2024 15:37:05 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '118'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: e51cd4cebe7349e410218d80f18650d3
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
                  id: 66b6f3c5-2733-442b-a558-960be4b5a921
                  value: 1.1.1.1
                  createdAt: '2024-07-12T15:37:04.871996078Z'
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````