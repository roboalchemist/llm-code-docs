# Source: https://docs.pinata.cloud/api-reference/endpoint/delete-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Group

> `org:groups:write`




## OpenAPI

````yaml delete /groups/{network}/{id}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /groups/{network}/{id}:
    delete:
      tags:
        - Groups
      summary: Delete Group
      description: |
        `org:groups:write`
      operationId: deleteGroup
      parameters:
        - name: network
          description: Target either the public or private IPFS network
          in: path
          schema:
            type: string
            enum:
              - public
              - private
          required: true
          example: public
        - name: id
          in: path
          schema:
            type: string
          required: true
          example: 01919eba-b4e4-7cc6-8a72-c01358ec8f8d
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Thu, 29 Aug 2024 15:22:17 GMT
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
                example: e603f9d52d268705312556d6064c9379
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