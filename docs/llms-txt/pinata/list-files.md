# Source: https://docs.pinata.cloud/api-reference/endpoint/list-files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# List Files

> `org:files:read`




## OpenAPI

````yaml get /files/{network}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /files/{network}:
    get:
      summary: List Files
      description: |
        `org:files:read`
      operationId: listFiles
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
        - name: name
          in: query
          schema:
            type: string
          description: Filter files by name
        - name: group
          in: query
          schema:
            type: string
          description: >-
            Filter fils by group_id. Pass `null` to show files that are not part
            of a group
        - name: mimeType
          in: query
          schema:
            type: string
          description: Filter files by mime_type
        - name: cid
          in: query
          schema:
            type: string
          description: Filter files by CID
        - name: cidPending
          in: query
          schema:
            type: boolean
          description: Return only files that are still waiting for a CID
          example: 'true'
        - name: metadata
          in: query
          style: deepObject
          explode: true
          schema:
            type: object
            additionalProperties: true
          description: Filter by key values in file metadata
        - name: limit
          in: query
          schema:
            type: integer
          description: Limit the number of results
          example: '10'
        - name: order
          in: query
          schema:
            type: string
            enum:
              - ASC
              - DESC
          description: Sort results by creation date with with ASC or DESC
        - name: pageToken
          in: query
          schema:
            type: string
          description: Paginate using the nextPageToken
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Tue, 27 Aug 2024 15:02:30 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '382'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: f60474dfa75f70cbde347239324f49cc
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
                      files:
                        type: array
                        items:
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
                      next_page_token:
                        type: string
              example:
                data:
                  files:
                    - id: e5323ea7-8a02-4486-9b6f-63c788810aeb
                      name: e093dbd3-f276-4bb3-a43e-60437725f410.txt
                      cid: >-
                        bafkreicnu2aqjkoglrlrd65giwo4l64pdajxffk6jtq2vb7yaiopc3yu7m
                      size: 36
                      number_of_files: 1
                      mime_type: text/plain
                      group_id: 18893556-de8e-4229-8a9a-27b95468dd3e
                      keyvalues:
                        whimsey: 'true'
                      created_at: '2024-08-27T14:57:51.485934Z'
                  next_page_token: MDE5MTk0NTctYzJjNi03NzBlLTkzOTEtOGM3MmM0ZjQxZjY0
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````