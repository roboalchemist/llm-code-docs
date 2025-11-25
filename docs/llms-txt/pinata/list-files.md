# Source: https://docs.pinata.cloud/api-reference/endpoint/list-files.md

# List Files

> `org:files:read`


## OpenAPI

````yaml get /files/{network}
paths:
  path: /files/{network}
  method: get
  servers:
    - url: https://api.pinata.cloud/v3
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        network:
          schema:
            - type: enum<string>
              enum:
                - public
                - private
              required: true
              description: Target either the public or private IPFS network
      query:
        name:
          schema:
            - type: string
              description: Filter files by name
        group:
          schema:
            - type: string
              description: >-
                Filter fils by group_id. Pass `null` to show files that are not
                part of a group
        mimeType:
          schema:
            - type: string
              description: Filter files by mime_type
        cid:
          schema:
            - type: string
              description: Filter files by CID
        cidPending:
          schema:
            - type: boolean
              description: Return only files that are still waiting for a CID
        metadata:
          schema:
            - type: object
              properties: {}
              description: Filter by key values in file metadata
          style: deepObject
          explode: true
        limit:
          schema:
            - type: integer
              description: Limit the number of results
        order:
          schema:
            - type: enum<string>
              enum:
                - ASC
                - DESC
              description: Sort results by creation date with with ASC or DESC
        pageToken:
          schema:
            - type: string
              description: Paginate using the nextPageToken
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
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
        examples:
          example:
            value:
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
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````