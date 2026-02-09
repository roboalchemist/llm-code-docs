# Source: https://docs.pinata.cloud/api-reference/endpoint/v3-revoke-api-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Revoke API Key

> `org:write`




## OpenAPI

````yaml delete /api_keys/{key}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /api_keys/{key}:
    delete:
      tags:
        - default
      summary: Revoke API Key
      description: |
        `org:write`
      parameters:
        - name: key
          in: path
          schema:
            type: string
          required: true
          example: 8624b6dd1e6f04
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Tue, 18 Jun 2024 18:26:07 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '9'
            Connection:
              schema:
                type: string
                example: keep-alive
            Strict-Transport-Security:
              schema:
                type: string
                example: max-age=15724800; includeSubDomains
          content:
            application/json:
              schema:
                type: object
              example: Revoked
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````