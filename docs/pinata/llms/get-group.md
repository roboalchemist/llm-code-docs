# Source: https://docs.pinata.cloud/api-reference/endpoint/get-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Group

> `org:groups:read`




## OpenAPI

````yaml get /groups/{network}/{id}
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
    get:
      tags:
        - Groups
      summary: Get Group
      description: |
        `org:groups:read`
      operationId: getGroup
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
          example: 01919976-955f-7d06-bd59-72e80743fb95
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Wed, 28 Aug 2024 14:50:47 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '184'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: b9bcd1c7dba0f7241ae8ee526fdc81be
            Strict-Transport-Security:
              schema:
                type: string
                example: max-age=15724800; includeSubDomains
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      id:
                        type: string
                      name:
                        type: string
                      is_public:
                        type: boolean
                      created_at:
                        type: string
              example:
                data:
                  id: 01919976-955f-7d06-bd59-72e80743fb95
                  name: Test Private Group
                  is_public: false
                  created_at: '2024-08-28T14:49:31.246596Z'
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````