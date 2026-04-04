# Source: https://docs.pinata.cloud/api-reference/endpoint/update-group.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Group

> `org:groups:write`




## OpenAPI

````yaml put /groups/{network}/{id}
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
    put:
      tags:
        - Groups
      summary: Update Group
      description: |
        `org:groups:write`
      operationId: updateGroup
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: Updated name for target group
                is_public:
                  type: boolean
                  description: Toggle if group is public or not
              example:
                name: Updated Name
                is_public: true
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
                  id: 01919ac8-a6f5-7e8e-a8a2-6cfe00122b90
                  name: Updated Name
                  is_public: true
                  created_at: '2024-08-28T20:58:46.96779Z'
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````