# Source: https://docs.pinata.cloud/api-reference/endpoint/update-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Update File

> `org:files:write`




## OpenAPI

````yaml put /files/{network}/{id}
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
    put:
      summary: Update File
      description: |
        `org:files:write`
      operationId: updateFile
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
          example: 01919457-c2c6-770e-9391-8c72c4f41f64
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: The updated name for a file
                keyvalues:
                  type: object
                  additionalProperties: true
                  description: Stringified key/values metadata
              example:
                name: Hello Files API
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Tue, 27 Aug 2024 15:12:50 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '298'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: b41144a3011804309872d413a6dbc3b0
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
                      cid:
                        type: string
                      size:
                        type: number
                      number_of_files:
                        type: number
                      mime_type:
                        type: string
                      group_id:
                        type: string
                      keyvalues:
                        type: object
                      created_at:
                        type: string
              example:
                data:
                  id: e5323ea7-8a02-4486-9b6f-63c788810aeb
                  name: e093dbd3-f276-4bb3-a43e-60437725f410.txt
                  cid: bafkreicnu2aqjkoglrlrd65giwo4l64pdajxffk6jtq2vb7yaiopc3yu7m
                  size: 36
                  number_of_files: 1
                  mime_type: text/plain
                  group_id: 18893556-de8e-4229-8a9a-27b95468dd3e
                  keyvalues:
                    whimsey: 'true'
                  created_at: '2024-08-27T14:57:51.485934Z'
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````