# Source: https://docs.pinata.cloud/api-reference/endpoint/delete-file-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete File by ID

> `org:files:write`




## OpenAPI

````yaml delete /files/{network}/{id}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /files/{network}/{id}:
    delete:
      summary: Delete File by ID
      description: |
        `org:files:write`
      operationId: deleteFile
      parameters:
        - name: network
          description: Target a file on either the public or private IPFS network
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
          example: 01919461-6d4c-7456-870d-0d1faeb90f46
      responses:
        '500':
          description: Internal Server Error
          headers:
            Date:
              schema:
                type: string
                example: Tue, 27 Aug 2024 15:09:20 GMT
            Content-Type:
              schema:
                type: string
                example: application/json
            Content-Length:
              schema:
                type: integer
                example: '201'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 79dbc0bba9ecb69876a9f935f1931f3c
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