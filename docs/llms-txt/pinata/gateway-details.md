# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/gateway-details.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Gateway Details

> `org:gateways:read`




## OpenAPI

````yaml get /gateways/{id}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways/{id}:
    get:
      tags:
        - default
      summary: Gateway Details
      description: |
        `org:gateways:read`
      parameters:
        - name: id
          in: path
          schema:
            type: string
          required: true
          description: ID of the target Gateway
          example: 01dae16b-699c-472a-a61e-975a7b9777bd
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Fri, 12 Jul 2024 15:10:18 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '823'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 5f66a3d6dca358f8351f5840160cd956
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
                  id: 01dae16b-699c-472a-a61e-975a7b9777bd
                  created_at: '2023-01-24T19:51:17.493Z'
                  domain: restricted-example
                  restrict: false
                  custom_domains:
                    - domain: ipfs.pinata.cloud
                      domain_validation_status: pending
                      custom_domain_id: 87980e39-fe71-4dba-9b05-3dfc66593539
                      ssl_validation_status: initializing
                  settings:
                    restriction_policies:
                      accessTokens:
                        - id: d199be6a-3bee-461b-b7fb-e1225eafe28e
                          value: key
                          createdAt: '2024-07-12T15:09:47.564042199Z'
                      allowedHosts:
                        - id: 8934893a-093c-4d3a-9cd8-2c034a7f4fb8
                          value: https://ipfs.pinata.cloud
                          createdAt: '2024-07-12T15:10:03.192988915Z'
                      allowedIPAddresses:
                        - id: e7d98003-d2b3-46ff-901e-2c666022004a
                          value: 1.1.1.1
                          createdAt: '2024-07-12T15:09:53.879274435Z'
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````