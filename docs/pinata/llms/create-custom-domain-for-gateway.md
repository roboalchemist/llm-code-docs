# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-custom-domain-for-gateway.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Custom Domain for Gateway

> `org:gateways:write`




## OpenAPI

````yaml post /gateways/{id}/custom_domain
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /gateways/{id}/custom_domain:
    post:
      tags:
        - default
      summary: Create Custom Domain for Gateway
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
                domain:
                  type: string
                  description: Custom domain for the target Gateway
              example:
                domain: ipfs2.pinata.cloud
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Fri, 12 Jul 2024 15:31:13 GMT
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
                example: ce0d865f56e8178bec28c0609ae7a9fc
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
                  domain: ipfs2.pinata.cloud
                  domain_validation_status: pending
                  custom_domain_id: 81bc0135-346d-4d81-ad81-1e313297702f
                  ssl_validation_status: initializing
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````