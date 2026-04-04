# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-gateway-key-restriction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Gateway Key Restriction

> `org:gateways:write`




## OpenAPI

````yaml post /gateways/{id}/access_tokens
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways/{id}/access_tokens:
    post:
      tags:
        - default
      summary: Create Gateway Key Restriction
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
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Fri, 12 Jul 2024 15:35:04 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '175'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 1d0a98a992503275b20c1998eb17ea0a
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
                  id: e8fe078b-38e8-4472-94e7-9023205232d2
                  value: key
                  createdAt: '2024-07-12T15:34:59.786198063Z'
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````