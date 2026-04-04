# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/delete-gateway-custom-domain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Gateway Custom Domain

> `org:gateways:write`




## OpenAPI

````yaml delete /gateways/{id}/custom_domain/{custom_domain_id}
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
    delete:
      tags:
        - default
      summary: Delete Gateway Custom Domain
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
        - name: custom_domain_id
          in: path
          schema:
            type: string
          required: true
          description: ID of the target Custom Domain
          example: 81bc0135-346d-4d81-ad81-1e313297702f
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Fri, 12 Jul 2024 18:48:59 GMT
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
                example: b5cab9febddabadf19b0d03ed2fe2de0
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