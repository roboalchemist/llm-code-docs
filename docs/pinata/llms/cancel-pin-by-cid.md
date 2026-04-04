# Source: https://docs.pinata.cloud/api-reference/endpoint/cancel-pin-by-cid.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel Request

> `org:files:write`




## OpenAPI

````yaml DELETE /files/public/pin_by_cid/{id}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /files/public/pin_by_cid/{id}:
    delete:
      summary: Cancel Request
      description: |
        `org:files:write`
      operationId: cancelPinByCID
      parameters:
        - name: id
          description: ID of the pin_by_cid request
          in: path
          schema:
            type: string
          required: true
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Tue, 27 Aug 2024 15:04:00 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '303'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 5cda7fd04bb31bc8c6bd461089fcfa1c
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