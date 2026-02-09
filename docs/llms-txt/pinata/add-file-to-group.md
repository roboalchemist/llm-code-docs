# Source: https://docs.pinata.cloud/api-reference/endpoint/add-file-to-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Add File To Group

> `org:groups:write`




## OpenAPI

````yaml put /groups/{network}/{id}/ids/{file_id}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /groups/{network}/{id}/ids/{file_id}:
    put:
      tags:
        - Groups
      summary: Add File To Group
      description: |
        `org:groups:write`
      operationId: addFileToGroup
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
          description: The ID of the target group
          schema:
            type: string
          required: true
          example: 01919ac8-a6f5-7e8e-a8a2-6cfe00122b90
        - name: file_id
          in: path
          description: The ID of the tart file to add to the group
          schema:
            type: string
          required: true
          example: bc2aad39-2594-4353-9404-f59bc4118e2c
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Thu, 29 Aug 2024 15:17:52 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '136'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 5cee9f024755176365a202b6ce5d29e4
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
              example:
                data: null
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````