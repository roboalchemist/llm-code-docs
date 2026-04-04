# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-gateway-host-origin-restriction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Gateway Host Origin Restriction

> `org:gateways:write`




## OpenAPI

````yaml post /gateways/{id}/hosts
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways/{id}/hosts:
    post:
      tags:
        - default
      summary: Create Gateway Host Origin Restriction
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
                host:
                  type: string
                  description: Host for target Gateway
              example:
                host: https://ipfs.pinata.cloud
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Fri, 12 Jul 2024 15:40:41 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '136'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 2084338cd283435cb925529798cf8f83
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
                  id: b0165cb6-59e2-476e-aa60-b63b9326bcc6
                  value: https://ipfs.pinata.cloud
                  createdAt: '2024-07-12T15:40:40.258353687Z'
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````