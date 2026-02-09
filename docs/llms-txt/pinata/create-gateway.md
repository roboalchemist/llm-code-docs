# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-gateway.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Gateway

> `org:gateways:write`




## OpenAPI

````yaml post /gateways
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways:
    post:
      tags:
        - default
      summary: Create Gateway
      description: |
        `org:gateways:write`
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                domain:
                  type: string
                  description: Desired name for Gateway subdomain
              example:
                domain: dweb5
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Fri, 12 Jul 2024 15:21:49 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '250'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 1c734bcad3dce59b9164d1088045a5be
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
                  id: 5eb8b151-77b3-4e46-8243-5b6282131a9e
                  created_at: '2024-07-12T15:21:47.966866Z'
                  domain: dweb3
                  restrict: false
                  custom_domains: []
                  settings:
                    restriction_policies:
                      accessTokens: []
                      allowedHosts: []
                      allowedIPAddresses: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````